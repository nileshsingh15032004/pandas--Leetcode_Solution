import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')
    weather['temp_diff'] = weather['temperature'].diff(periods=1)
    weather['Date_diff'] = weather['recordDate'].diff(periods=1)
    return pd.DataFrame(weather.query("temp_diff >0 and Date_diff =='1 days'").id)
