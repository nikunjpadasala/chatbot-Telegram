from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ('hello', 'hii', 'sup',):
        return "hey! how's it going?"

    if user_message in ('who are you?', 'who are you'):
        return 'i am chatbot'

    if user_message in ('how old are you?', 'how old are you'):
        return 'i am 20'

    if user_message in ('where you studied?', 'where you studied'):
        return 'Basgu'

    if user_message in ('where you live?', 'where you live'):
        return 'Sterlitamak, Russia'

    if user_message in (' I am What should I do?', 'I am What should I do'):
        return 'know what the Health Authority recommendations are'

    if user_message in ('who is noob?', 'who is noob'):
        return 'vidhen'

    if user_message in ('i dont know what to do now that I am sick?', 'i dont know what to do now that I am sick'):
        return "know what to do if you've fallen ill"

    if user_message in ('What should I do because I touched someone who are sick with corona?', 'What should I do because I touched someone who are sick with corona'):
        return "know what to do if you've been in contact with a person who has tested positive for Coronavirus/COVID-19"

    if user_message in ('How do I do to help my employes with corona?', 'How do I do to help my employes with corona'):
        return 'know what to do as an employer to protect your employees'

    if user_message in ('what should i do to minimise the spread?', 'what should i do to minimise the spread'):
        return 'know what you can do as a citizen to minimize the spread of Coronavirus/COVID-19'

    if user_message in ('I am not at risk is there anything I should do?', 'I am not at risk is there anything I should do'):
        return 'know what to do as a person who does not fall within any of the known risk groups'    

    if user_message in ('You a girl?', 'You a guy?', 'You a guy', 'You a girl', 'What is your gender?', 'What is your gender'):
        return 'I am Bot so that dont apply on me'

    if user_message in ('Can you ask something about myself?', 'Can you ask something about myself'):
        return "I'm a much better answerer than asker."

    if user_message in ('who is noob?', 'who is noob'):
        return 'vidhen'

    if user_message in ('who is noob?', 'who is noob'):
        return 'vidhen'

    if user_message in ('who is noob?', 'who is noob'):
        return 'vidhen'

    if user_message in ('who is noob?', 'who is noob'):
        return 'vidhen'

    if user_message in ('who is noob?', 'who is noob'):
        return 'vidhen'



    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')

        return str(date_time)

    return "I don't understand you"