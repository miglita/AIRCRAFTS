import smtplib, ssl
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import csv

html = "<html><table bgcolor=#ADD8E6><tr><th>AIRCRAFTS EU</th></tr>"
with open('EU_CNTRS.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        row = (f'{row["TAIL_NUMBER"]} , {row["MODEL_NUMBER"]} , {row["DESCRIPTION"]}, {row["COMPANY_NAME"]}, {row["CODE"]}, {row["COUNTRY_NAME"]}.')
        line_count += 1
        strRW = "<tr><td><hr>" + str(row) + "</hr></td></tr>"
        html = html + strRW

html = html + "</table></html>"

hs = open("table1foremail.html", 'w')
hs.write(html)
#--------------------------------------------------------------------------------------
html1 = "<html><table bgcolor=#FFA07A><tr><th>AIRCRAFTS NON EU</th></tr>"
with open('NON_EU_CNTRS.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        row = (f'{row["TAIL_NUMBER"]} , {row["MODEL_NUMBER"]} , {row["DESCRIPTION"]}, {row["COMPANY_NAME"]}, {row["CODE"]}, {row["COUNTRY_NAME"]}.')
        line_count += 1
        strRW1 = "<tr><td><hr>" + str(row) + "</hr></td></tr>"
        html1 = html1 + strRW1

html1 = html1 + "</table></html>"
hs = open("table1foremail1.html", 'w')
hs.write(html1)
#---------------------------------------------------------------------------------------
email = 'miglelevinskaite@gmail.com'
password = 'psswd'
send_to_email = 'miglelevinskaite@gmail.com'
subject = 'Information about Aircrafts'
message = 'Please see tables below:'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
# -----------------------------------------------------------------------------
msg.attach(MIMEText(html, 'html'))
msg.attach(MIMEText(html1, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()