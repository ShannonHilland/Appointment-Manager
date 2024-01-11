from appointment import Appointment
import os
calendar = []
def create_weekly_calendar():
    counter = 0
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    while counter < 6:
        day = weekday[counter]
        for time in range(9, 17):
           a = Appointment(day, time)
           calendar.append(a)
        counter += 1
    print('Weekly calendar created')

def find_appointment_by_time(day, time):     
    for appt in calendar:
        appt_day = appt.get_day_of_week()
        if appt_day == day:
            appt_time = appt.get_start_time_hour()
            if appt_time == time:
                return appt

def load_scheduled_appointments():
    filename = input('Enter appointment filename: ') 
    while os.path.exists(filename) != True:
        filename = input('File not found. Re-enter appointment filename: ')
    upload_file = open(filename, 'r')
    counter = 0
    for each_line in upload_file:
        appt_upload = each_line.strip().split(",")
        name = appt_upload[0]
        phone = appt_upload[1]
        appt_type = appt_upload[2]
        day = appt_upload[3]
        time = int(appt_upload[4])
        appt = find_appointment_by_time(day, time)
        appt.schedule(name, phone, appt_type)
        counter += 1
    print(f'{counter} appointments were loaded into the schedule')
    

def show_appointments_by_name(name):
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
    print("-"*70)
    for appt in calendar:
        appt_name = appt.get_client_name()
        if name in appt_name:
            print(appt.__str__())        

def show_appointments_by_day(day):
    for appt in calendar:
        appt_day = appt.get_day_of_week()
        if appt_day == day.title():
            print(appt.__str__())

def save_scheduled_appointments():
    filename = input('Enter appointment filename: ')
    file_exists = os.path.exists(filename)
    while file_exists == True:
        proceed = input('File already exists. Do you want to overwrite it (Y/N)? ') 
        if proceed == 'N' or proceed == 'n':
            filename = input('Enter appointment filename: ')
            file_exists = os.path.exists(filename)
        elif proceed =='Y' or proceed == 'y':
            file_exists = False
        else:
            filename = input('Invalid input. Enter appointment filename: ')   
            file_exists = os.path.exists(filename)
    save_file = open(filename, 'w')
    counter = 0
    for appt in calendar:
        appt_type = appt.get_appt_type()
        if appt_type != '':
            record = appt.format_record()
            save_file.write(f'{record}\n')
            counter += 1
    print(f'{counter} scheduled appointments have been successfully saved\nGood Bye!')

def menu():
    print("\nJojo's Hair Salon Appointment Manager")
    print("=====================================")
    print(" 1) Schedule an appointment")
    print(" 2) Find appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) Cancel an appointment")
    print(" 9) Exit the system")
    selection = input("select option: ")
    return selection

def main():
    create_weekly_calendar()
    uploadAppts = input('Would you like to load previously scheduled appointments from a file (Y/N)? ').upper()
    if uploadAppts == 'Y':
        load_scheduled_appointments()
    selection = int(menu())
    while selection in range(1,10):
        match selection:
            case 1:
                print('** Schedule an appointment **')
                day = input('What day:').title()
                print(day)
                time = int(input('Enter start hour (24 hour clock): '))
                newAppt = find_appointment_by_time(day, time)
                name = input('Client Name: ').title()
                phone = input('Client Phone: ')
                print('Appointment types')
                print('1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120')
                apptType = int(input('Type of Appointment: '))
                while apptType not in range(1,5):
                    apptType = int(input('Invalid entry, enter Type of Appointment (1-4)'))
                newAppt.schedule(name, phone, apptType)
                print(f'OK, {name}\'s appointment is scheduled!')
                selection = int(menu())
            case 2:
                print('** Find Appointment by Name **')
                name = input('Enter Client Name: ').title()
                print('Appointments for', name)
                show_appointments_by_name(name)
                selection = int(menu())
            case 3:
                print('** Print calendar for a specific day **')
                day = input('Enter day of week: ').title()
                print('Appointments for', day)
                show_appointments_by_day(day)
                selection = int(menu())
            case 4:
                print('\n** Cancel an appointment **')
                day = input('What day: ').title()
                startTime = int(input('Enter start hour (24 hour clock): '))
                endTime = startTime + 1
                newAppt = find_appointment_by_time(day, startTime)
                if newAppt == None:
                    print('Sorry that time slot is not in the weekly calendar!')
                else: 
                    name = newAppt.clientName   
                    if name == '':
                        print('This time slot isn\'t booked and doesn\'t need to be cancelled')
                    else:
                        newAppt.cancel()
                        print(f'Appointment: {day} {startTime}:00 - {endTime}:00 for {name} has been cancelled!')
                selection = int(menu())
            case 9:
                print('** Exit the system **')
                save = input('Would you like to save all scheduled appointments to a file (Y/N)? ').upper()
                if save == 'Y':
                    save_scheduled_appointments()
                else:
                    print('Good Bye!')
                selection = 10

if __name__ == "__main__":
    main()
