name = input("What is your name? ")
mood = input("How are you feeling today? ")
message = name + " feels " + mood + " today.\n"

file = open("mood.txt", "a")
file.write(message)
file.close()    

print("Your Mood was saved!")

