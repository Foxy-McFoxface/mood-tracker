name = input("What is your name? ")
mood = input("How are you feeling today? ")
message = name + " feels " + mood + " today.\n"
date = input("What is the date today? (MM/DD/YYYY) ")
message = date + ": " + message
mood_score = 0
if mood == "happy":
    mood_score = 80
elif mood == "sad":
    mood_score = 1
elif mood == "neutral":
    mood_score = 50
elif mood == "excited":
    mood_score = 100
elif mood == "angry":
    mood_score = 20
message = message + " Mood Score: " + str(mood_score) + "\n"

file = open("mood.txt", "a")
file.write(message)
file.close()    

print("Your Mood was saved!")

