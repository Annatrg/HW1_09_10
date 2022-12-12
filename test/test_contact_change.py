from model.contact import Contact
from random import randrange



def test_first_contact_change(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864",
                                work_phone="9995566", home_phone="8746327", secondary_phone="7635847",
                                email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                                year_of_birth="1996"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Anna", last_name="Torgova", address="Petersburg", mobile_phone="+79657989864",
                      work_phone="8764237", home_phone="872634234", secondary_phone="7635847",
                      email="torgova-anna@mail.ru", day_of_birth="11", month_of_birth="November", year_of_birth="1990")
    contact.id = int(old_contacts[index].id)
    app.contact.contact_change_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
