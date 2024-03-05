import numpy as np
import pandas as pd


def merge_xyz(x : pd.DataFrame, y : pd.DataFrame, z : pd.DataFrame):
    merged_df = pd.concat([x, y, z], axis=1)
    null_counter = pd.DataFrame(merged_df.isna().sum()).transpose()
    
    merged_df.fillna(value=0)
    
    return merged_df, null_counter

#пересчитываем длину уже для трехмерной системы коориднат
def calculate_length(df : pd.DataFrame):
    df['Length'] = np.sqrt(df['X']**2 + df['Y']**2 + df['Z']**2)
    df = df[['X', 'Y', 'Z', 'Length']]
    
    return df