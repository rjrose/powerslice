# Powerslice Poster

## Title

Powerslice: Supplying a world of new demands

## Contributors

Ryan Rosenberger, Boston University ECE

## Overview

- Powerslice is a portable, compact usb power splitter for portable electronic devices
- Takes an input from USB PD supply and divides it between a number of connected devices

## Methods

- Intial goal of building a physical prototype of the power splitter
- Researching available solutions showed that a physical implementation would be expensive in terms of money and time
- The biggest unknown with the project was how the arbitration between multiple devices would work
- How do multiple devices share a limited power source?
- 

## Results

- An initial power simulation in Matlab Simulink was generated to describe rough system behavior
- To further define and resolve the power arbitration problem, a python script was developed to develop and showcase a power management system
- Python script is able to handle a large number of connected devices, balancing power draw concerns between them

## Conclusions

- Initial management system works, is able to balance power between theoretical devices
- More development needed to add different charging schemes and handle nonidealities of real system

## Next Steps

- Add priority assignment capability: be able to funnel all power to one or more specific devices
- Handle real power variations, nonidealities of converters and losses in device
- Handle different charge rates, reallocating power as devices go through their charge cycles
- Once arbitration system is complete, can move onto physical realization of device

## Acknowledgements

None?