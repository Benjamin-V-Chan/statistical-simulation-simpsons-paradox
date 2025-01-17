import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_scatter_plots(df, group_col, x_col, y_col, output_file):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=group_col, palette="Set2")
    plt.title("Scatter Plot by Group")
    plt.savefig(output_file)
    plt.close()

def create_correlation_line_plot(correlations, output_file):
    groups = list(correlations.keys())
    values = list(correlations.values())
    plt.figure(figsize=(8, 5))
    plt.bar(groups, values, color="skyblue")
    plt.title("Group-wise Correlations")
    plt.xlabel("Group")
    plt.ylabel("Correlation")
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv("outputs/simpsons_data.csv")
    group_corr = {"1": 0.8, "2": -0.5, "3": 0.3}  # Replace with actual results
    create_scatter_plots(df, "Group", "X", "Y", "outputs/scatter_plot.png")
    create_correlation_line_plot(group_corr, "outputs/correlation_plot.png")
