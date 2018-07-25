import csv
import datetime

import entry
import customutils

class Log:

    def __init__(self, file_location):
        self.file_location = file_location

    def get_entries(self):
        entries = []
        with open(self.file_location, "r") as csv_in:
            entryin = csv.DictReader(csv_in, delimiter=',', lineterminator='\n')
            for row in entryin:
                target = entry.Entry(**dict(row))
                entries.append(target)
        return entries

    def write_new_entry(self, entry_input):
        with open(self.file_location, "w+") as csv_out:
            entryout = csv.DictWriter(csv_out, delimiter=',', fieldnames=entry_input.writable_dict.keys(), lineterminator='\n')
            entryout.writeheader()
            entryout.writerow(entry_input.writable_dict)