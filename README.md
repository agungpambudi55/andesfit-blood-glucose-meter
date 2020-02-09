# Andesfit Blood Glucose Meter
There are many medical devices for measuring blood glucose, one of which is the Andesfit Blood Glucose Meter with the ADF-B27 model. This medical device uses BLE (Bluetooth Low Energy) communication with GATT (Bluetooth Generic Attributes Generic Attribute Profile).

![Gambar][gambar-product-url]

## Subcribe handle plus two
File location : /usr/local/lib/python<version>/dist-packages/pygatt/device.py
Add this source code
```
def subscribe_handle_two(self, uuid, callback=None, indication=False, wait_for_response=True):
    value_handle = self.get_handle(uuid)
    characteristic = value_handle + 2
    properties = bytearray([0x2 if indication else 0x1, 0x0])

    with self._lock:
        if callback is not None:
            self._callbacks[value_handle].add(callback)

        if self._subscribed_handlers.get(value_handle, None) != properties:
            self.char_write_handle(characteristic, properties, wait_for_response=wait_for_response)
            self._subscribed_handlers[value_handle] = properties
            self._subscribed_uuids[uuid] = indication
            log.info("Subscribed to uuid=%s", uuid)
        else:
            log.debug("Already subscribed to uuid=%s", uuid)
```

## Measurement Data
How to get measurement data can use many ways, one of which uses the python programming language, for the source code program can be seen in AndesfitGlucoseMeter.py and BLE name is Samico GL.

![Gambar][gambar-screenshot-url]

<!-- MARKDOWN LINKS -->
[gambar-product-url]: https://github.com/agungpambudi55/andesfit-blood-glucose-meter/blob/master/Andesfit%20Blood%20Glucose%20Meter%20ADF-B27%20-%20Product.png
[gambar-screenshot-url]: https://github.com/agungpambudi55/andesfit-blood-glucose-meter/blob/master/Andesfit%20Blood%20Glucose%20Meter%20ADF-B27%20-%20Screenshot.png