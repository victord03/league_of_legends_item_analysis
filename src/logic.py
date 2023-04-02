
def create_lol_stats(raw_data_flat: dict, raw_data_percent: dict) -> tuple:
    flat = {x: float() for x in list(raw_data_flat.keys())}
    percent = {x: float() for x in list(raw_data_percent.keys())}

    return flat, percent


def update_cost_per_point_values(
        raw_data_flat: dict,
        raw_data_percent: dict,
        dict_flat_per_gold: dict,
        dict_percent_per_gold: dict,
        dict_flat_per_point: dict,
        dict_percent_per_point: dict
) -> tuple:

    for stat_name, data in raw_data_flat.items():
        dict_flat_per_gold[stat_name] = round(data["Amount"] / data["Cost"], 2)
        dict_flat_per_point[stat_name] = round(data["Cost"] / data["Amount"], 2)

    for stat_name, data in raw_data_percent.items():
        dict_percent_per_gold[stat_name] = round(data["Amount"] / data["Cost"], 2)
        dict_percent_per_point[stat_name] = round(data["Cost"] / data["Amount"], 2)

    return dict_flat_per_gold, dict_percent_per_gold, dict_flat_per_point, dict_percent_per_point


def isolate_stat(item_data: dict, stats_dict: dict):

    item_data_to_modify = item_data.copy()
    removed_stats = dict()

    for stat_name in item_data.keys():

        if stats_dict.get(stat_name):
            removed_stats[stat_name] = item_data_to_modify.pop(stat_name)

    for stat_name, value in removed_stats.items():

        stat_cost = round(stats_dict[stat_name] * value, 0)
        item_data_to_modify["Cost"] -= int(stat_cost)

    dict_temp = item_data_to_modify.copy()
    isolated_value_cost = dict_temp.pop("Cost")

    for stat_name, value in dict_temp.items():
        dict_temp[stat_name] = isolated_value_cost / value

    return dict_temp
