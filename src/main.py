import logic as lg
import data.items as item_data
from data.db import stat_cost_per_point


def main():

    # frame[["colA", "colB"]]                                   # retrieve one or more columns
    # frame.loc[i]                                              # retrieve a row (i = index)
    # frame.loc[i] = dict()                                     # add a new row (i = index)
    # frame["Cost per point"] = list()                          # add a new column
    # frame.drop(index=i, inplace=True)                         # delete a row in place (i = index)
    # frame.reset_index(drop=True, inplace=True)                # resets the indices after removing a row
    # frame.sort_values(by="col", ignore_index=True)            # does not modify original DF

    db = stat_cost_per_point

    # todo: make the following section modular (reusable function)

    item = item_data.trinity_force
    item_name = item_data.trinity_force["Name"]
    item_cost = item_data.trinity_force["Cost"]

    item2 = item_data.dead_mans_place
    item2_name = item_data.dead_mans_place["Name"]
    item2_cost = item_data.dead_mans_place["Cost"]

    stats_worth = lg.calculate_worth_of_raw_stats(item, db)
    print(f"{item_name} stats worth: {stats_worth:,} (representing {round((stats_worth / item_cost) * 100, 2)}% of the item price).")
    print("Number of passives:", lg.give_number_of_passives(item))
    print("Has Mythic:", lg.has_got_a_mythic(item))

    stats_worth = lg.calculate_worth_of_raw_stats(item2, db)
    print(f"{item2_name} stats worth: {stats_worth:,} (representing {round((stats_worth / item2_cost) * 100, 2)}% of the item price).")
    print("Number of passives:", lg.give_number_of_passives(item2))
    print("Has Mythic:", lg.has_got_a_mythic(item2))


if __name__ == "__main__":
    main()
