import os
import pandas as pd
import tqdm

def get_center_ids():
    return  ['shenzhen', 'hongkong', 'china', 'cebu', 'alberta', 'sfdowntown',
 'tt_sanfrancisco', 'iala', 'indiana', 'euston', 'uoft', 'la', 'nj',
 'santamonica', 'tt_pts', 'boston', 'beltsville', 'capitolhill', 'nyc',
 'chapelhill', 'rich', 'richmond', 'richflorida', 'ill', 'il', 'edinburgh',
 'sfciviccenter', 'maryland', 'raleigh', 'provo', 'washingtondc',
 'tt_georgetown', 'sheridan', 'arch', 'miss', 'durham', 'durham2', 'providence',
 'tt_providence', 'lond', 'london', 'manhattan', 'honolulu', 'rexburg',
 'valencia', 'gainesville', 'tt_osu', 'tt_numismatic', 'tt_getty',
 'tt_harvardernstmayr', 'pretoria', 'IIIT Hyderabad', 'CCL HYDERABAD',
 'sacramento', 'beijing', 'tt_bangalore', 'tt_sok', 'trent', 'guatemala',
 'tt_swinburne', 'BookScanUS', 'tt_amnh', 'harrisburg', 'amherst',
 'tt_stanfordlaw', 'tt_pem', 'tt_calacademy', 'tt_jakarta', 'hangzhou',
 'clemson', 'Osmania University', 'clarksville', 'tt_victoria', 'poughkeepsie',
 'tt_warwick', 'tt_riks', '1dollarscan (zLibro)', 'RMSC_IIITH']


def join_collection_data():
    collection_df = pd.DataFrame(columns=['identifier', 'scanningcenter'])
    dir = "/Volumes/Samsung_T5/scanning_labor_in_IA/collection-data/"
    for thing in tqdm.tqdm(os.listdir(dir)):
        if '._' in thing:
            pass
        else:
            print(dir + thing)
            df = pd.read_csv(dir + thing)
            collection_df = pd.concat([collection_df, df], ignore_index=True)

    collection_df.to_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/collection-data/combined_collection_data.csv')

def analyze_collections():
    collection_data = pd.read_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/collection-data/combined_collection_data.csv')
    known_centers = get_center_ids()
    found_centers = []
    print(len(known_centers))
    for i in range(len(collection_data)):
        this_center = collection_data.iloc[i]['scanningcenter']
        if str(this_center) == 'nan':
            pass
        else:
            if this_center not in known_centers:
                known_centers.append(this_center)
                found_centers.append(this_center)
            else:pass
    print(len(known_centers))
    print(len(found_centers))
    print(found_centers)

def analyze_data():
    text_df = pd.read_csv("/Volumes/Samsung_T5/scanning_labor_in_IA/texts-data.csv")
    print(len(text_df))

analyze_data()