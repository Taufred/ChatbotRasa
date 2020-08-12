## intent:greet
- hello
- hi
- Who are you
- Good to see you
- Good morning, bot!
- good evening
- sup
- What's up

## intent:ask_for_opening_hours
- what are your opening hours?
- when are you closing
- what are your business hours

## intent:inform_time_and_day
- I changed my mind, [Friday](day) would be better
- What time are you open 'til [this evening](time_of_day)
- How late are you open until [Tonight](day)?
- Hello MindBot! I would like to know when I can visit the company on [saturdays]{"entity": "day", "value": "Saturday"}?
- What time do you close [today](day)?
- when are you open on [Monday](day)?
- When are you open on [saturday](day)?
- What about [sun]{"entity": "day", "value": "Sunday"}
- are you open in the [afternoon](time_of_day)?
- I want to know when I can visit the company [saturday](day) [morning](time_of_day)
- [wednesday](day)
- What about [sundays]{"entity": "day", "value": "Sunday"}

## intent:apply
- I want an interview
- Do you have any jobs?

## intent:ask_for_form
- Do you have a form
- Please redirect me

## intent:book_session
- book me an expert session
- I would like to book one!
- I would like to talk to an expert
- I wanna book an expert session
- book

## intent:ask_faq
- What can you tell me about [AI](subject)?
- what's the [process](subject) like?
- What do you know about [AI](subject)?
- How can I [apply](subject) for a job her?
- Do I need a [diploma]{"entity": "subject", "value": "degree"}?

## intent:thank
- thx
- perfect thank you
- Thanks, mate
- well that was easy, thanks mr MindBot
- cool, thanks
- thank again

## intent:goodbye
- goodnight
- gotta go
- see you around
- Bye!
- Goodbye :)

## intent:affirm
- There is in fact!
- absolutely
- yes sir!
- sure
- yeah

## intent:deny
- you shouldnt
- no this does not work for me
- I do NOT want a session
- do you have something else
- don't like that

## intent:mood_great
- I'm good
- I am feeling very good

## intent:feedback
- 5 stars
- I liked it
- I'm happy about that
- It was good
- still pretty alright
- You are useless.
- It was terrific!
- not satisfied at all

## intent:mood_unhappy
- not very good
- sad

## intent:bot_challenge
- are you a human?

## intent:chatter
- What's my ID?
- Can you give me a phone number?
- 📚

## intent:ask_assistance
- please help me
- Can you assist me?

## intent:suggest
- Do something

## intent:out_of_scope
- 143dw

## intent:ask_more
- Answer my question
- Anything else?

## intent:state_name
- [Rudi Unruh](name)
- [Manu Fuchs](name)
- My name is [Peter Pan](name)
- [Vasiliy Kool C](name)
- [Allard Barends](name)
- [Denise Villeneuve](name)
- [Uisenma Borchu](name)
- [Günther Jauch](name)
- My name is [Yannick Ruppert](name)
- The name is [Schweitzer](name)
- [Marcus Winkler](name)
- [Marietjie Garnier](name)

## intent:state_e-mail
- [j.r@aol.de](e-mail)
- Send a mail to [brit@ney.de](e-mail)
- my email ist [marvin@barfin.de](e-mail)
- My email is [marv@barf.un](e-mail)
- My mail is [jan.feldmann@mindsquare.de](e-mail)

## intent:state_slot
- Please reserve [4](time-slot)
- [3](time-slot)
- slot [2](time-slot) please

## intent:calm_down
- chill out
- slower please
- relax a bit

## intent:state_user_ID
- I am user nr. [987654](user_ID)
- [937564](user_ID) is my User ID

## intent:greet+ask_for_opening_hours
- Hi when can I visit the company?

## intent:greet+inform_time_and_day
- hey there, what is the opening time on [Saturday](day)

## intent:greet+apply
- Good day, I'd like to know whether there are job opportunities

## intent:greet+ask_for_form
- Hey bot, please send me the link

## intent:greet+ask_faq
- yo bot how does the [application]{"entity": "subject", "value": "apply"} work?

## intent:greet+book_session
- hello do you offer sessions?

## intent:affirm+inform_time_and_day
- Yeah, [Wednesday](day) please

## intent:affirm+ask_faq
- For sure, who do I send the [application]{"entity": "subject", "value": "apply"} to?

## intent:state_name+state_e-mail
- [Nick Veerman](name), [nick@student.ru.nl](e-mail)

## intent:affirm+state_name
- yes and my name is [Tom Riddle](name)

## intent:affirm+apply
- yes, I'd like to apply

## intent:ask_faq+ask_for_form
- I want to know about the [application process]{"entity": "subject", "value": "apply"} and a link to the application page.

## intent:feedback+ask_for_form
- It was good but I still need the link for the application

## intent:book_session+inform_time_and_day
- I'd like to book a session on [Friday](day)

## intent:apply+ask_for_form
- I want to apply, please redirect me.

## intent:apply+ask_faq
- Are you hiring? Who do I send my [application]{"entity": "subject", "value": "apply"}?

## synonym:AI
- artificial intelligence
- ai
- Artificial Intelligence
- KI

## synonym:Friday
- fri
- friday
- Fridays
- fridays
- Fri

## synonym:Monday
- monday
- mondays
- mon
- Mondays
- Mon

## synonym:Saturday
- Saturdays
- saturdays
- sat
- saturday
- Sat

## synonym:Sunday
- sun
- sundays
- sunday
- Sundays
- Sun

## synonym:Thursday
- thu
- thursday
- Thursdays
- thursdays
- Thu

## synonym:Tuesday
- Tue
- tuesdays
- tuesday
- tue
- Tuesdays

## synonym:Wednesday
- Wednesdays
- wednesday
- wednesdays
- wed
- Wed

## synonym:apply
- application process
- application
- process

## synonym:degree
- diploma

## synonym:salary
- pay

## regex:e-mail
- [A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}

## regex:time-slot
- [0-9]{1}

## regex:user_ID
- [0-9]{6}
