# data_mining

The main objective of the project was to look at how hop concetration increasing over time and how hop production and price have changed along with it.

The bulk of the code is in the .py files FileAcquire.py and ProcessData.py. FileAquire has the functions that save all the PDFs locally, extract tables from the PDFs and save as CSV files, clean data in CSV files. ProcessData has functions used to process and extract key information from the CSV files. It also has functions to plot the data.

The data sources used are the Tax and Trade Bureau and the USDA.
https://www.ttb.gov/beer/statistics

https://usda.library.cornell.edu/concern/publications/s7526c41m?locale=en#release-items

Libraries used were requests, tabula, pandas, and matplotlib. To install tabula:
pip install tabula-py