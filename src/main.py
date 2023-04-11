import logic
import data.item_data as data
import pandas as pd


def main():

    stat_flat, stat_percent = logic.create_lol_stats(data.raw_data_flat, data.raw_data_percent)
    my_list = data.raw_data_flat, data.raw_data_percent, stat_flat, stat_percent, stat_flat, stat_percent

    stat_flat_per_gold, stat_percent_per_gold, stats_flat_per_point, stats_percent_per_point = logic.update_cost_per_point_values(*my_list)

    stat_flat_per_gold_sorted = dict(sorted(stat_flat_per_gold.items(), key=lambda x: x[1], reverse=True))
    stat_percent_per_gold_sorted = dict(sorted(stat_percent_per_gold.items(), key=lambda x: x[1], reverse=True))

    stat_flat_per_point_sorted = dict(sorted(stat_flat_per_gold.items(), key=lambda x: x[1]))
    stat_percent_per_point_sorted = dict(sorted(stat_percent_per_gold.items(), key=lambda x: x[1]))

    both_stat_flat_and_percent_per_point = stats_flat_per_point.copy()
    both_stat_flat_and_percent_per_point.update(stats_percent_per_point)

    # print(dict(sorted(both_stat_flat_and_percent_per_point.items(), key=lambda x: x[1])))

    # print(stat_flat_per_point_sorted)
    stat_flat_df = pd.DataFrame(stat_flat_per_point_sorted, index=["Cost per point"])
    # print(stat_flat_df.T)

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
    
    # print(logic.isolate_stat(dark_seal, stat_flat_per_point_sorted))

    print()
    data_df = pd.DataFrame(data.raw_data_flat, columns=["Amount", "Cost", "Value type"])
    #print(data_df.T)

    my_data = [data.hp, data.hp_regen, data.mana, data.mana_regen]
    frame = pd.DataFrame(my_data, columns=["Name", "Amount", "Cost", "Value type"])

    print(frame)
    # print()
    # print(list(zip(frame.Amount, frame.Name)))  # retrieve a column (or more)
    # print()
    # print(frame.loc[1])  # retrieve a row
    frame.loc[4] = data.attack  # add a row
    # frame["Cost per point"] = stat_flat_per_point_sorted  # add a column
    print()
    print(frame)


if __name__ == "__main__":
    main()
