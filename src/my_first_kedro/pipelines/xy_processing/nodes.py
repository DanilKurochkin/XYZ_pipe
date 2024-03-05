import numpy as np
import pandas as pd

#параметр scaler - есть простой множитель, например x в дюймах, y в футах
#добавил как такую возможность из разных систем измерения точки сводить
def merge_xy(x : pd.DataFrame, y : pd.DataFrame, params):
    x *= params['X_scaler']
    y *= params['Y_scaler']
    merged_df = pd.concat([x, y], axis=1)
    merged_df.fillna(value=0)
    
    return merged_df

#расстояние от нулевой точки СО в декартовой системе координат
def calculate_length(df : pd.DataFrame):
    df['Length'] = np.sqrt(df['X']**2 + df['Y']**2)
    
    return df