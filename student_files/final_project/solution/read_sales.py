from pathlib import Path

import pandas as pd

sales_tx_file = Path('../resources/sales_transactions.csv')


def get_sales(filepath: Path | str = None) -> pd.DataFrame:
    """
    Reads a sales transactions CSV file and returns it as a pandas DataFrame.

    Args:
        filepath (Path | str, optional): The path to the sales transactions CSV file.
                                         Defaults to the predefined sales transactions file.

    Returns:
        pandas.DataFrame: A DataFrame containing the sales transactions data.
    """
    
    if filepath is None:
        filepath = sales_tx_file
    try:
        sales = pd.read_csv(filepath, sep=',')
    except Exception as err:
        print(f'Unable to load data: {err.args[0]}')
        sales = None
    return sales
