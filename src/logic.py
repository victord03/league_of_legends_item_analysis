import pandas as pd


def store_stat_in_df(df: dict, row: pd.DataFrame, amount: float):
    """Part of the 'calculate_cost' function."""
    df["Cost per point"] = int(row["Cost per point"]) * amount
    df["Cost"] = "-"

def store_passive_in_df(df: dict, row: pd.DataFrame, amount: float):
    """Part of the 'calculate_cost' function."""
    df["Cost"] = int(row["Cost per point"]) * amount
    df["Cost per point"] = "-"

def calculate_cost(effect: dict, frame: pd.DataFrame, passive: bool) -> dict:
    """Given an 'effect' dict (see specific structure below) containing a known stat and the DataFrame, this function
    will populate the 'Cost per point' value in the 'effect' dict for later use.

    effect = {
        "Name": "",
        "Resource": "",
        "Amount": int(),
        "Cost per point": int(),
        "Cost": int(),
        "Value type": ""
    }

    """

    search_key = effect["Resource"]
    amount = effect["Amount"]

    index = frame.index[frame["Name"] == search_key].tolist()
    row = frame.loc[index]

    # todo: modification have been made here
    if not passive:
        store_stat_in_df(effect, row, amount)
    else:
        store_passive_in_df(effect, row, amount)

    return effect


def modify_dict_for_factoring_out(my_dict: dict, key1="Cost", key2="Value type") -> tuple:
    """Removes the keys 'Cost' and 'Value type' from the dict to allow for specific calculation."""
    return my_dict.pop(key1), my_dict.pop(key2)

def find_df_new_last_row_index(df: pd.DataFrame) -> int:
    """Give a dataframe, will return the next index that can be used to add a new row using the df.loc[index] method."""
    return df.tail(1).index.item() + 1

def create_df_row(keys: list, values: list) -> dict:
    """Zips key-value pairs to create a dictionary."""
    return dict(zip(keys, values))

def add_a_new_row_to_the_df(df: pd.DataFrame, row: dict, index: int):
    """Give a 'row' dict, adds it to an existing Df, at a specified index."""
    df.loc[index] = row

def adjust_item_cost(df: pd.DataFrame, compare_dict: dict, item_cost: int) -> tuple:

    compare_dict_copy = compare_dict.copy()

    for key in compare_dict:

        if key in list(df["Name"]):
            index = list(df["Name"]).index(key)
            cost_per_point_of_stat = df.iloc[index]["Cost per point"]
            item_cost -= cost_per_point_of_stat * compare_dict[key]
            compare_dict_copy.pop(key)

    return item_cost, compare_dict_copy



def factor_out_one_stat(
    item_data: dict, cost_per_point_frame: pd.DataFrame
) -> pd.DataFrame:
    """Given an item that provides however many known stats PLUS one other of unknown 'Cost per point', it will factor
    out all the known items, in order to calculate the value of the unknown stat. It will append it to the DataFrame."""

    # todo: need to separate iterations in two parts: one for stats, a second for passives

    total_cost_of_the_item, value_type = item_data.pop("Cost"), item_data.pop("Value type")

    total_cost_of_the_item, item_data_copy = adjust_item_cost(cost_per_point_frame, item_data, total_cost_of_the_item)

    result_key = list(item_data_copy.keys())[0]
    result_value = round(total_cost_of_the_item / list(item_data_copy.values())[0], 2)

    new_last_row_index = find_df_new_last_row_index(cost_per_point_frame)

    keys = ["Name", "Cost per point", "Value type"]
    values = [result_key, result_value, value_type]
    new_row_dict = create_df_row(keys, values)

    add_a_new_row_to_the_df(cost_per_point_frame, new_row_dict, new_last_row_index)

    return cost_per_point_frame


# todo: needs to be fixed
def quantify_a_passive_from_a_known_stat(new_effect: dict, frame: pd.DataFrame, passive: bool) -> pd.DataFrame:
    """Given a passive has correctly been translated to a single, known stat, this function will calculate its
    'cost per point' and append it to the DataFrame. The 'new_effect' dict has to have the specific keys, shown below

    new_effect = {
        "Name": "",
        "Resource": "",
        "Amount": int(),
        "Cost per point": int(),
        "Value type": ""
    }
    """
    new_effect = calculate_cost(new_effect, frame, passive)
    new_effect.pop("Resource")
    new_effect.pop("Amount")
    last_index = frame.tail(1).index.item()
    frame.loc[last_index] = new_effect
    frame = frame.sort_values(by="Cost per point", ignore_index=True)
    return frame
