import re
import itertools
from operator import itemgetter
from constants import *
from exceptions import *


class DataParser:
    """
    Masks, calculates url frequency and response-time stats
    """
    def __init__(self, records):
        self.records = records
        self.__mask()
        self.records.sort(key=itemgetter("primary_key"))

    def get_url_frequency(self):
        freq_output = []
        for k, records in itertools.groupby(self.records, lambda item: item["primary_key"]):
            records = list(records)
            number_of_records = len(records)
            any_record = records[0]
            freq_record_struct = {
                URL_KEY: any_record[URL_KEY], HTTP_METHOD_KEY: any_record[HTTP_METHOD_KEY],
                FREQUENCY_KEY: number_of_records
            }
            freq_output.append(freq_record_struct)

        return sorted(freq_output, key=lambda x: x['frequency'], reverse=True)

    def get_time_stats(self):
        stats_output = []
        for k, records in itertools.groupby(self.records, key=lambda x: (x['primary_key'])):
            records = list(records)
            min_time, max_time = DataParser.__get_minmax_response_time(records)
            average_time = DataParser.__get_avg_response_time(records)
            any_record = records[0]
            stats_record_struct = {
                URL_KEY: any_record[URL_KEY], HTTP_METHOD_KEY: any_record[HTTP_METHOD_KEY],
                'min_time': min_time, 'max_time': max_time, 'average_time': average_time
            }
            stats_output.append(stats_record_struct)

        return stats_output

    def __mask(self):
        for record in self.records:
            url = record.get('url', '')
            if url:
                masked_url = re.sub(r'/\d+', '/{id}', url)
                record['url'] = masked_url
                primary_key = record[HTTP_METHOD_KEY] + "_" + record[URL_KEY]
                record['primary_key'] = primary_key

    @staticmethod
    def __get_minmax_response_time(grouped_records):
        min_time, max_time = float('inf'), float('-inf')
        for record in (item['response_time'] for item in grouped_records):
            if not record.isdigit():
                raise IncorrectFileDataException
            record = float(record)
            min_time, max_time = min(record, min_time), max(record, max_time)
        return min_time, max_time

    @staticmethod
    def __get_avg_response_time(grouped_records):
        return round(sum([float(item["response_time"]) for item in grouped_records])
                     / len(grouped_records), 2)
