from random import randrange
from model.contact import Contact
import random


# работает и связь и БД, и проверка Check_ui
def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864",
                                home_phone="78129991133", work_phone="78120003425", secondary_phone="7635847",
                                email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                                year_of_birth="1996"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

