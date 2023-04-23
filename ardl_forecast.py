import pickle
#Import the required modules for data generation
import numpy as np

#Import the required modules for plot creation:
import matplotlib.pyplot as plt

#Import the required modules for DataFrame creation:
from statsmodels.tsa.ardl import ARDL
from statsmodels.tsa.ardl import ardl_select_order
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

with open('mts', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    data = pickle.load(f)


cities_dict = {}
# Define the start and end dates
start_date = '2004-01-01'
end_date = '2021-12-31'

for key, df in data.items():
    filtered_df = df.copy()
    filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
    filtered_df.fillna(method='ffill', inplace=True)  # Forward-fill
    filtered_df.fillna(method='bfill', inplace=True)  # Backward-fill
    filtered_df = filtered_df.asfreq('MS')  # Set the frequency to Month Start
    cities_dict[key] = filtered_df


one_city = cities_dict.get("Austin, TX")

#explanatory variables
exog_var = ['value_income', 'value_unemployment', 'value_gdp', 'value_population', 'value_crime',
           'value_tax', 'value_cpi', 'value_interest']


# function to run the ardl model
def run_ardl(data, exog_var):
    
    # run the adf and kpss test to determine stationary of exog variables
    for x in exog_var:
        adftest = adfuller(data[[x]], autolag="AIC")
        
        # dftest[1] is the p-value and if p-value is less than 0.05 then passes the test
        # value can be nan
        # if failed test then move on to kdf test
        # if failed kdf test then variable rejected
        # else variable is accepted 
        
        if (np.isnan(adftest[1]) or adftest[1] > 0.05):
            
            # remove variable because failed test
            if (np.isnan(adftest[1])):
                exog_var.remove(x)
            
            else:
                kpsstest = kpss(data[[x]], regression="c", nlags="auto")
                
                # remove variable because failed test
                if (np.isnan(kpsstest[1]) or kpsstest[1] > 0.05):
                    exog_var.remove(x)
                    
           
    # apply the ardl_model
    # split data into testing and training data
    # run ardl model on training data   
    train = data[ : int(len(data) * 0.8)]
    test = data[ int(len(data) * 0.8) : ]
       
    # setting the explanatory variables
    exog = train[exog_var]
    exog_oo = test[exog_var]
    
    # running ardl model for time purposes!!!
    #model = ARDL(train.value, 3, exog, 3)
    #ardl_model = model.fit()
    #print(ardl_model.summary())
    
    # using ardl_select_order to run the model 
    # may be hinder by time constraint
    sel_res = ardl_select_order(
        train.value, 3, exog, 3, ic="aic", trend="c"
    )
    ardl_model = sel_res.model.fit()
    print(ardl_model.summary())
    
    # predict housing prices with ardl model
    # compare between testing data and prediction result using ardl model
    p = ardl_model.predict(start = len(train), end = len(data) - 1, exog_oos = exog_oo)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(test['value'], label = 'actual')
    ax[0].plot(p, color='red', label = 'prediction')

    ax[1].plot(test['value'] - p)
    
    return 0

run_ardl(one_city, exog_var)

