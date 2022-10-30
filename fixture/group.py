from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # init_group_creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
    #    self.return_to_groups_page()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def first_group_change(self, new_group_data):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit_group_creation
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
      #  wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
