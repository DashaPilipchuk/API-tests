import pytest
from const import Constants
from const import ResponseBody
from client.courier import Courier
import allure
from faker import Faker
fake = Faker()

login = fake.name()
password = fake.password()
name = fake.first_name()


class TestCourier:
    @allure.title('create new courier')
    def test_create_courier(self):
        data = {
            "login": login,
            "password": password,
            "firstName": name
                }
        courier = Courier()
        response = courier.post_v1_create_courier(Constants.URL, data=data)
        assert response.status_code == 201 and response.json() == ResponseBody.OK_TRUE

    @allure.title('can`t create two couriers with the same login')
    def test_cant_create_two_couriers_the_same_login(self):
        data = {
            "login": Constants.TEST_LOGIN,
            "password": password,
            "firstName": name
        }
        courier = Courier()
        response = courier.post_v1_create_courier(Constants.URL, data=data)
        assert response.status_code == 409 and response.json() == ResponseBody.WRONG_LOGIN

    @allure.title('can`t create courier without required field')
    @pytest.mark.parametrize("test_login, test_password", [("", password), (login, "")])
    def test_create_courier_without_required_fields(self, test_login, test_password):
        data = {
            "login": test_login,
            "password": test_password,
            "firstName": name
        }
        courier = Courier()
        response = courier.post_v1_create_courier(Constants.URL, data=data)
        assert response.status_code == 400 and response.json() == ResponseBody.WITHOUT_DATA_TO_CREATE

    @allure.title('delete courier')
    def test_delete_courier(self, prepare_courier_for_delete):
        courier = Courier()
        courier_id = prepare_courier_for_delete.json()["id"]
        response = courier.delete_v1_courier(url=Constants.URL, id=courier_id)
        assert response.status_code == 200 and response.json() == ResponseBody.OK_TRUE

    @allure.title('can`t delete courier without id')
    def test_delete_courier_without_id(self, prepare_courier):
        courier = Courier()
        response = courier.delete_v1_courier(url=Constants.URL, id="")
        assert response.status_code == 404 and response.json() == ResponseBody.NOT_FOUND

    @allure.title('can`t delete courier with wrong id')
    def test_delete_courier_with_wrong_id(self, prepare_courier):
        courier = Courier()
        response = courier.delete_v1_courier(url=Constants.URL, id="56789")
        assert response.status_code == 404 and response.json() == ResponseBody.WRONG_ID
