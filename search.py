import datetime
import re

import entry

class Search:

    def __init__(self):
        ##Playing with REGEX.  Probably not the best approach.
        self.options = {funct:funct for funct in re.findall(r"\b\w+(?<!_{2})\b",str(Search.__dict__.keys()))
                        if funct != "dict_keys"}

    def __str__(self):
        return_string = list(self.options.keys())
        return "Search Options: \n"+"\n".join(return_string)

    @classmethod
    def by_date(cls, date, entries):
        compare_format = "m-%d-%Y"
        matching_entries = []
        try:
            formatted_datetime = datetime.datetime.strptime(date, entry.Entry.date_format)
        except (ValueError, TypeError) as err:
            print("Please use formating as follows: ".format(compare_format))
            raise err

        for each in entries:
            if datetime.date(each.start_time, compare_format) == datetime.date(formatted_datetime, compare_format):
                matching_entries.append(each)
        return matching_entries

    @classmethod
    def by_time_spent(cls, time_spent, entries):
        matching_entries = []
        pass

    @classmethod
    def exact(cls, exact_phrase, entries):
        matching_entries = []
        pass

    @classmethod
    def regex(self, target_string, entries):
        matching_entries = []
        pass


s = Search()

print(s.options)
print(s)

print(datetime.date.strftime(datetime.datetime.now(), '%m-%d-%Y'))