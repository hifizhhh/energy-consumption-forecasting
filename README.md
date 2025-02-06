# Energy Consumption Forecasting

## Overview

This project focuses on predicting future energy consumption based on historical data. The goal is to build a model that can accurately forecast energy usage, which can help utility companies optimize energy production and reduce costs.

## Dataset

The dataset used in this project is the **Household Power Consumption Dataset** from the UCI Machine Learning Repository. It contains measurements of electric power consumption in one household with a one-minute sampling rate over a period of almost 4 years.

### Dataset Features

- **Date**: Date in format dd/mm/yyyy.
- **Time**: Time in format hh:mm:ss.
- **Global_active_power**: Household global minute-averaged active power (in kilowatts).
- **Global_reactive_power**: Household global minute-averaged reactive power (in kilowatts).
- **Voltage**: Minute-averaged voltage (in volts).
- **Global_intensity**: Household global minute-averaged current intensity (in amperes).
- **Sub_metering_1/2/3**: Energy sub-metering (in watt-hour of active energy).

## Project Steps

1. **Data Preprocessing**:

   - Handle missing values.
   - Convert data types and extract time-based features.
   - Resample data to a consistent time frequency.

2. **Exploratory Data Analysis (EDA)**:

   - Visualize energy consumption trends.
   - Analyze seasonality and correlations.

3. **Model Building**:

   - Implement time series models like ARIMA, Prophet, and LSTM.
   - Train and evaluate the models.

4. **Model Evaluation**:

   - Use metrics like MAE and RMSE to evaluate model performance.
   - Visualize actual vs. predicted energy consumption.

5. **Model Improvement**:
   - Add additional features (e.g., weather data).
   - Tune hyperparameters and experiment with advanced models.

## How to Run the Code

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/energy-consumption-forecasting.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption) and place it in the `data/` folder.
4. Run the Jupyter Notebook or Python script:
   ```bash
   jupyter notebook energy_consumption_forecasting.ipynb
   ```

## Requirements

The following libraries are required to run the code:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `prophet`
- `tensorflow`
- `scikit-learn`

You can install them using:

```bash
pip install -r requirements.txt
```

## Results

### Model Performance

- **ARIMA**: MAE = X, RMSE = Y
- **Prophet**: MAE = X, RMSE = Y
- **LSTM**: MAE = X, RMSE = Y

### Visualization

![Actual vs Predicted Energy Consumption](images/actual_vs_predicted.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset provided by [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption).
- Inspired by various time series forecasting tutorials and projects.
