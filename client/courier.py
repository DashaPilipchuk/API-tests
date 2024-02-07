import requests
import allure


class Courier:
    @allure.step('create new courier')
    def post_v1_create_courier(self, url, data):
        return requests.post(f'{url}/api/v1/courier', data)

    @allure.step('delete courier')
    def delete_v1_courier(self, url, id):
        return requests.delete(f'{url}/api/v1/courier/{id}')

    @allure.step('take courier login')
    def post_v1_login_courier(self, url, data):
        return requests.post(f'{url}/api/v1/courier/login', data)

