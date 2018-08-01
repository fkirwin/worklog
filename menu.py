import datetime
import sys

import customutils
import entry
import log

class Menu:
    DEFAULT_LOG = 'entries.CSV'

    def __init__(self):
        self.options ={"Menu":["mm", self.display_main_menu],
                       "New Entry": ["ne", self.write_entry],
                       "Search Entries": ["se", self.search_entries],
                       "Exit the program": ["e", self.exit_program]}

    def run(self):
        while True:
            self.display_main_menu()
            user_choice = input("Enter an option: ")
            if user_choice in self.options.keys():
                action = self.options.get(user_choice)
                action()
            elif user_choice in [each[0] for each in self.options.values() if user_choice == each[0]]:
                action = [each[1] for each in self.options.values() if user_choice == each[0]]
                action[0]()
            else:
                print("{} is not a valid choice".format(user_choice))


    def display_main_menu(self):
        """The main menu."""
        print("Greetings!  Here are our options.")
        for name, method in self.options.items():
            print("Type {} or {} to access {}.  {}"
                  .format(name, method[0], method[1].__name__.replace("_", " "), method[1].__doc__))

    def write_entry(self):
        """Write a single entry to file."""
        print("Please fill out the following to write an entry to file.")
        attempt = 3
        while attempt > 0:
            try:
                title = self._get_title()
                start_time = self._get_start_time()
                time_spent = self._get_time_spent()
                notes = self._get_details()
                new_entry = entry.Entry(title, start_time, time_spent, notes)
                log_connection = log.Log(self.DEFAULT_LOG)
                log_connection.write_new_entry(new_entry)
            except Exception as exc:
                print(exc)
                attempt-=1
            else:
                print(str(new_entry))
                print("Entry was successful!  Heading back to the main menu.")
                break
        self.display_main_menu()


    def search_entries(self):
        """Search all available entries based on user criterias."""
        print("Please select a method to search for entries.")

    def _get_title(self):
        title = input("Please enter a title for this entry:")
        if title:
            return title
        else:
            return self._get_title()

    def _get_start_time(self):
        try:
            start_time = input("Please enter a start time for the task in the following format {}.  "
                       "Or type 'now' to stamp with current date and time:"
                       .format(entry.Entry.date_format
                               .replace("%", " ").replace("- ", "-").replace(": ", ":")))
            if start_time.lower() == "now":
                start_time = datetime.datetime.now().strftime(entry.Entry.date_format)
            customutils.generate_proper_date_from_string(start_time, entry.Entry.date_format)
            return start_time
        except:
            print("Format was invalid.  Please try again.")
            return self._get_start_time()

    def _get_time_spent(self):
        try:
            time_spent = input("Please enter a number of minutes applied to the task:")
            int(time_spent)
            return time_spent
        except:
            print("Please enter valid integer.")
            return self._get_time_spent()

    def _get_details(self):
        notes = input("Enter details:")
        if notes:
            return notes
        else:
            return self._get_details()

    def exit_program(self):
        """Exits the program."""
        print("Have a nice day.")
        sys.exit(0)


