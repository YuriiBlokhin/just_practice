class BaseUser:
    def __init__(self):
        self.response = None
        self.response_json = None


    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_name(self, payload):
        assert self.response_json['name'] == payload['name']

    def check_gender(self, payload):
        assert self.response_json['gender'] == payload['gender']

    def check_email(self, payload):
        assert self.response_json['email'] == payload['email']

    def check_status(self, payload):
        assert self.response_json['status'] == payload['status']