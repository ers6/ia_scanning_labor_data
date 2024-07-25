# READ ME
This GitHub repository contains the scripts used to collect and analyze the dataset underlying the *Scanning Labor in the Internet Archive* project. *Scanning Labor* collects and analyzes book metadata records from Internet Archive (IA) to make visible, reappraise, and highlight inequities faced by Internet Archive scanning workers, or the employees who scan the books encompassing Internet Archive's [text collection](https://archive.org/details/texts).  

The repository holds 4 subdirectories within it: 
- **access-ia-metadata-records**: holding the python scripts for collecting, combining, and geocoding the 9 million record texts dataset 
- **analyze-blog-posts**: holding the scraped Internet Archive blog posts dataset by David Satten-Lopez and a jupyter notebook for exploring it.
- **center_visuals**: contians a notebook for building visualizations of the data for each center and all the centers as a whole. Each center has its own subdirectory containing visualizations of its particular scanning output. 
- **metadata-analysis**:  contains the jupyter notebook in which we calculated measures to approximate the varying degrees of overwork at each scanning center. The subdirectory, **metadata-records-analysis-csvs** contains csv files with the results. 

