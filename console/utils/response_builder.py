from console.entities.html_response import CustomResponse


class ResponseBuilder:
    def build_response_success(self, data) -> CustomResponse:
        return CustomResponse(result='success', error_message=None, data=data)

    def build_response_error(self, error_message) -> CustomResponse:
        return CustomResponse(result='error', error_message=error_message, data=None)
