command= ""
while command != 'Quit':
    command = input('>')
    if command == 'start':
        print("Car is started , Ready to GO")
    elif command == 'stop':
        print("Car is stopped")
    elif command == 'help':
        print("""
start -> start the car 
stop -> stop the car 
quit-> exit""")
    elif command == 'Quit':
        break
else:
    print("Nothing!")