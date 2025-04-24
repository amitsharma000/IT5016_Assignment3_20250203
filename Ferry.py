# Global for storing all the datas...

all_requisitions = []
approved_list = []
pending_list = []
not_approved_list = [] 


class SimpleRequisition:
    requisition_number = 20000
    
   # this make a new form and give requisition number
    def __init__(self):
        SimpleRequisition.requisition_number += 1
        self.req_id = SimpleRequisition.requisition_number
        self.date = ""
        self.staff_name = "" 
        self.staff_id = ""
        self.items = {}
        self.total = 0
        self.status = "pending"
        self.approval_ref = "not yet"

    # ask staff for name, date and ids

    def get_staff_details(self):
        print("\n Staff Information ")
        self.date = input("Give date (DD/MM/YYYY): ")
        self.staff_name = input("Whats your name?: ")
        self.staff_id = input("Staff ID please: ")
        

    # adding items and price one by one
    def add_items(self):
        print("\n Add items what you want ")
        while True:
            item_name = input("Item name (type 'done' to stop): ")
            if item_name.lower() == "done":
                break      
            try:
                item_price = float(input("Price of item: $"))
                self.items[item_name] = item_price
                self.total += item_price
            except:
                print("Price is not write. Try again")
        print("All item done. Total is: $", self.total)

    
    # check if auto approved or need manager..
    def check_approval(self):
        if self.total < 500:
            self.status = "Approved"    
            self.approval_ref = self.staff_id + str(self.req_id)[-3:]
            approved_list.append(self)
        else:  
            self.status = "pending"
            pending_list.append(self)

    # if pending, manager can approve or not... 
    def manager_decision(self):
        if self.status == "pending":
            print("\nThis Requisition is still pending")
            print(f"Staff: {self.staff_name}, Total: ${self.total}")
            decision = input("Manager choice (approve / not approve / skip): ").lower()
            if decision == "approve":    
                self.status = "Approved"
                self.approval_ref = self.staff_id + str(self.req_id)[-3:]
                pending_list.remove(self)
                approved_list.append(self)
            elif decision == "not approve":   
                self.status = "Not Approved"
                self.approval_ref = "Not available"
                pending_list.remove(self)
                not_approved_list.append(self)
            else:
                print("Skip this for now.")
                

    # show all details of one forms
    
    def show_details(self):
        print("\nPrinting Requisitions:")
        print(f"DATE: {self.date}")
        print(f"Requisition: {self.req_id}")  
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")   
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref}")


# Function to show total stats...
def show_statistics():
    print("\n Show Summary ")
    print("All requisitions done:", len(all_requisitions))
    print("Approved:", len(approved_list))
    print("Pending:", len(pending_list))
    print("Not Approved:", len(not_approved_list))

while True:
    req = SimpleRequisition()
    req.get_staff_details()
    req.add_items()
    req.check_approval()
    req.manager_decision()
    req.show_details()
    all_requisitions.append(req)

    again = input("\nDo new requisition? (yes / no): ").lower()
    if again != "yes":
        break
        
# END show stats  
show_statistics()
