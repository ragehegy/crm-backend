import logging

logger = logging.getLogger(__name__)

class RequestLogger:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        response = self.get_response(request)

        logger.info("method=%s path=%s"%(request.method, request.path))
        return response