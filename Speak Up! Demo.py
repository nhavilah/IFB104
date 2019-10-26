#unit testing demo: Speak Up!

def speak_up(phrase,exclaim):
    loud_phrase=phrase.upper()
    loud_phrase=loud_phrase+'!!!'*exclaim
    return loud_phrase

#main program
greeting = 'henlo'
print(speak_up(greeting,7))
print(speak_up('Good'+'bye',3+4))

