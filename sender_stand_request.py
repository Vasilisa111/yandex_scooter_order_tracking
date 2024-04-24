# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data



def post_new_order():
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.new_order_body)

def get_order_tracking(track):
    return requests.get(url=configuration.URL_SERVICE + configuration.ORDER_TRACKING_PATH + str(track))