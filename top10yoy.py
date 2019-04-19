import pandas as pd 

def top10parks():
    top10list = pd.read_excel('top10list.xlsx', index_col=0)
    return top10list.to_dict(orient="index")