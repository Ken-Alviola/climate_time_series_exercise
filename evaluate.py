import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# to evaluated performance using rmse
from sklearn.metrics import mean_squared_error
from math import sqrt 

def evaluate(validate,yhat_df,target_var):
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse

def plot_and_eval(train,validate,yhat_df,target_var):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. 
    it will als lable the rmse. 
    '''
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label='Train', linewidth=1)
    plt.plot(validate[target_var], label='Validate', linewidth=1)
    plt.plot(yhat_df[target_var], label = 'Prediction',lw=2)
    plt.title(target_var)
    plt.legend()
    rmse = evaluate(validate,yhat_df,target_var)
    print(target_var, round(rmse,3))
    plt.show()

# function to store the rmse so that we can compare
def append_eval_df(validate,eval_df,yhat_df,model_type, target_var):
    '''
    this function takes in as arguments the type of model run, and the name of the target variable. 
    It returns the eval_df with the rmse appended to it for that model and target_var. 
    '''
    rmse = evaluate(validate, yhat_df, target_var)
    d = {'model_type': [model_type], 'target_var': [target_var],
        'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)