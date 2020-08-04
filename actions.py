from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import EventType, SlotSet, SessionStarted, ActionExecuted

import calendar
import json


# BACKGROUND DATA - SHOULD BE STORED IN A DATABASE OR RETRIEVED FROM A SERVER
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
	}

}


#Returns the opening hours for a specific day or even time of day
def find_opening_hours(day, time_of_day):
	#Find out the number that belongs to the day
	days = []
	for day_name in calendar.day_name:
		days.append(day_name.lower())
	days = dict(zip(days, range(7))); 
	if day.lower() in days:
		day_nr = days[day.lower()]
	else:
		return ""
	#retrieve the opening hours from that number
	opening_hours = OPENING_HOURS[day_nr]

	#optionally return only one part of the hours
	if time_of_day!=None:
		if time_of_day.lower() in morning:
			opening_hours = opening_hours["morning"]
		elif time_of_day.lower() in evening:
			opening_hours = opening_hours["evening"]
		result = str(opening_hours)
	else:
		result = "{} and {}".format(opening_hours["morning"],opening_hours["evening"])
	return result

#Action deals with any question by replying with the opening hours
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
		#retrieve
		day = tracker.get_slot("day")
		if day.lower() == "today" or day.lower() == "tonight":
			my_date = date.today()
			day_name = calendar.day_name[my_date.weekday()]
		elif day.lower() == "tomorrow":
			my_date = date.today()
			tomorrow = my_date + datetime.timedelta(days=1)
			day_name = calendar.day_name[tomorrow .weekday()]
		elif day.lower() == "all" or day.lower() == "every":
			dispatcher.utter_message("Sorry, our opening hours differ from day to day. Please ask for specific day, so that I can retrieve the correct information.")
			return [SlotSet("time_of_day", None)]
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
		return [SlotSet("time_of_day", None)]

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
		dispatcher.utter_message("I will redirect you to the application form, just click [here](https://taufred.github.io/)!")
		return []
		

class Book_session_form(FormAction):
	def name(self) -> Text:
		return "book_session_form"
#
	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return ["name","e-mail","time-slot"]

	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		name = tracker.get_slot("name")
		dispatcher.utter_message("I have booked a session for {} on Friday! You will receive a confirmation mail with further instructions.".format(name))
		return [SlotSet("time-slot", None)]
		
class FAQ_form(FormAction):
	def name(self) -> Text:
		return "faq_form"
#
	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return ["subject"]

	def slot_mappings(self) -> Dict[Text, Any]:
		return {"subject": self.from_entity(entity="subject",
									intent= ["ask_faq"])}

	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		subject = tracker.get_slot("subject")
		if subject == "AI":
			dispatcher.utter_message("AI describes machines, which, by the use of algorithms, solve tasks autonomously and adaptively. If you want to know more about this subject, we offer special expert sessions on Fridays! Would you like to book one?")
		elif subject == "apply":
			dispatcher.utter_message("You can apply by filling in your details on our website. It will be read by our personnel and you will get an answer after a couple of days! Should I redirect you to the application form?")
		elif subject == "degree":
			dispatcher.utter_message("To work at this firm you need to at least have completed one bachelor's study in an IT-field! Data Science and AI students are welcome as well. Should I redirect you to the application form?")
		elif subject == "salary":
			dispatcher.utter_message("The salary highly depends on the specific function you are applying for. I suggest checking the details on the application form. Should I redirect you to the application form?")
		else:
			dispatcher.utter_message("I do not know anything about {}. Would you like to book an expert session?".format(subject))
		return []

class Find_slots_form(FormAction):
	def name(self) -> Text:
		return "find_slots_form"
#
	@staticmethod
	def required_slots(tracker:Tracker) -> List[Text]:
		'''A List of required slots that the form has to fill'''
		return ["name","e-mail"]

	def slot_mappings(self) -> Dict[Text, Any]:
		return {"name": self.from_entity(entity="name",
									intent= ["state_name"]),
				"e-mail": self.from_entity(entity="e-mail",
									intent= ["state_e-mail"])}

	def submit(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		name = tracker.get_slot("name")
		e_mail = tracker.get_slot("e-mail")
		dispatcher.utter_message("We have slots available at 1: 10:15, 2: 11:15 and 3: 12:45 for you on Friday, {}. Please reply with the slot number you want to reserve.".format(name))
		return []


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        dispatcher.utter_message("Welcome, my name is MindBot. Before we start, would you be so kind to tell me your user ID from the survey?")
        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))
        return events