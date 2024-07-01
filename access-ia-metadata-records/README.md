# Metadata Collection Method
This folder contains the scripts I used to create the [9 million record dataset](https://wustl.box.com/s/sd9nvxbh3hym7uycia5bul2a7cu4q9rn). 

Each item (be it a book, website, or audio file) uploaded to Internet Archive(IA) contains a metadata record accessible via the Internet Archive API. Metadata fields for an IA are extensive, and there are very few required fields for an upload to work. See the [IA developer documentation](https://archive.org/developers/metadata-schema/i). for more information on fields.  One such field, the “scanningcenter” field indicates at which scanning center an object was scanned for upload into Internet Archive. This field can therefore be used to trace a history of the archive's creation and provide insight into conditions of the human workers who created it. We wrote the scripts contained in this folder to 1) amass as complete a list as possible of all unique "scanningcenter" entries across all IA records, and 2) collect relevant metadata fields for all text records scanned at the scanning centers. 

## Scanning Center Identification
IA does not make public a complete list of all scanning centers, so we had to identify them through sifting through item metadata records. To do so, we queried large collections in Internet Archive and returning only the “scanningcenter” field. I queried the 14 largest texts collections as of June 2023: 
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
following collections using the gets_collection_data function in this python file:  'americana', 'printdisabled', 
Please note that these are not all the collections in Internet Archive. Rather, they are the largest text collections with the fewest overlapping titles as one text can be a member of multiple collections. View the results of these queries here. Using this method, we generated a list of 102 unique entries in the 'scanningcenter' field.
## Metadata Set Collection
On 2023-06-06, we queried the IA API for a list of items that contained one of the 102 values in the “scanningcenter” field and asked it to return the following metadata fields for all matching items: [ id, sponsor, scandate, donor, scanner, shipping_container, operator, imagecount, scanningcenter] using this python script. 
We merged the datasets for each 102 scanning centers into one large texts dataset using the script linked here. 
Finally, we geocoded and merged the dataset. See the locations key and geocoding script. Access the geocoded texts dataset as a csv file here. 

[INSERT MORE ON GEOCODING METHODOLOGY]  We geocoded scanningcenters manually by combing through Internet Archive’s blog - 
The 110 entries in the scanningcenter field to 102 actual scanning center locations (as some of them are duplicates - i.e., il and uiuc both refer to the University of Illinois’ scanning center).
procedure: 
see if all books scanned at a center are part of a single institution’s collection - i.e., all books scanned at ‘tt_stlouis’ are part of Washington University in St. Louis’s IA collection (this is usually the case) - then assign lat/lon coordinates based on that institution’s location
reference IA’s 990 tax return records + bills of lading for a matching name or location. For example, IA has a contract with a company called Innodata that has a location in Cebu, Philippines. So, we geocode the ‘cebu’ center to Innodata Knowledge Service’s Mandaue City location.
Missing data
We only have 9 million records; there are 37 million in IA. Part of me wonders if this is because the rest don’t  have a scanningcenter metadata field. The ‘scanningcenter’ field is not required for upload. When I’ve uploaded items to the IA from my machine (not as a worker in a scanning center), I didn’t supply a ‘scanningcenter’ field. Here’s an example of an IA record that I uploaded using the IA Python library. 
