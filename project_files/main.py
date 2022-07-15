import email
from date import *
from time_report import *
from  mail import *

def main():
    """
    Mainloop with different funtionality. Mostly printing text in terminal and taking input from user.
    """
    report = TimeReport()    

    list_of_actions = [1,2,3,4,5,6,7,8]
    action_string = "\nAvailable actions:\n1: Show actions\n2: Report time\n3: Delete specific object\n4: Delete all objects\n5: Delete report\n6: Write report\n7: Send report\n8: Exit time_report"
    print("\nWelcome to time_report!")
    print(action_string)
    
    while True:
        try:
            action = int(input("\nInput action: "))
            if not (action in list_of_actions):
                print("\nAction not valid. Please try again by entering an action followed by enter: ")
        except:
            print("Action not valid. Please try again by entering an action followed by enter: ")
        if action == 1:
            print(action_string)
        elif action == 2:
            action_2_bool = True
            while action_2_bool:
                try:
                    report.add_date(Date(input("\nEnter date on format YYYY-MM-DD: "), input ("Enter hours worked: "), input ("Enter minutes worked: "), input("Enter comment: ")))
                    action_2_bool = False
                except:
                    print("\nInput not valid! Please try again.\n")
        elif action == 3:
            action_3_bool = True
            while action_3_bool:
                try:
                    report.delete_object(input("\nEnter object date on format YYYY-MM-DD: "))
                    action_3_bool = False
                except:
                    print("\nInput not valid! Please try again.\n")
        elif action == 4:
            report.delete_objects()
            print("\nObjects deleted.")
        elif action == 5:
            report.delete_report()
            print("\nReport deleted.")
        elif action == 6:
            action_6_bool = True
            while action_6_bool:
                try:
                    month = input("\nEnter month of report on format Month: ")
                    report.write_to_file(month)
                    print("\n" + report.__str__(month))
                    print("\nReport written to external file.")
                    action_6_bool = False
                except:
                    print("\nInput not valid! Please try again.")
        elif action == 7:
            action_7_bool = True
            while action_7_bool:
                try:
                    mail(input("\nEnter month of report on format Month: "))
                    action_7_bool = False
                except:
                    print("\nInput not valid! Please try again.")
        elif action == 8:
            print("\n")
            return 

if __name__ == "__main__":
    main()