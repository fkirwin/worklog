import csv


class Log:

    def __init__(self, file_location):
        self.file_location = file_location

    def get_entries(self):
        with open(self.file_location, "r") as csv_in:
            entries_in = csv.reader(csv_in, delimiter=',', quotechar='|')


    def write_new_entry(self, entry):
        with open(self.file_location, "a") as csv_out:
            entries_out = csv.writer(csv_out, delimiter=',', quotechar='|')
            entries_out.writerow()