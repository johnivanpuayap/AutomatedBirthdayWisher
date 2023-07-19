import pandas as pd
import datetime as dt
import random
import smtplib

# Enter the Login Credentials
my_email = "johnivanpuayapamerica@gmail.com"
my_password = "xznqqbtxetfshwuy"

# Load the Date Today
month = dt.datetime.now().month
day = dt.datetime.now().day

# Load the Birthdays
data = pd.read_csv("birthdays.csv")
birthdays_today = data[(data['month'] == month) & (data['day'] == day)]

# Check if there are birthdays today
if not birthdays_today.empty:
    for index, row in birthdays_today.iterrows():
        # Choose a message
        with open(f"letter_templates\letter_{random.randint(1, 3)}.txt") as file:
            message = file.read()
            message = "Subject: Happy Birthday!\n\n" + message

        # Change the Name
        custom_message = message.replace("[NAME]", row['name'])

        # Send the Email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row['email'], msg=custom_message)


print(f"Sent {len(birthdays_today)} emails today")