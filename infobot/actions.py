# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import time
import datetime

#
class SaveName(Action):

     def name(self) -> Text:
         return "action_save_name"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import datetime
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Daksha/Downloads/gold-atlas-317314-f7aeaec8d97a.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("Unify_Goals_Demo").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all recorda
        name = tracker.get_slot("PERSON")
        
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
        name = tracker.get_slot("PERSON")
        sheet.update_cell(2,4, name)

        return []

class SaveDOB(Action):
#
    def name(self) -> Text:
        return "action_save_dob"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Daksha/Downloads/gold-atlas-317314-f7aeaec8d97a.json", scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("Unify_Goals_Demo").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        daofbi = tracker.get_slot("date")
        
        sheet.update_cell(2, 5, daofbi) 


        return []
    
class Saveyearofgrad(Action):
#
    def name(self) -> Text:
        return "action_save_gradyear"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Daksha/Downloads/gold-atlas-317314-f7aeaec8d97a.json", scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("Unify_Goals_Demo").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        grad_year = tracker.get_slot("year")
                
        sheet.update_cell(2, 6, grad_year) 

        return []
    
class Saveexpyear(Action):
#
    def name(self) -> Text:
        return "action_save_expyear"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Daksha/Downloads/gold-atlas-317314-f7aeaec8d97a.json", scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("Unify_Goals_Demo").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        exp_year = tracker.get_slot("exp")
        
        sheet.update_cell(2, 7, exp_year) 

        return []
    
class SaveTechSkills(Action):
#
    def name(self) -> Text:
        return "action_save_techskills"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/Daksha/Downloads/gold-atlas-317314-f7aeaec8d97a.json", scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("Unify_Goals_Demo").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        tech_skills = tracker.get_slot("skill")
                
        sheet.update_cell(2, 8, tech_skills) 
        
                        
        return []
    
