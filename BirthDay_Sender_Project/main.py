# Automated Birthday Wisher

import random
import datetime as dt
import pandas as pd
import smtplib

my_email = "SENDERS_EMAIL"
password = "SENDERS_PASSWORD"

with open("birthdays.csv") as file:
    birthdays = pd.read_csv(file)
    birth_list = birthdays.to_dict(orient="records")
    now=dt.datetime.now()

    for item in birth_list:
        if (item["month"]==now.month) and (item["day"]==now.day):
            with open("letter_1.txt",) as edit_file:
                letter=edit_file.read()
                letter=letter.replace("[Name]",item["name"].title())
              
                # this is for creating file tocheck the output
                # with open(f"letter_for_{item['name']}.txt","w") as send_file:
                #     send_file.write(letter)
                #     send_file.close()

                with open("Quotes.txt") as file:
                    all_quotes = file.readlines()
                    quote = random.choice(all_quotes)

                with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    message = f"Subject:Happy Birthday To You Dear {item['name']}\n\nFirst a small push up quote for you\n{quote} {letter}"
                    connection.sendmail(from_addr=my_email, to_addrs=item['email'], msg=message.encode('utf-8'))

            edit_file.close()
    file.close()


# pythoneverywhere

# if we need to send automatically use pythoneverywhere and upload the files priority wise
# then run give/enable required permissions then set a remainder for running the code everyday at some time
# it will run and send it to people who have birthday on that day
