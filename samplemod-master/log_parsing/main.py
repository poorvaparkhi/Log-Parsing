from input.read_file import FileReader
from processor.data_parser import DataParser
from output.console import ConsolePrinter
from constants import *
from exceptions import *


class Orchestrator:
    """
    Orchestrates the flow between the classes to first read input from file, send it to data processing class
    and then finally print it in formatted fashion.
    """
    def __init__(self):
        self.records = []
        self.console_printer = ConsolePrinter()

    def start(self):
        """
        Main entry point of the application.
        :return:
        """
        f = FileReader('log_input_parser.csv', 'r')
        for idx, row in enumerate(f.read()):
            self.records.append(row)
        if not self.records:
            raise RecordsNotPresentException
        print(self.records)
        data_processor = DataParser(self.records)
        time_stats = data_processor.get_time_stats()
        url_freq = data_processor.get_url_frequency()
        self.console_printer.print_table([HTTP_METHOD_KEY,
                                        URL_KEY, FREQUENCY_KEY], url_freq)
        self.console_printer.print_table(
            [HTTP_METHOD_KEY, URL_KEY, 'min_time', 'max_time', 'average_time'], time_stats)

if __name__ == "__main__":
    o = Orchestrator()
    o.start()
