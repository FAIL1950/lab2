class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message("2. View rows")
        self.show_message("3. Update row")
        self.show_message("4. Delete row")
        self.show_message("5. Quit")
        return input("Enter your choice: ")


    def show_extra_menu(self):
        self.show_message("\nTables: ")
        self.show_message("1. Tourists")
        self.show_message("2. Organizers")
        self.show_message("3. Events")
        self.show_message("4. Phone_nums")
        self.show_message("5. Back")
        return input("Enter your choice: ")

    def show_tourists(self, j):
        print("Tourists: ")
        for i in j:
            print(f"TouristID: {i.TouristID}, F_name: {i.F_name}, L_name: {i.L_name}, email: {i.email}")

    def show_organizers(self, j):
        print("Organizers: ")
        for i in j:
            print(f"OrganizerID: {i.ОrganizerID}, F_name: {i.F_name}, L_name: {i.L_name}, email: {i.email}")

    def show_events(self, j):
        print("Events: ")
        for i in j:
            print(f"EventID: {i.EventID}, Title: {i.Title}, Type: {i.Type}, Date: {i.Date}, Address_ID: {i.Address_ID}")

    def show_nums(self, j):
        print("Phone_nums: ")
        for i in j:
            print(f"PhoneID: {i.PhoneID}, Tourist_ID: {i.Tourist_ID}, Number: {i.Number}")

    def show_t_e(self, j):
        print("Tourists_Events: ")
        for i in j:
            print(f"Tourist: {i.Tourist}, Event_t: {i.Event_t}, booking_time: {i.booking_time}")

    def show_o_e(self, j):
        print("Оrganizers_Events: ")
        for i in j:
            print(f"Оrganizer: {i.Оrganizer}, Event_o: {i.Event_o}")


    def get_tourist_organizer_input(self):
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        email = input("Enter email: ")
        return f_name,l_name,email
    def get_event_input(self):
        title = input("Enter event title: ")
        type_ = input("Enter event type: ")
        date = input("Enter event date: ")
        address_id = input("Enter event address_id: ")
        return title, type_, date, address_id

    def get_phone_input(self):
        tourist_id = input("Enter tourist_id: ")
        number = input("Enter number: ")
        return tourist_id, number

    def get_id(self):
        return input("Enter ID: ")

    def get_cnt(self):
        return input("Enter enter number of lines to create: ")

    def show_message(self, message):
        print(message)
