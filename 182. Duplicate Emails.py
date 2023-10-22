import pandas as pd

def duplicate_emails(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.duplicated(subset='email', keep='last')][['email']].drop_duplicates()
