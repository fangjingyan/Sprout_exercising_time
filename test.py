import unittest
from exercise_time import CountTime


class TestStringMethods(unittest.TestCase):
    def test_empty_input(self):
        ts = []
        hr = []
        min_hr = 130
        expected = 0
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_one_data_less_than_Min(self):
        ts = [2]
        hr = [72]
        min_hr = 130
        expected = 0
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_one_data_larger_than_Min(self):
        ts = [2]
        hr = [140]
        min_hr = 130
        expected = 0
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_within_break_less_than_Min(self):
        ts = [2, 10]
        hr = [72, 82]
        min_hr = 130
        expected = 0
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_within_break_larger_than_Min(self):
        ts = [2, 10]
        hr = [72, 140]
        min_hr = 130
        expected = 0
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_within_break_both_larger_than_Min(self):
        ts = [2, 10]
        hr = [130, 140]
        min_hr = 130
        expected = 8
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_within_break_all_larger_than_Min(self):
        ts = [2, 10, 100]
        hr = [130, 140, 140]
        min_hr = 130
        expected = 98
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_exceed_break_both_larger_than_Min(self):
        ts = [2, 200]
        hr = [130, 140]
        min_hr = 130
        expected = 0
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_exceed_break_all_larger_than_Min(self):
        ts = [2, 10, 200]
        hr = [130, 140, 140]
        min_hr = 130
        expected = 8
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)

    def test_complicated_situation(self):
        ts = [2, 5, 10, 20, 35, 100, 110, 120, 400, 450, 900]
        hr = [72, 83, 110, 135, 136, 140, 140, 140, 140, 135, 150]
        min_hr = 130
        expected = 150
        sol = CountTime()
        res = sol.exercise_time_simplified(ts, hr, min_hr)
        self.assertEqual(expected, res)
