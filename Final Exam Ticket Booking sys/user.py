class Bus:
    def __init__(self,number,route,total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False
class Passenger:
    def __init__(self,name,phone,bus):
        self.name = name
        self.phone = phone
        self.bus = bus

class Admin:
    def __init__(self,username="admin",password = "1234"):
        self.username = username
        self.password = password
    def login(self,username,password):
        return self.username == username and self.password == password

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()
        self.admin_logged_in = False
    def add_bus(self,number,route,seats):
        if self.admin_logged_in:
            bus = Bus(number,route,seats)
            self.buses.append(bus)
        else:
            print("Admin login required to add new bus.")
    
    def find_bus(self,number):
        for bus in self.buses:
            if bus.number == number:
               return bus
        return None
    
    def book_ticket(self,bus_number,name,phone):
        bus = self.find_bus(bus_number)
        if not bus:
            print("Bus not found")
            return
        if bus.book_seat():
            passenger = Passenger(name,phone,bus)
            self.passengers.append(passenger)
            print(f"Ticket booked for {name}. Fare: ৳500")
        else:
            print("No available seats on this bus.")

    def show_buses(self):
        if not self.buses:
            print("No busses available")
            return 
        for bus in self.buses:
            print(f"Bus {bus.number} - Route: {bus.route} - Available seats: {bus.available_seats()}") 
    
    def admin_menu(self):
        while self.admin_logged_in:
            print("\n--- Admin Menu ---")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            choice = input("Enter choice: ")
            if choice == '1':
                number = input("Enter bus number: ")
                route  = input("Enter route: ")
                seats = int(input("Enter total seats: "))
                self.add_bus(number,route,seats)
            elif choice == '2':
                self.show_buses()
            elif choice == '3':
                self.admin_logged_in = False
                print("Logged out successfully.")
            else:
                print("Invalid choice. Try")
    
    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. Admin Login")
            print("2. Book Ticket")
            print("3. View Buses")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter Password")
                if self.admin.login(username,password):
                    self.admin_logged_in = True
                    print("Admin login successful")
                    self.admin_menu()
                else:
                    print("Invalid user or password")
            elif choice == '2':
                bus_number = input("Enter bus number: ")
                name = input("Enter your name: ")
                phone = input("Enter your phone number: ")
                self.book_ticket(bus_number,name,phone)
            elif choice == '3':
                self.show_buses()
            elif choice == '4':
                break
            else:
                print("Invalid choice")

jamil = BusSystem()
jamil.user_menu()
                    

                
