from pathlib import Path
import requests


def save_pdfs_locally(sites, filenames):
    """
    acquires data from a list of sites and saves the files locally

    Args:
        sites: a list of links for the PDFs
        filenames: a list of filenames for the corresponding PDFs

    Returns:
        locally saved PDFs in the root directory
    """
    for i, site in enumerate(sites):
        file_name = Path(filenames[i])
        url = site
        response = requests.get(url)
        file_name.write_bytes(response.content)
    return print("files saved locally")
