import pickle
from os.path import exists

filepath = 'files/storedSplitManager.pickle'
if exists(filepath):
    file = open(filepath, 'rb')
    split_manager = pickle.load(file)
    file.close()
    print('cached')

print([i for i in split_manager.workouts])