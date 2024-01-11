class Appointment:
    '''This class contains the properties of each appointment'''
    def __init__(self, dayOfWeek, startTimeHour):
        self.clientName = ""
        self.clientPhone = ""
        self.apptType = ""
        self.dayOfWeek = dayOfWeek
        self.startTimeHour = startTimeHour
    def get_client_name(self):
        return self.clientName
    def get_client_phone(self):
        return self.clientPhone
    def get_appt_type(self):
        return self.apptType
    def get_day_of_week(self):
        return self.dayOfWeek
    def get_start_time_hour(self):
        return self.startTimeHour
    def get_appt_type_desc(self):
        type = self.get_appt_type()
        match type:
            case '':
                type = 'Available'
            case 1:
                type = 'Mens Cut'
            case 2:
                type = 'Ladies Cut'
            case 3:
                type = 'Mens Colouring'
            case 4:
                type = 'Ladies Colouring'
        return type
    def get_end_time_hour(self):
        start = self.get_start_time_hour()
        end = start + 1
        return end
    def set_client_name(self, client_name):
        self.clientName = client_name
    def set_client_phone(self, client_phone):
        self.clientPhone = client_phone
    def set_appt_type(self, appt_type):
        self.apptType = appt_type
    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)
    def cancel(self):
        self.set_client_name('')
        self.set_client_phone('')
        self.set_appt_type('')
    def format_record(self):
        clientName = self.get_client_name()
        clientPhone = self.get_client_phone() 
        apptType = self.get_appt_type()
        dayOfWeek = self.get_day_of_week()
        startTimeHour = self.get_start_time_hour()
        record = f'{clientName},{clientPhone},{apptType},{dayOfWeek},{startTimeHour}'
        return record
    def __str__(self):
        clientName = self.get_client_name()
        clientPhone = self.get_client_phone() 
        apptType = self.get_appt_type_desc()
        dayOfWeek = self.get_day_of_week()
        startTimeHour = self.get_start_time_hour()
        if startTimeHour < 10:
            startTimeHour = f'0{startTimeHour}'
        endTimeHour = self.get_end_time_hour()
        appointment = f'{clientName:<20}{clientPhone:<15}{dayOfWeek:<10}{startTimeHour}:00  -  {endTimeHour}:00\t {apptType:<20}'
        return appointment

#p = Appointment('Thursday', 10)
#p.set_appt_type(1)
#print(p.get_client_name(), p.get_client_phone(), p.get_appt_type(), p.get_day_of_week(), p.get_start_time_hour())
#print(p.get_appt_type_desc())
#print(p.get_end_time_hour())
#print(p.get_client_name(), p.get_client_phone(), p.get_appt_type())
#p.schedule('Shannon', '403-289-9353', 3)
#print(p.get_client_name(), p.get_client_phone(), p.get_appt_type())
#p.cancel()
#print(p.get_client_name(), p.get_client_phone(), p.get_appt_type())
#print(p.format_record())
#print(p.__str__())