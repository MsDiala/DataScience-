# Forecasting Stock Prices with Seasonal ARIMA
## Introduction
The following code demonstrates how to use Seasonal Autoregressive Integrated Moving Average (SARIMA) to forecast monthly stock prices. The SARIMA model is a popular statistical method for time series analysis and forecasting. It is a variation of the ARIMA model that includes additional parameters to account for seasonality in the data.

## Dependencies
The code uses the following libraries:

`numpy` (v1.20.3): a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
`pandas` (v1.3.3): a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of the Python programming language.
`matplotlib` (v3.4.3): a plotting library for the Python programming language and its numerical mathematics extension NumPy.
`statsmodels` (v0.13.0): a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.

## Data
The dataset used in this code is a text file called "prices.txt". It contains the monthly closing stock prices of a particular company from January 2014 to December 2018.

## Code Overview
The code follows the following steps:

- Import the necessary libraries: `numpy`, `pandas`, `matplotlib`, and `statsmodels`.
- Load the data from the text file using `pandas`.
- Convert the "Date" column to a datetime format and sort the data by date.
- Resample the data to get the mean of the monthly closing stock prices.
- Visualize the time series data using `matplotlib`.
- Decompose the time series into its trend, seasonal, and residual components using `statsmodels`.
- Identify the optimal parameters for the SARIMA model using a grid search.
` Train the SARIMA model using the optimal parameters identified in the previous step .
- Generate forecasts using the trained SARIMA model.
- Visualize the forecasts using `matplotlib`.

## Step-by-Step Guide
- Import the necessary libraries
The following libraries are imported:

- Import necessary libraries:
`
   import warnings
    import itertools
    import numpy as np
    import matplotlib.pyplot as plt
    warnings.filterwarnings("ignore")
    plt.style.use('fivethirtyeight')
    import pandas as pd
    import statsmodels.api as sm
    import matplotlib
`

    - The `warnings` module is used to suppress warnings.
    - The `itertools` module is used to generate all possible combinations of ARIMA parameters.
    - The `numpy` module is used for numerical operations.
    - The `matplotlib` and pyplot modules are used for plotting and visualization.
    - The `pandas` module is used for data manipulation and analysis.
    - The `statsmodels` module is used for statistical modeling.
- Set matplotlib parameters:
`matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
`
These lines set the size and font of the axis labels and tick labels in matplotlib plots.

- Read in the data:
`df = pd.read_csv('prices.txt')
stock=df
`
This reads in a CSV file of stock prices and stores it in a pandas DataFrame called df.
The stock DataFrame is a copy of df.

- Explore the data:
`stock.head()
stock['Date'].min()
stock['Date'].max()
`
These lines display the first few rows of the DataFrame and the minimum and maximum dates in the Date column.

- Prepare the data:
`stock.Date = pd.to_datetime(stock.Date, format='%Y%m%d', errors='ignore')
stock = stock.sort_values('Date')
stock.isnull().sum()
stock = stock.groupby('Date')['Price'].sum().reset_index()
stock = stock.set_index('Date')
stock.index
stock.index = pd.to_datetime(stock.index)
monthly_mean = stock.Price.resample('M').mean()
monthly_mean['2018':]
`

    - These lines convert the `Date` column to a datetime format and sort the DataFrame by date.
    - The `Price` column is aggregated by month and the mean is taken to create a new time series called `monthly_mean`.
    - The `monthly_mean` time series is resampled at a monthly frequency and missing values are filled with the mean of the previous and next observations.
    - The `monthly_mean` time series is sliced to only include data from 2018 onwards.

- Visualize the time series:
`monthly_mean.plot(figsize=(15, 6))
plt.show()
`
This code creates a line plot of the monthly_mean time series.

- Decompose the time series:
`from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(monthly_mean, model='additive')
fig = decomposition.plot()
plt.show()
`
This code decomposes the monthly_mean time series into its seasonal, trend, and residual components using an additive model.
The seasonal, trend, and residual components are plotted on separate subplots.

- Use a grid search approach to find the best SARIMA model:

`p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
l_param = []
l_param_seasonal=[]
l_results_aic=[]
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(monthly_mean,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility
`

After all models have been fit, we determine the set of parameters that results in the lowest AIC value. We then fit our final SARIMAX model using the optimal parameters and display the model summary using results.summary().tables[1].

`
minimum=l_results_aic[0]
for i in l_results_aic[1:]:
    if i < minimum: 
        minimum = i
i=l_results_aic.index(minimum)
mod = sm.tsa.statespace.SARIMAX(monthly_mean,
                                order=l_param[i],
                                seasonal_order=l_param_seasonal[i],
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()

print(results.summary().tables[1])
`
