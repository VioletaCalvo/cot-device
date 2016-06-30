from gpiozero import LED, Button
from time import sleep
import json
import requests
from signal import pause

print 'starting ...'

# Set platform constants (credentials and URLs)
USER_ID = 'xxxxxxxxxxxxxxxxxxxx'
DEVICE_ID = 'xxxxxxxxxxxxxxxxxxxxxxxx'
DEVICE_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
GET_HOST = "https://communitythings.herokuapp.com/io_get"
PUT_HOST = "https://communitythings.herokuapp.com/io_put"


# DEFINE IO VARIABLE NAMES
# Configure input variables
led_1 = LED(19)
led_2 = LED(13)
led_3 = LED(6)
rainbow_led = LED(5)
#push_1 = Button(10)
#push_2 = Button(22)
push_3 = Button(27)

# Toogle on led 1 and 2 to show starting state on device
led_1.on()
led_2.on()

# define a output dict to process desired values from platform
output_dict = {
    'led_1': led_1,
    'led_2': led_2,
    'led_3': led_3,
    'rainbow_led': rainbow_led
    }

get_data = {
    'deviceId': DEVICE_ID,
    'deviceKey': DEVICE_KEY
}

put_data = get_data

# Send new values to platform on IO change
def onChange():
    put_data['IO'] = [
        {
            'id': 'led_1',
            'value': led_1.is_lit,
            'type': 'DO'
        },
        {
            'id': 'led_2',
            'value': led_2.is_lit,
            'type': 'DO'
        },
        {
            'id': 'push_1',
            'value': push_3.is_pressed,
            'type': 'DI'
        }
    ]
    put_json = json.dumps(put_data)
    payload = {'data': put_json, 'userId': USER_ID}
    r_get = requests.put(PUT_HOST, data=payload)
    if r_get.text != 'Got it!':
        print r_get.text

# Configure push_1 on change actions
push_3.when_pressed = onChange
push_3.when_released = onChange

get_json = json.dumps(get_data)
payload = {'data': get_json, 'userId': USER_ID}

# on startup, send device status to the platform
print 'sending status to the platform...'
onChange()

print 'RUNNING...'
# Toogle on all leds to show running state
led_1.on()
led_2.on()
led_3.on()
rainbow_led.on()

while True:
    # Get output desired values from platform
    r_put = requests.get(GET_HOST, data=payload)
    if r_put.status_code is 200:
        res = r_put.json()
        if res['needs_update']:
            for desired in res['desired_values']:
                if desired['id'] in output_dict.keys():
                    output = output_dict[desired['id']]
                    print desired
                    print output.is_lit
                    if output.is_lit is not desired['value']:
                        output.toggle()
                else:
                    print 'WARNING: received non valid output id!'
            # Send status to the platform
            onChange()
            
    else:
        print r_put.text
    sleep(3)

# DEFINE IO VARIABLE NAMES
# Configure input variables
led_1 = LED(19)
led_2 = LED(13)
led_3 = LED(6)
rainbow_led = LED(5)
push_1 = Button(10)
push_2 = Button(22)
push_3 = Button(27)

# Toogle on led 1 and 2 to show starting state on device
led_1.on()
led_2.on()

# define a output dict to process desired values from platform
output_dict = {
    'led_1': led_1,
    'led_2': led_2,
    'led_3': led_3,
    'rainbow_led': rainbow_led
    }

get_data = {
    'deviceId': DEVICE_ID,
    'deviceKey': DEVICE_KEY
}

put_data = get_data

# Send new values to platform on IO change
def onChange():
    put_data['IO'] = [
        {
            'id': 'led_1',
            'value': led_1.is_lit,
            'type': 'DO'
        },
        {
            'id': 'led_2',
            'value': led_2.is_lit,
            'type': 'DO'
        },
        {
            'id': 'led_3',
            'value': led_3.is_lit,
            'type': 'DO'
        },
        {
            'id': 'rainbow_led',
            'value': rainbow_led.is_lit,
            'type': 'DO'
        },
        {
            'id': 'push_1',
            'value': push_1.is_pressed,
            'type': 'DI'
        },
        {
            'id': 'push_2',
            'value': push_2.is_pressed,
            'type': 'DI'
        },
        {
            'id': 'push_3',
            'value': push_3.is_pressed,
            'type': 'DI'
        }
    ]
    put_json = json.dumps(put_data)
    payload = {'data': put_json, 'userId': USER_ID}
    r_get = requests.put(PUT_HOST, data=payload)
    if r_get.text != 'Got it!':
        print r_get.text

# Configure push_1 on change actions
push_1.when_pressed = onChange
push_1.when_released = onChange
push_2.when_pressed = onChange
push_2.when_released = onChange
push_3.when_pressed = onChange
push_3.when_released = onChange

get_json = json.dumps(get_data)
payload = {'data': get_json, 'userId': USER_ID}

# on startup, send device status to the platform
print 'sending status to the platform...'
onChange()

print 'RUNNING...'
# Toogle on all leds to show running state
led_1.on()
led_2.on()
led_3.on()
rainbow_led.on()

while True:
    # Get output desired values from platform
    r_put = requests.get(GET_HOST, data=payload)
    if r_put.status_code is 200:
        res = r_put.json()
        if res['needs_update']:
            for desired in res['desired_values']:
                if desired['id'] in output_dict.keys():
                    output = output_dict[desired['id']]
                    print desired
                    print output.is_lit
                    if output.is_lit is not desired['value']:
                        output.toggle()
                else:
                    print 'WARNING: received non valid output id!'
            # Send status to the platform
            onChange()
            
    else:
        print r_put.text
    sleep(3)

