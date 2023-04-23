import pandas as pd


def calc_cost_per_point_values(raw_dataframe: pd.DataFrame) -> pd.DataFrame:
    list_of_values = list()
    for row in raw_dataframe.iterrows():
        list_of_values.append(round(row[1]["Cost"] / row[1]["Amount"], 2))

    raw_dataframe["Cost per point"] = list_of_values

    return raw_dataframe


def factor_out_one_stat(
    item_data: dict, cost_per_point_frame: pd.DataFrame
) -> pd.DataFrame:

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
