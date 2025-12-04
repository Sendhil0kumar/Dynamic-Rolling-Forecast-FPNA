import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Generate Dates (3 years monthly)
dates = pd.date_range(start='2022-01-01', periods=36, freq='ME')

# 2. Simulate "Budget" (Steady growth: 2% monthly)
budget = [100000 * (1.02 ** i) for i in range(36)]

# 3. Simulate "Actuals" (Volatile: Budget + Seasonality + Noise)
seasonality = np.sin(np.linspace(0, 3.14 * 6, 36)) * 10000
noise = np.random.normal(0, 5000, 36)
actuals = [b + s + n for b, s, n in zip(budget, seasonality, noise)]

# 4. Create DataFrame
df = pd.DataFrame({'Date': dates, 'Budget': budget, 'Actuals': actuals})

# 5. Add "Variance" Logic
df['Variance'] = df['Actuals'] - df['Budget']
df['Variance_%'] = df['Variance'] / df['Budget']

# Export
print("Data generated for Power BI Analysis.")
