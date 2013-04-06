#!/usr/bin/python
# vim: ai:ts=4:sw=4:sts=4:et:fileencoding=utf-8
#
# ADXL345 accelerometer control class
#
# Copyright 2013 Michal Belica <devel@beli.sk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#

import smbus

def int_sw(x):
    """Interpret integer as signed word"""
    return x - 0xffff if x > 0x7fff else x

class SensorADXL345(object):
    """Class for control of ADXL345 digital accelerometer.
    Data polling is supported at the moment.
    """
    def __init__(self, bus_nr, addr):
        """ Sensor class constructor
        Params:
            bus_nr .. I2C bus number
            addr   .. ADXL345 device address
        """
        self.bus = smbus.SMBus(bus_nr)
        self.addr = addr

    def standby(self, stdby = True):
        """Put device into standby mode or back to measure mode
        The device is in standby mode after power up."""
        self.bus.write_byte_data(self.addr, 0x2d, 0x08 if stdby else 0)

    def data_format(self, fullres, range):
        """Set data format
        Params:
            range   .. +-2, 4, 8 or 16g
            fullres .. full resolution up to 13bit or fixed 10bit
        """
        range_bits = {2: 0, 4: 1, 8: 2, 16: 3}
        fr_bit = 8 if fullres else 0
        self.bus.write_byte_data(self.addr, 0x31, fr_bit | range_bits[range])

    def output_data_rate(self, rate, low_power = False):
        """Set output data rate and low-power mode
        Params:
            rate .. code from this list:
                0.10Hz 0x0
                0.20Hz 0x1
                0.39Hz 0x2
                0.78Hz 0x3
                1.56Hz 0x4
                3.13Hz 0x5
                6.25Hz 0x6
                12.5Hz 0x7
                25Hz   0x8
                50Hz   0x9
                100Hz  0xA
                200Hz  0xB
                400Hz  0xC
                800Hz  0xD
                1600Hz 0xE
                3200Hz 0xF
            low_power .. enable/disable low power mode
        """
        lp_bit = 16 if low_power else 0
        if not (rate >= 0 and rate <= 0xf):
            raise ValueError("Invalid output data rate code.")
        self.bus.write_byte_data(self.addr, 0x2c, rate | lp_bit)
        

    def default_init(self):
        """Initialization with default values
        Standby mode off, +-2g range, 10-bit fixed resolution, 100Hz ODR.
        """
        self.data_format(False, 2)
        self.output_data_rate(0xA)
        self.standby(False)

    def read_data(self):
        """Read and return data tuple for x, y and z axis as signed integers
        from 10 to 13 bit range according to data format.
        """
        ax = int_sw(self.bus.read_word_data(self.addr, 0x32))
        ay = int_sw(self.bus.read_word_data(self.addr, 0x34))
        az = int_sw(self.bus.read_word_data(self.addr, 0x36))
        return (ax, ay, az)

if __name__ == '__main__':
    import time
    sensor = SensorADXL345(1, 0x53)
    sensor.default_init()
    time.sleep(0.1)
    ax, ay, az = sensor.read_data()
    sensor.standby()
    print ax, ay, az

