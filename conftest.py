import pytest
from client.courier import Courier
from const import Constants
from faker import Faker
fake = Faker()

login = fake.name()
password = fake.password()
name = fake.first_name()


@pytest.fixture()
def prepare_courier():
    data_post = {
        "login": login,
        "password": password,
        "firstName": name
    }
    data_post_login = {
        "login": login,
        "password": password
    }
    courier = Courier()
    courier.post_v1_create_courier(Constants.URL, data=data_post)
    r = courier.post_v1_login_courier(Constants.URL, data=data_post_login)
    courier_id = r.json()["id"]
    yield courier.delete_v1_courier(Constants.URL, id=courier_id)

