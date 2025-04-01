# program of train Ticket booking, using class / staticmethods. 
import random

print("\nHello passenger, Book your ticket.\n")

class train:

    def ticket(harry):
        harry.client = input("Name: ")
        harry.destination = input("Destination: ")
        harry.seats = input("No. of seats: ")
        print(f"\nTicket booked for: {harry.client}")
        
    @staticmethod    
    def status():
        a = random.randint(0,100)
        if (a==0):
            print("STATUS: All seats are booked.\n")
        else:
            print(f"STATUS: {a} seats left.\n")
            
object = train()
object.ticket()
train.status()
