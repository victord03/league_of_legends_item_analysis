import logic
import data.item_data as data
import pandas as pd


def main():

    my_data = [data.hp, data.hp_regen, data.mana, data.mana_regen, data.armor, data.mr, data.attack, data.ap, data.mov_sp, data.att_sp, data.crit_chance]
    frame = pd.DataFrame(my_data, columns=["Name", "Amount", "Cost", "Value type"])

    # target_frame = frame[["col1", "col2", "col3]]             # retrieve one or more columns
    # frame.loc[1]                                              # retrieve a row
    # frame.loc[4] = data.attack                                # add a new row
    # frame["Cost per point"] = new_column_data                 # add a new column
    # print(frame.T.sort_values(by="col", ignore_index=True))   # does not modify original DF


    def calc_cost_per_point_values(raw_dataframe: pd.DataFrame):
        list_of_values = list()
        for row in raw_dataframe.iterrows():
            list_of_values.append(round(row[1]["Cost"] / row[1]["Amount"], 2))

        raw_dataframe["Cost per point"] = list_of_values

        return raw_dataframe


    frame = calc_cost_per_point_values(frame)
    target_frame = frame[["Name", "Cost per point", "Value type"]]
    target_frame = target_frame.sort_values(by="Cost per point", ignore_index=True)
    print()
    print(target_frame)

    kindlegem = {
        "Health": 200,
        "Cdr": 10,
        "Cost": 800,
    }

    dark_seal = {
        "Ap": 15,
        "Hp": 40,
        "Glory Passive": 1,
        "Cost": 350
    }

    isolated_value = logic.isolate_stat(kindlegem, target_frame)
    print()
    print(isolated_value)

    # stat_flat_df["CDR"] = isolated_value["Cdr"]




if __name__ == "__main__":
    main()
