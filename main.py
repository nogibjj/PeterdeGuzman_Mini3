# import packages
from mylib.lib import (
    read_congressdata,
    mean_age,
    median_age,
    std_age,
    generate_hist_member_age_bycongress,
)


def main(url):
    # load data with custom function
    df = read_congressdata(url)
    # summary statistics
    print(f"The mean age in this dataset is {mean_age(df):.2f}.")
    print(f"The median age in this dataset is {median_age(df):.2f}.")
    print(f"The standard deviation of age in this dataset is {std_age(df):.4f}.")
    # generate histogram of age distribution
    generate_hist_member_age_bycongress(df, 113, "113th_congress")


if __name__ == "__main__":
    url = "https://github.com/fivethirtyeight/data/blob/master/congress-age/congress-terms.csv?raw=true"
    main(url)
