"""Functional tests for converting a CSV file to XML"""

import unittest
import csv

class main_use_case(unittest.TestCase):
    def setUp(self):
        self.csv_keys = ['text', 'integer', 'date']
        self.test_one = ['one', 1, '2014-02-23']
        self.test_two = ['two', 2, '24/2/14']
        self.csv_filename = 'testfile.csv'
        self.template = """

"""

    def tearDown(self):
        pass

    def make_csv(self):
        """Create a juicy old CSV file."""



# TODO: As a user, I select a CSV file from disc
    def test_csv_file_selection(self):
        """As a user, I select a CSV file from disc."""


# TODO: The app automatically converts the CSV to a list of dictionaries
# TODO: As a user, I provide a filename for an XML template
# TODO: The app automatically generates XML based on the template and CSV
# TODO: As a user, I choose where to save XML to


if __name__ == '__main__':
    unittest.main()