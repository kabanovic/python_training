import re
from random import randrange
from model.contact import Contact


def test_contact_on_home_page(app, db):
    contact_list = app.contact.get_contact_list()
    contact_db_list = db.get_contact_list()
    contact_list.sort(key=Contact.id_or_max)
    contact_db_list.sort(key=Contact.id_or_max)
    assert len(contact_list) == len(contact_db_list)
    for i in range(len(contact_db_list)):
        assert contact_list[i].firstname == contact_db_list[i].firstname
        assert contact_list[i].lastname == contact_db_list[i].lastname
        assert contact_list[i].adress == contact_db_list[i].adress
        assert contact_list[i].all_mails == merge_mails(contact_db_list[i])
        assert contact_list[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_db_list[i])


#def test_phones_on_contact_view_page(app):
 #    contact_from_view_page = app.contact.get_contact_from_view_page(0)
  #   contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
   #  assert contact_from_view_page.homephone == contact_from_edit_page.homephone
   #  assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    # assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
   #  assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
     return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
     return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x), filter(lambda x: x is not None,
                                 [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_mails(contact):
     return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


