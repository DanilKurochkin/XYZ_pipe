import numpy as np
import pandas as pd

def merge_xy(x : pd.DataFrame, y : pd.DataFrame):
    merged_df = pd.concat([x, y], axis=1)
    merged_df.fillna(value=0)
    
    return merged_df

def calculate_length(df : pd.DataFrame):
    df['Length'] = np.sqrt(df['X']**2 + df['Y']**2)
    
    return df