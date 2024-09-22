# import packages
import zipfile

from mylib.lib import (
    read_csv_ncvoterdata,
    mean_age,
    median_age,
    std_age,
)


def main(file_zip, file_txt):
    # load data with zipfile and custom function
    with zipfile.ZipFile(file_zip) as z:
        with z.open(file_txt) as f:
            df = read_csv_ncvoterdata(f)
    # summary statistics
    print(f"The mean age in this dataset is {mean_age(df):.2f}.")
    print(f"The median age in this dataset is {median_age(df):.2f}.")
    print(f"The standard deviation of age in this dataset is {std_age(df):.4f}.")
    df["Age Group"] = df["age_at_year_end"].apply(recode_age_groups)
    make_categorical_agecat(df)
    # generate histogram of age distribution
    generate_histogram_age(df, "age_histogram")
    # generate population pyramid of age and gender
    generate_age_gender_pyramid(df, "age_gender_pyramid")


if __name__ == "__main__":
    main(file_zip, file_txt)
