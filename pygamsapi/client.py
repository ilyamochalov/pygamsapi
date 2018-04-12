"""Define a GAMS API client."""
import json

from .api import BaseAPI


class GamsClient(BaseAPI):
    """Define a GAMS API client."""

    def __init__(self, api_key=None):
        """Initialize."""
        self._api_key = api_key
        super(GamsClient, self).__init__()

    def latest(self, node_uuid):
        """Retrieve latest records for a node."""
        uri = 'nodes/{0}/records/latest'.format(node_uuid)
        return self.get(uri)

    def nodes(self):
        """Retrive nodes list"""
        uri = 'nodes'
        return self.get(uri)
