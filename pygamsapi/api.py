"""Define object for interacting with GAMS API."""

import requests
from requests.auth import HTTPBasicAuth

API_BASE_URL = 'https://api.measureofquality.com/v2'
BASIC_AUTH_USER = 'api'


class BaseAPI(object):
    """Define a class that represents an API request."""

    def __init__(self, base_url=API_BASE_URL):
        """Initialize."""
        self.base_url = base_url

    def request(self, method_type, uri, **kwargs):
        """Define a generic request."""
        if self._api_key:
            kwargs['auth'] = HTTPBasicAuth(BASIC_AUTH_USER, self._api_key)

        full_url = '{0}/{1}'.format(self.base_url, uri)
        method = getattr(requests, method_type)
        res = method(full_url, **kwargs)

        return self.response(res)

    def get(self, uri, **kwargs):
        """Define a generic GET request."""
        return self.request('get', uri, **kwargs)

    def response(self, res):
        """Define a generic response"""
        if res.status_code == 200:
            return res.json()
        else:
            return {}
