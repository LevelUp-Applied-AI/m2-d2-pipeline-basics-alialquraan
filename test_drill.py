"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # TODO: Create a pd.Series with at least one NaN value
    # TODO: Call clean_column() on it
    # TODO: Assert no NaN values remain in the result
    # TODO: Assert the NaN was filled with the correct median value
   
    data = pd.Series([1, np.nan, 3]) 
    
    result = clean_column(data)
    
    assert result.isna().sum() == 0  
    assert result[1] == 2.0         

def test_compute_revenue():
    # TODO: Create two small pd.Series (quantity and price)
    # TODO: Call compute_revenue() on them
    # TODO: Assert the result matches the expected element-wise product
    quantity = pd.Series([2, 10])
    price = pd.Series([5, 3])
    
    revenue = compute_revenue(quantity, price)
    
    expected = pd.Series([10, 30])
    pd.testing.assert_series_equal(revenue, expected)