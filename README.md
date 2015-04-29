# trinity

**Trinity is BRAND NEW, no commits (yet).**

### Overview

Trinity is a Python-based abstraction layer for hardware APIs. It's specifically geared towards the Internet of Things (IoT). Here are some examples:

```Python
trinity.off('lights')
trinity.off('thermostat')
trinity.off('wall socket')
```

Device-specific functions are also abstracted:

```Python
trinity.set('lights', 50)
trinity.set('thermostat', 75)
```

These are equivalent to:

```Python
trinity.set('lights', option='brightness', value=50, units='percent')
trinity.set('thermostat', option='temperature', value=75, units='fahrenheit')
```

The devices are registered beforehand:

```Python
trinity.register(device='Nest Thermostat', host=192.168.1.2)
trinity.register(device='Philips Hue Light Bulb', host=192.168.1.3)
trinity.register(device='Belkin Wemo', host=192.168.1.4)
```

### Configuration
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

Trinity can infer the option that should be modified based on the type and dimension of the ```value``` argument. Thus, we can set the color by calling:


```Python
trinity.set('lights', value=(0,122,255))
```

Or, more explicitly:

```Pythonwifi
trinity.set('lights', option='color', value=(0,122,255), units=('red,'green','blue'))
```



### Future Goals
Initial work will focus on WiFi devices. Later on I hope to support devices that communicate via RF/Infrared/Bluetooth.