from faker import Faker
fake = Faker()


def post_payload():
    return {
    "name":  fake.name(),
    "gender":"male",
    "email":fake.email(),
    "status":"active"
}

def patch_payload():
    return {
    "name":fake.name(),
    "email":fake.email(),
    "gender": "male",
    "status":"active"
}