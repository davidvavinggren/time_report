import pickle
import math

class TimeReport():
    
    def __init__(self):
        """
        Initiate TimeReport. Load data from file. 
        """
        self.objects = self.read("files/objects.txt")   
        self.month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
        self.weekday_hours_normal_worked = 0
        self.weekday_minutes_normal_worked = 0
        self.weekday_hours_overtime_worked = 0
        self.weekday_minutes_overtime_worked = 0
        self.weekend_hours_normal_worked = 0
        self.weekend_minutes_normal_worked = 0
        self.weekend_hours_overtime_worked = 0
        self.weekend_minutes_overtime_worked = 0
    
    def add_date(self, date):
        """
        Add year to TimeReport if not already added. 
        """
        list = []
        for object in self.objects:
            list.append(object.date)
        if date.date not in list:
            self.objects.append(date)
            self.write("files/objects.txt", date)
        return
    
    def read(self, filename):
        """
        Read data from file and return it. data will be a dict. Before data is returned all keys are converted to ints.
        """
        try:
            with open(filename, 'rb') as file:
                object = pickle.load(file)
        except:
            return []
        return object

    def write(self, filename, object):
        """
        Write object to file named filename.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.objects, file)
        return

    def delete_object(self, date):
        """
        Delete date from self.objects.
        """
        index = 0
        for object in self.objects:
            if object.date == date:
                self.objects.pop(index)
            index += 1
        self.write("files/objects.txt", self.objects)
        if self.objects == []:
            self.delete_data()
        return

    def delete_objects(self):
        """"
        Wipe data.txt from content (does not delete the file).
        """
        open('files/objects.txt', 'w').close()
        return
    
    def delete_report(self):
        """"
        Wipe data.txt from content (does not delete the file).
        """
        open('files/report.txt', 'w').close()
        return
    
    def __str__(self, month):
        """
        __str__ method for TimeReport class.
        """
        string = "Time report for {}:\n\n".format(month)
        string += "Date" + "          " + "Hours" + "     " + "Minutes" + "     " + "Comment\n"
        weekday_hours_normal = 0
        weekday_minutes_normal = 0
        weekday_hours_overtime = 0
        weekday_minutes_overtime = 0
        weekend_hours_normal = 0
        weekend_minutes_normal = 0
        weekend_hours_overtime = 0
        weekend_minutes_overtime = 0

        for object in self.objects:
            if object.month == self.month_dict[month]:    
                if object.is_weekend:
                    weekend_hours_normal += object.hours
                    weekend_minutes_normal += object.minutes
                    weekend_hours_overtime += object.overtime_hours
                    weekend_minutes_overtime += object.overtime_minutes
                else:
                    weekday_hours_normal += object.hours
                    weekday_minutes_normal += object.minutes
                    weekday_hours_overtime += object.overtime_hours
                    weekday_minutes_overtime += object.overtime_minutes
                
                string += object.__str__() + "\n"
        self.weekday_hours_normal_worked = weekday_hours_normal + math.floor(weekday_minutes_normal / 60)
        self.weekend_hours_normal_worked = weekend_hours_normal + math.floor(weekend_minutes_normal / 60)
        self.weekday_hours_overtime_worked = weekday_hours_overtime + math.floor(weekday_minutes_overtime / 60)
        self.weekend_hours_overtime_worked = weekend_hours_overtime + math.floor(weekend_minutes_overtime / 60)
        self.weekday_minutes_normal_worked = weekday_minutes_normal % 60
        self.weekend_minutes_normal_worked = weekend_minutes_normal % 60
        self.weekday_minutes_overtime_worked = weekday_minutes_overtime % 60
        self.weekend_minutes_overtime_worked = weekend_minutes_overtime % 60
        string += "\nSummary:\n\nWeekday normal time: {} hours and {} minutes\
                                 \nWeekday after 16:00: {} hours and {} minutes\
                                 \nWeekend normal time: {} hours and {} minutes\
                                 \nWeekend after 16:00: {} hours and {} minutes".format(self.weekday_hours_normal_worked,\
                                                                                        self.weekday_minutes_normal_worked,\
                                                                                        self.weekday_hours_overtime_worked,\
                                                                                        self.weekday_minutes_overtime_worked,\
                                                                                        self.weekend_hours_normal_worked,\
                                                                                        self.weekend_minutes_normal_worked,\
                                                                                        self.weekend_hours_overtime_worked,\
                                                                                        self.weekend_minutes_overtime_worked) 
        return string

    def write_to_file(self, month = None):
        """
        Write to file if input is valid. Majority of work done by __str__().
        """
        try:
            with open("files/{}_report.txt".format(month.lower()), 'w') as file:
                file.write(self.__str__(month))
        except:
            return False
        return


    