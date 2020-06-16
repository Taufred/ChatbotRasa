## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## opening hours
* greet
 - utter_greet
* ask_for_opening_hours
 - utter_ask_time_and_day
* inform_time_and_day{"day": "Monday"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - slot{"day":"Monday"}
* thank
 - utter_goodbye

## opening hours + day
* greet
 - utter_greet
* inform_time_and_day{"day": "Monday"}
 - slot{"day":"Monday"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
* thank
 - utter_goodbye

## opening hours + time
* greet
 - utter_greet
* inform_time_and_day{"time_of_day": "morning"}
 - slot{"time_of_day":"morning"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - utter_goodbye

## opening hours + time + day
* greet
 - utter_greet
* inform_time_and_day{"day": "Tuesday", "time_of_day": "afternoon"}
 - slot{"day":"Tuesday"}
 - slot{"time_of_day":"afternoon"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
* thank
 - utter_goodbye
 