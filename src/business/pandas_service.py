import pandas as pd

from core.constants import OUTPUT_TABLE_FILENAME
from core.directory_utils import get_outputs_folder


def export_data_to_csv(data):
    main_df = get_table_file()

    data_to_be_added = pd.DataFrame()
    for table in data:
        new_df = map_data_to_df(table)
        new_df = new_df.astype(str)
        data_to_be_added = merge_dataframes(data_to_be_added, new_df)

    main_df = merge_dataframes(main_df, data_to_be_added)
    save_extracted_data_to_csv(main_df)


def map_data_to_df(data):
    df = pd.DataFrame(data)
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])

    return df


def merge_dataframes(df1, df2):
    if df1.empty:
        return df2

    if df2.empty:
        return df1

    return pd.merge(df1, df2)


def get_table_file():
    outputs_folder = get_outputs_folder()
    output_file_path = outputs_folder + '/' + OUTPUT_TABLE_FILENAME
    try:
        df = pd.read_csv(output_file_path)
    except FileNotFoundError:
        df = pd.DataFrame()

    return df


def save_extracted_data_to_csv(df):
    outputs_folder = get_outputs_folder()
    output_file_path = outputs_folder + '/' + OUTPUT_TABLE_FILENAME
    df.to_csv(output_file_path)
