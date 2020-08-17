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

## opening hours + time of day + day
* greet
 - utter_greet
* ask_for_opening_hours
 - utter_ask_time_and_day
* inform_time_and_day{"day": "Tuesday","time_of_day":"evening"}
 - slot{"day":"Tuesday"}
 - slot{"time_of_day":"evening"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
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

## opening hours sad
* inform_time_and_day
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - slot{"requested_slot": "day"}
 - utter_need_day
* deny
 - utter_anything_else

## application 1
* greet
 - utter_greet
* apply
 - slot{"subject":"apply"}
 - utter_application
* deny
 - utter_anything_else

## application 2.1
* greet
 - utter_greet
* apply
 - slot{"subject":"apply"}
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
 - slot{"subject":"apply"}
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
    - utter_chatter

## Feedback
> check_conversation_finish
    - utter_ask_feedback
* feedback
    - action_tag_feedback
    - utter_anything_else

## interactive_story_1
* book_session
    - utter_ask_name
* state_name{"name": "Jan Feldmann"}
    - slot{"name": "Jan Feldmann"}
    - utter_ask_e-mail
* state_e-mail{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - find_slots_form
    - form{"name": "find_slots_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - form{"name": null}
    - slot{"requested_slot": null}
* state_slot{"time-slot": "2"}
    - slot{"time-slot": "2"}
    - book_session_form
    - form{"name": "book_session_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
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
    - slot{"subject":"apply"}
    - utter_application
* ask_more
    - faq_form
    - form{"name": "faq_form"}
    - slot{"subject":"apply"}
    - slot{"requested_slot": "null"}

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
    - action_tag_feedback
    - utter_anything_else
* deny
    - utter_goodbye

## tell_user_ID
* state_user_ID{"user_ID":"437463"}
    - utter_greet

## user_asks_more
* feedback
    - action_tag_feedback
    - utter_anything_else
* affirm
    - utter_tasks

## calm_down
* calm_down
 - utter_calm

## assistance
* ask_assistance
 - utter_tasks

## deny_feedback
 - utter_ask_feedback
* deny
 - utter_anything_else

## faq_ai_into_affirm
* ask_faq{"subject":"AI"}
    - slot{"subject": "AI"}
    - faq_form
    - form{"name": "faq_form"}
    - slot{"subject": "AI"}
    - form{"name": null}
* affirm
    - utter_ask_name
* state_name{"name": "Yannick Ruppert"}
    - slot{"name": "Yannick Ruppert"}
    - utter_ask_e-mail
* state_e-mail{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - find_slots_form
    - form{"name": "find_slots_form"}
    - slot{"name": "Yannick Ruppert"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - form{"name": null}
    - slot{"requested_slot": null}
* state_slot{"time-slot": "2"}
    - slot{"time-slot": "2"}
    - book_session_form
    - form{"name": "book_session_form"}
    - slot{"name": "Yannick Ruppert"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"time-slot":"2"}
    - form{"name": null}
    - slot{"requested_slot": null}

## deny_goodbye
 - utter_goodbye
* deny
 - utter_anything_else

## book_session_no_name
 - utter_ask_name
* state_name
 - utter_need_name
* deny
 - utter_anything_else

## book_session_no_mail
 - utter_ask_e-mail
* state_e-mail
 - find_slots_form
 - form{"name":"find_slots_form"}
 - slot{"name": "Jan"}
 - slot{"requested_slot": "e-mail"}
 - utter_need_mail
* deny
 - utter_anything_else

## book_session_no_slot
* state_e-mail{"e-mail": "jan.feldmann@mindsquare.de"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - find_slots_form
    - form{"name": "find_slots_form"}
    - slot{"name": "Yannick Ruppert"}
    - slot{"e-mail": "jan.feldmann@mindsquare.de"}
    - form{"name": null}
    - slot{"requested_slot": null}
* state_slot
    - book_session_form
    - form{"name":"book_session_form"}
    - slot{"requested_slot": "time-slot"}
    - utter_need_slot

## book_session_into_opening_times
* book_session
    - utter_ask_name
* state_name{"name": "Jan Feldmann"}
    - slot{"name": "Jan Feldmann"}
    - utter_ask_e-mail
* state_e-mail{"e-mail": "jan.feldmann@mindsquare.com"}
    - slot{"e-mail": "jan.feldmann@mindsquare.com"}
    - find_slots_form
    - form{"name": "find_slots_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* state_slot{"time-slot": "2"}
    - slot{"time-slot": "2"}
    - book_session_form
    - form{"name": "book_session_form"}
    - slot{"name": "Jan Feldmann"}
    - slot{"e-mail": "jan.feldmann@mindsquare.com"}
    - slot{"time-slot":"2"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_for_opening_hours
    - utter_ask_time_and_day
* inform_time_and_day{"day":"saturday"}
    - slot{"day": "saturday"}
    - opening_hours_form
    - form{"name":"opening_hours_form"}
    - form{"name": null}
    - slot{"time_of_day": null}

## usertesting_1
* greet
  - utter_greet
* state_slot{"time-slot":"1"}
  - slot{"time-slot": "2"}
  - book_session_form
  - form{"name": "book_session_form"}
  - slot{"requested_slot":"name"}
  - form{"name": null}
  - utter_ask_name
* deny
  - utter_anything_else
* affirm
  - utter_tasks
* inform_time_and_day{"day":"saturday"}
  - slot{"day":"saturday"}
  - opening_hours_form
  - form{"name":"opening_hours_form"}
  - form{"name":null}
  - slot{"time_of_day":null}
* thank
  - utter_welcome
  - utter_ask_feedback
* feedback
  - action_tag_feedback
  - utter_anything_else
* ask_for_form
  - application_form
  - form{"name":"application_form"}
  - form{"name":null}
  - slot{"requested_slot":null}
* thank
  - utter_welcome
  - utter_ask_feedback
* feedback
  - action_tag_feedback
  - utter_anything_else
* affirm
  - utter_tasks
* book_session
  - utter_ask_name
* state_name
  - utter_need_name
* state_name{"name":"Miriam Webster"}
  - slot{"name":"Miriam Webster"}
  - utter_ask_e-mail
* state_e-mail{"e-mail":"miriam.webster@words.com"}
  - slot{"e-mail":"miriam.webster@words.com"}
  - find_slots_form
  - form{"name":"find_slots_form"}
  - slot{"name":"Miriam Webster"}
  - slot{"e-mail":"miriam.webster@words.com"}
  - form{"name": null}
  - slot{"requested_slot": null}
* thank
  - utter_need_slot
* state_slot{"time-slot":"2"}
  - slot{"time-slot":"2"}
  - book_session_form
  - form{"name":"book_session_form"}
  - slot{"name":"Miriam Webster"}
  - slot{"e-mail":"miriam.webster@words.com"}
  - slot{"time-slot":"2"}
  - form{"name":null}
  - slot{"requested_slot":null}
  - slot{"time-slot":null}
* ask_faq{"subject":"AI"}
  - slot{"subject":"AI"}
  - faq_form
  - form{"name":"faq_form"}
  - form{"name": null}
  - slot{"requested_slot":null}
* deny
  - utter_anything_else
* deny
  - utter_goodbye

## session_start
* state_user_ID {"user_ID": 532785}
  - utter_greet
* ask_for_opening_hours
  - utter_ask_time_and_day

## affirm1
* ask_faq{"subject":"apply"}
  - slot{"subject":"AI"}
  - faq_form
  - form{"name":"faq_form"}
  - form{"name": null}
  - slot{"requested_slot":null}
* affirm
  - application_form
  - form{"name":"application_form"}
  - form{"name":null}
  - slot{"requested_slot":null}

## affirm2
* ask_faq{"subject":"AI"}
  - slot{"subject":"AI"}
  - faq_form
  - form{"name":"faq_form"}
  - form{"name": null}
  - slot{"requested_slot":null}
* affirm
  - utter_ask_name

## affirm3
* deny
  - utter_anything_else
* affirm
  - utter_tasks

## ask_more
* thank
  - utter_welcome
  - utter_ask_feedback
* ask_more
  - utter_tasks

## deny anything else
  -utter_anything_else
* deny
  - utter_goodbye

## greet+openinghours
* greet+ask_for_opening_hours
  - utter_greet
  - utter_ask_time_and_day

## greet+day
* greet+inform_time_and_day{"day": "Monday"}
 - utter_greet
 - slot{"day":"Monday"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - slot{"time_of_day": null}

## greet+apply
* greet+apply
  - utter_greet
  - utter_application 

## greet+ask_for_form
* greet+ask_for_form
 - utter_greet
 - application_form
 - form{"name":"application_form"}
 - form{"name":null}

## greet+faq
* greet+ask_faq{"subject":"apply"}
 - utter_greet
 - slot{"subject":"apply"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}

## greet+book
* greet+book_session
  - utter_greet
  - utter_ask_name

## affirm+day
* state_user_ID
 - utter_greet
* ask_for_opening_hours
 - utter_ask_time_and_day
* affirm+inform_time_and_day{"day": "Tuesday"}
 - slot{"day":"Tuesday"}
 - opening_hours_form
 - form{"name":"opening_hours_form"}
 - form{"name": null}
 - slot{"time_of_day": null}

## affirm+ask_faq
* affirm+ask_faq{"subject": "apply"}
 - slot{"subject":"apply"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}

## state_name_and_mail
* state_name+state_e-mail{"name":"Myrte Nijhuis","e-mail":"myrte@myrte.de"}
  - slot{"name":"Myrte Nijhuis"}
  - slot{"e-mail":"myrte@myrte.de"}
  - find_slots_form
  - form{"name":"find_slots_form"}
  - form{"name": null}
  - slot{"requested_slot": null}

## affirm+state_name
* affirm+state_name{"name": "Jan Feldmann"}
    - slot{"name": "Jan Feldmann"}
    - utter_ask_e-mail

## affirm+apply
* affirm+apply
 - utter_application 

## ask_faq+ask_for_form
* ask_faq+ask_for_form{"subject":"apply"}
 - slot{"subject":"apply"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
 - application_form
 - form{"name":"application_form"}
 - form{"name":null}

## feedback+form
* feedback+ask_for_form
  - action_tag_feedback
  - application_form
  - form{"name":"application_form"}
  - form{"name":null}
  - utter_anything_else

## book+day
* book_session+inform_time_and_day{"day":"Friday"}
 - utter_ask_name

## apply+form
* apply+ask_for_form
 - application_form
 - form{"name":"application_form"}
 - form{"name":null}

## apply+ask_faq
* apply+ask_faq{"subject":"apply"}
 - slot{"subject":"apply"}
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}

## Story from conversation with 9012289bf9af40b0a2e41dd14f719bc9 on August 11th 2020
* state_user_ID{"user_ID":"456128"}
    - utter_greet
* greet+ask_for_opening_hours
    - utter_greet
    - utter_ask_time_and_day
* inform_time_and_day{"day":"Saturday","time_of_day":"morning"}
    - slot{"day":"Saturday"}
    - slot{"time_of_day":"morning"}
    - opening_hours_form
    - form{"name":"opening_hours_form"}
    - slot{"day":"Saturday"}
* book_session
    - utter_ask_name
* state_name{"name":"Ju"}
    - slot{"name":"Ju"}
    - utter_ask_e-mail
* state_e-mail{"e-mail":"juse@ju.de"}
    - slot{"e-mail":"juse@ju.de"}
    - find_slots_form
    - form{"name":"find_slots_form"}
    - slot{"name":"Ju"}
    - slot{"e-mail":"juse@ju.de"}
* state_slot{"time-slot":"3"}
    - book_session_form
    - form{"name":"book_session_form"}
* thank
    - utter_welcome
    - utter_ask_feedback
* feedback
    - action_tag_feedback
    - utter_anything_else


## Story from conversation with 3cae0edbacb44e3ba265a4d4373de6a5 on August 17th 2020
* greet
  - utter_greet
* apply
  - utter_application
* ask_more
  - application_form
  - form{"name":"application_form"}
  - form{"name":null}

## faq no subject
 - faq_form
 - form{"name":"faq_form"}
 - form{"name":null}
 - slot{"requested_slot": "subject"}
 - utter_default

## form+openinghours
* ask_for_form+inform_time_and_day{"day":"Sunday"}
  - application_form
  - form{"name":"application_form"}
  - form{"name":null}
  - slot{"day":"Monday"}
  - opening_hours_form
  - form{"name":"opening_hours_form"}
  - form{"name": null}
  - slot{"time_of_day": null}

## affirm+book_session
* affirm+book_session
  - utter_ask_name