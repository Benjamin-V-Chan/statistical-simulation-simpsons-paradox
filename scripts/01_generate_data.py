import numpy as np
import pandas as pd

def generate_simpsons_data(samples_per_group, group_effects):
    data = []
    for group_id, (slope, intercept) in enumerate(group_effects):
        x = np.random.uniform(0, 100, samples_per_group)
        y = slope * x + intercept + np.random.normal(0, 10, samples_per_group)
        group_data = pd.DataFrame({
            "Group": [group_id + 1] * samples_per_group,
            "X": x,
            "Y": y
        })
        data.append(group_data)
    return pd.concat(data, ignore_index=True)

if __name__ == "__main__":
    samples_per_group = 100
    group_effects = [(0.5, 10), (-0.3, 20), (0.2, -5)]
    df = generate_simpsons_data(samples_per_group, group_effects)
    df.to_csv("outputs/simpsons_data.csv", index=False)
