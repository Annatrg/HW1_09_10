# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact
from application import Application

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    def test_add_contact(self):
        self.app.login(login="admin", password="secret")
        self.app.add_new_contact(Contact(first_name="Anna", last_name="Torgova", address="Spb", mobile_phone="79657989864", email="torgova-anna@mail.ru", day_of_birth="26", month_of_birth="November",
                             year_of_birth="1996"))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()

