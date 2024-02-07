import pytest
from const import Constants
from client.order import Order
import allure
from faker import Faker
fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()


class TestOrder:
    @allure.title('create new order')
    @pytest.mark.parametrize("color", ['BLACK', 'GREY', ('BLACK '
                                                         'GREY'), ""])
    def test_create_order(self, color):
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": "Водный стадион",
            "metroStation": 4,
            "phone": phone,
            "rentTime": 5,
            "deliveryDate": "2024-07-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                color
            ]
        }
        order = Order()
        response = order.post_v1_create_order(Constants.URL, data)
        assert response.status_code == 201 and "track" in response.json()

    @allure.title('get order list')
    def test_get_orders_list(self):
        order = Order()
        response = order.get_v1_orders_list(Constants.URL)
        assert response.status_code == 200 and "orders" in response.json()
