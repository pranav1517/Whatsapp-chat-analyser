# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from datetime import datetime

def date_convert(date_string):
    
    date_string = date_string.upper()
    format = '%d/%m/%Y, %I:%M %p - '
    my_date = datetime.strptime(date_string, format)

    # This prints '2009-11-29 03:17 AM'
    return str(my_date)
    

def getdata(data):


    # regular expression pattern for splitting text data
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\w{2}\s-\s'

    # getting names from data
    messages = re.split(pattern,data)
    # 0th element is empty string hence we consider from 1
    messages = messages[1:]

    # getting dates from data
    dates = re.findall(pattern,data)

    # creating dataframe which contains messages and dates as columns
    df = pd.DataFrame({'user_message':messages,'datetime':dates})
    df['datetime'] = df['datetime'].apply(date_convert)
    df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')
 

    # creating new columns from datetime column
    df['date'] = df['datetime'].dt.date
    df['year'] = df['datetime'].dt.year
    df['month_num'] = df['datetime'].dt.month
    df['month'] = df['datetime'].dt.month_name()
    df['day_num'] = df['datetime'].dt.day
    df['day'] = df['datetime'].dt.day_name()
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute

    # getting list of users and messages from user_message column
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]: # checking for users
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group-notification')
            messages.append(entry[0])
    
    # creating new columns of users and messages list
    df['user'] = users
    df['message'] = messages

    # droping the user_message column now that we have separate columns for user and messages
    df.drop(['user_message'],axis=1,inplace=True)
    df.drop(['datetime'],axis=1,inplace=True)

    cols = ['user', 'message', 'date', 'year', 'month_num', 'month', 'day_num', 'day','hour', 'minute']
    df = df[cols]

    period = []
    for hour in df[['day', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df





