from datetime import date, datetime as dt
import pandas as pd
import calendar
import re

class SplitManager:

    def __init__(self):
        self.workouts = []

    def add_workout(self, workoutName):
        if self.workouts.count(workoutName) == 0:
            self.workouts.append(workoutName)

    def edit_workout(self, workoutName, newName):
        ind = self.workouts.index(workoutName)
        self.workouts[ind] = newName

    def delete_workout(self, workoutName):
        if self.workouts.count(workoutName) > 0:
            self.workouts.remove(workoutName)




class CalendarManager:
    
    def __init__(self):
        dates = pd.date_range('2022-01-01', '2025-01-01')
        self.calendar = {date.date(): None for date in dates}

    #track or update
    def track_workout(self, date, workoutName):
        
        try:
            date_converted = dt.strptime(date, '%Y-%m-%d').date()
            self.calendar[date_converted] = workoutName
        except Exception:
            pass


    def delete_tracked_workout(self, date):
        
        try:
            date_converted = dt.strptime(date, '%Y-%m-%d').date()
            self.calendar.pop(date_converted)
        except Exception:
            pass


    #returns calendar dictionary with only tracked days, order reversed
    def generate_trimmed_calendar(self):
        
        keys = list(self.calendar.keys())
        keys.sort(reverse=True)

                
        trimmed_calendar = {}

        for key in keys:
            if self.calendar[key] is not None:
                trimmed_calendar[key] = self.calendar[key]

        return trimmed_calendar


        
        


    def run_analytics(self):
        
        #calculate days worked out in last 7
        days_worked_out = 0
        today = date.today()
        today_minus7 = (date.today() - pd.DateOffset(days=7)).date()

        for key, value in self.generate_trimmed_calendar().items():
            if key <= today and key > today_minus7:
                days_worked_out += 1

        return f"You worked out {days_worked_out} times in the last week!"

        
        


    




# split = SplitManager()

# split.add_workout(workoutName='Upper 1')

# split.add_workout('Lower 1')

# split.add_workout('Upper 2')

# split.add_workout('Lower 2')

# print(split.workouts)

# willCalendar = CalendarManager()

# willCalendar.track_workout('2022-11-16', 'Upper')

# print(willCalendar.generate_trimmed_calendar())

# print(willCalendar.run_analytics())




