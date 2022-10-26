# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864", email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                            year_of_birth="1996"))


def test_add_contact_2(app):
    app.contact.add(Contact(first_name="123", last_name="345", address="567", mobile_phone="23423", email="t234234@mail.ru", day_of_birth="26", month_of_birth="November",
                            year_of_birth="1996"))
