import pandas as pd 
import seaborn as sns
import matplotlib.pylab as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', 20)
    return df

def convert_datatypes(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

def summary_statistics(df):
    return df.describe()

def resample_data_h(df):
    df.set_index('Timestamp', inplace=True, drop=False)    
    hourly_data = df.resample('h').mean()
    return hourly_data

def resample_data_m(df):
    df.set_index('Timestamp', inplace=True, drop=False)
    monthly_data = df.resample('ME').mean()
    return monthly_data 

def plot_monthly_radiation(df):
    monthly_data = resample_data_m(df)

    plt.figure(figsize=(12, 6))
    columns = ['GHI', 'DNI', 'DHI']
    colors = ['purple', 'orange', 'teal']

    for column, color in zip(columns, colors):
        sns.lineplot(data=monthly_data, x=monthly_data.index, y=column, label=column, color=color)
        
    plt.title('Solar Radiation over the months')
    plt.xlabel('Time in months')
    plt.ylabel('Solar Radiation (W/m²)')

    plt.show()
    

def main():
    # files = ['benin_prepared.csv', 'togo_prepared.csv', 'sierraleone_prepared.csv']
    # for file in files:
    file_path = f''
    df = load_data(file_path)
    convert_datatypes(df)
    summary_statistics(df)
    resample_data_h(df)
    resample_data_m(df)
    plot_monthly_radiation(df)
    #plot_monthly_data( df)
    

if __name__ == "__main__":
    main()