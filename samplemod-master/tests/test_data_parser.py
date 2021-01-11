import main
from processor.data_parser import DataParser

import unittest


class TestMain(unittest.TestCase):
    def get_mock_records(self):
        return [{'timestamp': '1581589077', 'url': '/book/74/return', 'method': 'GET', 'response_time': '45',
          'response_code': '200'},
         {'timestamp': '1581589122', 'url': '/book/9876', 'method': 'GET', 'response_time': '57',
          'response_code': '200'},
         {'timestamp': '1581589179', 'url': '/book/97', 'method': 'PUT', 'response_time': '117',
          'response_code': '200'},
         {'timestamp': '1581589400', 'url': '/person/43/details', 'method': 'GET', 'response_time': '87',
          'response_code': '200'},
         {'timestamp': '1581589487', 'url': '/book/9876', 'method': 'PUT', 'response_time': '234',
          'response_code': '200'},
         {'timestamp': '1581589721', 'url': '/person/1/details', 'method': 'GET', 'response_time': '35',
          'response_code': '200'},
         {'timestamp': '1581589756', 'url': '/person/all', 'method': 'GET', 'response_time': '102',
          'response_code': '200'},
         {'timestamp': '1581590247', 'url': '/book/14/return', 'method': 'GET', 'response_time': '53',
          'response_code': '200'},
       {'timestamp': '1581591175', 'url': '/book/1', 'method': 'PUT', 'response_time': '20', 'response_code': '200'}]

    def test_url_freq(self):
        data_processor = DataParser(self.get_mock_records())
        result = data_processor.get_url_frequency()

        expected_result = [{'frequency': 3, 'method': 'PUT', 'url': '/book/{id}'},
                           {'frequency': 2, 'method': 'GET', 'url': '/book/{id}/return'},
                           {'frequency': 2, 'method': 'GET', 'url': '/person/{id}/details'},
                           {'frequency': 1, 'method': 'GET', 'url': '/book/{id}'},
                           {'frequency': 1, 'method': 'GET', 'url': '/person/all'}]
        self.assertEqual(result, expected_result)

    def test_time_stats(self):
        data_processor = DataParser(self.get_mock_records())
        result = data_processor.get_time_stats()

        expected_result = [{'average_time': 57.0,
                            'max_time': 57.0,
                            'method': 'GET',
                            'min_time': 57.0,
                            'url': '/book/{id}'},
                           {'average_time': 49.0,
                            'max_time': 53.0,
                            'method': 'GET',
                            'min_time': 45.0,
                            'url': '/book/{id}/return'},
                           {'average_time': 102.0,
                            'max_time': 102.0,
                            'method': 'GET',
                            'min_time': 102.0,
                            'url': '/person/all'},
                           {'average_time': 61.0,
                            'max_time': 87.0,
                            'method': 'GET',
                            'min_time': 35.0,
                            'url': '/person/{id}/details'},
                           {'average_time': 123.67,
                            'max_time': 234.0,
                            'method': 'PUT',
                            'min_time': 20.0,
                            'url': '/book/{id}'}]
        self.assertEqual(result, expected_result)