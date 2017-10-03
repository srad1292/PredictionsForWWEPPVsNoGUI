class AddWrestler:

    def __init__(self):
        wrestler_name = self.get_name()
        if(wrestler_name == -1):
            print("Add Wrestler Cancelled")
        else:
            #Call function to add them to the wrestle table
            print("%s Saved As New Wrestle"%(wrestler_name))
            

    def get_name(self):
        name = ""
        confirm = False
        while(confirm == False):
            name = input("Name Of New Wrestler: ")
            correct = input("Do you want to save '%s' (y/n/can): "%(name))
            if(correct == "y"):
                return name
            elif(correct == "can"):
                return -1
            

a_w = AddWrestler()
