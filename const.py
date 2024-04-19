class Constants:
    URL = 'http://qa-scooter.praktikum-services.ru'
    TEST_LOGIN = 'DaRia'
    TEST_PASSWORD = '12345678'


class ResponseBody:
    NOT_FOUND = {"code": 404, "message": "Not Found."}
    WRONG_ID = {"code": 404, "message": "Курьера с таким id нет."}
    OK_TRUE = {"ok": True}
    WITHOUT_DATA_TO_CREATE = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    WRONG_LOGIN = {"code": 409, "message":"Этот логин уже используется. Попробуйте другой."}
    ID_DATA = {"id": 260399}
    WITHOUT_DATA_TO_LOGIN = {"code": 400, "message": "Недостаточно данных для входа"}
    WRONG_DATA_TO_LOGIN = {"code": 404, "message": "Учетная запись не найдена"}
