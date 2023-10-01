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
    appl.login("admin", "secret")
    appl.add_contact(Contact("Name2", "Middle2", "Surname2", "89991234567"))
    appl.logout()

