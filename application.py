import log
import entry
import search
import menu
import customutils
import datetime

if __name__ == '__main__':
    m = menu.Menu()
    m.run()

    '''
    l = log.Log('entries.csv')
    e = entry.Entry("testing", _start_time=datetime.datetime.now(), _time_spent=10)
    l.write_new_entry(e)
    lst_entries = l.get_entries()
    s = search.Search(lst_entries)
    e = s.by_date("07-27-2018")
    print(e[0])
    f = s.by_time_spent(10)
    print(f[0])
    g = s.exact('testing')
    print(g[0])
    h = s.regex('t.s')
    print(h[0])
    '''