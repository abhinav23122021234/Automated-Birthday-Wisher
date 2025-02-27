##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random
import datetime as dt
MY_EMAIL="add_your_gmail"
MY_PASSWORD="add_your_app_password"
# 1. Update the birthdays.csv

def add_person(name,email,year,month,day):
    data = pd.read_csv( "birthdays.csv" )
    person1={
        "name":str(name),
        "email":str(email),
        "year":int(year),
        "month":int(month),
        "day":int(day)
    }


    data = pd.concat( [data, pd.DataFrame( [person1] )], ignore_index=True )

    data.to_csv("birthdays.csv")


add_person("Ayush","ayushjaiswal300404@gmail.com",2005,4,30)
add_person(name="Aishwarya",email="theprettyyou27@gmail.com",year=2005,month=2,day=27)


# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
today_tuple=(now.month,now.day)
data=pd.read_csv("birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    filepath=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter_file:
        content=letter_file.read()
        content=content.replace("[NAME]",birthday_person["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP( "smtp.gmail.com" ) as connection:
        connection.starttls()
        connection.login( MY_EMAIL, MY_PASSWORD )
        connection.sendmail( from_addr=MY_EMAIL,
                             to_addrs=birthday_person["email"],
                             msg=f"Subject:Happy Birthday!\n\n{content}" )



