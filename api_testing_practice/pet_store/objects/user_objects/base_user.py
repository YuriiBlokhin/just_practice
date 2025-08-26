import requests


class BaseUser:
    def __init__(self):
        self.response = None
        self.response_json = None

    def check_response_200(self):
        assert self.response.status_code == 200

    def check_response_404(self):
        assert self.response.status_code == 404