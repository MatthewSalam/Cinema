import random
import string

#Making sure all constants are defined and the tickets start off empty
tickets = []
max_ticket = 50
ticketid = 0

def create_new_ticket():
    #Allowing a registered user create a definite amount of tickets
    global ticketid
    ticketid = ticketid + 1
    if tickets == 50:
      print("Sorry, all tickets have been sold out")
    else:
        print("Proceed")
    TicketMovie = (input("MovieName; "))
    SerialNumber = ''.join(random.choice(string.ascii_lowercase) for i in range(50))
    ticket = {"ticketid": ticketid, "TicketMovie": TicketMovie, "SerialNumber": SerialNumber}
    print("Ticket created successfully")          
    tickets.append(ticket)
    print(tickets)
    return

def view_tickets():
    #Allowing user(s) to view already made tickets
    print(tickets)
    for ticket in tickets:
        print("Ticketid: ", ticket["ticketid"], "Movie: ", ticket["TicketMovie"], "SerialNumber: ", ticket["SerialNumber"] )
        return
    
def view_ticket_by_id():
    #Allowing a specific user to see his own ticket alone
   ticketid = int(input("Enter the ticketid:  "))
   for ticket in tickets:
      if ticket["ticketid"] == ticketid:
         print("Ticketid: ", ticket["ticketid"], "Movie: ", ticket["TicketMovie"], "SerialNumber: ", ticket["SerialNumber"])
         break
      
def cancel_ticket_by_id():
    #Allowing a user cancel his own ticket
   ticketid = int(input("Enter the ticketid:  "))
   for ticket in tickets:
      if ticket["ticketid"] == ticketid:
         tickets.remove(ticket)
         print("Ticket cancelled successfully")
         break

def tikOperation():
    #Showing the available operations to a user
  print("Operations Available")
  print("1. Create ticket")
  print("2. View tickets")
  print("3. View ticket by ID")
  print("4. Cancel ticket by ID")
  operation = int(input("Pick an operation: 1, 2, 3 or 4   "))

  if operation == 1:
    create_new_ticket()
  elif operation == 2:
    view_tickets()
  elif operation == 3 :
    view_ticket_by_id()
  elif operation == 4:
    cancel_ticket_by_id()
  else:
    print("Invalid operation")
  user_satisfaction = input("Are you satisfied:  Y or N  ").upper()
  print(user_satisfaction)
  if user_satisfaction == "Y" or "y":
     print("Thank you for using our services")
  else:
     print("Please provide feedback")
