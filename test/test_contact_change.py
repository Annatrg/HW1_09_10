from model.contact import Contact
from random import randrange

def test_first_contact_change(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864",
                                work_phone="9995566", home_phone="8746327", secondary_phone="7635847",
                                email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                                year_of_birth="1996"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Anna_", last_name="_Torgova", address="St. Petersburg", mobile_phone="+79657989864",
                      work_phone="8764237", home_phone="872634234", secondary_phone="7635847",
                      email="torgova-anna@mail.ru", day_of_birth="11", month_of_birth="November", year_of_birth="1990")
    app.contact.contact_change_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
