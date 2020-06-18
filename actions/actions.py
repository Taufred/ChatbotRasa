from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import datetime
import calendar
#
#
#

morning = ["morning", "noon"]
evening = ["evening", "afternoon", "night"]

OPENING_HOURS = {
	0:	{
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
	6:	{
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
			dispatcher.utter_message("Sorry, I couldn't find any opening hours on {}.".format(day_name), results)
			return []
		elif time_of_day == None:
			dispatcher.utter_message("These are the opening hours on {}: ".format(day_name), results)
		else:
			dispatcher.utter_message("These are the opening hours on {} in the {}: ".format(day_name,time_of_day), results)
		return []

