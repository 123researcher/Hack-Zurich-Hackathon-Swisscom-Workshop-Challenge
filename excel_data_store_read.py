import pandas as pd
import os

def DataStore(name,visiting_place,visiting_time,returning_time)

    if os.path.isfile("user_data.xlsx"):
        df=pd.read_excel("user_data.xlsx")
        df.append([[name,visiting_place,visiting_time, returning_time]])
        df.to_excel("user_data.xlsx",=False)
    else:
        df=pd.DataFrame([[name,visiting_place,visiting_time,returning_time]],
                        columns=[name,visiting_place,visiting_time,returning_time])
        df.to_excel("user_data.xlsx",=False)
