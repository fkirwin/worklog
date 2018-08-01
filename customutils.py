import datetime

def generate_proper_date_from_date(dt_object, fmt):
    return datetime.datetime.strptime(dt_object.strftime(fmt),fmt)

def generate_proper_date_from_string(str_object, fmt):
    return datetime.datetime.strptime(str_object, fmt)




