import datetime


class Entry:

    column_delim = ","
    row_delim = "\n"
    msg = "Title: {} {} Total Duration: {} {} Started: {} {} Ended: {} {} Notes: {} {}"
    date_format = "%m-%d-%Y %H:%M:%S"

    def __init__(self, title, notes=None, start_time=datetime.datetime.now(), time_spent=None):
        self.title = title
        self._notes = notes
        self._start_time = start_time
        self._time_spent = time_spent


    def __str__(self):
        if self.time_spent:
            return_msg = self.msg.format(self.title, self.row_delim,
                                         str(self.time_spent) + " minutes", self.row_delim,
                                         datetime.datetime.strftime(self.start_time, self.date_format), self.row_delim,
                                         datetime.datetime.strftime(self.get_end_time(), self.date_format), self.row_delim,
                                         self.notes, self.row_delim)
        else:
            return_msg = self.msg.format(self.title, self.row_delim,
                             datetime.datetime.strftime(self.start_time, self.date_format), self.row_delim,
                             "No end time set yet.", self.row_delim,
                             "Can't calculate - no time spent entered.", self.row_delim,
                             self.notes, self.row_delim)
        return return_msg

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def set_start_time(self, start_time=datetime.datetime.now()):
        self._start_time = start_time

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        if notes:
            self._notes = notes
        else:
            self._notes = "N/A"

    @property
    def time_spent(self):
        return self._time_spent

    @time_spent.setter
    def time_spent(self, time_minutes):
        try:
            self._time_spent = time_minutes
        except (ValueError, TypeError) as err:
            print("The parameter entered was not a valid number.  Please enter a valid decimal or integer")
            raise err

    def get_end_time(self):
        try:
            end_time = self.start_time + datetime.timedelta(minutes=self.time_spent)
        except (ValueError, TypeError) as err:
            print("A valid amount of time spent on the task has not been entered.  Please enter that number.")
            raise err
        return end_time


e = Entry("test")

