import pandas as pd
import os
import tqdm

def main():
    joins_center_tables()
    combine_datasets()
    make_text_dataset()

def joins_center_tables():
    dir = "/Volumes/Samsung_T5/scanning_labor_in_IA/scancenter-data"
    for thing in tqdm.tqdm(os.listdir(dir)):
        subdir = dir + "/"+thing +"/"
        center = thing.split('-')[0]
        print(center)
        scanner_file = subdir + center+ "-scanner.csv"
        sponsor_file = subdir + center + "-sponsor.csv"
        scandate_file = subdir + center + "-scandate.csv"
        donor_file = subdir + center + "-donor.csv"
        imagecount_file = subdir + center + "-imagecount.csv"
        operator_file = subdir + center + "-operator.csv"
        shippingcont_file = subdir + center + "-shipping_container.csv"
        mediatype_file = subdir + center + "-mediatype.csv"
        scandate_df = pd.read_csv(scandate_file)
        scandate_df['scandate'] = pd.to_datetime(scandate_df['scandate'], format='%Y%m%d%H%M%S', errors='coerce')
        sponsor_df = pd.read_csv(sponsor_file)
        scanner_df = pd.read_csv(scanner_file)
        mediatype_df = pd.read_csv(mediatype_file)
        donor_df = pd.read_csv(donor_file)
        imagecount_df = pd.read_csv(imagecount_file)
        operator_df = pd.read_csv(operator_file)
        shippingcont_df = pd.read_csv(shippingcont_file)

        merged = scandate_df.merge(sponsor_df, on='identifier', how='left')
        merged = merged.merge(scanner_df, on='identifier', how='left')
        merged = merged.merge(donor_df, on='identifier', how='left')
        merged = merged.merge(imagecount_df, on='identifier', how='left')
        merged = merged.merge(operator_df, on='identifier', how='left')
        merged = merged.merge(shippingcont_df, on='identifier', how='left')
        merged = merged.merge(mediatype_df, on='identifier', how='left')
        merged['scanningcenter'] = center
        merged.to_csv(subdir + center + "-combined.csv")


def combine_datasets():
    dir = "/Volumes/Samsung_T5/scanning_labor_in_IA/scancenter-data"
    df = pd.DataFrame(columns=['Unnamed: 0', 'identifier', 'scandate', 'sponsor', 'scanner', 'donor',
       'imagecount', 'operator', 'shipping_container', 'mediatype',
       'scanningcenter'])
    for thing in tqdm.tqdm(os.listdir(dir)):
        subdir = dir + "/" + thing + "/"
        center = thing.split('-')[0]
        print(center)
        center_df = pd.read_csv(subdir+ center +'-combined.csv')
        df = pd.concat([df, center_df], ignore_index=True)
    df.to_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/combined-data.csv')

def make_text_dataset():
    ia_data = pd.read_csv("/Volumes/Samsung_T5/scanning_labor_in_IA/combined-data.csv")
    ia_texts = ia_data.loc[ia_data['mediatype'] == 'texts']
    print(len(ia_texts))
    ia_texts.to_csv("/Volumes/Samsung_T5/scanning_labor_in_IA/texts-data.csv")



main()