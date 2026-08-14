# LEGO SPIKE Prime 3D Printer

A working 3D printer built primarily from LEGO Education SPIKE Prime parts.

The printer uses LEGO motors to control movement in three axes and a 3D printing pen to melt and deposit filament. The machine is controlled by Python running on a single SPIKE Prime Hub.

![Finished LEGO 3D Printer](Screenshot%202026-08-12%20120936.png)

## Project Demo

[Watch the LEGO 3D Printer in action](8311.mp4)

## What It Does

This project turns LEGO SPIKE Prime parts into a functional small-scale 3D printer.

The printer can:

- move the print head left and right
- move the print bed forward and backward
- raise and lower the printing mechanism
- use a Force Sensor during setup
- control six LEGO motors from one SPIKE Prime Hub
- use a real 3D printing pen to extrude filament
- print a programmed multi-layer design

## How It Works

The printer has three controlled movement axes:

- **Z Axis — Ports A + B**
- **X Axis — Port C**
- **Y Axis — Ports E + F**
- **Force Sensor — Port D**

The paired motors keep the larger moving sections of the printer aligned.

Python code controls the motors by rotating them specific numbers of degrees. These motor rotations are converted into small movements of the print head and print bed.

The 3D printing pen supplies the melted filament while the LEGO mechanism controls where that filament is placed.

## Hardware

- 1 LEGO SPIKE Prime Hub
- 3 LEGO large motors
- 3 LEGO small motors
- 1 LEGO Force Sensor
- LEGO Technic beams, frames, gears, axles, pins, and connectors
- 1 3D printing pen
- 3D printer filament
- small piece of parchment paper for the print surface

Most of the LEGO components came from two LEGO Education SPIKE Prime kits.

## Wiring

| Port | Device / Function |
|---|---|
| A | Z-axis motor |
| B | Z-axis motor |
| C | X-axis motor |
| D | Force Sensor |
| E | Y-axis motor |
| F | Y-axis motor |

For additional wiring information, see:

[**Wiring Guide**](wiring.md)

## Software

The printer is controlled using Python for the LEGO Education SPIKE Prime Hub.

The complete program is here:

[**printer.py**](printer.py)

The program contains:

- motor pairing
- movement functions
- X, Y, and Z calibration
- precise movement calculations
- diagonal movement
- shape drawing
- multi-pass printing
- multi-layer printing
- startup positioning
- Force Sensor setup control

## How to Run the Printer

1. Assemble the printer.
2. Connect the motors and Force Sensor to the correct Hub ports.
3. Load [`printer.py`](printer.py) into the LEGO SPIKE Prime Python environment.
4. Transfer the program to the SPIKE Prime Hub.
5. Insert filament into the 3D printing pen.
6. Place parchment paper on the print surface.
7. Turn on the 3D printing pen and allow it to reach operating temperature.
8. Run the Python program.
9. Allow the printer to complete its setup movement.
10. Press the Force Sensor when the program is ready.
11. The automated printing sequence will begin.

## Assembly Instructions

Detailed assembly information is available here:

[**Assembly Instructions**](instructions.md)

The major parts of the build are:

1. LEGO Technic base
2. moving print bed
3. vertical support structure
4. X-axis mechanism
5. Y-axis mechanism
6. Z-axis mechanism
7. 3D printing pen holder
8. filament feed
9. Force Sensor
10. SPIKE Prime Hub and wiring

## Bill of Materials

The complete parts and estimated cost list is here:

[**BOM.csv**](BOM.csv)

The project uses parts from two SPIKE Prime kits plus:

- a 3D printing pen
- filament
- parchment paper

## Project Photos

### Finished Printer

![Finished LEGO SPIKE Prime 3D Printer](Screenshot%202026-08-12%20120936.png)

### Printer Mechanism

![LEGO 3D Printer mechanism](8302.jpg)

### Test Print

![LEGO 3D Printer test print](6268.jpg)

## Repository Files

| File | Purpose |
|---|---|
| [`printer.py`](printer.py) | Python program that controls the printer |
| [`instructions.md`](instructions.md) | Assembly instructions |
| [`wiring.md`](wiring.md) | Wiring and SPIKE Prime port information |
| [`BOM.csv`](BOM.csv) | Bill of materials and estimated costs |
| [`8311.mp4`](8311.mp4) | Video of the printer |
| `8302.jpg` | Project photo |
| `6268.jpg` | Printing test photo |
| `Screenshot 2026-08-12 120936.png` | Finished printer photo |

## Safety

The 3D printing pen becomes hot during use.

Keep hands, LEGO parts, wires, and other materials away from the heated nozzle while the printer is operating. Turn the pen off and allow it to cool before adjusting the print-head mechanism.

## Project Goal

The goal of this project was to see whether LEGO SPIKE Prime could be used to build and program a functioning three-axis 3D printer.

The project combines LEGO mechanical engineering, Python programming, motor synchronization, calibration, and additive manufacturing into one machine.
