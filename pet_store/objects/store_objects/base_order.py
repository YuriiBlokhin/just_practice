class BaseOrder:
    def __init__(self):
        self.response = None
        self.response_json = None

    def check_response_200(self):
        return self.response.status_code == 200