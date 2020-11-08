from pathlib import Path
import requests
import tabula
import pandas as pd


def save_pdfs_locally(sites, filenames, folder):
    """
    acquire data from a list of sites and save the files locally

    Args:
        sites: a list of links for the PDFs
        filenames: base filenames for the corresponding PDFs
                    as strings in a list
        folder: the folder name within the root directory
                to save files in as a string

    Returns:
        locally saved PDFs in the root directory
    """
    for i, site in enumerate(sites):
        file_name = Path('{0}/{1}.pdf'.format(folder, filenames[i]))
        url = site
        response = requests.get(url)
        file_name.write_bytes(response.content)


def pdf_to_dataframe(pdf_names, folder_origin, folder_final,
                     area=None, stream=False):
    """
    extract tables from pdfs and save as csv files

    Args:
        pdf_names: the names of pdf files as strings in a list
        folder_origin: the name of the folder the pdfs are in
        folder_final: the name of the folder to save csv files in
        area: area of PDF tDo focus on if applicable with coordinates in a set
        stream: put True if tables are without gridlines

    Returns:
        locally saved csv files
    """
    for files in pdf_names:
        pdf_file = Path('{0}/{1}.pdf'.format(folder_origin, files))
        table = tabula.read_pdf(pdf_file, area=area,
                                pages=1, stream=stream, silent=True)
        table = table[0]
        csv_name = Path('{0}/{1}.csv'.format(folder_final, files))
        table.to_csv(csv_name, index=False, header=False)


def store_all_files_locally():
    """
    Has lists of all pdf sites and list of names for each file.
    Run all files through save_pdf_locally function.
    """
    sites = ["https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2008_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2009_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2010_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2011_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2012_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2013_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/production_size/"
             "2014_brew_prod_size_ttb_gov.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2008/200812beer.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2009/200912beer.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2010/201012beer.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2011/201112beer.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2012/201212beer.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2013/201312beer.pdf",
             "https://www.ttb.gov/images/pdfs/statistics/2014/201412beer.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/kk91fp42q/ft848t498/hops-12-18-2008.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/z603r129r/kh04ds58d/hops-12-18-2009.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/gf06g547j/1j92gb498/hops-12-17-2010.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/kp78gk52g/sb397c25c/hops-12-21-2011.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/p2676z23j/5t34sn67z/hops-12-17-2012.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/s4655k17x/6682x7013/hops-12-17-2014.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/736667257/mg74qq22v/hops-12-17-2015.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/x346d6868/sx61dp955/hops-12-16-2016.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/8910jx41k/df65vb71z/hops-12-19-2017.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/2801pm326/1831cq318/hopsan18.pdf",
             "https://downloads.usda.library.cornell.edu/usda-esmis/files/"
             "s7526c41m/37720v08z/v405sr612/hopsan19.pdf"]
    filenames = ["NumBrewers2008", "NumBrewers2009", "NumBrewers2010",
                 "NumBrewers2011", "NumBrewers2012", "NumBrewers2013",
                 "NumBrewers2014", "Materials2008", "Materials2009",
                 "Materials2010", "Materials2011", "Materials2012",
                 "Materials2013", "Materials2014", "Hops2008",
                 "Hops2009", "Hops2010", "Hops2011", "Hops2012",
                 "Hops2014", "Hops2015", "Hops2016", "Hops2017",
                 "Hops2018", "Hops2019"]

    save_pdfs_locally(sites, filenames, "PDFData")


def clean_hop_csv():
    """
    cleans imperfections in hop data from using tabula library
    """
    for year in range(2008, 2020, 1):
        csv_name = Path('ExtractedCSV/Hops{0}.csv'.format(year))
        if year == 2013:
            continue
        # format of PDFs change after 2009, those files are cleaned differently
        if year > 2009:
            data = pd.read_csv(csv_name, names=["year", "acres harvested", "1",
                                                "2", "yield per acre(1000 lbs)",
                                                "production", "3",
                                                "$ per lb avg",
                                                "total value ($1000)"])
            data = data[21:24]
            # removes empty columns
            data = data.drop(columns=["1", "2", "3"])
            data.to_csv(csv_name, index=False, header=True)

        else:
            data = pd.read_csv(csv_name, names=["year", "1", "acres harvested",
                                                "yield per acre(1000 lbs)",
                                                "production",
                                                "$ per lb avg",
                                                "total value ($1000)"])
            data = data[21:24]
            data = data.drop(columns=["1"])
            data.to_csv(csv_name, index=False, header=True)
