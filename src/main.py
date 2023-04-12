import logic
import data.item_data as data
import pandas as pd
from input_output import operations as iops


def main():

    my_data = [
        data.hp,
        data.hp_regen,
        data.mana,
        data.mana_regen,
        data.armor,
        data.mr,
        data.attack,
        data.ap,
        data.mov_sp,
        data.att_sp,
        data.crit_chance,
    ]
    frame = pd.DataFrame(my_data, columns=["Name", "Amount", "Cost", "Value type"])

    # target_frame = frame[["col1", "col2", "col3]]             # retrieve one or more columns
    # frame.loc[1]                                              # retrieve a row
    # frame.loc[4] = data.attack                                # add a new row
    # frame["Cost per point"] = new_column_data                 # add a new column
    # print(frame.T.sort_values(by="col", ignore_index=True))   # does not modify original DF

    frame = logic.calc_cost_per_point_values(frame)

    kindlegem = {
        "Health": 200,
        "Ability Haste": 10,
        "Cost": 800,
        "Value type": "Flat"
    }

    dark_seal = {"AP": 15, "Health": 40, "Glory": 1, "Cost": 350, "Value type": "Passive"}

    print()
    frame = logic.factor_out_one_stat(dark_seal, frame)
    frame = logic.factor_out_one_stat(kindlegem, frame)

    target_frame = frame[["Name", "Cost per point", "Value type"]]
    target_frame = target_frame.sort_values(by="Cost per point", ignore_index=True)
    # print(target_frame)

    # I/O
    file_path = "data_frame.csv"
    iops.save_to_csv_file(frame, file_path)
    # iops.read_from_csv_file(file_path)


if __name__ == "__main__":
    main()
