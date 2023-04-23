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
    # frame = pd.DataFrame(my_data, columns=["Name", "Amount", "Cost", "Value type"])

    # frame[["colA", "colB"]]                                   # retrieve one or more columns
    # frame.loc[i]                                              # retrieve a row (i = index)
    # frame.loc[i] = dict()                                     # add a new row (i = index)
    # frame["Cost per point"] = list()                          # add a new column
    # frame.drop(i)                                             # delete a row (i = index)
    # frame.sort_values(by="col", ignore_index=True)            # does not modify original DF

    # frame = logic.calc_cost_per_point_values(frame)

    # frame = logic.factor_out_one_stat(dark_seal, frame)

    # I/O
    current_path = r"../data/data_frame.csv"

    def save_file(frame: pd.DataFrame, file_path: str) -> None:
        iops.save_to_csv_file(frame, file_path)

    def read_file(file_path: str) -> pd.DataFrame:
        return iops.read_from_csv_file(file_path)

    new_frame = read_file(current_path)
    # new_frame = new_frame[["Name", "Cost per point", "Value type"]].sort_values(by="Cost per point", ignore_index=True)

    print(new_frame)

    # save_file(new_frame, current_path)


if __name__ == "__main__":
    main()
