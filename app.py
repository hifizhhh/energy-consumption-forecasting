import pandas as pd

# Load dataset
data = pd.read_csv(
    "C:/Users/aljau/energy-consumption-forecasting/data/household_power_consumption.txt",
    sep=";",
    parse_dates=["Date"],
    infer_datetime_format=True,
)
print(data.head())

data.isnull().sum()
data.fillna(method="ffill", inplace=True)  # Forward fill missing values

data["Global_active_power"] = pd.to_numeric(
    data["Global_active_power"], errors="coerce"
)

data["Hour"] = data["Date"].dt.hour
data["Day_of_week"] = data["Date"].dt.dayofweek
data["Month"] = data["Date"].dt.month

import matplotlib.pyplot as plt

# Plot energy consumption over time
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Global_active_power"])
plt.title("Energy Consumption Over Time")
plt.xlabel("Date")
plt.ylabel("Global Active Power (kW)")
plt.show()

data.groupby("Hour")["Global_active_power"].mean().plot(kind="bar")
plt.title("Averange Energy Consumption by Hour")
plt.xlabel("Hour")
plt.ylabel("Global Active Power (kW)")
plt.show()

import seaborn as sns

sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

train_size = int(len(data) * 0.8)
train, test = data.iloc[:train_size], data.iloc[train_size:]

from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA model
model = ARIMA(train["Global_active_power"], order=(5, 1, 0))  # (p, d, q)
model_fit = model.fit()

from prophet import Prophet

# Prepare data for Prophet
prophet_data = train[["Date", "Global_active_power"]].rename(
    columns={"Date": "ds", "Global_active_power": "y"}
)

# Fit Prophet model
model = Prophet()
model.fit(prophet_data)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np


# Prepare data for LSTM
def create_dataset(data, look_back=24):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i : (i + look_back)])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)


X_train, y_train = create_dataset(train["Global_active_power"].values)
X_test, y_test = create_dataset(test["Global_active_power"].values)

# Build LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], 1)))
model.add(Dense(1))
model.compile(loss="mean_squared_error", optimizer="adam")

# ARIMA
predictions = model_fit.forecast(steps=len(test))

# Prophet
future = model.make_future_dataframe(periods=len(test))
forecast = model.predict(future)

# LSTM
predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(test["Global_active_power"], predictions)
rmse = mean_squared_error(test["Global_active_power"], predictions, squared=False)
print(f"MAE: {mae}, RMSE: {rmse}")

plt.figure(figsize=(12, 6))
plt.plot(test["Date"], test["Global_active_power"], label="Actual")
plt.plot(test["Date"], predictions, label="Predicted")
plt.title("Actual vs Predicted Energy Consumption")
plt.xlabel("Date")
plt.ylabel("Global Active Power (kW)")
plt.legend()
plt.show()
