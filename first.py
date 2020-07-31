from datetime 

import datetime

import csv

calculate the number of hours between start and end times for the working period


def timeDifference(start, end):
    return (end - start).seconds / 3600

# Calculate amount earned (Rate=5)


def getAmountEarned(timeDifference):
    return timeDifference*5


# get start time, end time(with date) and timeDifference, total amount to the csv file
def addToFile(start, end, timeDifference, totalAmount):
    toAdd = [[start, end, timeDifference, timeDifference, totalAmount]]
    with open('calc.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(toAdd)


# when the user chooses to enter start and end dates and times

# start Date and Time for the work hour
def getDateAndTimeInput(endOrStart):
    Date = input(f'Enter {endOrStart} date in YYYY-MM-DD: ')
    year, month, day = map(int, Date.split('-'))
    Time = input(f'Enter {endOrStart} time in HH:MM ')
    hour, minute = map(int, Time.split(':'))
    return datetime(year, month, day, hour, minute)

#so we can now save all the logs to the csv file as directed.
