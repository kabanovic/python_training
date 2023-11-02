from model.contact import Contact
from model.contact import Contact
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import randrange
import random


def test_del_some_contact(app, db, check_ui):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    app.contact.delete_some_cont_by_id(contact.id)
    try:
        element = WebDriverWait(app.wd, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Edit']"))
        )
        element.click()
    except:
        print("!!!")
    assert len(old_contacts) - 1 == app.contact.count_cont()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)