from kodzik import User
import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        self.users =[User('Andrzej', 'L', '11-01-1970'),
            User('Karol', 'M', '11-05-1992'),
            User('Ewelina', 'Dąbek', '01-12-1990'),
            User('Michał', 'Waleczny', '31-03-1980'),]
    def test_get_full_username(self):
        u = self.users[0]
        expected = u.first_name + " " + u.last_name
        result = u.get_full_username()
        self.assertEqual(expected,result)

    def test_date_format(self):
        u=self.users[0]

        split=u.birth_date.split('-')
        self.assertEqual(len(split),3)