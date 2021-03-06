IMU sensors
===========

[Python][1] classes to interface with IMU sensors via I2C protocol on
[Raspberry Pi][2] and similar platforms.

Developed for [Quad/Pi project][5]

Included is support for these sensors:

 * ADXL345 digital accelerometer
 * ITG3200 digital gyroscope

Only polling is supported at the moment (no interrupts).

Documentation
-------------

Please see [project wiki][3] for some code examples and hardware tips.

Requirements
------------

 * Python 2
 * kernel driver for your I2C controller loaded
 * SMBus python module (package python-smbus in Debian)
 * superuser access may be needed for accessing I2C

Development
-----------

[Project page][4] is hosted on Github.

License
-------

Copyright 2013 Michal Belica < *devel* at *beli* *sk* >

```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/ .
```

You find a copy of the GNU General Public License in file LICENSE distributed
with the software.

[1]: http://python.org/ "Python official website"
[2]: http://www.raspberrypi.org/ "Raspberry Pi official website"
[3]: https://github.com/beli-sk/IMU_sensors/wiki "IMU sensors project wiki"
[4]: https://github.com/beli-sk/IMU_sensors "IMU sensors project page"
[5]: http://www.coders.sk/quadpi "Quad/Pi project"
