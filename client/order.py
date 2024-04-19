import requests
import allure


class Order:
    @allure.step('create new order')
    def post_v1_create_order(self, url, data):
        return requests.post(f'{url}/api/v1/orders', json=data)

    @allure.step('get order list')
    def get_v1_orders_list(self, url):
        return requests.get(f'{url}/api/v1/orders')

