# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading the stock price data into panda dataframes
intel_data = pd.read_csv("Intel.csv")
nvidia_data = pd.read_csv("Nvidia.csv")
amd_data = pd.read_csv("AMD.csv")

# Summary statistics for each dataset
intel_summary = intel_data.describe()
nvidia_summary = nvidia_data.describe()
amd_summary = amd_data.describe()

# Visual comparison of all 3 dataset plotted on a graph
plt.figure(figsize=(10, 6))
plt.plot(intel_data['date'], intel_data['close'], label='Intel')
plt.plot(nvidia_data['date'], nvidia_data['close'], label='Nvidia')
plt.plot(amd_data['date'], amd_data['close'], label='AMD')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Comparison')
plt.legend()
plt.xticks(
    ticks=intel_data['date'][::len(intel_data)//5],
    labels=intel_data['date'].iloc[::len(intel_data)//5],  # Using dates as labels
    rotation=45  # Rotating labels for better readability
)
plt.show()

# Daily Return Percentage Plot of all 3 datasets
intel_daily_return = intel_data['close'].pct_change()
nvidia_daily_return = nvidia_data['close'].pct_change()
amd_daily_return = amd_data['close'].pct_change()

plt.figure(figsize=(10, 6))
plt.plot(intel_data['date'], intel_daily_return, label='Intel')
plt.plot(nvidia_data['date'], nvidia_daily_return, label='Nvidia')
plt.plot(amd_data['date'], amd_daily_return, label='AMD')
plt.xlabel('Date')
plt.ylabel('Daily Return Percentage')
plt.title('Daily Return Percentage Comparison')
plt.legend()
plt.xticks(
    ticks=intel_data['date'][::len(intel_data)//5],
    labels=intel_data['date'].iloc[::len(intel_data)//5],  # Using dates as labels
    rotation=45  # Rotating labels for better readability
)
plt.show()

# Change in Stock's Price Over Time
intel_price_change = ((intel_data['close'].iloc[-1] - intel_data['close'].iloc[0]) / intel_data['close'].iloc[0]) * 100
nvidia_price_change = ((nvidia_data['close'].iloc[-1] - nvidia_data['close'].iloc[0]) / nvidia_data['close'].iloc[0]) * 100
amd_price_change = ((amd_data['close'].iloc[-1] - amd_data['close'].iloc[0]) / amd_data['close'].iloc[0]) * 100

print("\nChange in Stock's Price Over Time:")
print("Intel:", intel_price_change, "%")
print("Nvidia:", nvidia_price_change, "%")
print("AMD:", amd_price_change, "%")