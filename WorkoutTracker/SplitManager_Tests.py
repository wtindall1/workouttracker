import unittest
from tracker import SplitManager

class TestSplitManager(unittest.TestCase):
    
    def test_instantiation_creates_empty_array(self):
        splitmanager = SplitManager()
        self.assertEqual(splitmanager.workouts,[], "Expected empty array instance variable")

    def test_add_workout_appends_to_array(self):
        splitmanager = SplitManager()
        splitmanager.add_workout('Run')
        self.assertTrue(splitmanager.workouts[0] == 'Run', 'Expected run to be added to workouts array')


if __name__ == '__main__':
    unittest.main()
