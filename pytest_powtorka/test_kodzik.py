from kodzik import User
import pytest
@pytest.fixture
def users():
    return [
    User('Andrzej', 'L', '11-01-1970'),
    User('Karol','M','11-05-1992'),
    User('Ewelina','Dąbek','01-12-1990'),
    User('Michał','Waleczny','31-03-1980'),

]

def test_get_full_username(users):
    u = users[0]
    assert u.get_full_username() == u.first_name + ' ' + u.last_name

def test_date_format(users):
    u=users[0]
    split=u.birth_date.split('-')
    assert len(split) == 3