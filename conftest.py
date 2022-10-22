
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    fixture.session.login(login="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
