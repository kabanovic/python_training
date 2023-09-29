# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from contact import Contact
from fixt import Applicat

@pytest.fixture
def appl(request):
    fixture = Applicat()
    request.addfinalizer(fixture.destr)
    return fixture

def test_add_contact(appl):
    appl.login("admin", "secret")
    appl.add_contact(Contact("Name2", "Middle2", "Surname2", "89991234567"))
    appl.logout()

