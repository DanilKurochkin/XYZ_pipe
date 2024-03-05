import numpy as np
import pandas as pd

def merge_xyz(xy : pd.DataFrame, z : pd.DataFrame, params):
    z *= params['Z_scaler']
    merged_df = pd.concat([xy, z], axis=1)
    merged_df.fillna(value=0)
    
    return merged_df

def calculate_length(df : pd.DataFrame):
    df['Length'] = np.sqrt(df['Length']**2 + df['Z']**2)
    df = df[['X', 'Y', 'Z', 'Length']]
    
    return df