# trinity

**Trinity is BRAND NEW, no commits (yet). The name Trinity comes from [this scene](https://www.youtube.com/watch?v=6AOpomu9V6Q) in The Matrix.**

### Overview

Trinity is a Python-based abstraction layer for hardware APIs. It's specifically geared towards the Internet of Things (IoT). Here are some simple examples:

```Python
trinity.off('lights')
trinity.on('thermostat')
trinity.off('wall socket')
trinity.on('drone')
```

Device-specific functions are also abstracted:

```Python
trinity.set('lights', 50)
trinity.set('thermostat', 75)
trinity.set('wall socket', 30)
trinity.set('lights', (0,122,255))
trinity.set('drone', (5,3,2))
```

These are equivalent to:

```Python
trinity.set('lights', option='brightness', value=50, units='percent')
trinity.set('thermostat', option='temperature', value=75, units='fahrenheit')
trinity.set('wall socket', option='shutoff timer', value=30, units='minutes')
trinity.set('lights', option='color', value=(0,122,255), units=('red,'green','blue'))
trinity.set('drone', option='location delta', value=(1,3,2), units=('meters','meters','meters'))
```

### Configuration


A device must be registered before it can be used:

```Python
trinity.register(device='Nest Thermostat', host=192.168.1.2)
trinity.register(device='Philips Hue Light Bulb', host=192.168.1.3)
trinity.register(device='Belkin Wemo', host=192.168.1.4)
trinity.register(device='Parrot AR.Drone 2.0', host=192.168.1.5)
```

Trinity uses standardized configuration files for each device:

```
# Trinity config file for Philips Hue light bulb

[Device Name]

Philips Hue Light Bulb

[Device Connection]

ip

[Commands]

on  # Turns the light bulb on.
off # Turns the light bulb off. 
brightness (percent, integer)|'max' # Sets the light bulb brightness.
color (red,integer) (blue,integer) (green,integer) # Sets the light bulb brightness.

[Command Execution]

on; POST /on
off; POST /off
brightness; POST /brightness; (percent, integer)|'max'
color; POST /color; (red,integer) (blue,integer) (green,integer)

[Synonyms]

light(s), bulb(s)
```


### Future Goals
* Initial work will focus on WiFi devices. Later on I hope to support devices that communicate via RF/Infrared/Bluetooth.
* A calibration process would be useful to synchronize devices.