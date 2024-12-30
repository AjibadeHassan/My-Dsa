def time_conversion(s):
    # convert time from 12-hour format to 24-hour format
    from datetime import datetime
    parsedtime = datetime.strptime(s,'%I:%M:%S%p').strftime('%H:%M:%S')
    return parsedtime



# convert time from 24-hour format to 12-hour format


def convert_time(s):
    from datetime import datetime
    parsed_time = datetime.strptime(s,'%H:%M%:S').strftime('%I:M:S%p')