from model.contact import Contact
from model.contact import Contact
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_del_contact(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_cont()
    try:
        element = WebDriverWait(app.wd, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Edit']"))
        )
        element.click()
    except:
        print("!!!")
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts