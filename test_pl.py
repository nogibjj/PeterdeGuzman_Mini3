import zipfile

import polars as pl

# update data source so it can be read in polars

file_zip = "https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvoter8.zip"
file_txt = "ncvoter32.txt"


def read_csv_ncvoterdata(file_txt):
    return pl.read_csv(file_txt, has_header=True, encoding="utf8")


with zipfile.ZipFile(file_zip) as z:
    with z.open(file_txt) as f:
        df = read_csv_ncvoterdata(f)
