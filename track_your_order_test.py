import configuration
import data
import sender_stand_request
# Василиса Матвеева, 15-я когорта — Финальный проект. Инженер по тестированию плюс
def test_track_your_order():
    order_response = sender_stand_request.post_new_order()
    track = order_response.json()["track"]
    track_response = sender_stand_request.get_order_tracking(track)
    assert track_response.status_code == 200
