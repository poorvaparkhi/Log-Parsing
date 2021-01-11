class ConsolePrinter:
    """
    Takes a set of headers and any blob of data as input and spits out the data
    as a formatted table
    """
    def __init__(self):
        pass

    def print_table(self, headers, data):
        format_row = "{:<30}" * len(headers)
        table = ["-" * 30 * len(headers), format_row.format(*headers)]
        for row in data:
            args = []
            for col in headers:
                cell_value = row.get(col, '')
                args.append(cell_value)
            table.append(format_row.format(*args))
        table.append("-" * 30 * len(headers))
        for string in table:
            print(string)



