import pandas as pd
from os import path, chdir

"""
# I/O
current_path = r"../data/data_frame.csv"

def save_file(frame: pd.DataFrame, file_path: str) -> None:
    iops.save_to_csv_file(frame, file_path)

def read_file(file_path: str) -> pd.DataFrame:
    return iops.read_from_csv_file(file_path)

frame = read_file(current_path)

# save_file(frame, current_path)

"""


def save_to_csv_file(my_dataframe: pd.DataFrame, file_path="data_frame.csv") -> None:

    file_exists_message = "\nFile exists, overwrite ?\n> "
    chosen_not_to_overwrite = "\nFile not saved."

    chdir("../data/")

    if path.exists(file_path):
        choice = input(file_exists_message)

        if "y" in choice.lower():
            my_dataframe.to_csv(file_path)
        else:
            print(chosen_not_to_overwrite)

    else:
        my_dataframe.to_csv(file_path, index=False)


def read_from_csv_file(file_path="data_frame.csv") -> pd.DataFrame:
    return pd.read_csv(file_path, index_col=0)
