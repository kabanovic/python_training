# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.fixt import Applicat

@pytest.fixture
def appl(request):
    fixture = Applicat()
    request.addfinalizer(fixture.destr)
    return fixture

def test_add_contact(appl):
    appl.sess.login("admin", "secret")
    appl.contact.add(Contact("Name3", "Middle3", "Surname3", "89991234567"))
    appl.sess.logout()

