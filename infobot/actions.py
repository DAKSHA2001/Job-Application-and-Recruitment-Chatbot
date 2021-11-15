# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import time
import datetime
import random
import smtplib
import json
import csv
import pygsheets
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
        
scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]

creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:/Users/Daksha/Downloads/gold-atlas-317314-f7aeaec8d97a.json", scope
        )
client = gspread.authorize(creds)

class SaveDetails(Action):
    def name(self) -> Text:
        return "action_save_details"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        sheet = client.open("Applicant_Sheet").sheet1  # Open the spreadhseet
        # name = tracker.get_slot("PERSON")

        date = datetime.date.today()
        time = datetime.datetime.now()
        date = str(date)
        hour = time.hour
        hour = str(hour)
        minu = time.minute
        minu = str(minu)
        time_1 = str(hour) + str(minu)
        to_save = [date, hour, minu]
        sheet.insert_row(to_save, 2)
        # name= tracker.latest_message['intent'].get('PERSON')

        # name = SlotSet("requested_slot", PERSON)
        job_role = tracker.get_slot("role")
        sheet.update_cell(2, 4, job_role)
        name = tracker.get_slot("PERSON")
        sheet.update_cell(2, 5, name)
        daofbi = tracker.get_slot("date")
        sheet.update_cell(2, 6, daofbi)
        email_id = tracker.get_slot("email")
        sheet.update_cell(2, 7, email_id)
        phone_number = tracker.get_slot("phone")
        sheet.update_cell(2, 8, phone_number)   
        grad_year = tracker.get_slot("year")
        sheet.update_cell(2, 9, grad_year)
        exp_year = tracker.get_slot("exp")
        sheet.update_cell(2, 10, exp_year)
        tech_skills = tracker.get_slot("skill")
        sheet.update_cell(2, 11, tech_skills)
        resume_link = tracker.get_slot("resume")
        sheet.update_cell(2, 12, resume_link)        
        sheet.update_cell(2, 13, "Application Submitted")
        
        return []
    
class AuthenticateEmail(Action):
    def name(self) -> Text:
        return "action_ask_emailotp"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text = "A 4-digit has been sent to your entered email ID for verification\n\n Please enter the OTP received")
        email_id = tracker.get_slot("email")
        otp_read = str(tracker.get_slot("emailotp"))
        server=smtplib.SMTP('smtp.gmail.com',587)
 
        server.starttls()

        otp=''.join([str(random.randint(0,9)) for i in range(4)])
        otp_msg='Hello, Your OTP is '+str(otp)

        msg = EmailMessage()
        msg.set_content(otp_msg)

        msg['Subject'] = 'OTP Verification from Chatbot'
        msg['From'] = "dakshaiscool@gmail.com"
        msg['To'] = email_id

        email = 'dakshaiscool@gmail.com'
        password = 'wbycchelinxzgjnq'
        server.login(email,password) 

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email,password)
        server.send_message(msg)
        server.quit()
        
        
          
        #while(otp_read):
        #    if(otp_read == otp):
        #        dispatcher.utter_message(text="Your Email is verified")
        #    else:
        #        dispatcher.utter_message("Your entered OTP is wrong")
        #        return[SlotSet("emailotp", None)]
            
        return[]
        
class ConfirmStatus(Action):
    def name(self) -> Text:
        return "action_confirm_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        check_email = str(tracker.get_slot("confirm_mail"))
        
        sheet = client.open("Applicant_Sheet").sheet1
        
        for i in range(1,9999):
            if str(sheet.cell(i,7).value) == check_email:
                break
            
        dispatcher.utter_message(text = "Role(s) Applied for: {}\n".format(sheet.cell(i,4).value)+"\nName Given: {}\n".format(sheet.cell(i,5).value)+"\nDate of Birth: {}\n".format(sheet.cell(i,6).value)+"\nEmail ID: {}\n".format(sheet.cell(i,7).value)+"\nMobile Number: {}\n".format(sheet.cell(i,8).value)+"\nYear of Graduation: {}\n".format(sheet.cell(i,9).value)+"\nYears of Experience: {}\n".format(sheet.cell(i,10).value)+"\nTechnical Skills: {}".format(sheet.cell(i,11).value)+"\nLink to Resume: {}".format(sheet.cell(i,12).value)+"\nCurrent Status of your application: {}".format(sheet.cell(i,13).value))
            else:
                dispatcher.utter_message(text = "Sorry! No data found for {}".format(sheet.cell(i,7).value))
        
        return[]
        
#class ActionSessionStarted(Action):
    #def name(self):
        #return "action_session_start"
    #async def run(self, dispatcher, tracker, domain):
        #events = [SessionStarted()]
        #message = 'Hello, I am a ChatBot'
        #dispatcher.utter_message(message)
        #events.append(ActionExecuted("action_listen"))
        #return events
    