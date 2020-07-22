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
* thank
 - utter_welcome
> check_conversation_finish

## application 1
* greet
 - utter_greet
* apply
 - utter_application
* deny
> check_conversation_finish

## application 2
* greet
 - utter_greet
* apply
 - utter_application
* affirm
* ask_for_form
 - application_form
* thank
 - utter_welcome
> check_conversation_finish

## book AI expert session 1
* greet
 - utter_greet
* ask_faq{"subject":"AI"}
 - slot{"subject":"AI"}
 - faq_form
* book_session
 - book_session_form
* thank
 - utter_welcome
> check_conversation_finish

## New Story
* greet
    - utter_greet
* ask_faq{"subject":"AI"}
    - slot{"subject":"AI"}
    - faq_form
    - form{"name":"faq_form"}
    - slot{"subject":"AI"}
    - slot{"subject":"AI"}
    - form{"name":null}
    - slot{"requested_slot":null}
* book_session
    - book_session_form
    - form{"name":"book_session_form"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thank
 - utter_welcome
> check_conversation_finish

## Assistance + Book Session
* greet
 - utter_greet
* ask_assistance
 - utter_tasks
* ask_book_session
 - book_session_form
* thank
 - utter_welcome
> check_conversation_finish

## New Story
* greet
    - utter_greet
* ask_assistance
    - utter_tasks
* book_session
    - book_session_form
    - form{"name":"book_session_form"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thank
 - utter_welcome
> check_conversation_finish

## New Story
* chatter
    - utter_iamabot


## Positive Feedback
> check_conversation_finish
    - utter_ask_feedback
* feedback{"sentiment": "pos"}
    - slot{"sentiment": "pos"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else

## Neutral Feedback
> check_conversation_finish
    - utter_ask_feedback
* feedback{"sentiment": "neu"}
    - slot{"sentiment": "neu"}
    - action_tag_feedback
    - utter_thumbsup
    - utter_anything_else

## Negative Feedback
> check_conversation_finish
    - utter_ask_feedback
* feedback{"sentiment": "neg"}
    - slot{"sentiment": "neg"}
    - action_tag_feedback
    - utter_ask_suggestion
* suggest
    - utter_thanks
    - utter_anything_else

