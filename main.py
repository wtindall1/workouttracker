from flask.views import MethodView
from flask import Flask, render_template, request
from WorkoutTracker import tracker
from wtforms import Form, StringField, SubmitField, SelectField, DateField
from datetime import date, datetime as dt
import pickle
from os.path import exists

app = Flask(__name__)


#load stored calendarmanager or initialise if doesn't exist
filepath = 'files/storedCalendarManager.pickle'
if exists(filepath):
    file = open(filepath, 'rb')
    calendar_manager = pickle.load(file)
    file.close()
else:
    calendar_manager = tracker.CalendarManager()

#load stored splitmanager or initialise if doesn't exist
filepath = 'files/storedSplitManager.pickle'
if exists(filepath):
    file = open(filepath, 'rb')
    split_manager = pickle.load(file)
    file.close()
else:
    split_manager = tracker.SplitManager()



class HomePage(MethodView):
    
    def get(self):
        workout_to_log = LogForm()

        return render_template('home_page.html', 
                                calendar=calendar_manager.generate_trimmed_calendar(), 
                                workout_to_log=workout_to_log,
                                workout_list=split_manager.workouts,
                                Analytics=calendar_manager.run_analytics())


    def post(self):
        workout_to_log = LogForm(request.form)

        print(workout_to_log.date.data)

        calendar_manager.track_workout(workout_to_log.date.data, workout_to_log.workout.data)

        #store objects to pickle files
        file = open('files/storedCalendarManager.pickle', 'wb')
        pickle.dump(calendar_manager, file)
        file.close()

        return self.get()                                                           
        


class LogForm(Form):


    workout = SelectField("Workout completed: ", choices=split_manager.workouts)
    date = DateField("Date: ", default=dt.today)
    button = SubmitField("Log")




class WorkoutsPage(MethodView):

    #display split & buttons
    def get(self):

        split_form = SplitForm()

        return render_template('workouts_page.html',
                                workout_list=split_manager.workouts,
                                split_form=split_form)

    #add or remove workout
    def post(self):
        
        splitform = SplitForm(request.form)

        #if name = add or remove
        if 'add' in request.form:
            split_manager.add_workout(splitform.add.data)
        elif 'remove' in request.form:
            split_manager.delete_workout(splitform.remove.data)

        #store objects to pickle files
        file = open('files/storedSplitManager.pickle', 'wb')
        pickle.dump(split_manager, file)
        file.close()

        return self.get()



class SplitForm(Form):

    add = StringField("Add a workout: ")
    addButton = SubmitField("Add")

    remove = SelectField("Remove a workout: ", choices=split_manager.workouts)
    removeButton = SubmitField("Remove")

    homeButton = SubmitField("Back to homepage")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/workouts', view_func=WorkoutsPage.as_view('workouts_page'))

app.run(debug=True)

