from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    # проверяем наличие хотя бы одного контакта. Если его нет - создаем
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864",
                                work_phone="9995566", home_phone="8746327", secondary_phone="7635847",
                                email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                                year_of_birth="1996"))
    # выбираем случайный контакт
  #  contacts = db.get_contact_list()
   # contact = random.choice(contacts)
    # проверяем наличие хотя бы одной группы. Если её нет - создаем
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_del"))
    # выбираем случайную группу
    groups = db.get_group_list()
    group = random.choice(groups)

    # добавляем контакт в группу

    contacts_for_add_in_group = orm.get_contacts_not_in_group(group)
    if contacts_for_add_in_group == []:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864",
                                work_phone="9995566", home_phone="8746327", secondary_phone="7635847",
                                email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                                year_of_birth="1996"))
        contact_for_add_in_group = orm.get_contacts_not_in_group(group)[0]
    else:
        contact_for_add_in_group = random.choice(contacts_for_add_in_group)


    # app.contact.add_contact_to_group(contact.id, group.id)
    app.contact.add_contact_to_group(contact_for_add_in_group, group)

    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact_for_add_in_group in contacts_in_group
