import csv
from pathlib import Path
PARENT_PATH = "resources"


class FileReader:
    """
    Reads a CSV file and converts csv rows to python in-memory dictionary data structure
    """
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.path = Path(PARENT_PATH) / self.file_name
        self.mode = mode

    def read(self):
        """
        reads and transforms csv rows to python in-memory dictionary data structure
        :return: csv file data lazily
        """
        #Open the file in universal newline mode with 'rU'
        # for backwards compatibility
        try:
            with open(self.path, 'rU') as data:
                reader = csv.DictReader(data)
                for row in reader:
                    #that the data is evaluated lazily. The file is not opened, read, or parsed until you need it.
                    # No more than one row of the file is in memory at any given time
                    yield row
        except FileNotFoundError:
            f"Wrong file or file path given for {self.path}"
            raise RuntimeError

    @classmethod
    def __read_in_chunks(cls, file_object, chunk_size=1024):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

