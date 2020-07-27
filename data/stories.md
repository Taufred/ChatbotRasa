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
 - slot{"time_of_day": null}
* thank
 - utter_welcome
> check_conversation_finish

## opening hours + day
* greet
 - utter_greet
* inform_time_and_day{"day": "Monday"}
 - slot{"day":"Monday"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - slot{"time_of_day": null}
* thank
 - utter_welcome
> check_conversation_finish

## opening hours + time
* greet
 - utter_greet
* inform_time_and_day{"time_of_day": "morning"}
 - slot{"time_of_day":"morning"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - slot{"time_of_day": null}
* thank
 - utter_welcome
> check_conversation_finish

## opening hours + time + day
* greet
 - utter_greet
* inform_time_and_day{"day": "Tuesday", "time_of_day": "afternoon"}
 - slot{"day":"Tuesday"}
 - slot{"time_of_day":"afternoon"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - slot{"time_of_day": null}
* thank
 - utter_welcome
> check_conversation_finish

## application 1
* greet
 - utter_greet
* apply
 - utter_application
* deny
 - utter_anything_else

## application 2.1
* greet
 - utter_greet
* apply
 - utter_application
* affirm
 - application_form
* thank
 - utter_welcome
> check_conversation_finish

## application 2.2
* greet
 - utter_greet
* apply
 - utter_application
* ask_for_form
 - application_form
* thank
 - utter_welcome
> check_conversation_finish

## application 3
* greet
 - utter_greet
* ask_faq{"subject":"apply"}
 - slot{"subject":"apply"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
* affirm
 - application_form
* thank
 - utter_welcome
> check_conversation_finish

## application 4
* greet
 - utter_greet
* ask_faq{"subject":"apply"}
 - slot{"subject":"apply"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
* deny
 - utter_anything_else

## book AI expert session 1
* greet
 - utter_greet
* ask_faq{"subject":"AI"}
 - slot{"subject":"AI"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
* book_session
 - utter_ask_name
* state_name{"name":"Harry Potter"}
 - slot{"name":"Harry Potter"}
 - utter_ask_e-mail
* state_e-mail{"e-mail":"hp_seeker@hogwarts.com"}
 - slot{"e-mail":"hp_seeker@hogwarts.com"}
 - find_days_form
 - form{"name":"find_days_form"}
 - form{"name":"null"}
* state_day
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot
 - slot{"time-slot":"2"}
 - book_session_form
 - form{"name":"book_session_form"}
 - form{"name":"null"}
* thank
 - utter_welcome
> check_conversation_finish

## book AI expert session 2
* greet
 - utter_greet
* ask_faq{"subject":"AI"}
 - slot{"subject":"AI"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
* affirm
 - utter_ask_name
* state_name{"name":"Harry Potter"}
 - slot{"name":"Harry Potter"}
 - utter_ask_e-mail
* state_e-mail{"e-mail":"hp_seeker@hogwarts.com"}
 - slot{"e-mail":"hp_seeker@hogwarts.com"}
 - find_days_form
 - form{"name":"find_days_form"}
 - form{"name":"null"}
* state_day
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot
 - slot{"time-slot":"2"}
 - book_session_form
 - form{"name":"book_session_form"}
 - form{"name":"null"}
* thank
 - utter_welcome
> check_conversation_finish

## book AI expert session 3
* greet
 - utter_greet
* ask_faq{"subject":"AI"}
 - slot{"subject":"AI"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
* deny
 - utter_anything_else

## New Story
* greet
 - utter_greet
* ask_faq{"subject":"AI"}
 - slot{"subject":"AI"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
* book_session
 - utter_ask_name
* state_name{"name":"Harry Potter"}
 - slot{"name":"Harry Potter"}
 - utter_ask_e-mail
* state_e-mail{"e-mail":"hp_seeker@hogwarts.com"}
 - slot{"e-mail":"hp_seeker@hogwarts.com"}
 - find_days_form
 - form{"name":"find_days_form"}
 - form{"name":"null"}
* state_day
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot
 - slot{"time-slot":"2"}
 - book_session_form
 - form{"name":"book_session_form"}
 - form{"name":"null"}
* thank
 - utter_welcome
> check_conversation_finish

## Assistance + Book Session
* greet
 - utter_greet
* ask_assistance
 - utter_tasks
* book_session
 - utter_ask_name
* state_name{"name":"Harry Potter"}
 - slot{"name":"Harry Potter"}
 - utter_ask_e-mail
* state_e-mail{"e-mail":"hp_seeker@hogwarts.com"}
 - slot{"e-mail":"hp_seeker@hogwarts.com"}
 - find_days_form
 - form{"name":"find_days_form"}
 - form{"name":"null"}
* state_day
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot
 - slot{"time-slot":"2"}
 - book_session_form
 - form{"name":"book_session_form"}
 - form{"name":"null"}
* thank
 - utter_welcome
> check_conversation_finish

## New Story
* chatter
    - utter_iamabot

## Feedback
> check_conversation_finish
    - utter_ask_feedback
* feedback
    - utter_thumbsup
    - utter_anything_else
