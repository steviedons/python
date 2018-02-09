import re
import requests
import os


def get_stat_value(filename):
    """ from a stats file return a dict with all the fields and values"""
    fields = []
    stats = []

    with open(filename) as file_object:
        for line in file_object:
            # Match the fields
            field = re.match('<mt>(.*)</mt>', line.lstrip().rstrip())
            if field:
                fields.append(field.group(1))
            # Match the values
            stat = re.match('<r>(.*)</r>', line.lstrip().rstrip())
            if stat:
                stats.append(stat.group(1))
    return dict(zip(fields, stats))

def send_stats_to_influxdb(dbname, server, field, value):
    """ send stats to influxdb database dbname with the server the value came from and the 
     field name provided """

    url_string = 'http://localhost:8086/write?db=' + dbname
    data_string = field + ',server=' + server + ' value=' + value

    r = requests.post(url_string, data=data_string)

def remove_file_extension_and_path(filename):
    """taking a full path return the filename with the path and extension removed"""
    base = os.path.basename(filename)
    return os.path.splitext(base)[0]

def collect_and_send(stats_files):
    """collect the stats from the give files and send them to infludb"""
    for file in stats_files:
        stats_from_file = get_stat_value(file)
        print remove_file_extension_and_path(file)
        for key, value in stats_from_file.items():
            send_stats_to_influxdb('testdb', remove_file_extension_and_path(file), key, value)

# Should just have to add the mas, ntf and mms files to this list and it will add all of the stats.

files = ['/opt/mio/perf/sms/sms-tn-00/pmagent-sms-tn-00.xpd',
              '/opt/mio/perf/sms/sms-tn-00/pmagent-sms-tn-01.xpd']

collect_and_send(files)
