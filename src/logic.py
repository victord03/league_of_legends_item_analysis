import pandas as pd


# todo: FIX THIS FUNCTION
def isolate_stat(item_data: dict, dataframe_values_per_point: pd.DataFrame):

    item_data_to_modify = item_data.copy()
    removed_stats = dict()

    for stat_name in item_data.keys():

        print("\n", dataframe_values_per_point.loc[1][0])

        if dataframe_values_per_point.loc[1][0] == stat_name:
            removed_stats[stat_name] = item_data_to_modify.pop(stat_name)

    for stat_name, value in removed_stats.items():

        stat_cost = round(dataframe_values_per_point[stat_name] * value, 0)
        item_data_to_modify["Cost"] -= int(stat_cost)

    dict_temp = item_data_to_modify.copy()
    isolated_value_cost = dict_temp.pop("Cost")

    for stat_name, value in dict_temp.items():
        dict_temp[stat_name] = isolated_value_cost / value

    return dict_temp
