pygamsapi: a thin Python wrapper for the GAMS© API
=========================================================


.. code:: py

    In [1]: import pygamsapi

    In [2]: client = pygamsapi.GamsClient("key-XXXX")

    In [3]: client.nodes()
    Out[3]:
    [{'detail_uri': 'https://api.measureofquality.com/v2/nodes/064e7fd0-ac7b-11e6-86ee-cb0a91583c9f',
     'latest_uri': 'https://api.measureofquality.com/v2/nodes/064e7fd0-ac7b-11e6-86ee-cb0a91583c9f/records/latest',
     'name': 'Guest Room Air Quality',
     'uuid': '064e7fd0-ac7b-11e6-86ee-cb0a91583c9f'},
    {'detail_uri': 'https://api.measureofquality.com/v2/nodes/1baa96ac-a64f-11e6-bf43-b15a0db64587',
     'latest_uri': 'https://api.measureofquality.com/v2/nodes/1baa96ac-a64f-11e6-bf43-b15a0db64587/records/latest',
     'name': 'Topaz Air Quality',
     'uuid': '1baa96ac-a64f-11e6-bf43-b15a0db64587'},
    {'detail_uri': 'https://api.measureofquality.com/v2/nodes/1ba98cb2-a64f-11e6-869e-619f4fad7e6a',
     'latest_uri': 'https://api.measureofquality.com/v2/nodes/1ba98cb2-a64f-11e6-869e-619f4fad7e6a/records/latest',
     'name': 'Westin Club Air Quality',
     'uuid': '1ba98cb2-a64f-11e6-869e-619f4fad7e6a'}]

    In [4]: for n in client.nodes():
      ...:     print(client.latest(n['uuid']))
      ...:
    {'ts': '2018-03-22T09:25:02+00:00', 'fields': {'voc': '0.107', 'pm10': '3.2', 'temperature': '23.55', 'humidity': '31.45', 'pm25': '21.1', 'co2': '423'}, 'uuid': '064e7fd0-ac7b-11e6-86ee-cb0a91583c9f', 'levels': {'voc': 0, 'pm10': 0, 'temperature': None, 'humidity': None, 'pm25': 1, 'co2': 0}, 'outdoor_uri': 'https://api.measureofquality.com/v2/okq/cn:shanghai:jinganjiancezhan/records/latest'}
    {'ts': '2018-03-22T09:27:02+00:00', 'fields': {'voc': '0.164', 'pm10': '23.9', 'temperature': '25.48', 'humidity': '33.64', 'pm25': '19.4', 'co2': '707'}, 'uuid': '1baa96ac-a64f-11e6-bf43-b15a0db64587', 'levels': {'voc': 0, 'pm10': 0, 'temperature': None, 'humidity': None, 'pm25': 1, 'co2': 1}, 'outdoor_uri': 'https://api.measureofquality.com/v2/okq/cn:shanghai:jinganjiancezhan/records/latest'}
    {'ts': '2018-03-22T09:25:03+00:00', 'fields': {'voc': '0.067', 'pm10': '30.2', 'temperature': '26.50', 'humidity': '32.24', 'pm25': '39.8', 'co2': '598'}, 'uuid': '1ba98cb2-a64f-11e6-869e-619f4fad7e6a', 'levels': {'voc': 0, 'pm10': 0, 'temperature': None, 'humidity': None, 'pm25': 2, 'co2': 0}, 'outdoor_uri': 'https://api.measureofquality.com/v2/okq/cn:shanghai:jinganjiancezhan/records/latest'}

