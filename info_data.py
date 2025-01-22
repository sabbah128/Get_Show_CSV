import pandas as pd

def basic_data(df):
    numeric_col = [col for col in df.select_dtypes(exclude="O").columns if col != "target"]
    obj_col = df.select_dtypes(include="O").columns.to_list()

    print("Numeric Cols :", numeric_col)
    print("Object Cols : ", obj_col)

    basic_info_dic = {col: 
                {
                    "mean": df[col].mean(), 
                    "median": df[col].median(),
                    "min": df[col].min(),
                    "max": df[col].max(),
                    "missing value": df[col].isnull().sum(),
                } 
        for col in numeric_col}

    return numeric_col, obj_col, basic_info_dic