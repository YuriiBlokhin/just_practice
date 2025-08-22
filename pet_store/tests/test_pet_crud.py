import time
from pet_store.objects.pet_objects.create_pet import CreateNewPet
from pet_store.objects.pet_objects.delete_pet import DeletePet
from pet_store.objects.pet_objects.get_pet import GetPet
from pet_store.objects.pet_objects.update_pet import UpdatePet


def test_create_pet(pet_base_url, pet_payload):
    new_pet_endpoint = CreateNewPet()
    new_pet_endpoint.create_new_pet(pet_base_url, pet_payload)
    new_pet_endpoint.check_response_200()
    new_pet_endpoint.check_response_name(pet_payload['name'])

def test_get_pet(pet_base_url, pet_id):
    time.sleep(3) # for sure server have enough time to create an object
    get_pet_endpoint = GetPet()
    get_pet_endpoint.get_pet_by_id(pet_base_url, pet_id)
    get_pet_endpoint.check_response_200()
    get_pet_endpoint.check_response_id(pet_id)

def test_update_pet(pet_base_url, pet_id, pet_update_payload):
    update_pet_endpoint = UpdatePet()
    update_pet_endpoint.update_pet(pet_base_url, pet_id, pet_update_payload)
    update_pet_endpoint.check_response_200()
    update_pet_endpoint.check_response_name(pet_update_payload['name'])

def test_delete_pet(pet_base_url, pet_id):
    time.sleep(3)
    delete_pet_endpoint = DeletePet()
    delete_pet_endpoint.delete_pet_by_id(pet_base_url, pet_id)
    delete_pet_endpoint.check_response_200()
    get_deleted_pet_by_id = GetPet()
    get_deleted_pet_by_id.get_pet_by_id(pet_base_url, pet_id)
    get_deleted_pet_by_id.check_response_404(pet_id)



