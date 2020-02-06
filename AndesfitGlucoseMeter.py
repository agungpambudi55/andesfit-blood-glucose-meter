'''
Created on Jan 2020

Contributor :
- Agung Pambudi <agung.pambudi5595@gmail.com>
- Azman Latif <azman.latif@mail.ugm.ac.id>
'''

import pygatt

#import logging
#logging.basicConfig()
#logging.getLogger('pygatt').setLevel(logging.DEBUG)

def handleData(handle, value):
    if len(value) == 12:
        bloodGlucoseHigh, bloodGlucoseLow = value[10] << 8, value[9] & 0xFF
        bloodGlucose = str(bloodGlucoseHigh | bloodGlucoseLow)

        print('Blood Glucose {} mg/dL'.format(bloodGlucose))

try:
    adapter = pygatt.GATTToolBackend(hci_device='hci0')
    adapter.start()

    for discover in adapter.scan(run_as_root=True, timeout=5):
        if discover['name'] == 'Samico GL':
            try:
                print('Device found, try to connect with device')
                device = adapter.connect(discover['address'], address_type=pygatt.BLEAddressType.random) # ADF Type Random
                print('Connected with device')

                # ADF Write Characteristics, set up date time
                device.char_write_handle(0x21, [0x5A, 0x0A, 0x00, 0x14, 0x0F, 0x05, 0x09, 0x05, 0x01, 0x9D], True)
                # ADF Notify Characteristics, 0x24 handle FFF4 + 2
                device.char_write_handle(0x26, [0x01, 0x00], True)                
                print('Write successfully')

                while True:
                    # Subcribe value handle + 2
                    device.subscribe_handle_two('0000fff4-0000-1000-8000-00805f9b34fb', callback=handleData)

            except KeyboardInterrupt:
                print('Terminate')
            except:
                print('Failed to connect with device')
            finally:
                device.disconnect()
                
except KeyboardInterrupt:
    print('Terminate')
except:
    print('Something went wrong with adapter')
finally:
    adapter.stop()