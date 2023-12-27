import sqlalchemy
from sqlalchemy import exc
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
import re
from datetime import datetime

Base = declarative_base()

class Database:

    def __init__(self):
        engine = create_engine("postgresql://postgres:55krotvkaske@localhost:5432/postgres")
        self.session_class = sessionmaker(bind=engine)

    def get_all_address(self):
        s = self.session_class()
        tmp = s.query(Address).order_by(Address.AddressID.asc()).all()
        s.close()
        return tmp

    def get_all_orgs(self):
        s = self.session_class()
        tmp = s.query(Оrganizers).order_by(Оrganizers.ОrganizerID.asc()).all()
        s.close()
        return tmp

    def get_all_tours(self):
        s = self.session_class()
        tmp = s.query(Tourists).order_by(Tourists.TouristID.asc()).all()
        s.close()
        return tmp
    def get_all_phones(self):
        s = self.session_class()
        tmp = s.query(Phone).order_by(Phone.PhoneID.asc()).all()
        s.close()
        return tmp
    def get_all_events(self):
        s = self.session_class()
        tmp = s.query(Events).order_by(Events.EventID.asc()).all()
        s.close()
        return tmp

    def is_email(self, email):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, email) is not None:
            return True
        else:
            return False

    def not_null(self, str):
        if len(str) > 0:
            return True
        else:
            return False

    def is_date(self, input_string):
        try:
            datetime.strptime(input_string, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def add_tourist(self,f_name,l_name,email):
        s = self.session_class()
        b = True
        if self.is_email(email) and self.not_null(f_name) and self.not_null(l_name):
            s.add(Tourists(F_name=f_name, L_name=l_name, email=email))
            try:
                s.commit()
            except exc.SQLAlchemyError:
                b = False
        else:
            b = False


        s.close()
        return b


    def add_organizer(self,f_name,l_name,email):
        s = self.session_class()
        b = True
        if self.is_email(email) and self.not_null(f_name) and self.not_null(l_name):
            s.add(Оrganizers(F_name=f_name, L_name=l_name, email=email))
            try:
                s.commit()
            except exc.SQLAlchemyError:
                b = False
        else:
            b = False


        s.close()
        return b

    def add_event(self,title, type_, date, address_id):
        s = self.session_class()
        b = True
        if self.not_null(title) and self.not_null(type_) and self.is_date(date):
            s.add(Events(Title=title, Type=type_, Date=date,Address_ID=address_id))
            try:
                s.commit()
            except exc.SQLAlchemyError:
                b = False
        else:
            b = False


        s.close()
        return b

    def add_phone_num(self,tourist_id, number):
        s = self.session_class()
        b = True
        if self.not_null(number):
            s.add(Phone(Tourist_ID=tourist_id,Number=number))
            try:
                s.commit()
            except exc.SQLAlchemyError:
                b = False
        else:
            b = False


        s.close()
        return b

    def update_tour(self, id, f_name, l_name, email):
        s = self.session_class()
        b = True
        t = s.query(Tourists).get(id)
        if t == None:
            b = False
        if b:
            if self.not_null(f_name):
                t.F_name = f_name
            if self.not_null(l_name):
                t.L_name = l_name
            if self.not_null(email):
                if self.is_email(email):
                    t.email = email
                else:
                    b = False
            if b:
                try:
                    s.commit()
                except exc.SQLAlchemyError:
                    b = False
        s.close()
        return b

    def update_org(self, id, f_name, l_name, email):
        s = self.session_class()
        b = True
        t = s.query(Оrganizers).get(id)
        if t == None:
            b = False
        if b:
            if self.not_null(f_name):
                t.F_name = f_name
            if self.not_null(l_name):
                t.L_name = l_name
            if self.not_null(email):
                if self.is_email(email):
                    t.email = email
                else:
                    b = False
            if b:
                try:
                    s.commit()
                except exc.SQLAlchemyError:
                    b = False
        s.close()
        return b

    def update_event(self, id, title, type_, date, address_id):
        s = self.session_class()
        b = True
        t = s.query(Events).get(id)
        if t == None:
            b = False
        if b:
            if self.not_null(title):
                t.Title = title
            if self.not_null(type_):
                t.Type = type_
            if self.not_null(date):
                if self.is_date(date):
                    t.Date = date
                else:
                    b = False
            if self.not_null(address_id):
                c = s.query(Address).get(address_id)
                if c is not None:
                    t.Address_ID = address_id
                else:
                    b = False
            if b:
                try:
                    s.commit()
                except exc.SQLAlchemyError:
                    b = False
        s.close()
        return b


    def update_phone(self, id, tourist_id, number):
        s = self.session_class()
        b = True
        t = s.query(Phone).get(id)
        if t == None:
            b = False
        if b:
            if self.not_null(number):
                t.Number = number
            if self.not_null(tourist_id):
                c = s.query(Tourists).get(tourist_id)
                if c is not None:
                    t.Tourist_ID = tourist_id
                else:
                    b = False
            if b:
                try:
                    s.commit()
                except exc.SQLAlchemyError:
                    b = False
        s.close()
        return b

    def delete_p(self,id):
        s = self.session_class()
        t = s.query(Phone).get(id)
        if t == None:
            s.close()
            return False
        else:
            s.delete(t)
            s.commit()
            s.close()
            return True

    def cnt_t(self, id):
        s = self.session_class()
        cnt_t = s.query(TouristsEventsAssoc).filter(TouristsEventsAssoc.Tourist == id).count()
        t = s.query(TouristsEventsAssoc).filter(TouristsEventsAssoc.Tourist == id)
        cnt_p = s.query(Phone).filter(Phone.Tourist_ID == id).count()
        p = s.query(Phone).filter(Phone.Tourist_ID == id)
        s.close()
        return cnt_t,t,cnt_p,p

    def cnt_o(self, id):
        s = self.session_class()
        cnt_o = s.query(OrganizersEventsAssoc).filter(OrganizersEventsAssoc.Оrganizer == id).count()
        o = s.query(OrganizersEventsAssoc).filter(OrganizersEventsAssoc.Оrganizer == id)
        s.close()
        return cnt_o,o

    def cnt_e(self,id):
        s = self.session_class()
        e1 = s.query(TouristsEventsAssoc).filter(TouristsEventsAssoc.Event_t == id).count()
        ee1 = s.query(TouristsEventsAssoc).filter(TouristsEventsAssoc.Event_t == id)
        e2 = s.query(OrganizersEventsAssoc).filter(OrganizersEventsAssoc.Event_o == id).count()
        ee2 = s.query(OrganizersEventsAssoc).filter(OrganizersEventsAssoc.Event_o == id)
        s.close()
        return e1,ee1,e2,ee2

    def delete_t(self,id):
        s = self.session_class()
        t = s.query(Tourists).get(id)
        if t == None:
            s.close()
            return False
        else:
            s.delete(t)
            s.commit()
            s.close()
            return True

    def delete_o(self,id):
        s = self.session_class()
        t = s.query(Оrganizers).get(id)
        if t == None:
            s.close()
            return False
        else:
            s.delete(t)
            s.commit()
            s.close()
            return True

    def delete_e(self,id):
        s = self.session_class()
        t = s.query(Events).get(id)
        if t == None:
            s.close()
            return False
        else:
            s.delete(t)
            s.commit()
            s.close()
            return True

class OrganizersEventsAssoc(Base):
    __tablename__ = 'Оrganizers_Events'
    Оrganizer = Column(Integer, ForeignKey('Оrganizers.ОrganizerID'), primary_key=True)
    Event_o = Column(Integer, ForeignKey('Events.EventID'), primary_key=True)


class TouristsEventsAssoc(Base):
    __tablename__ = 'Tourists_Events'
    Tourist = Column(Integer, ForeignKey('Tourists.TouristID'), primary_key=True)
    Event_t = Column(Integer, ForeignKey('Events.EventID'), primary_key=True)
    booking_time = Column(Date, primary_key=True, unique=True)

class Оrganizers(Base):
    __tablename__ = 'Оrganizers'
    ОrganizerID = Column(Integer, primary_key=True, nullable=False, unique=True)
    F_name = Column(String(30), nullable=False)
    L_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)

    events = relationship("Events", secondary='Оrganizers_Events', back_populates="organizers")

class Events(Base):
    __tablename__ = 'Events'
    EventID = Column(Integer, primary_key=True, nullable=False, unique=True)
    Title = Column(String(100), nullable=False)
    Type = Column(String(30), nullable=False)
    Date = Column(Date, nullable=False)
    Address_ID = Column(Integer, ForeignKey('Address.AddressID'), nullable=False)

    address = relationship("Address", back_populates="events")
    tourists = relationship("Tourists", secondary='Tourists_Events', back_populates="events")
    organizers = relationship("Оrganizers", secondary='Оrganizers_Events', back_populates="events")

class Tourists(Base):
    __tablename__ = 'Tourists'
    TouristID = Column(Integer, primary_key=True, nullable=False, unique=True)
    F_name = Column(String(30), nullable=False)
    L_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)

    phones = relationship("Phone", order_by="Phone.PhoneID", back_populates="tourist")
    events = relationship("Events",secondary='Tourists_Events', back_populates="tourists")

class Phone(Base):
    __tablename__ = 'Phone_nums'
    PhoneID = Column(Integer, primary_key=True, nullable=False, unique=True)
    Tourist_ID = Column(Integer, ForeignKey('Tourists.TouristID'), nullable=False)
    Number = Column(String(16), nullable=False, unique=True)

    tourist = relationship("Tourists", back_populates="phones")

class Address(Base):
    __tablename__ = 'Address'
    AddressID = Column(Integer, primary_key=True, nullable=False, unique=True)
    Country = Column(String(30), nullable=False)
    City = Column(String(30), nullable=False)
    Street = Column(String(30), nullable=False)
    House = Column(String(30), nullable=False)

    events = relationship("Events",order_by="Events.EventID", back_populates="address")







