
from re import M
import pandas as pd


# this function converts a timestamp in HH:MM:SS into an integer # of seconds 
import nacl
from numpy import False_
from regex import F
from sqlalchemy import case


def clean_sleep(df, col):
    ser = df[col].copy()
    for i in range(len(ser)):
        curr_time = ser.iloc[i]
        hours, mins, secs = curr_time.split(':')
        decimal_time = int(hours)*3600 + int(mins)*60 + int(secs)
        ser.iloc[i] = decimal_time
    df[col] = ser
    return df 


# this function converts an integer # of seconds into a string of hours/min/secs
def sec_to_hours(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    d=["{} hours {} mins {} seconds".format(a, b, c)]
    return d

# this function allocates a series for each day of the week
# note: uses the 'fromDate' column to mark when sleep started
# rather than the day when I woke up
def separate_days(df):
    ser = df["fromDate"].copy()
    mon = []
    tues = []
    wed = []
    thurs = []
    fri = []
    sat = []
    sun = []
    for i in range(len(ser)):
        curr_day = ser.iloc[i]
        mon_check = ser.str.contains('Monday', case=False, na=False)
        if mon_check.iloc[i] == True:
            mon.append(df["asleep"].iloc[i])
        tues_check = ser.str.contains('Tuesday', case=False, na=False)
        if tues_check.iloc[i] == True:
            tues.append(df["asleep"].iloc[i])
        wed_check = ser.str.contains('Wednesday', case=False, na=False)
        if wed_check.iloc[i] == True:
            wed.append(df["asleep"].iloc[i])
        thurs_check = ser.str.contains('Thursday', case=False, na=False)
        if thurs_check.iloc[i] == True:
            thurs.append(df["asleep"].iloc[i])
        fri_check = ser.str.contains('Friday', case=False, na=False)
        if fri_check.iloc[i] == True:
            fri.append(df["asleep"].iloc[i])
        sat_check = ser.str.contains('Saturday', case=False, na=False)
        if sat_check.iloc[i] == True:
            sat.append(df["asleep"].iloc[i])
        sun_check = ser.str.contains('Sunday', case=False, na=False)
        if sun_check.iloc[i] == True:
            sun.append(df["asleep"].iloc[i])
    mon = pd.Series(mon)
    tues = pd.Series(tues)
    wed = pd.Series(wed)
    thurs = pd.Series(thurs)
    fri = pd.Series(fri)
    sat = pd.Series(sat)
    sun = pd.Series(sun)
    week = {'Monday':mon, 'Tuesday':tues, 'Wednesday':wed, 'Thursday':thurs, 'Friday':fri, 'Saturday':sat, 'Sunday':sun }
    return week


    # this function also works with each day of the week in individual series
    # the seconds of sleep will be rounded to the nearest hundredth of an hour
    # and then each day of the week's series will be evaluated to determine
    # which day of the week has the most occurences of the mode value (8.78)
def mode_by_day(df):
    M, T, W, R, F, Sa, Su = ([], ) * 7
    curr_col = df["Monday"]
    for i in range(len(df["Monday"])):
        curr_day = df["Monday"].iloc[i]
        hours = round(df["Monday"].iloc[i]/3600, 2)
        M.append(hours)
    M = pd.Series(M).dropna()
    # )print(M)
    curr_col = df["Tuesday"]
    for i in range(len(df["Tuesday"])):
        curr_day = df["Tuesday"].iloc[i]
        hours = round(curr_day/3600, 2)
        T.append(hours)
    T = pd.Series(T).dropna()
    curr_col = df["Wednesday"]
    for i in range(len(df["Wednesday"])):
        curr_day = df["Wednesday"].iloc[i]
        hours = round(curr_day/3600, 2)
        W.append(hours)
    W = pd.Series(W).dropna()
    curr_col = df["Thursday"]
    for i in range(len(df["Thursday"])):
        curr_day = df["Thursday"].iloc[i]
        hours = round(curr_day/3600, 2)
        R.append(hours)
    R = pd.Series(R).dropna()
    curr_col = df["Friday"]
    for i in range(len(df["Friday"])):
        curr_day = df["Friday"].iloc[i]
        hours = round(curr_day/3600, 2)
        F.append(hours)
    F = pd.Series(F).dropna()
    curr_col = df["Saturday"]
    for i in range(len(df["Saturday"])):
        curr_day = df["Saturday"].iloc[i]
        hours = round(curr_day/3600, 2)
        Sa.append(hours)
    Sa = pd.Series(Sa).dropna()
    curr_col = df["Sunday"]
    for i in range(len(df["Sunday"])):
        curr_day = df["Sunday"].iloc[i]
        hours = round(curr_day/3600, 2)
        Su.append(hours)
    Su = pd.Series(Su).dropna()
    week = {'Monday':M, 'Tuesday':T, 'Wednesday':W, 'Thursday':R, 'Friday':F, 'Saturday':Sa, 'Sunday':Su }
    return week
