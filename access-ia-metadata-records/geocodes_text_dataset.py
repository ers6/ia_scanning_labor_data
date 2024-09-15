import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


def main(): 
    texts = pd.read_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/texts-data.csv', low_memory=False)
    loc_key = pd.read_csv("https://raw.githubusercontent.com/ers6/ia_scanning_labor_data/main/metadata-analysis/metadata-records-analysis-csvs/location_key.csv")
    texts['name'] = ''
    texts['lat'] = ''
    texts['long'] = ''
    i = 0
    for i in range(len(texts)):
        geocoder = geocodes_centers(texts.iloc[i]['scanningcenter'], loc_key)
        texts.at[i, 'name'] = geocoder['name']
        texts.at[i, 'lat'] = geocoder['lat']
        texts.at[i, 'long'] = geocoder['long']
        i += 1
    texts.to_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/geocoded-texts-data.csv')

    
def redo_geocode():
    texts = pd.read_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/geocoded-texts-data-no-microfilm.csv', low_memory=False)
    texts = texts[['identifier', 'scandate', 'sponsor', 'scanner', 'donor',
       'imagecount', 'operator', 'shipping_container', 'mediatype',
       'scanningcenter']]
    loc_key = pd.read_csv("https://raw.githubusercontent.com/ers6/ia_scanning_labor_data/main/metadata-analysis/metadata-records-analysis-csvs/location_key.csv")
    print(texts.keys())
    texts['name'] = ''
    texts['lat'] = ''
    texts['long'] = ''
    i = 0
    for i in range(len(texts)):
        geocoder = geocodes_centers(texts.iloc[i]['scanningcenter'], loc_key)
        texts.at[i, 'name'] = geocoder['name']
        texts.at[i, 'lat'] = geocoder['lat']
        texts.at[i, 'long'] = geocoder['long']
        i += 1
        print(str(i) + "/"+ str(len(texts)))
    texts.to_csv('/Volumes/Samsung_T5/scanning_labor_in_IA/geocoded-texts-data_v1.csv')




def geocodes_centers(scan_center, the_geocoder):
    i = 0
    for i in range(len(the_geocoder)):
        if scan_center.lower().strip() == the_geocoder.iloc[i]['scan_center'].lower().strip():
            # print(the_geocoder.iloc[i])
            return {'name': the_geocoder.iloc[i]['name'].strip(),
                   'lat': the_geocoder.iloc[i]['lat'],
                   'long': the_geocoder.iloc[i]['long']}
        else: pass
        i += 1
        

# main()
redo_geocode()