import json

from rest_framework.renderers import JSONRenderer


class JSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''

        if 'ErrorDetail' in str(data):
            response = json.dumps(data)
        else:
            response = json.dumps({
                'status_code': renderer_context['response'].status_code,
                'data': data,
            })
        return response