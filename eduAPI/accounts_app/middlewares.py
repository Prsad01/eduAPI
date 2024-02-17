import logging

request_logs_path = ''
response_log_path = ''




class RequestLogging:
    def __init__(self,get_response) -> None:
        self.get_response = get_response
        self.request_logger = logging.getLogger('request_logger')
        self.response_logger = logging.getLogger('response_logger')

    def __call__(self, request):

        response = self.get_response(request)

        request_log_data = {
            'user':request.user.username,
            'method':request.method,
        }
        self.request_logger.info(f"incoming request {request_log_data}")

        response_log_data = {
            'status_code':response.status_code
        }
        print()
        if response.status_code >= 400:
            self.response_logger.error(f"Error {response.status_code}: {response.content}")
        else:
            self.response_logger.info(f"Response {response.status_code}: {response.content}")

        return response
        