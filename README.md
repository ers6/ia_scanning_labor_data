# READ ME
This GitHub repository contains the scripts used to collect and analyze the dataset underlying the *Scanning Labor in the Internet Archive* project. *Scanning Labor* collects and analyzes 9 million book metadata records from Internet Archive (IA) to make visible, reappraise, and highlight inequities faced by Internet Archive scanning workers, or the employees who scan the books encompassing Internet Archive's [text collection](https://archive.org/details/texts).  

The repository holds 4 subdirectories within it: 
- **[access-ia-metadata-records](https://github.com/ers6/ia_scanning_labor_data/tree/main/access-ia-metadata-records)** has the python scripts for collecting, combining, and geocoding the 9 million record texts dataset. The README file in this subdirectory details the methodology for collecting and geocoding the metadata dataset.
- **metadata-analysis**:  contains the jupyter notebook in which we calculated measures to approximate the varying degrees of (over)work at each scanning center. The subdirectory, **metadata-records-analysis-csvs** contains csv files with the results. 
- **center_visuals** holds a notebook for building visualizations of the data for each center and all the centers as a whole. Each center has its own subdirectory containing visualizations of its particular scanning output. 
- **analyze-blog-posts** contains a scraped Internet Archive blog posts dataset by David Satten-Lopez and a jupyter notebook for exploring it.


