# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864", email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                            year_of_birth="1996")
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_contact_2(app):
  #  old_contacts = app.group.get_contact_list()
   # app.contact.add(Contact(first_name="123", last_name="345", address="567", mobile_phone="23423", email="t234234@mail.ru", day_of_birth="26", month_of_birth="November",
   #                         year_of_birth="1996"))
  #  new_contacts = app.group.get_contact_list()
  #  assert len(old_contacts) + 1 == len(new_contacts)
