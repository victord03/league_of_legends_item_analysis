import pandas as pd


def calc_cost_per_point_values(raw_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Only used the first time the script is run. Requires manual setup in 'main.py' file but can then be removed
    forever."""
    list_of_values = list()
    for row in raw_dataframe.iterrows():
        list_of_values.append(round(row[1]["Cost"] / row[1]["Amount"], 2))

    raw_dataframe["Cost per point"] = list_of_values

    return raw_dataframe


def calculate_cost(effect: dict, frame: pd.DataFrame, passive: bool) -> dict:
    """Given an 'effect' dict (see specific structure below) containing a known stat and the DataFrame, this function
    will populate the 'Cost per point' value in the 'effect' dict for later use.

    effect = {
        "Name": "",
        "Resource": "EXISTANT STAT",
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
        effect["Cost per point"] = int(row["Cost per point"]) * amount
        effect["Cost"] = "-"
    else:
        effect["Cost per point"] = "-"
        effect["Cost"] = int(row["Cost per point"]) * amount

    return effect

def factor_out_one_stat(
    item_data: dict, cost_per_point_frame: pd.DataFrame
) -> pd.DataFrame:
    """Given an item that provides however many known stats PLUS one other of unknown 'Cost per point', it will factor
    out all the known items, in order to calculate the value of the unknown stat. It will append it to the DataFrame."""

    # todo: need to separate iterations in two parts: one for stats, a second for passives

    total_cost_of_the_item = item_data.pop("Cost")
    value_type = item_data.pop("Value type")
    item_data_copy = item_data.copy()

    for key in item_data:

        if key in list(cost_per_point_frame["Name"]):
            index = list(cost_per_point_frame["Name"]).index(key)
            cost_per_point_of_stat = cost_per_point_frame.iloc[index]["Cost per point"]
            total_cost_of_the_item -= cost_per_point_of_stat * item_data[key]
            item_data_copy.pop(key)

    result_key = list(item_data_copy.keys())[0]
    result_value = round(total_cost_of_the_item / list(item_data_copy.values())[0], 2)

    frame_last_index = cost_per_point_frame.tail(1).index.item()
    cost_per_point_frame.loc[frame_last_index + 1] = {
        "Name": result_key,
        "Cost per point": result_value,
        "Value type": value_type,
    }

    return cost_per_point_frame


def quantify_a_passive_from_a_known_stat(new_effect: dict, frame: pd.DataFrame, passive: bool) -> pd.DataFrame:
    """Given a passive has correctly been translated to a single, known stat, this function will calculate its
    'cost per point' and append it to the DataFrame. The 'new_effect' dict has to have the specific keys, shown below

    new_effect = {"Name": "", "Resource": "EXISTANT STAT", "Amount": int(), "Cost per point": int(), "Value type": ""}
    """
    new_effect = calculate_cost(new_effect, frame, passive)
    new_effect.pop("Resource")
    new_effect.pop("Amount")
    last_index = frame.tail(1).index.item()
    frame.loc[last_index] = new_effect
    frame = frame.sort_values(by="Cost per point", ignore_index=True)
    return frame
