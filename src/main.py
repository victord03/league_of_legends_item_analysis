import logic
from data.item_data import raw_data_flat, raw_data_percent


def main():

    stat_flat, stat_percent = logic.create_lol_stats(raw_data_flat, raw_data_percent)
    my_list = raw_data_flat, raw_data_percent, stat_flat, stat_percent, stat_flat, stat_percent

    stat_flat_per_gold, stat_percent_per_gold, stats_flat_per_point, stats_percent_per_point = logic.update_cost_per_point_values(*my_list)

    stat_flat_per_gold_sorted = dict(sorted(stat_flat_per_gold.items(), key=lambda x: x[1], reverse=True))
    stat_percent_per_gold_sorted = dict(sorted(stat_percent_per_gold.items(), key=lambda x: x[1], reverse=True))

    stat_flat_per_point_sorted = dict(sorted(stat_flat_per_gold.items(), key=lambda x: x[1]))
    stat_percent_per_point_sorted = dict(sorted(stat_percent_per_gold.items(), key=lambda x: x[1]))

    both_stat_flat_and_percent_per_point = stats_flat_per_point.copy()
    both_stat_flat_and_percent_per_point.update(stats_percent_per_point)

    # print(dict(sorted(both_stat_flat_and_percent_per_point.items(), key=lambda x: x[1])))

    print()
    print(stat_flat_per_point_sorted)
    print()

    kindlegem = {
        "Hp": 200,
        "Cdr": 10,
        "Cost": 800,
    }

    dark_seal = {
        "Ap": 15,
        "Hp": 40,
        "Glory Passive": 1,
        "Cost": 350
    }

    pickaxe = {
        "Attack": 25,
        "Cost": 875
    }
    
    print(logic.isolate_stat(dark_seal, stat_flat_per_point_sorted))


if __name__ == "__main__":
    main()
