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
 - form{"name":"application_form"}
 - form{"name":null}
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
 - form{"name":"application_form"}
 - form{"name":null}
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
 - form{"name":"application_form"}
 - form{"name":null}
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
* inform_time_and_day{"day":"Tuesday"}
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot{"time-slot":"2"}
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
* inform_time_and_day{"day":"Tuesday"}
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot{"time-slot":"2"}
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
* inform_time_and_day{"day":"Tuesday"}
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot{"time-slot":"2"}
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
* inform_time_and_day{"day":"Tuesday"}
 - slot{"day":"Tuesday"}
 - find_slots_form
 - form{"name":"find_slots_form"}
 - form{"name":"null"}
* state_slot{"time-slot":"2"}
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

## interactive_story_1
* book_session
    - utter_ask_name
* state_name{"name": "Jan Feldmann"}
    - slot{"name": "Jan Feldmann"}
    - utter_ask_e-mail
* state_e-mail{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - find_days_form
    - form{"name": "find_days_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform_time_and_day{"day": "Tuesday"}
    - slot{"day": "Tuesday"}
    - find_slots_form
    - form{"name": "find_slots_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"day": "Tuesday"}
    - form{"name": null}
    - slot{"requested_slot": null}
* state_slot{"time-slot": "2"}
    - slot{"time-slot": "2"}
    - book_session_form
    - form{"name": "book_session_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"day": "Tuesday"}
    - slot{"time-slot":"2"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank
    - utter_welcome
    - utter_ask_feedback

## interactive_story_2
* greet
    - utter_greet
* inform_time_and_day{"day": "Friday", "time_of_day": "night"}
    - slot{"day": "Friday"}
    - slot{"time_of_day": "night"}
    - opening_hours_form
    - form{"name": "opening_hours_form"}
    - slot{"day": "Friday"}
    - slot{"time_of_day": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* apply
    - utter_application
* ask_more
    - faq_form
    - form{"name": "faq_form"}
    - slot{"requested_slot": "subject"}

## interactive_story_2
* ask_faq{"subject": "apply"}
    - slot{"subject": "apply"}
    - faq_form
    - form{"name": "faq_form"}
    - slot{"subject": "apply"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - application_form
    - form{"name": "application_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
>check_conversation_finish

## interactive_story_3
* ask_faq{"subject": "degree"}
    - slot{"subject": "degree"}
    - faq_form
    - form{"name": "faq_form"}
    - slot{"subject": "degree"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - application_form
    - form{"name": "application_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
>check_conversation_finish

## interactive_story_3
* ask_faq{"subject": "salary"}
    - slot{"subject": "salary"}
    - faq_form
    - form{"name": "faq_form"}
    - slot{"subject": "salary"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - application_form
    - form{"name": "application_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye
>check_conversation_finish


## interactive_story_4
* greet
    - utter_greet
* ask_faq{"name": "mindsquare", "subject": "salary"}
    - slot{"name": "mindsquare"}
    - slot{"subject": "salary"}
    - faq_form
    - form{"name": "faq_form"}
    - slot{"subject": "salary"}
    - slot{"subject": "salary"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - application_form
    - form{"name": "application_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank
    - utter_welcome
    - utter_ask_feedback
* feedback
    - utter_thumbsup
    - utter_anything_else
* deny
    - utter_goodbye
