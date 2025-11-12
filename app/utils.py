import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load CSV file into a DataFrame."""
    df = pd.read_csv(filepath)
    return df

def plot_boxplot(df, metric, countries):
    """Generate a boxplot for a selected metric and countries."""
    df_filtered = df[df['Country'].isin(countries)]
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df_filtered, x='Country', y=metric, palette='Set2')
    plt.title(f'{metric} Distribution by Country')
    plt.tight_layout()
    return plt

def plot_bar(df, metric, countries):
    """Generate a bar chart for average metric values per country."""
    df_filtered = df[df['Country'].isin(countries)]
    avg_values = df_filtered.groupby('Country')[metric].mean().sort_values(ascending=False)
    plt.figure(figsize=(6,4))
    sns.barplot(x=avg_values.index, y=avg_values.values, palette='Set2')
    plt.ylabel(f'Average {metric}')
    plt.title(f'Average {metric} by Country')
    plt.tight_layout()
    return plt

def top_regions(df, metric, countries):
    """Return average metric per country."""
    df_filtered = df[df['Country'].isin(countries)]
    top = df_filtered.groupby('Country')[metric].mean().sort_values(ascending=False)
    return top

