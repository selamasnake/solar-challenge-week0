import pandas as pd 

def load_data(file_path):
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', 20)
    return df

def explore_data(df):
    print("Shape of the data:", df.shape)
    print("Info of the data:", df.info())
    print("First 5 rows:", df.head(5))
    print("Data types of the columns:", df.dtypes)

def convert_datatypes(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

#check for missing values
def handle_missing_values(df):
    if (df.isnull().sum()) > 0:
        print(df.isnull().sum() > 0)
    return df

def drop_columns(df):
    df = df.drop(['Comments'], axis=1).copy()
    return df

def remove_negative_values(df):
    df = df[df['GHI'] >= 0]
    df = df[df['DNI'] >= 0]
    df = df[df['DHI'] >= 0]
    return df

def summary_statistics(df):
    return df.describe()

def calculate_zscore(df):
    df_for_zscore = df.drop(['Timestamp'], axis= 1).copy()
    df_zscores = (df_for_zscore - df_for_zscore.mean()) / df_for_zscore.std()
    outliers = df_zscores.abs() > 3
    df['Outliers'] = outliers.any(axis=1)
    outlier_rows = df[df['Outliers'] == True]
    print("Count of rows with outlier values -", df['Outliers'].sum())
    print(outlier_rows.head(5))
    return df_for_zscore

# def update_outliers(df):
#     df_for_zscore = df.drop(['Timestamp'], axis= 1).copy()
#     df_zscores = (df_for_zscore - df_for_zscore.mean()) / df_for_zscore.std()
#     outliers = df_zscores.abs() > 3

#     df_zscore_corrected = df_for_zscore.copy()  
#     mean = df_for_zscore.mean()

#     for column in df_for_zscore.columns:
#         column_mean = mean[column]
#         df_zscore_corrected[column] = df_for_zscore[column].where(~outliers[column], column_mean)

#     df_zscore_corrected['Timestamp'] = df['Timestamp']
#     cols = ['Timestamp'] + [col for col in df_zscore_corrected.columns if col != 'Timestamp']
#     df_zscore_corrected = df_zscore_corrected[cols]
#     df = df_zscore_corrected
#     return df


def main():
    file_path = '../data/benin-malanville.csv'
    df = load_data(file_path)
    explore_data(df)
    convert_datatypes(df)
    handle_missing_values(df)
    drop_columns(df)
    remove_negative_values(df)
    summary_statistics(df)
    calculate_zscore(df)

if __name__ == "__main__":
    main()
    
    
