
import streamlit

# alarming about the unusual stop
def calculater_time(speed,eta):
    if speed == 0 & eta > 1.0:
        contact_admin()
        

# constantly checking time w.r.t speed
def timer(speed,user_loc,distance_covered,eta):
    if speed > 0:
        wait_time = (user_loc - distance_covered)/speed
        send_end_user_message(wait_time)
    elif speed == 0 & eta < 1.0:
        wait_time = wait_time + 1
        calculater_time(speed,wait_time)          
        

# create a for loop which constantly updates speed, starts with location 1 and ends at end location

def speeds(destination,stops):
    user_loc  = 10 # assuming user location
    distance_covered = 0
    speed = 25
    eta = 0
    while(distance_covered != destination[len(destination)-1]):
          # avg speed
        eta = timer(speed,user_loc,distance_covered,eta)
        if distance_covered in stops:
            speed = 0
        elif distance_covered == user_loc:
            speed = 0    
        elif distance_covered == 21:
            speed = 0
            eta = 11
        elif speed == 0 & distance_covered not in stops:
            flag = contact_admin()    
        
            if flag == 1:
                contact_admin()
            else:
                speed = 25
                
        distance_covered = distance_covered + 1
        print(distance_covered)


def contact_admin():
    check_incident()

def check_incident():
    response = contact_driver()   
    
    if response == 1:
        real_incident = "Bus has some mechanincal fault, send new bus immediately"
        send_admin(real_incident,1)
        send_end_user_message("Bus break down, sorry for the inconvenience")
        return 1
    if response == 2:
        real_incident = "Bus has some electrical fault, send new bus immediately"
        send_admin(real_incident,1)
        send_end_user_message("Bus break down, sorry for the inconvenience")
        return 1
    if response == 3:
        real_incident = "There is an accident on the route! "
        send_admin(real_incident,0)
        send_end_user_message("There is an accident on the route! Sorry to keep you waiting")
        return 1
    if response == 4:
        real_incident = "Bus has been invloved in a mishap! Call medics!"
        send_admin(real_incident,2)
        send_end_user_message("Bus break down, sorry for the inconvenience")  
        return 1  
    else:
        return 0

def contact_driver():
    # driver knows the options
    options = [1,2,3,4]
    choice = options[2]
    return choice
    

def send_admin(input,action):
    # Here the admin gets to know the real reason behind the fault
    # its there decision what to update the end user
    
    if action == 2:
        # call 911
        pass
    
    if action == 0:
        send_end_user_message("It's the peak hours, sorry but we're stuck in a jam")
    
    if action == 1:
        send_new_bus()
        send_end_user_message("We're facing some difficulties, arrving to your stop in a while")
    
    
def send_new_bus():
    user_eta()

def send_end_user_message(message):
    print(message)
    
    
## VARIABLES

## user_loc -> start to destn

## 

destination = []

for i in range(1,31):
    destination.append(i)
    
stops = [1,6,13,17,21,24,26,28,30]
#wait_time = 1
speeds(destination,stops)