Started = False
while True:
    user_input = input(">").lower()
    if user_input == "help":
        print("""
        start - to start the car"
        stop - to stop the car"
        quit - to exit
        """)
    elif user_input == "start":
        if Started:
            print("The Car is already started!")
        else:
            Started = True
            print("Car Started!")
    elif user_input == "stop":
        if not Started:
            print("Please Turn on the engine!")
        else:
            Started = False
            print("Car Stopped!")
    elif user_input == "quit":
        break
    else:
       print("I don't understand that...") 