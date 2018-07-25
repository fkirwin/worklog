import datetime

import customutils

class Entry:
    column_delim = ","
    row_delim = "\n"
    msg = "Title: {} {} Total Duration: {} {} Started: {} {} Ended: {} {} Notes: {} {}"
    date_format = "%m-%d-%Y %H:%M:%S"

    def __init__(self, _title, _start_time, _time_spent, _notes=None):
        self._title = _title
        self._start_time = self.__handle_date(_start_time)
        self._time_spent = int(_time_spent)
        self._notes = _notes


    def __str__(self):
        if self._time_spent:
            return_msg = self.msg.format(self._title, self.row_delim,
                                         str(self._time_spent) + " minutes", self.row_delim,
                                         datetime.datetime.strftime(self._start_time, self.date_format), self.row_delim,
                                         datetime.datetime.strftime(self.get_end_time, self.date_format),
                                         self.row_delim,
                                         self._notes, self.row_delim)
        else:
            return_msg = self.msg.format(self._title, self.row_delim,
                                         "Can't calculate - no time spent entered.", self.row_delim,
                                         datetime.datetime.strftime(self._start_time, self.date_format), self.row_delim,
                                         "No end time set yet.", self.row_delim,
                                         self._notes, self.row_delim)
        return return_msg

    @property
    def writable_dict(self):
        return dict(_title=self.title,
                    _start_time=datetime.datetime.strftime(self._start_time, self.date_format),
                    _time_spent=self.time_spent,
                    _notes=self.notes)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = self.__handle_date(start_time)

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def time_spent(self):
        return self._time_spent

    @time_spent.setter
    def time_spent(self, time_minutes):
        try:
            self._time_spent = int(time_minutes)
        except (ValueError, TypeError) as err:
            print("The parameter entered was not a valid number.  Please enter a valid decimal or integer")
            raise err

    @property
    def get_end_time(self):
        try:
            end_time = self._start_time + datetime.timedelta(minutes=self._time_spent)
        except (ValueError, TypeError) as err:
            print("A valid amount of time spent on the task has not been entered.  Please enter that number.")
            raise err
        return end_time

    def __handle_date(self, target_date):
        try:
            if isinstance(target_date, str):
                return customutils.generate_proper_date_from_string(target_date, self.date_format)
            else:
                return customutils.generate_proper_date_from_date(target_date, self.date_format)
        except Exception as err:
            print("Something went wrong with setting the date")
            raise err

