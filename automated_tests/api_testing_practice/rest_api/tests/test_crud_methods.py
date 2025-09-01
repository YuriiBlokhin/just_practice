from automated_tests.api_testing_practice.rest_api.objects.create_object import CreateObject
from automated_tests.api_testing_practice.rest_api.objects.get_object import GetObject
from automated_tests.api_testing_practice.rest_api.objects.update_object import UpdateObject
from automated_tests.api_testing_practice.rest_api.objects.delete_object import DeleteObject


def test_create_object(payload):
    new_object_endpoint = CreateObject()
    new_object_endpoint.create_new_object(payload)
    new_object_endpoint.check_response_200()
    new_object_endpoint.check_response_name(payload['name'])


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(obj_id)
    get_object_endpoint.check_response_200()
    get_object_endpoint.check_response_id(obj_id)


def test_update_object(obj_id, update_payload):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_objet_by_id(obj_id, update_payload)
    update_object_endpoint.check_response_200()
    update_object_endpoint.check_response_name(update_payload['name'])


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object_by_id(obj_id)
    delete_object_endpoint.check_response_200()
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(obj_id)
    get_object_endpoint.check_response_404(obj_id)


