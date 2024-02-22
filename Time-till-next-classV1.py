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
    correct_input = False
    valid_hour = False
    valid_minute = False
    valid_meridian = False

    #Get current hour input
    while valid_hour != True:
        current_hour = input("Enter the current hour: ")
        valid_hour = hourvalid(current_hour)

    current_hour = int(current_hour)

    #get user input of current minute and send to error catching function           
    while valid_minute != True:
        current_minute = input("Enter the current minute: ")
        valid_minute = minutevalid(current_minute)

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

#function prompts user for class starting time and converts into minutes    
def classfun():
    #initializing variables for a while loop
    correct_input = False
    valid_hour = False
    valid_minute = False
    valid_meridian = False

    #Get current hour input
    while valid_hour != True:
        class_hour = input("\nEnter the class start time hour: ")
        valid_hour = hourvalid(class_hour)

    class_hour = int(class_hour)

    #This loop checks if the value is an integer and between 0 and 60           
    while valid_minute != True:
        class_minute = input("Enter the class starting time minute: ")
        valid_minute = minutevalid(class_minute)

    class_minute = int(class_minute)
    
    #12 hour time conversion
    while valid_meridian != True:
        class_half = input("AM or PM?: ")
        valid_meridian = meridianvalid(class_half)

    #add hours for pm
    if class_half.upper() == 'PM':
        class_hour += 12
            
    class_hourminutes = class_hour * 60

    class_time = class_hourminutes + class_minute

    return class_time


def travel():
    #travel time in minutes
    valid_travel = False
    
    while valid_travel != True:
        travel_minute = input("\nEnter the time it takes to get to your class in minutes: ")
        valid_travel = travelvalid(travel_minute)
    
    return travel_minute

#below are four error checking functions

#This function checks if the value is an integer and between 1 and 12
def hourvalid(hour):
        try:
            hour = int(hour)
            
            if hour < 1 or hour > 12:
                raise Exception
        
        except ValueError:
            print("\nPlease enter an integer for the current hour\n")
            hour = 'oopsies'
        except:
            print("\nPlease enter a valid integer between 1 and 12\n")


        if (type(hour) is int) and (1 <= hour <= 12):
            valid_hour = True

        else:
            valid_hour = False

        return valid_hour

#This function checks if the value is an integer and between 0 and 60
def minutevalid(minute):
        try:
            minute = int(minute)
            
            if minute < 0 or minute > 59:
                raise Exception
        
        except ValueError:
            print("\nPlease enter an integer for the current minute\n")
            minute = 'oopsies'
        except:
            print("\nPlease enter a valid integer between 0 and 59\n")


        if (type(minute) is int) and (0 <= minute <= 59):
            valid_minute = True

        else:
            valid_minute = False

        return valid_minute

#function checks if either 'AM' or 'PM' are entered (case insensitive)
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
        
    if (type(travel_minute) is int) and travel_minute > 0:
        valid_travel = True

    else:
        valid_travel = False
        
    return valid_travel


main()
