import csv

import entry


class Log:
    """File IO"""

    def __init__(self, file_location):
        self.file_location = file_location
        try:
            open(self.file_location, 'a').close()
        except Exception as exc:
            raise exc

    def get_entries(self):
        entries = []
        with open(self.file_location, "r") as csv_in:
            entryin = csv.DictReader(csv_in, delimiter=',', lineterminator='\n')
            for row in entryin:
                target = entry.Entry(**dict(row))
                entries.append(target)
        return entries

    def write_new_entry(self, entry_input):
        sniffer = csv.Sniffer()
        header = False
        with open(self.file_location, "r+") as csv_out:
            try:
                header = sniffer.has_header(csv_out.read(1024))
            except:
                pass
        with open(self.file_location, "a+") as csv_out:
            entryout = csv.DictWriter(csv_out,
                                      delimiter=',',
                                      fieldnames=entry_input.writable_dict.keys(),
                                      lineterminator='\n')
            if header:
                entryout.writerow(entry_input.writable_dict)
            else:
                entryout.writeheader()
                entryout.writerow(entry_input.writable_dict)
