import pandas as pd

def calculate_groupwise_correlations(df, group_col, x_col, y_col):
    correlations = {}
    for group in df[group_col].unique():
        group_data = df[df[group_col] == group]
        correlations[group] = group_data[x_col].corr(group_data[y_col])
    return correlations

def calculate_overall_correlation(df, x_col, y_col):
    return df[x_col].corr(df[y_col])

if __name__ == "__main__":
    df = pd.read_csv("outputs/simpsons_data.csv")
    group_corr = calculate_groupwise_correlations(df, "Group", "X", "Y")
    overall_corr = calculate_overall_correlation(df, "X", "Y")
    with open("outputs/analysis_summary.txt", "w") as file:
        file.write(f"Group-wise correlations: {group_corr}\n")
        file.write(f"Overall correlation: {overall_corr}\n")
