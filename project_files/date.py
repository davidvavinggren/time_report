import datetime

class Date(object):
    
    def __init__(self, date, hours, minutes, comment):
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
        
        def input_correct(date, hours, minutes, comment):
            """
            Validate input by checking format and content and if the numbers are reasonable. 
            """
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
        
        if not input_correct(date, int(hours), int(minutes), comment):
            raise Exception

    def __str__(self):
        """
        __str__ method for Date class.
        """
        if self.hours < 10 and self.minutes < 10:
            return self.date + "    " + str(self.hours) + "         " + str(self.minutes) + "           " + self.comment
        elif self.hours < 10 and self.minutes >= 10:
            return self.date + "    " + str(self.hours) + "         " + str(self.minutes) + "          " + self.comment
        elif self.hours >= 10 and self.minutes < 10:
            return self.date + "    " + str(self.hours) + "        " + str(self.minutes) + "           " + self.comment
        elif self.hours >= 10 and self.minutes >= 10:
            return self.date + "    " + str(self.hours) + "        " + str(self.minutes) + "          " + self.comment