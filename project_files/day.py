import datetime

class Day(object):
    
    def __init__(self, day, hours, minutes, comment):
        self.date = datetime.datetime.now()
        self.year = self.date.year
        
        def day_correct(day):
            index_list = [4,7]
            integers = [0,1,2,3,4,5,6,7,8,9]
            index = 0
            for c in day:
                if not (index in index_list):
                    try:
                        if not (int(c) in integers):
                            return False
                        if index >= 0 and index <= 3:
                            if int(day[0:4]) > self.year:
                                return False
                        elif index >= 5 and index <= 6:
                            if int(day[5]) == 0:
                                if int(day[6]) > 12 or int(day[6]) < 0:
                                    return False
                            else:
                                if int(day[5:7]) > 12 or int(day[5:7]) < 0:
                                    return False
                        elif index >= 8 and index <= 9:
                            if int(day[8]) == 0:
                                if int(day[9]) > 31 or int(day[9]) < 0:
                                    return False
                            else:
                                if int(day[8:10]) > 31 or int(day[8:10]) < 0:
                                    return False
                    except:
                        return False
                elif day[index] != "-":
                    return False
                index += 1
            return True
        
        def input_correct(day, hours, minutes, comment):
            if (not (hours < 25 and hours >= 0)) or (not (minutes < 60 and minutes >= 0)):
                return False
            if type(comment) != str:
                return False
            if type(day) != str:
                return False
            if len(day) != 10:
                return False
            if not day_correct(day):
                return False
            return True
        
        if not input_correct(day, int(hours), int(minutes), comment):
            raise Exception

        
        
        