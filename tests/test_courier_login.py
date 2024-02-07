import pytest
from const import Constants
from client.courier import Courier
import allure
from faker import Faker
fake = Faker()

fake_login = fake.name()
fake_password = fake.password()


class TestCourierLogin:
    @allure.title('get courier login')
    def test_courier_login(self):
        courier = Courier()
        data = {
            "login": Constants.TEST_LOGIN,
            "password": Constants.TEST_PASSWORD,
                }
        response = courier.post_v1_login_courier(Constants.URL, data=data)
        assert response.status_code == 200 and response.json() == {"id": 260399}

    @allure.title('can`t get courier login without required fields')
    @pytest.mark.parametrize("test_login, test_password", [("", Constants.TEST_PASSWORD), (Constants.TEST_LOGIN, "")])
    def test_courier_login_without_required_fields(self, test_login, test_password):
        courier = Courier()
        data = {
            "login": test_login,
            "password": test_password,
        }
        response = courier.post_v1_login_courier(Constants.URL, data=data)
        assert response.status_code == 400 and response.json() == {"code": 400, "message": "Недостаточно данных для "
                                                                                           "входа"}

    @allure.title('can`t get courier login with wrong login or password')
    @pytest.mark.parametrize("test_login, test_password", [(fake_login, Constants.TEST_PASSWORD), (Constants.TEST_LOGIN, fake_password)])
    def test_courier_login_with_wrong_login_or_password(self, test_login, test_password):
        courier = Courier()
        data = {
            "login": test_login,
            "password": test_password,
        }
        response = courier.post_v1_login_courier(Constants.URL, data=data)
        assert response.status_code == 404 and response.json() == {"code": 404, "message": "Учетная запись не найдена"}


