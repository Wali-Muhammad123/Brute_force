import pandas as pd 
def create_matrix(path):
    df=pd.read_csv(path)
    if len(df)==len(df.columns):
        return df.to_numpy()
    else:
        print("Error")
        return 0
if __name__=='__main__':
    path=r"C:\Users\HP\Desktop\graph.csv"
    df=create_matrix(path)
    print(df)
    df=pd.read_csv(path)
    print(df)