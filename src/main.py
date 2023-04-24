import logic
import pandas as pd
from input_output import operations as iops
from data import added_items as addi


def main():

    # frame[["colA", "colB"]]                                   # retrieve one or more columns
    # frame.loc[i]                                              # retrieve a row (i = index)
    # frame.loc[i] = dict()                                     # add a new row (i = index)
    # frame["Cost per point"] = list()                          # add a new column
    # frame.drop(index=i, inplace=True)                         # delete a row in place (i = index)
    # frame.reset_index(drop=True, inplace=True)                # resets the indices after removing a row
    # frame.sort_values(by="col", ignore_index=True)            # does not modify original DF

    # I/O
    current_path = r"../data/data_frame.csv"

    def save_file(frame: pd.DataFrame, file_path: str) -> None:
        iops.save_to_csv_file(frame, file_path)

    def read_file(file_path: str) -> pd.DataFrame:
        return iops.read_from_csv_file(file_path)

    new_frame = read_file(current_path)

    new_effect = {
        "Name": "Drain",
        "Resource": "Mana",
        "Amount": 1.1,
        "Cost per point": int(),
        "Cost": int(),
        "Value type": "Per 5 seconds"
    }

    frame_b = new_frame
    frame_b = logic.quantify_a_passive_from_a_known_stat(new_effect, frame_b, passive=True)
    print(frame_b)

    # new_frame = logic.factor_out_one_stat(addi.dorans_ring, new_frame)

    # print()
    # print(new_frame)


    # save_file(new_frame, current_path)


if __name__ == "__main__":
    main()
