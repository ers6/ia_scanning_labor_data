
import json
import csv
import internetarchive as ia
import tqdm
import requests
import pandas as pd
import os
# gets scanning center metadata for each scanning center and saves to a local directory. Queries based just on id and a metadata field to optimize the request process. use join_tables.py to join the data tables for each scanning center together on shared id. 

# don't run this- it will not work on your machine. This is just how I generated a list of all of the ids for the scanning centers I was interested in. I found these ids iteratively through running get_collections_data(). 
def gets_ids():
    ids_df = pd.read_csv("/Users/elizabethschwartz/Documents/access-ia-metadata-records/data/scan-center-ids-left.csv")['scan_center_ids']
    ids = []
    i = 0
    for i in range(len(ids_df)):
        try:
            for item in ids_df.iloc[i].split('||'):
                ids.append(item.strip())
            i += 1
        except AttributeError:
            pass
    print(ids)

def gets_scancenter_data():
    center_ids = ['nj', 'tt_pts', 'boston', 'Boston', 'tt_bostonuniversity', 'beltsville', 'capitolhill', 'Capitolhill', 'nyc', 'chapelhill', 'rich', 'richmond', 'richflorida', 'ill', 'il', 'edinburgh', 'sfciviccenter', 'maryland', 'raleigh', 'provo', 'washingtondc', 'tt_georgetown', 'sheridan', 'arch', 'miss', 'durham', 'durham2', 'Durham', 'providence', 'tt_providence', 'lond', 'london', 'manhattan', 'honolulu', 'rexburg', 'valencia', 'gainesville', 'tt_osu', 'tt_numismatic', 'tt_getty', 'tt_harvardernstmayr', 'pretoria', 'RMSC-IIITH', 'CCLHYDERBAD', 'CCLHYDERABAD', 'S.V.Digital LibraryTTD', 'IIIT Hyderabad', 'CCL HYDERABAD', 'sacramento', 'beijing', 'tt_bangalore', 'tt_sok', 'trent', 'guatemala', 'tt_swinburne', 'BookScanUS', 'tt_amnh', 'harrisburg', 'amherst', 'tt_stanfordlaw', 'tt_pem', 'tt_calacademy', 'tt_jakarta', 'hangzhou', 'clemson', 'Osmania University', 'clarksville', 'tt_victoria', 'poughkeepsie', 'tt_warwick', 'tt_riks', '1dollarscan (zLibro)']
    remainders = ['tt_stlouis', 'saltlakecity',  'tt_louisville', 'tt_oberlin', 'tt_clatsopcounty',  'brussels', 'tt_harrisburg', 'tt_statenisland', 'utah', 'hbl_storrs', 'tt_perkins',  'tt_harvardwidener', 'Hong Kong', 'George Blood, L.P.', 'AP Press Academy Archives', 'hamilton', 'tt_nybg', 'mobot',  'bali']
    metadata_fields = ['donor', 'imagecount', 'mediatype', 'operator', 'scandate', 'scanner', 'shipping_container', 'sponsor']
    # for this_id in tqdm.tqdm(center_ids):
    for this_id in tqdm.tqdm(remainders):
        path = "/Volumes/Samsung_T5/scanning_labor_in_IA/scancenter-data/" + str(this_id) + "-data"
        try:
            os.mkdir(path)
        except OSError:
            pass
        for metadata_field in metadata_fields:
            r = requests.get(
            "https://archive.org/advancedsearch.php?q=scanningcenter%3A" + str(this_id) +
            "&fl%5B%5D=identifier&fl%5B%5D=" + metadata_field + "&rows=6000000&output=csv&callback=callback&save=no")
            # change the path on your machine if you want this to work!
            file_path = "/Volumes/Samsung_T5/scanning_labor_in_IA/scancenter-data/"+str(this_id) +"-data/" + str(this_id) +"-" +metadata_field+ ".csv"
            open(file_path, "wb").write(r.content)

def gets_collection_data():
    # not all the collections but pretty large ones that don't seem to bew accounted for in other collections
    
    collection_ids = ['americana', 'printdisabled', 'internetarchivebooks', 'inlibrary', 'booksbylanguage_arabic', 'booksbylanguage', 'JaiGyan', 'digitallibraryindia', 'toronto', 'folkscanomy', 'biodiversity', 'europeanlibraries', 'china','newspapers']
    metadata_fields = ['scanningcenter']
    # for this_id in tqdm.tqdm(center_ids):
    for this_id in tqdm.tqdm(collection_ids):
        for metadata_field in metadata_fields:
            r = requests.get(
            "https://archive.org/advancedsearch.php?q=collection%3A" + str(this_id) +
            "&fl%5B%5D=identifier&fl%5B%5D=" + metadata_field + "&rows=6000000&output=csv&callback=callback&save=no")
            # path- change if you want to work on your machine
            file_path = "/Volumes/Samsung_T5/scanning_labor_in_IA/collection-data/"+str(this_id)+ '-' +metadata_field+ ".csv"
            open(file_path, "wb").write(r.content


def makes_results_csv(results, outfile_name):
    headers = results[0].keys()
    rows = results
    print(rows)
    with open(outfile_name, 'w', encoding='UTF-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)

        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)
            except AttributeError:
                pass
def get_metadata(id):
    metadata = ia.get_item(id).metadata
    return {"id": id,
            "sponsor": get_sponsor(metadata),
            "scandate": get_scandate(metadata),
            "donor": get_donor(metadata),
            "scanner": get_scanner(metadata),
            "shipping_container": get_shipping_container(metadata),
            "operator": get_operator(metadata),
            "imagecount": get_imagecount(metadata),
            "scanningcneter": "hongkong"}


def get_scanner(metadata):
    try:
        return metadata['scanner']
    except KeyError:
        return ""


def get_shipping_container(metadata):
    try:
        return metadata['shipping_container']
    except KeyError:
        return ""


def get_operator(metadata):
    try:
        return metadata['operator']
    except KeyError:
        return ""

def get_imagecount(metadata):
    try:
        return metadata['imagecount']
    except KeyError:
        return ""


def get_sponsor(metadata):
    try:
        return metadata['sponsor']
    except KeyError:
        return ""


def get_donor(metadata):
    try:
        return metadata['donor']
    except KeyError:
        return ""


def get_scandate(metadata):
    try:
        return metadata['scandate']
    except KeyError:
        return ""


def json_unpacking(json_file):
    with open(json_file, 'r') as f:
        ids = json.load(f)
    return ids["docs"]


gets_scancenter_data()
# gets_collection_data()
