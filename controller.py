from model import Database
from view import View


class Controller:
    def __init__(self):
        self.model = Database()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.add_new_tourist()
                elif c1 == '2':
                    self.add_new_organizer()
                elif c1 == '3':
                    self.add_new_event()
                elif c1 == '4':
                    self.add_new_phone_num()


            elif choice == '2':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.view_t()
                elif c1 == '2':
                    self.view_o()
                elif c1 == '3':
                    self.view_e()
                elif c1 == '4':
                    self.view_p()
            elif choice == '3':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.update_t()
                elif c1 == '2':
                    self.update_o()
                elif c1 == '3':
                    self.update_e()
                elif c1 == '4':
                    self.update_p()
            elif choice == '4':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.delete_t()
                elif c1 == '2':
                    self.delete_o()
                elif c1 == '3':
                    self.delete_e()
                elif c1 == '4':
                    self.delete_p()
            elif choice == '5':
                break



    def add_new_tourist(self):
        f_name,l_name,email = self.view.get_tourist_organizer_input()
        b = self.model.add_tourist(f_name,l_name,email)
        if b:
            self.view.show_message("Tourist added successfully!")
        else:
            self.view.show_message("\nERROR: WRONG INPUT!")

    def add_new_organizer(self):
        f_name, l_name, email = self.view.get_tourist_organizer_input()
        b = self.model.add_organizer(f_name, l_name, email)
        if b:
            self.view.show_message("Organizer added successfully!")
        else:
            self.view.show_message("\nERROR: WRONG INPUT!")

    def add_new_event(self):
        title, type_, date, address_id = self.view.get_event_input()
        b = self.model.add_event(title, type_, date, address_id)
        if b:
            self.view.show_message("Event added successfully!")
        else:
            self.view.show_message("\nERROR: WRONG INPUT!")

    def add_new_phone_num(self):
        tourist_id, number = self.view.get_phone_input()
        b = self.model.add_phone_num(tourist_id, number)
        if b:
            self.view.show_message("Phone_num added successfully!")
        else:
            self.view.show_message("\nERROR: WRONG INPUT!")

    def view_t(self):
        t = self.model.get_all_tours()
        self.view.show_tourists(t)

    def view_o(self):
        t = self.model.get_all_orgs()
        self.view.show_organizers(t)

    def view_e(self):
        t = self.model.get_all_events()
        self.view.show_events(t)

    def view_p(self):
        t = self.model.get_all_phones()
        self.view.show_nums(t)

    def update_t(self):
        id = self.view.get_id()
        f_name, l_name, email = self.view.get_tourist_organizer_input()
        b = self.model.update_tour(id, f_name, l_name, email)
        if b:
            self.view.show_message(f"Tourist id = {id} updated successfully!")
        else:
            self.view.show_message("ERROR: WRONG INPUT!")

    def update_o(self):
        id = self.view.get_id()
        f_name, l_name, email = self.view.get_tourist_organizer_input()
        b = self.model.update_org(id, f_name, l_name, email)
        if b:
            self.view.show_message(f"Organizer id = {id} updated successfully!")
        else:
            self.view.show_message("ERROR: WRONG INPUT!")

    def update_e(self):
        id = self.view.get_id()
        title, type_, date, address_id = self.view.get_event_input()
        b = self.model.update_event(id, title, type_, date, address_id)
        if b:
            self.view.show_message(f"Event id = {id} updated successfully!")
        else:
            self.view.show_message("ERROR: WRONG INPUT!")

    def update_p(self):
        id = self.view.get_id()
        tourist_id, number = self.view.get_phone_input()
        b = self.model.update_phone(id, tourist_id, number)
        if b:
            self.view.show_message(f"Phone id = {id} updated successfully!")
        else:
            self.view.show_message("ERROR: WRONG INPUT!")

    def delete_p(self):
        id = self.view.get_id()
        b = self.model.delete_p(id)
        if b:
            self.view.show_message("Phone deleted successfully!")
        else:
            self.view.show_message("ERROR: wrong id")

    def delete_t(self):
        id = self.view.get_id()
        cnt_t,t,cnt_p,p = self.model.cnt_t(id)

        if cnt_t > 0 or cnt_p > 0:
            self.view.show_message("\nWARNING:\n")
            self.view.show_message("You need to manually delete these rows in the tables, due to the fact that they contain references to the id of the row being deleted, and then try to delete again")
            if cnt_t > 0:
                self.view.show_message("\n")
                self.view.show_t_e(t)
            if cnt_p > 0:
                self.view.show_message("\n")
                self.view.show_nums(p)
                self.view.show_message("\n")

        else:
            b = self.model.delete_t(id)
            if b:
                self.view.show_message("Tourist deleted successfully!")
            else:
                self.view.show_message("ERROR: WRONG ID")


    def delete_o(self):
        id = self.view.get_id()
        cnt_o, o = self.model.cnt_o(id)

        if cnt_o > 0:
            self.view.show_message("\nWARNING:\n")
            self.view.show_message("You need to manually delete these rows in the tables, due to the fact that they contain references to the id of the row being deleted, and then try to delete again")
            self.view.show_message("\n")
            self.view.show_o_e(o)
            self.view.show_message("\n")

        else:
            b = self.model.delete_o(id)
            if b:
                self.view.show_message("Organizer deleted successfully!")
            else:
                self.view.show_message("ERROR: WRONG ID")

    def delete_e(self):
        id = self.view.get_id()
        e1, ee1, e2, ee2 = self.model.cnt_e(id)

        if e1 > 0 or e2 > 0:
            self.view.show_message("\nWARNING:\n")
            self.view.show_message(
                "You need to manually delete these rows in the tables, due to the fact that they contain references to the id of the row being deleted, and then try to delete again")
            if e1 > 0:
                self.view.show_message("\n")
                self.view.show_t_e(ee1)
            if e2 > 0:
                self.view.show_message("\n")
                self.view.show_o_e(ee2)
                self.view.show_message("\n")

        else:
            b = self.model.delete_e(id)
            if b:
                self.view.show_message("Event deleted successfully!")
            else:
                self.view.show_message("ERROR: WRONG ID")

