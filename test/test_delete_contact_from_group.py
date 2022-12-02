from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    # Проверяем есть ли хотя бы одна группа
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="HW7_", header="HW7", footer="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    # Проверяем есть ли хотя бы один контакт
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864",
                                work_phone="9995566", home_phone="8746327", secondary_phone="7635847",
                                email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                                year_of_birth="1996"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    # Проверяем есть ли контакт в группе
    if len(db.get_contact_in_group_list()) == 0:
        app.contact.add_contact_to_group(contact.id, group.name)
    # Сам тест
    contacts_with_groups = db.get_contact_in_group_list()
    contact_with_group = random.choice(contacts_with_groups)
    app.contact.delete_contact_from_group(contact_with_group)

    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact not in contacts_in_group
