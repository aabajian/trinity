# trinity

**Trinity is BRAND NEW, no commits (yet).**

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

Trinity uses standardized configuration files for each device:

```
# Trinity config file for Philips Hue light bulb

[Device Identifier]

18686361 # I made this up.

[Device Name]

Philips Hue Light Bulb

[Device Connection]

ip

[Commands]

on  # Turns the light bulb on.
off # Turns the light bulb off. 
temperature PERCENTAGE # Sets the light bulb brightness to PERCENTAGE percentage.

[Command Execution]

on; POST /on
off; POST /off
temperature; POST /temperature; parameters=(percentage, INTEGER)

[Synonyms]

light(s), bulb(s)
```