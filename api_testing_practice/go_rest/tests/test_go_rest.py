from api_testing_practice.go_rest.objects.create_user_object import CreateUser
from api_testing_practice.go_rest.objects.delete_user_object import DeleteUser
from api_testing_practice.go_rest.objects.get_user_by_id_object import GetUserById
from api_testing_practice.go_rest.objects.get_users_list_object import GetUsersList
from api_testing_practice.go_rest.objects.update_user_object import UpdateUser


def test_get_users_list(authorization):
    users_list = GetUsersList()
    users_list.get_users_list(authorization)
    users_list.check_response_is_200()
    users_list.check_response_not_empty()

def test_create_user(authorization, payload):
    new_user = CreateUser()
    new_user.create_user(authorization, payload)
    new_user.check_response_is_201()
    new_user.check_name(payload)
    new_user.check_gender(payload)
    new_user.check_email(payload)
    new_user.check_status(payload)

def test_get_user_by_id(user_id, authorization, payload):
    get_user = GetUserById()
    get_user.get_user_by_id(user_id, authorization)
    get_user.check_response_is_200()
    get_user.check_name(payload)
    get_user.check_gender(payload)
    get_user.check_email(payload)
    get_user.check_status(payload)

def test_update_user(user_id_for_update_user, authorization, update_payload):
    update_user = UpdateUser()
    update_user.update_user(user_id_for_update_user, authorization, update_payload)
    update_user.check_response_is_200()
    update_user.check_updated_name(update_payload)
    update_user.check_updated_email(update_payload)
    update_user.check_updated_status(update_payload)

def test_delete_user(user_id, authorization):
    delete_user = DeleteUser()
    delete_user.delete_user(user_id, authorization)
    delete_user.check_response_is_204()
    verify_user_deleted = GetUserById()
    verify_user_deleted.get_user_by_id(user_id, authorization)
    verify_user_deleted.check_response_is_404()
