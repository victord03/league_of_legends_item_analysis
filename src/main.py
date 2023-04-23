import logic
import pandas as pd
from input_output import operations as iops


def main():

    # frame[["colA", "colB"]]                                   # retrieve one or more columns
    # frame.loc[i]                                              # retrieve a row (i = index)
    # frame.loc[i] = dict()                                     # add a new row (i = index)
    # frame["Cost per point"] = list()                          # add a new column
    # frame.drop(i)                                             # delete a row (i = index)
    # frame.sort_values(by="col", ignore_index=True)            # does not modify original DF

    # frame = logic.factor_out_one_stat(dark_seal, frame)

    # I/O
    current_path = r"../data/data_frame.csv"

    def save_file(frame: pd.DataFrame, file_path: str) -> None:
        iops.save_to_csv_file(frame, file_path)

    def read_file(file_path: str) -> pd.DataFrame:
        return iops.read_from_csv_file(file_path)

    new_frame = read_file(current_path)

    drain = {"Name": "Drain", "Effect": "Mana Regen", "Amount": 1.1, "Cost per point": int(), "Value type": "Per 5 seconds"}
    # drain = logic.calculate_cost(drain, new_frame)

    def add_a_new_row(frame: pd.DataFrame, new_line: dict) -> pd.DataFrame:
        new_line.pop("Effect")
        new_line.pop("Amount")
        last_index = frame.tail(1).index.item()
        frame.loc[last_index] = new_line
        return frame

    # add_a_new_row(new_frame, drain)
    # new_frame = new_frame.sort_values(by="Cost per point", ignore_index=True)
    print(new_frame)

    # todo: add columns 1) passive: bool 2) resource: str (for "per 5 second" values)

    # new_frame = logic.factor_out_one_stat(, new_frame)

    # save_file(new_frame, current_path)


if __name__ == "__main__":
    main()
