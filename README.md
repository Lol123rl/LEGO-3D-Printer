# LEGO-3D-Printer
A LEGO SPIKE Prime 3D printer project.
# LEGO SPIKE Prime 3D Printer

A working 3D printer built mostly from parts from two LEGO Education SPIKE Prime kits.

The printer uses LEGO motors to move the printing mechanism and a 3D printing pen to melt and place filament.

## Software

The printer is controlled by Python code for the LEGO Education SPIKE Prime Hub.

The full program is available here:

[`printer.py`](printer.py)

### Port Setup

- Ports A + B = Z axis
- Port C = X axis
- Port D = Force Sensor
- Ports E + F = Y axis

### How to Run

1. Connect all motors and the Force Sensor to the correct SPIKE Prime ports.
2. Open `printer.py` in the LEGO SPIKE Prime Python environment.
3. Transfer the program to the Hub.
4. Run the program.
5. The printer performs its setup routine.
6. Press the Force Sensor when prompted.
7. The printer begins printing the 662 logo.

## Main Hardware

- 2 LEGO Education SPIKE Prime kits
- 3 large LEGO motors
- 3 small LEGO motors
- 1 LEGO Force Sensor
- 1 3D printing pen
- 3D printer filament
- Parchment paper for the printing surface

## How It Works

The LEGO structure controls the movement of the printer while the 3D printing pen provides the heated filament.

The motors move the printer mechanism in different directions so filament can be placed layer by layer.

## Bill of Materials

A complete parts and cost list is available in [`BOM.csv`](BOM.csv).

## Project Photos

### Finished LEGO 3D Printer

![Finished LEGO 3D Printer](Screenshot%202026-08-12%20120936.png)

### Front View

![LEGO 3D Printer Front View](8302.jpg)

### Printing Test

![LEGO 3D Printer Printing Test](6268.jpg)
