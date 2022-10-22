from model.contact import Contact


def test_first_contact_change(app):
    app.contact.first_contact_change(Contact(first_name="Anna_", last_name="_Torgova", address="St. Petersburg", mobile_phone="+79657989864", email="torgova-anna@mail.ru", day_of_birth="11", month_of_birth="November",
                            year_of_birth="1990"))
