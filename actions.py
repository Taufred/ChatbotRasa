from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import EventType

import calendar
import json
import io
import os
import requests
#
#
#

morning = ["morning", "noon"]
evening = ["evening", "afternoon", "night"]

OPENING_HOURS = {
	6:	{
		"morning": "closed",
		"evening": "closed"
	},
	1:	{
		"morning": "08:00 - 12:30",
		"evening": "14:00 - 17:00"
	},
	2:	{
		"morning": "08:00 - 14:30",
		"evening": "15:00 - 19:00"
	},
	3:	{
		"morning": "08:00 - 14:30",
		"evening": "15:00 - 19:00"
	},
	4:	{
		"morning": "09:00 - 14:30",
		"evening": "15:00 - 19:00"
	},
	5:	{
		"morning": "08:00 - 14:30",
		"evening": "15:00 - 18:00"
	},
	0:	{
		"morning": "11:00 - 14:30",
		"evening": "15:00 - 18:00"
	},

}


def find_opening_hours(day, time_of_day):
	days = []
	for day_name in calendar.day_name:
		days.append(day_name.lower())
	days = dict(zip(days, range(7))); 
	day_nr = days[day.lower()]
	opening_hours = OPENING_HOURS[day_nr]

	if time_of_day!=None:
		if time_of_day.lower() in morning:
			opening_hours = opening_hours["morning"]
		elif time_of_day.lower() in evening:
			opening_hours = opening_hours["evening"]
	return str(opening_hours)


class Opening_Hours_Form(FormAction):
#
	def name(self) -> Text:
		return "opening_hours_form"

	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return ["day"]

	def slot_mappings(self) -> Dict[Text, Any]:
		return {"day": self.from_entity(entity="day",
										intent= ["inform_time_and_day"])}
#
	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		day = tracker.get_slot("day")
		if day.lower() == "today" or day.lower() == "tonight":
			my_date = date.today()
			day_name = calendar.day_name[my_date.weekday()]
		elif day.lower() == "tomorrow":
			my_date = date.today()
			tomorrow = my_date + datetime.timedelta(days=1)
			day_name = calendar.day_name[tomorrow .weekday()]
		else:
			day_name = day
		time_of_day = tracker.get_slot("time_of_day")

		results = find_opening_hours(day_name, time_of_day)
		if len(results) == 0:
			dispatcher.utter_message("Sorry, I couldn't find any opening hours on {}.".format(day_name)+results)
		elif time_of_day == None:
			dispatcher.utter_message("These are the opening hours on {}: ".format(day_name)+results)
		else:
			dispatcher.utter_message("These are the opening hours on {} in the {}: ".format(day_name,time_of_day)+results)
		return []

class Application_form(FormAction):
	def name(self) -> Text:
		return "application_form"
#
	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return []

	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		dispatcher.utter_message("I will redirect you to the application form, if you click [here](https://mindsquare.de/schnellbewerbung-mindsquare/)!")
		return []
		

class Book_session_form(FormAction):
	def name(self) -> Text:
		return "book_session_form"
#
	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return []

	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		dispatcher.utter_message("I have booked a session for you!")
		return []
		
class FAQ_form(FormAction):
	def name(self) -> Text:
		return "faq_form"
#
	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return ["subject"]

	def slot_mappings(self) -> Dict[Text, Any]:
		return {"day": self.from_entity(entity="subject",
									intent= ["ask_faq"])}

	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		subject = tracker.get_slot("subject")
		dispatcher.utter_message("This is a generic answer about subject: {}. Would you like to book an expert session?".format(subject))
		return []

def tag_convo(tracker: Tracker, label: Text) -> None:
    """Tag a conversation in Rasa X with a given label"""
    #config = os.environ.get("RASA_X_HOST", "rasa-x:5002")
    config = os.environ.get("RASA_X_HOST", "localhost:5002")
    endpoint = f"http://{config}/api/conversations/{tracker.sender_id}/tags"
    requests.post(url=endpoint, data=label)
    return


class ActionTagFeedback(Action):
    """Tag a conversation in Rasa X as positive or negative feedback, save the positive Story. Negative Stories should be reviewed. """

    def name(self):
        return "action_tag_feedback"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
    	

        feedback = tracker.get_slot("sentiment")

        if feedback == "pos":
        	label = '[{"value":"postive feedback","color":"76af3d"}]'
        	#export_stories_to_file(tracker.events,tracker.sender_id,export_path="./data/stories.md")
        elif feedback == "neg":
            label = '[{"value":"negative feedback","color":"ff0000"}]'
        else:
        	return []
        tag_convo(tracker, label)

        return []
