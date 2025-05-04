import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully with {len(df)} rows.")
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

def summarize_data(df):
    print("Basic summary:")
    print(df.describe(include='all'))
    print("\nMissing values:")
    print(df.isnull().sum())

def plot_top_districts(df, top_n=10):
    sorted_df = df.sort_values(by='avg_commits', ascending=False).head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=sorted_df, x='district', y='avg_commits', palette='magma')
    plt.title(f'Top {top_n} Districts by Average Commits')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/top_districts.png')
    plt.show()

def correlation_matrix(df):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig('plots/correlation_matrix.png')
    plt.show()
