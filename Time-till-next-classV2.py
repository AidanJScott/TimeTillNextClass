#program takes user input of current time, class starting time, and time it
#takes to get to class, and calculates how long until user must leave for class

def main():
    current_time = int(current())
    class_time = int(classfun())
    travel_minute = int(travel())

    #calculate and display time left
    time_remaining = (class_time - travel_minute - current_time)
    hours = time_remaining // 60
    minutes = time_remaining % 60
    if time_remaining >= 0:
        print(f'\nYou have {hours} hour{"(s)"} and {minutes} minute{"(s)"} until you have to leave for class.')
    else:
        print("You are late to class, LEAVE")

#function prompts user for current time and converts into minutes    
def current():
    #initializing variables for a while loop
    valid_hour = False
    valid_minute = False
    valid_timeformat = False
    valid_meridian = False

    while(valid_timeformat != True) or (valid_hour != True) or (valid_minute != True):
        i_current_time = input("Please enter the current time in hh:mm format:\n")

        valid_timeformat = timeformat(i_current_time)
                 
        if valid_timeformat == True:
            if len(i_current_time) == 4:
                i_current_time = "0" + i_current_time

            #splices inputs into hour and minute values    
            current_hour = i_current_time[0:2]
            current_minute = i_current_time[3:]

            valid_hour = hourvalid(current_hour)
            valid_minute = minutevalid(current_minute)

    #convert string literals to integers for later operations
    current_hour = int(current_hour)
    current_minute = int(current_minute)
    
    #12 hour time conversion
    while valid_meridian != True:
        current_half = input("AM or PM?: ")
        valid_meridian = meridianvalid(current_half)

    #add hours for pm
    if current_half.upper() == 'PM':
        current_hour += 12

    #calculate total minutes passed in a day     
    current_hourminutes = current_hour * 60

    current_time = current_hourminutes + current_minute

    return current_time
            
        
def classfun():
    #initializing variables for a while loop
    valid_hour = False
    valid_minute = False
    valid_timeformat = False
    valid_meridian = False

    while(valid_timeformat != True) or (valid_hour != True) or (valid_minute != True):
        i_class_time = input("Please enter the class starting time in hh:mm format:\n")

        valid_timeformat = timeformat(i_class_time)
                 
        if valid_timeformat == True:
            if len(i_class_time) == 4:
                i_class_time = "0" + i_class_time
            
            class_hour = i_class_time[0:2]
            class_minute = i_class_time[3:]

            valid_hour = hourvalid(class_hour)
            valid_minute = minutevalid(class_minute)

    #convert string literals to integers for later operations
    class_hour = int(class_hour)
    class_minute = int(class_minute)
    
    #12 hour time conversion
    while valid_meridian != True:
        class_half = input("AM or PM?: ")
        valid_meridian = meridianvalid(class_half)

    #add hours for pm
    if class_half.upper() == 'PM':
        class_hour += 12

    #calculate total minutes passed in a day     
    class_hourminutes = class_hour * 60

    class_time = class_hourminutes + class_minute

    return class_time
    return

def travel():
    #travel time in minutes
    valid_travel = False

    #send to format checking function
    while valid_travel != True:
        travel_minute = input("\nEnter the time it takes to get to your class in minutes: ")
        valid_travel = travelvalid(travel_minute)

    #return the minute value to the main function
    return travel_minute

def timeformat(i_time):
    valid_format = False
    
    #format single digit hour entries
    if len(i_time) == 4:
        i_time = "0" + i_time

    #checking length and formatting
    if len(i_time) != 5 or ":" not in i_time:
        print("Error: the time entered is not in hh:mm format\n")

    elif len(i_time) == 5 and ":" in i_time:
        valid_format = True

    #return boolean value to loop in the time functions
    return valid_format

#Checks if the hour entered is within 12 hour time bounds (1-12)
def hourvalid(hour):
    try:
        hour = int(hour)
        
        if hour < 1 or hour > 12:
            raise Exception
    
    except ValueError:
        print("Error: Hour value must be an integer\n")
        valid_hour = False
        
    except:
        print("Error: Hour value must be between 1 and 12\n")
        valid_hour = False


    if (type(hour) is int) and (1 <= hour <= 12):
        valid_hour = True

    #returns boolean value to the time function
    return valid_hour

#Checks if the entered minute is within time format bounds (0-60)
def minutevalid(minute):
    try:
        minute = int(minute)
        
        if minute < 0 or minute > 59:
            raise Exception
    
    except ValueError:
        print("Error: Minute value must be an integer\n")
        valid_minute = False
        
    except:
        print("Error: Minute value must be between 0 and 59\n")
        valid_minute = False


    if (type(minute) is int) and (0 <= minute <= 59):
        valid_minute = True

    #return boolean value to the time function
    return valid_minute
    

def meridianvalid(current_half):
    if current_half.upper() == 'PM':
        valid_meridian = True
                               
    elif current_half.upper() != 'AM' and current_half.upper() != 'PM':
        print("Please enter either 'AM' or 'PM'")
        valid_meridian = False

    elif current_half.upper() == 'AM':
        valid_meridian = True
            
    return valid_meridian

#function checks if travel time in minutes is a valid integer
def travelvalid(travel_minute):
    try:
        travel_minute = int(travel_minute)

        if travel_minute < 0:
            raise Exception
        
    except ValueError:
        print("\nPlease enter an integer for time it takes to get to class in minutes\n")
        travel_minute = 'oopsies'

    except:
        print("\nPlease enter a valid integer above 0\n")
        
    if (type(travel_minute) is int) and travel_minute >= 0:
        valid_travel = True

    else:
        valid_travel = False
        
    return valid_travel

main()
