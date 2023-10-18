from sys import maxsize

class Contact:

    def __init__(self, firsname=None, middlename=None, lastname=None, telephone=None, id=None):
        self.firstname = firsname
        self.middlename = middlename
        self.lastname = lastname
        self.telephone = telephone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.telephone == other.telephone

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize