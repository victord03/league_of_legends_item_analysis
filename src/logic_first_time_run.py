import pandas as pd

def initial_calc_cost_per_point_values(raw_dataframe: pd.DataFrame) -> list:
    """Only used the first time the script is run. Runs the function of calculating the CPP."""
    list_of_values = list()

    for row in raw_dataframe.iterrows():
        list_of_values.append(round(row[1]["Cost"] / row[1]["Amount"], 2))

    return list_of_values


def initial_store_cost_per_point_to_dataframe(raw_dataframe: pd.DataFrame, list_of_values: list):
    """Only used the first time the script is run. Runs the function of storing the cost per point to the Df."""
    raw_dataframe["Cost per point"] = list_of_values


def initial_run_calc_and_store_cost_per_point(raw_dataframe: pd.DataFrame):
    """Only used the first time the script is run. Requires manual setup in 'main.py' file but can then be removed
        forever."""
    list_of_values = initial_calc_cost_per_point_values(raw_dataframe)
    initial_store_cost_per_point_to_dataframe(raw_dataframe, list_of_values)
    return raw_dataframe