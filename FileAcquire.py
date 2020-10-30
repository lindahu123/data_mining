from pathlib import Path
import requests
import tabula
import pandas as pd


def save_pdfs_locally(sites, filenames, folder):
    """
    acquires data from a list of sites and saves the files locally

    Args:
        sites: a list of links for the PDFs
        filenames: base filename for the corresponding PDFs

    Returns:
        locally saved PDFs in the root directory
    """
    for i, site in enumerate(sites):
        file_name = Path('{0}/{1}.pdf'.format(folder, filenames[i]))
        url = site
        response = requests.get(url)
        file_name.write_bytes(response.content)
    return print("files saved locally")


def pdf_to_dataframe(pdf_names, folder_origin, folder_final, area=None):
    """
    extracts dataframes from pdfs

    Args:
        file: 

    Returns:
        locally saved csv files
    """
    for files in pdf_names:
        pdf_file = Path('{0}/{1}.pdf'.format(folder_origin, files))
        table = tabula.read_pdf(pdf_file, area=area, pages=1)
        table = table[0]
        csv_name = Path('{0}/{1}.csv'.format(folder_final, files))
        table.to_csv(csv_name, index=False, header=False)
    pass
