import urllib.request
import re
import json
import smtplib
import sys
from datetime import datetime

NO_SHARES = 1585

def scrape(url_to_open, regex):
    """ From the url and the regex return a list of the values found """

    try:
        html_open = urllib.request.urlopen(url_to_open)
        html = html_open.read()

        pattern = re.compile(regex)
        value = re.findall(pattern, str(html))
    except urllib.error.HTTPError:
        print('Could not connect to web site to do the scrape')
        sys.exit(1)
    else:
        return value

def noticeEMail(usr, psw, fromaddr, toaddr, subject, msg):
    """
    Sends an email message through GMail once the script is completed.
    Developed to be used with AWS so that instances can be terminated
    once a long job is done. Only works for those with GMail accounts.

    starttime : a datetime() object for when to start run time clock
    usr : the GMail username, as a string
    psw : the GMail password, as a string
    fromaddr : the email address the message will be from, as a string
    toaddr : a email address, or a list of addresses, to send the
    message to
    """
    # Initialize SMTP server
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usr, psw)
    # Send email
    senddate = datetime.strftime(datetime.now(), '%Y-%m-%d')
    m = "Date: %s\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (
        senddate, fromaddr, toaddr, subject)
    server.sendmail(fromaddr, toaddr, m + msg)
    server.quit()


def get_share_price():
    """ Grab the share price  and return a list of matches"""

    price = scrape("http://uk.finance.yahoo.com/q?s=ERIC-B.ST", '"regularMarketPrice":{"raw":(.+?),"')
    return price

def get_exchange_rate():
    """ scrape the current exchange rate and return a list of rates """

    exrate = scrape("http://themoneyconverter.com/GBP/SEK.aspx", 'SEK/GBP = (.+?)</div>')
    return exrate

def log_output_json(output):
    """ takes a dictionary and adds it to a log file as json """

    with open('/home/steve/share_ouput.log', 'a') as f:
        json.dump(output, f, indent=2)

def work_out_value(price, exchange):
    """ give the current share price and exchange rate return the total value in pounds """

    try:
        value = (float(price[0]) / float(exchange[0])) * NO_SHARES
    except IndexError:
        print("There was an issue with the web scrape")
        return None
    return value

def build_email_message():
    """ check the values of NO_SHARES, build and email and send it """

    ericsson_price = get_share_price()
    krona_exchange = get_exchange_rate()

    value = work_out_value(ericsson_price, krona_exchange)

    if value == None:
        sys.exit(1)

    output = {'today': str(datetime.today()), 
              'todays_price': float(ericsson_price[0]), 
              'todays_exchange': float(krona_exchange[0]),
              'total_value': value}

    output_subject = "Total share value: %.2f" % output['total_value']
    output_msg = "Time the check was made: %s\nTodays share price: %.2f\nToday's exchange rate: %.2f\n" % (
                output['today'], 
                output['todays_price'], 
                output['todays_exchange'])

    print(output_subject)
    print(output_msg)

    noticeEMail('steviedonsnotif@gmail.com', 
                '0TlKCN27ytHa', 
                'steviedonsnotif@gmail.com', 
                'steviedons@gmail.com',
                output_subject, 
                output_msg)

    log_output_json(output)

if __name__ == '__main__':
    build_email_message()
