from analyzer import load_data, summarize_data, plot_top_districts, correlation_matrix

def main():
    file_path = 'district_scores.csv'
    df = load_data(file_path)

    if df is not None:
        summarize_data(df)
        plot_top_districts(df, top_n=10)
        correlation_matrix(df)

if __name__ == "__main__":
    main()
