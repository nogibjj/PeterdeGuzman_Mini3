# Test functions created in main.py script

from test_lib import test_generate_hist_member_age_bycongress
import numpy as np
import polars as pl


if __name__ == "__main__":
    # Load Test Data
    np.random.seed(0)
    n_individuals = 3000
    ages = np.random.randint(80, 114, size=n_individuals)  # Ages between 80 and 113
    parties = np.random.choice(
        ["D", "R", "I"], size=n_individuals
    )  # Randomly assign parties
    congress_numbers = np.random.randint(
        80, 113, size=n_individuals
    )  # Congress numbers from 80 to 113

    # Create a Polars DataFrame
    test_df = pl.DataFrame(
        {"age": ages, "party": parties, "congress": congress_numbers}
    )
    test_generate_hist_member_age_bycongress()

main()
