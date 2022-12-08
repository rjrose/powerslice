# Device Power Arbitration in Python

## Overview

This section contains much of the work regarding managing power demands between multiple devices. The overall goal was to create a python script that can allocate a limited pool of available power to any number of connected devices. This would serve as an initial stepping stone towards an eventual physical implementation of the PowerSlice device.

## Components

The components/features of this python script are as follows:

1. A pool of power of a fixed size that is allocated to connected devices, representing a USB PD supply connected to the PowerSlice device.
2. A dictionary to store connected device information, including device name, maximum/desired power draw, and allocated power
3. Functions to add/remove devices from the dictonary, analagous to connecting/disconnecting devices from the PowerSlice device. Adding a device allocates either the devices maximum power if able or any remaining power in the pool. Removing a device returns any allocated power to the available power pool.
4. A power balancing function. If the power pool is large enough, the function assigns each device its maximum power. If it is not, an "under power factor" is computed (maximum power draw/combined maximum power draw of all connected devices). This power factor is then multiplied by the maximum power draw of each device to determine allocated power. This results in each device receiving the same proportion of their maximum power, which is an initial attempt at fairly balancing power between a number of connected devices.
5. Printing/plotting functions to display current system state.

## File explanation/purposes

The initial development of this script revolved around creating a number of application specific classes, with an object oriented approach. This quickly ballooned in terms of complexity, and distracted away from the original purpose of the exercise. The initial object oriented approach consisted of:

- A power pool class in powerpool.py with test poolTest.py
- A power port class in powerport.py
- A power system class in powersystem.py with test systemTest.py

On a second attempt, a simpler device management scheme allowing the program to be self contained in one file was atttempted. Initially, a more rudimentary data structure with a list of tuples was tried in powerManager.py. This was found difficult to work with, so a dictionary was used in powerManagerV2.py. This was much more feasible to work with, so this became the final implementation of the script.
