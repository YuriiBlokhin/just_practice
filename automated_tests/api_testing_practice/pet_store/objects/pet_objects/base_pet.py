class BaseEndpoint:
    def __init__(self):
        self.response = None
        self.response_json = None

    def check_response_200(self):
        assert self.response.status_code == 200

    def check_response_name(self, name):
        assert self.response_json["name"] == name