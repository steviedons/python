import subprocess
import sys
import re
import requests

COMMANDS = {'iwu-tn-00-o':' /opt/msgcore/iwu/emgstat -host 192.168.40.101 -port 7185 | grep IN',
            'iwu-tn-01-o':' /opt/msgcore/iwu/emgstat -host 192.168.40.102 -port 7185 | grep IN'}

def send_stats_to_influxdb(dbname, server, field, value):
    """ send stats to influxdb database dbname with the server the value came from and the
     field name provided """

    url_string = 'http://10.0.30.83:8086/write?db=' + dbname
    data_string = field + ',server=' + server + ' value=' + value

    r = requests.post(url_string, data=data_string)

def main():
    for server, command in COMMANDS.items():
        ssh = subprocess.Popen(["ssh", "root@%s" % server, command],
                                 shell=False,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()

        if result == []:
            error = ssh.stderr.readlines()
            print >>sys.stderr, "ERROR: %s" % error
        else:
            for r in result:
                bind = r.split()
                client = bind[0]
                mps_value = bind[8]
                print client + mps_value
                send_stats_to_influxdb('miodb', server, client, str(mps_value))

if __name__ == "__main__":
    main()