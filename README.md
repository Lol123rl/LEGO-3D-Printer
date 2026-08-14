# LEGO SPIKE Prime 3D Printer

A functional 3D printer built mostly from LEGO Education SPIKE Prime parts.

The printer uses LEGO motors to move the printing mechanism in three axes while a real 3D printing pen melts and deposits filament.

## Final Printer

![Final LEGO SPIKE Prime 3D Printer](8302.jpg)

This is the final version of the printer. The orange filament spool is mounted above the machine so filament can feed directly down into the 3D printing pen.

## Video

[Watch the LEGO 3D Printer in action](8311.mp4)

## What It Does

The printer can:

- move the print head left and right
- move the printing mechanism forward and backward
- raise and lower the print head
- use a Force Sensor during setup
- control movement from a LEGO SPIKE Prime Hub
- feed filament into a real heated 3D printing pen
- print programmed shapes in multiple passes and layers

## How It Works

The LEGO structure acts like the frame and motion system of a normal 3D printer.

The SPIKE Prime Hub runs Python code that tells the motors exactly how far to rotate. Gears, axles, beams, and linkages convert those motor rotations into movement of the printer.

The 3D printing pen provides the heated nozzle and melted filament.

### Current Port Setup

| Port | Function |
|---|---|
| A | Z-axis motor |
| B | Z-axis motor |
| C | X-axis motor |
| D | Force Sensor |
| E | Y-axis motor |
| F | Y-axis motor |

More information is available in the [Wiring Guide](wiring.md).

## Hardware

The build uses parts from two LEGO Education SPIKE Prime kits, including:

- LEGO SPIKE Prime Hub
- 3 large LEGO motors
- 3 small LEGO motors
- LEGO Force Sensor
- Technic beams and frames
- gears
- axles
- pins
- connectors
- structural panels

Additional materials:

- 3D printing pen
- 3D printer filament
- parchment paper for the print surface

See the complete cost and materials list in [BOM.csv](BOM.csv).

## Software

The printer is controlled by Python running on the LEGO SPIKE Prime Hub.

The complete program is here:

### [printer.py](printer.py)

The program includes:

- motor pairing
- X-axis movement
- Y-axis movement
- Z-axis movement
- calibration values
- travel movement
- precise line drawing
- diagonal movement
- triangle drawing
- square/diamond drawing
- circle drawing
- multiple passes for thicker prints
- multiple printed layers
- startup positioning
- Force Sensor input

The current program prints a small FIRST-style logo made from several geometric shapes.

## How to Run

1. Build the printer and check that all moving parts can move freely.
2. Connect the motors and Force Sensor to the correct SPIKE Prime ports.
3. Load [`printer.py`](printer.py) into the LEGO SPIKE Prime Python environment.
4. Transfer the program to the Hub.
5. Load filament into the 3D printing pen.
6. Place parchment paper on the printing surface.
7. Turn on the printing pen.
8. Allow the pen to heat up.
9. Run the Python program.
10. Allow the printer to complete its setup movements.
11. Press the Force Sensor when the program is ready.
12. The printer begins its automated print routine.

## Assembly

Detailed building information is available here:

### [Assembly Instructions](instructions.md)

The main sections of the printer are:

1. base
2. print surface
3. vertical frame
4. X-axis mechanism
5. Y-axis mechanism
6. Z-axis mechanism
7. print-head carriage
8. 3D printing pen holder
9. filament spool holder
10. Force Sensor
11. SPIKE Prime Hub
12. wiring

## Project Photos

### Final Version

The final printer has the orange filament spool mounted above the print head.

![Final LEGO 3D Printer](8302.jpg)

### Printing Test

This photo shows the printer with filament already deposited onto the print surface.

![LEGO 3D Printer test print](6268.jpg)

### Earlier Build / Prototype

This was an earlier version used while developing and testing the printer.

![Earlier LEGO 3D Printer prototype](Screenshot%202026-08-12%20120936.png)

## Development

The printer went through several changes during development.

Early versions were used to test:

- frame strength
- motor placement
- print-head movement
- filament feeding
- print-bed alignment
- motor calibration

The final version added the elevated filament spool so the filament could feed more directly into the printing pen.

## Bill of Materials

The full bill of materials is available here:

### [BOM.csv](BOM.csv)

The BOM includes the two SPIKE Prime kits, 3D printing pen, filament, and printing surface material.

## Repository Files

| File | Purpose |
|---|---|
| [`printer.py`](printer.py) | Python program controlling the printer |
| [`instructions.md`](instructions.md) | Assembly guide |
| [`wiring.md`](wiring.md) | Wiring and port information |
| [`BOM.csv`](BOM.csv) | Bill of materials and estimated cost |
| [`8311.mp4`](8311.mp4) | Video of the printer |
| `8302.jpg` | Final printer photo |
| `6268.jpg` | Printing-test photo |
| `Screenshot 2026-08-12 120936.png` | Earlier prototype photo |

## Safety

The 3D printing pen has a heated nozzle.

While the printer is operating:

- do not touch the nozzle
- keep wires away from the hot end
- keep LEGO pieces away from the nozzle
- keep filament clear of moving gears
- turn the pen off before adjusting the print-head mechanism
- allow the pen to cool before handling the nozzle

## Project Goal

The goal of this project was to find out whether LEGO SPIKE Prime could be used to create a working small-scale 3D printer.

The project combines:

- LEGO mechanical engineering
- Python programming
- motor synchronization
- gear systems
- motion calibration
- sensor input
- additive manufacturing
