from day import *

def main():
    
    list_of_actions = [1,2,3]
    action_string = "\nAvailable actions:\n1: Show actions\n2: Report time\n3: Exit time_report"
    print("Welcome to time_report!")
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
                    day = Day(input("\nEnter date on format YYYY-MM-DD: "), input ("Enter hours worked: "), input ("Enter minutes worked: "), input("Enter comment: "))
                    action_2_bool = False
                except:
                    print("\nInput not valid! Please try again.")

        elif action == 3:
            return 

if __name__ == "__main__":
    main()