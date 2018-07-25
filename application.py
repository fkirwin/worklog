import log
import entry
import search
import menu
import customutils
import datetime

if __name__ == '__main__':
    l = log.Log('entries.csv')
    e = entry.Entry("testing", _start_time=datetime.datetime.now(), _time_spent=10)
    l.write_new_entry(e)
    lst_entries = l.get_entries()
    print(lst_entries[0])
    s = search.Search(lst_entries)
    e = s.by_date("07-24-2018")
    print(e[0])
    #print(e[0].title)