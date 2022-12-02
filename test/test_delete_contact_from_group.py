from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app, db, orm):

    # проверяем что вообще есть контакты и группы
  #  if db.get_contact_list() == 0:
    #    app.contact.add(Contact(first_name="Anna", last_name="Torgova"))
  #  contacts = db.get_contact_list()
   # contact = random.choice(contacts)

   # if len(db.get_group_list()) == 0:
   #     app.group.create(Group(name="test_del"))
  #  groups = db.get_group_list()
   # group = random.choice(groups)

    # проверяем есть ли в какой-нибудь группе любой контакт. Если нет, то добавляем
  #  if db.get_contact_in_group_list == 0:
   #     app.contact.add_contact_to_group(contact.id, group.name)

    # удаляем контакт из группы
    # получаем список контактов в группах
   # contacts_with_groups = orm.get_contact_list()
   # contact_with_group = random.choice(contacts_with_groups)
    contacts_with_groups = db.get_contact_in_group_list()
    contact_with_group = random.choice(contacts_with_groups)
    app.contact.delete_contact_from_group(contact_with_group)
