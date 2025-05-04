import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Function to load data from CSV file
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully with {len(df)} rows.")
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

# Function to summarize the data
def summarize_data(df):
    print("Basic summary:")
    print(df.describe(include='all'))
    print("\nMissing values:")
    print(df.isnull().sum())

# Function to plot top N districts by average commits
def plot_top_districts(df, top_n=10):
    # Ensure the 'plots' directory exists
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # Sort the data by average commits and select top N districts
    sorted_df = df.sort_values(by='avg_commits', ascending=False).head(top_n)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=sorted_df, x='district', y='avg_commits', palette='magma')
    plt.title(f'Top {top_n} Districts by Average Commits')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot in 'plots/' folder
    plt.savefig('plots/top_districts.png')
    plt.close()  # Close the plot to avoid showing

# Function to plot correlation matrix
def correlation_matrix(df):
    # Ensure the 'plots' directory exists
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # Create the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.tight_layout()

    # Save the plot in 'plots/' folder
    plt.savefig('plots/correlation_matrix.png')
    plt.close()  # Close the plot to avoid showing

