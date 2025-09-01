import time
from automated_tests.api_testing_practice.pet_store.objects.store_objects.create_order import CreateOrder
from automated_tests.api_testing_practice.pet_store.objects.store_objects.delete_order import DeleteOrder
from automated_tests.api_testing_practice.pet_store.objects.store_objects.get_order import GetOrder

def test_create_order(payload, base_store_url):
    create_order_endpoint = CreateOrder()
    create_order_endpoint.create_order(base_store_url, payload)
    create_order_endpoint.check_response_200()

def test_get_order(order_id, base_store_url):
    get_order_endpoint = GetOrder()
    get_order_endpoint.get_order_by_id(base_store_url, order_id)
    get_order_endpoint.check_response_200()

def test_delete_order(order_id, base_store_url):
    time.sleep(2)
    delete_order_endpoint = DeleteOrder()
    delete_order_endpoint.delete_order(base_store_url, order_id)
    delete_order_endpoint.check_response_200()
    verify_order_is_deleted = GetOrder()
    verify_order_is_deleted.get_order_by_id(base_store_url, order_id)
    verify_order_is_deleted.check_response_404(order_id)