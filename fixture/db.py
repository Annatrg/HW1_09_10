import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
            return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
            return list

    #def get_contact_list(self):
        #list = []
        #cursor = self.connection.cursor()
        #try:
         #   cursor.execute("SELECT id, firstname, lastname, address, home, mobile, work, email, phone2 FROM addressbook")
          #  for row in cursor:
           #     (id, first_name, last_name, address, home_phone, mobile_phone, work_phone, email, secondary_phone) = row
            #    list.append(Contact(id=str(id), first_name=first_name, last_name=last_name, address=address,
             #                     home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, email=email,
              #                    secondary_phone=secondary_phone))
       # finally:
        #    cursor.close()
         #   return list

    def destroy(self):
        self.connection.close()
