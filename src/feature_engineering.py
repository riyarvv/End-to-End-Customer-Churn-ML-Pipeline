import pandas as pd 
import numpy as np

def create_new_customer_feature(df):
    """
    Create a binary feature indicating whether a customer is new.
    Customers with tenure less than or equal to 12 months are considered new.
    """
    df["NewCustomer"]=(df["tenure"]<=12).astype(int)
    return df 

def create_tenure_group(df):
  
    bins = [0,12,24,48,72]

    labels = [
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-72 Months"
    ]

    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    return df

def create_monthlyCharge_classifier(df):
    """
    Identifies customers having monthly charges greater than the median value
    """
    median_charge = 70

    df["HighMonthlyCharges"] = (
      df["MonthlyCharges"] > median_charge
    ).astype(int)

    return df 



