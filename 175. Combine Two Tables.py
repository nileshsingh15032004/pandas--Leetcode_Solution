import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged_df = person.merge(address, on='personId', how='left')
    result_df = merged_df[['firstName', 'lastName', 'city', 'state']]
    return result_df
