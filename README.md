# statistical-simulation-simpsons-paradox

## Project Overview

Simpson's Paradox is a statistical phenomenon in which a trend that appears in several different groups of data disappears or reverses when the groups are combined. This paradox often arises in real-world data, such as medical studies, social science research, and sports statistics. The purpose of this project is to simulate and analyze this paradox using synthetic data, providing insight into how it occurs and how to identify it.

### Mathematical Explanation

Consider the relationship between two variables, X and Y, across multiple groups:

1. Within each group:
   - Y is linearly dependent on X: `Y = mX + c + e`, where:
     - `m` is the slope (group-specific).
     - `c` is the intercept (group-specific).
     - `e` is random noise (normally distributed).

2. When combining the groups:
   - The overall correlation between X and Y may differ significantly from the group-specific correlations. This is due to variations in the group slopes (`m`) and intercepts (`c`), as well as the distribution of X across groups.

Simpson's Paradox arises when:
- The direction or magnitude of the relationship between X and Y changes when data is aggregated.
- This reversal can mislead conclusions unless group-specific analyses are conducted.

This simulation generates synthetic datasets to demonstrate the paradox, calculates correlations, and visualizes the results.

---

## Folder Structure

The project is organized as follows:

```
project-root/
├── scripts/                # Contains all Python scripts for the simulation
│   ├── 01_generate_data.py # Script to generate synthetic datasets
│   ├── 02_analyze_data.py  # Script to calculate correlations and identify the paradox
│   └── 03_visualize_data.py # Script to create visualizations of the data
├── outputs/                # Stores results
│   ├── simpsons_data.csv   # Generated dataset
│   ├── analysis_summary.txt # Summary of correlations
│   ├── scatter_plot.png    # Scatter plot of the dataset
│   └── correlation_plot.png # Group-wise correlation plot
├── README.md               # Project documentation
└── requirements.txt        # List of required Python packages
```

---

## Usage

1. **Generate Data:**
   - Run the data generation script to create synthetic datasets:
     ```bash
     python scripts/01_generate_data.py
     ```
   - The generated dataset will be saved as `outputs/simpsons_data.csv`.

2. **Analyze Data:**
   - Calculate correlations and identify the paradox:
     ```bash
     python scripts/02_analyze_data.py
     ```
   - Results will be saved in `outputs/analysis_summary.txt`.

3. **Visualize Data:**
   - Create scatter plots and correlation visualizations:
     ```bash
     python scripts/03_visualize_data.py
     ```
   - Visualizations will be saved in the `outputs/` folder as `.png` files.

---

## Requirements

To run this project, ensure the following requirements are met:

- Python 3.8 or later
- Required Python libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```
  - numpy
  - pandas
  - matplotlib
  - seaborn