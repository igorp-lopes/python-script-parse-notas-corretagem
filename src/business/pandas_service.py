import pandas as pd

from core.constants import OUTPUT_TABLE_FILENAME
from core.directory_utils import get_outputs_folder


def get_table_file():
    outputs_folder = get_outputs_folder()
    try:
        df = pd.read_csv(outputs_folder + OUTPUT_TABLE_FILENAME)
    except FileNotFoundError:
        df = pd.DataFrame()

    return df
