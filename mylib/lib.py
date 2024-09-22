# Import Packages
import polars as pl
import matplotlib.pyplot as plt
import os


# Data Loading


# url = "https://github.com/fivethirtyeight/data/blob/master/congress-age/congress-terms.csv?raw=true"


def read_congressdata(url):
    return pl.read_csv(url, has_header=True, truncate_ragged_lines=True)


# Descriptive Statistics
def mean_age(df):
    # calculate mean of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's onlmeany one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].mean()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def median_age(df):
    # calculate median of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].median()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def std_age(df):
    # calculate standard deviation of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].std()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


# Data Visualization


def generate_hist_member_age_bycongress(df, congress, plot_name):
    # create a histogram of ages
    # for Congressional Members as filtered for a specific Congress
    congress_df = df.filter(pl.col("congress") == congress)
    plt.figure(figsize=(10, 6))
    plt.hist(congress_df["age"], bins=20, color="orange", edgecolor="black")
    plt.title(f"Age Distribution of Congress Members for the {congress:.0f}th Congress")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    subfolder = "Output Images"
    file_path = os.path.join(subfolder, plot_name)
    plt.savefig(file_path)
    plt.show()
