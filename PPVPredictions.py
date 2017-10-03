#import os

class MainScreen:

    def __init__(self):
        options = ["Add Card", "Edit Card", "View Card",
                   "Add Wrestler", "Edit Wrestler", "View Wrestler",
                   "Statistics"]
        self.display(options)
        choice = self.get_option()
        self.execute_menu_item(choice)
        

    def display(self,options):
        line_one = "1: %s\t\t2: %s\t\t3: %s"%(options[0],options[1],options[2])
        line_two = "4: %s \t5: %s\t6: %s"%(options[3],options[4],options[5])
        line_three = "\t\t\t7: %s\t\t"%(options[6])
        print ("%s\n%s\n%s"%(line_one,line_two,line_three))
        return

    def get_option(self):
        choice = -1
        condition = False;
        while condition == False:
            #get user choice
            choice = int(input("Select A Menu Item: "))
            if(choice >= 1 and choice <= 7):
                condition = True
            else:
                print("Input must be a number between 1 and 7")
            return choice

    def execute_menu_item(self,choice):
        file_name = ""
        if(choice == 1):
            file_name = "AddCard.py"
        elif(choice == 2):
            file_name = "EditCard.py"
        elif(choice == 3):
            file_name = "ViewCard.py"
        elif(choice == 4):
            file_name = "AddWrestler.py"
        elif(choice == 5):
            file_name = "EditWrestler.py"
        elif(choice == 6):
            file_name = "ViewWrestler.py"
        elif(choice == 7):
            file_name = "Statistics.py"
        exec(open("./%s"%(file_name)).read())
        return
        

        
exe = MainScreen()
