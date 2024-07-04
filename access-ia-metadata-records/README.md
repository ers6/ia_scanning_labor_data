# Metadata Collection Method
This folder contains the scripts I used to create the [9 million metadata record dataset](https://wustl.box.com/s/sd9nvxbh3hym7uycia5bul2a7cu4q9rn). 

Each item (be it a book, website, or audio file) uploaded to Internet Archive(IA) contains a metadata record accessible via the Internet Archive API. Metadata fields for an IA are extensive, and there are very few required fields for an upload to work. See the [IA developer documentation](https://archive.org/developers/metadata-schema/i). for more information on fields.  One such field, the `scanningcenter` field indicates at which scanning center an object was scanned for upload into Internet Archive. This field can therefore be used to trace a history of the archive's creation and provide insight into conditions of the human workers who created it. We wrote the scripts contained in this folder to 1) amass as complete a list as possible of all unique `scanningcenter` entries across all IA records, and 2) collect relevant metadata fields for all text records scanned at the scanning centers. 

## Scanning Center Identification
IA does not make public a complete list of all scanning centers, so we had to identify them through sifting through item metadata records. To do so, we queried large collections in Internet Archive and returning only the `scanningcenter` field. We wrote a python script to queried the 14 largest texts collections as of June 2023: 
- 'internetarchivebooks'
- 'inlibrary'
- 'booksbylanguage_arabic'
- 'booksbylanguage'
- 'JaiGyan'
- 'digitallibraryindia'
- 'toronto'
- 'folkscanomy'
- 'biodiversity'
- 'europeanlibraries'
- 'china'
- 'newspapers'

You can locate the script in the gets_collection_data function in [get_center_data.py](https://github.com/ers6/ia_scanning_labor_data/blob/516fe1ad2d14e1fa8e71ba74e31ebf9c349f2329/access-ia-metadata-records/get_center_data.py). Please note that these are not all the collections in Internet Archive. Rather, they are the largest text collections with the fewest overlapping titles as one text can be a member of multiple collections. View the results of [these queries here](https://wustl.app.box.com/folder/271952490091). Using this method, we generated a list of 110 unique entries in the `scanningcenter` field.

## Metadata Set Collection
On 2023-06-06, we queried the IA API for a list of items that contained one of the 110 values in the `scanningcenter` field. For every item with one of the 110 `scanningcenter` values, we collected the following metadata fields: [ id, sponsor, scandate, donor, scanner, shipping_container, operator, imagecount, scanningcenter] using the `gets_center_data` [python function](https://github.com/ers6/ia_scanning_labor_data/blob/99eb04d13bea6a5a9bb153c29f777b5958c16a18/access-ia-metadata-records/get_center_data.py). 
We merged the datasets for each 102 scanning centers into one large texts dataset using the [script linked here](https://github.com/ers6/ia_scanning_labor_data/blob/5b6761ddd5385b9fde53c67d95dfa4e89cbdb47d/access-ia-metadata-records/get_center_data.py). Due to the size of the dataset and IA's API timing out, we gathered data one field at a time and then merged them into one large csv file per center. You can access the csv files for each 102 center (both combined and raw) in [this box folder](https://wustl.box.com/s/nigtbfcot4z17pk3by6h6kbijxtfgla9). 

### Geocoding Methodology
While there are 110 unique entries in the 'scanningcenter' field as of June 2023, we identified 102 unique scanning centers using geocoding methodologies. Geocoding refers to the practice of assigning geographic data to a place name. We geocoded scanningcenters manually by combing through Internet Archive’s blog, identifying if all books scanned at a center were also in an institution's collection, and referncing IA's 990 tax returns and bills of lading. 
#### Blog Posts Example
Internet Archive's blog posts include an article on the establishment of a scanning program at UCLA. Books referenced within the blog post have a 'scanningcenter' field of 'la'. So, we geocode 'la' as UCLA. 

#### Institutional Collection Example
All books with the scanning center values 'il' and 'ill' are part of the University of Illinois at Urbana-Champaign's collection. Therefore, we assumed both represent the same scanning center and assigned latitude and longitude coordinates based on that institution’s location. 

#### Bills of Lading & 990s Example 
IA has a contract with a company called Innodata that has a location in Cebu, Philippines. So, we geocode the ‘cebu’ center to Innodata Knowledge Service’s Mandaue City location.
Finally, we geocoded and merged the dataset. 

See the [locations key](https://github.com/ers6/ia_scanning_labor_data/blob/96391c4acd75f4123cce3abb2aba074cb65de79a/location_key.csv) and [geocoding script](https://github.com/ers6/ia_scanning_labor_data/blob/516fe1ad2d14e1fa8e71ba74e31ebf9c349f2329/access-ia-metadata-records/get_center_data.py). Access the geocoded texts dataset as a [csv file here](https://wustl.box.com/s/etz5tswr99ie7rf5fqlu2lg8gvg3mryb). 

# What's Missing
We only have 9 million text records; there were 37 million text records in IA at the time of data collection. Part of me wonders if this is because the rest don’t  have a scanningcenter metadata field. The ‘scanningcenter’ field is not required for upload. When I’ve uploaded items to the IA from my machine (not as a worker in a scanning center), I didn’t supply a ‘scanningcenter’ field. Here’s an example of an IA record that I uploaded using the IA Python library. 
