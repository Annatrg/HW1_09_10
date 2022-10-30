from model.contact import Contact


def test_first_contact_change(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864", email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                            year_of_birth="1996"))
    contact = Contact(first_name="Anna_", last_name="_Torgova", address="St. Petersburg", mobile_phone="+79657989864", email="torgova-anna@mail.ru", day_of_birth="11", month_of_birth="November",
                            year_of_birth="1990")
    app.contact.first_contact_change(contact)
    contact.id = old_contacts[0].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
