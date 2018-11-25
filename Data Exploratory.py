# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 01:14:07 2018

@author: Jacky
"""
# =============================================================================
# see how many numeric and categorical variables are out there
# =============================================================================
categorical_list = []
numerical_list = []
for i in application.columns.tolist():
    if application[i].dtype=='object':
        categorical_list.append(i)
    else:
        numerical_list.append(i)
print('Number of categorical features:', str(len(categorical_list)))
print('Number of numerical features:', str(len(numerical_list)))

# =============================================================================
# explore culumn appearance by time
# =============================================================================
# Function to plot time series data
def plot_vs_time(data_frame, column, calculation='mean', span=10):
    if calculation == 'mean':
        group_temp = data_frame.groupby('date')[column].mean().reset_index()
    if calculation == 'count':
        group_temp = data_frame.groupby('date')[column].count().reset_index()
    if calculation == 'nunique':
        group_temp = data_frame.groupby('date')[column].nunique().reset_index()
    group_temp = group_temp.ewm(span=span).mean()
    fig = plt.figure(figsize=(10,3))
    plt.plot(group_temp['date'], group_temp[column])
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.title('%s versus time' %column)
plot_vs_time(news_train_df, 'sourceId', calculation='count', span=10)
plt.title('News count vs time')
plt.ylabel('Count')

# =============================================================================
# find out missing data
# =============================================================================
def find_missing(data):
    # number of missing values
    count_missing = data.isnull().sum().values
    # total records
    total = data.shape[0]
    # percentage of missing
    ratio_missing = count_missing/total
    # return a dataframe to show: feature name, # of missing and % of missing
    return pd.DataFrame(data={'missing_count':count_missing, 'missing_ratio':ratio_missing}, index=data.columns.values)
find_missing(application_train).head(12)

# =============================================================================
# remove outliers
# =============================================================================
# Function to remove outliers
def remove_outliers(data_frame, column_list, low=0.02, high=0.98):
    temp_frame = data_frame
    for column in column_list:
        this_column = data_frame[column]
        quant_df = this_column.quantile([low,high])
        low_limit = quant_df[low]
        high_limit = quant_df[high]
        temp_frame[column] = data_frame[column].clip(lower=low_limit, upper=high_limit)
    return temp_frame






















