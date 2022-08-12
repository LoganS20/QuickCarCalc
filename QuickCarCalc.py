import pandas as pd
import numpy as np

# Under 30000km
yearBUY = {2022: 45000.0,
           2021: 35000.0,
           2020: 23000.0,
           2019: 21000.0,
           2018: 19000.0,
           2017: 17000.0,  # More options in this year
           2016: 16000.0,
           2015: 16000.0,
           2014: 16000.0,
           2013: 13500.0,
           2012: 13000.0}

# Cheapest Under 120000km. up to 5 years on
yearSELL = {
            2021: 35000.0,
            2020: 22000.0,
            2019: 19000.0,
            2018: 16500.0,
            2017: 12000.0,
            2016: 12000.0,
            2015: 10000.0,
            2014: 9000.0,
            2013: 9000.0,
            2012: 9000.0,
            2011: 10000.0,
            2010: 9000.0,
            2009: 9000.0,
            2008: 9000.0,
            2007: 8000.0}


def cost(year, sellTime):

    if (year - sellTime) > 2012:
        battery_expense = 0
    else:
        battery_expense = 3000

    depreciation = yearBUY[year] - yearSELL[year - sellTime]

    totalcost = battery_expense + depreciation

    d = {'Year': [year],
         'Battery Expense': [battery_expense],
         'Depreciation': [depreciation],
         'Cost to Buy': [yearBUY[year]],
         'Cost to Sell': [yearSELL[year - sellTime]],
         'Ownership time (years)': [sellTime],
         'Final Cost': [totalcost]}

    df = pd.DataFrame(data=d)
    return df


final = cost(2012, 3)
sellTime = [3, 4, 5]

for j in sellTime:
    for i in yearBUY:
        if i == 2012:
            continue
        else:
            final = pd.concat([final, cost(i, j)])

#pd.set_option('display.max_columns', None)
final = final.sort_values(by=['Final Cost'])
print(final)
