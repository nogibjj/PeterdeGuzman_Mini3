# Testing Created Functions with Dataset
# Import Packages
import polars as pl
import os
import numpy as np
import math

from mylib.lib import mean_age, median_age, std_age, generate_hist_member_age_bycongress

# Load Test Data
np.random.seed(0)

# Parameters
n_individuals = 3000
ages = np.random.randint(80, 114, size=n_individuals)  # Ages between 80 and 113
parties = np.random.choice(
    ["D", "R", "I"], size=n_individuals
)  # Randomly assign parties
congress_numbers = np.random.randint(
    80, 113, size=n_individuals
)  # Congress numbers from 80 to 113

# Create a Polars DataFrame
test_df = pl.DataFrame({"age": ages, "party": parties, "congress": congress_numbers})


# Test Analysis Functions
def test_mean_age():
    mean_test = mean_age(test_df)
    assert math.isclose(mean_test, 96.175333, abs_tol=0.005)


def test_median_age():
    median_test = median_age(test_df)
    assert math.isclose(median_test, 96.0, abs_tol=0.01)


def test_std_age():
    std_test = std_age(test_df)
    assert math.isclose(std_test, 9.841013162724245, abs_tol=0.001)


# Test Visualization Functions
def test_generate_hist_member_age_bycongress():
    plot_name = "test_histogram"
    congress = "113"
    generate_hist_member_age_bycongress(test_df, congress, plot_name)
    file_path = os.path.join("Output Images", plot_name)
    test_df.assertTrue(os.path.isfile(file_path), f"{file_path} does not exist.")


if __name__ == "__main__":
    test_mean_age()
    test_median_age()
    test_std_age()
