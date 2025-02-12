import pandas as pd
import numpy as np

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Salary': [70000, 80000, 60000, 95000]
}

df = pd.DataFrame(data)

# Print summary statistics
print(df.describe())
