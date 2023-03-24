import datetime
import math

class Date(object):
    
    def __init__(self, date, hours, minutes, overtime_hours, overtime_minutes, is_weekend, comment):
        """
        Initiate Date. Import current date from datetime. Split up arguments and save in different class variables. 
        """
        self.current_date = datetime.datetime.now()
        self.current_year = self.current_date.year
        self.current_month = self.current_date.month
        self.current_day = self.current_date.day

        self.date = date
        self.year = int(date[0:4])
        self.month = int(date[5:7])
        self.day = int(date[8:10])
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.overtime_hours = int(overtime_hours)
        self.overtime_minutes = int(overtime_minutes)
        if is_weekend == "y":
            self.is_weekend = True
        elif is_weekend == "n":
            self.is_weekend = False
        self.comment = comment
        
        def date_correct_format():
            """
            Help function to input_correct(). Check date input by user. Return false if the date does not consist of integers in positions it should. 
            """
            index_list = [4,7]
            index = 0
            for c in self.date:
                if not (index in index_list):
                    try:
                        int(c)
                    except:
                        return False
                index += 1
            return True

        def date_correct():
            """
            Help function to input_correct(). Ensures user can not input dates in the future. 
            """
            if self.year < self.current_year:
                if self.month > 0 and self.month < 13 and self.day > 0 and self.day < 32:
                    return True
            elif self.year == self.current_year:
                if self.month < self.current_month:
                    if self.day > 0 and self.day < 32:
                        return True
                elif self.month == self.current_month:
                    if self.day > 0 and self.day <= self.current_day:
                        return True
            return False
        
        def input_correct(date, hours, minutes, comment, boolean):
            """
            Validate input by checking format and content and if the numbers are reasonable. 
            """
            if not isinstance(boolean, bool):
                return False
            if (not (hours < 25 and hours >= 0)) or (not (minutes < 60 and minutes >= 0)):
                return False
            if type(comment) != str:
                return False
            if type(date) != str:
                return False
            if len(date) != 10:
                return False
            if not date_correct() or not date_correct_format():
                return False
            return True
        
        if (not input_correct(self.date, int(self.hours), int(self.minutes), self.comment, self.is_weekend)) or (not input_correct(self.date, int(self.overtime_hours), int(self.overtime_minutes), self.comment, self.is_weekend)):
            print("hej")
            raise Exception

    def __str__(self):
        """
        __str__ method for Date class.
        """
        total_hours = self.hours + self.overtime_hours + math.floor((self.minutes + self.overtime_minutes) / 60)
        total_minutes = (self.minutes + self.overtime_minutes) % 60
        if total_hours < 10 and total_minutes < 10:
            return (self.date + "    " + "{}" + "         " + "{}" + "           " + self.comment).format(str(total_hours), str(total_minutes))
        elif total_hours < 10 and total_minutes >= 10:
            return (self.date + "    " + "{}" + "         " + "{}" + "          " + self.comment).format(str(total_hours), str(total_minutes))
        elif total_hours >= 10 and total_minutes < 10:
            return (self.date + "    " + "{}" + "        " + "{}" + "           " + self.comment).format(str(total_hours), str(total_minutes))
        elif total_hours >= 10 and total_minutes >= 10:
            return (self.date + "    " + "{}" + "        " + "{}" + "          " + self.comment).format(str(total_hours), str(total_minutes))