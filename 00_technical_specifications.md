# Vitaprint hardware technical specifications

## CNC XYZ mechanics: 3020T
- Machine size:
  -- Width: 410mm (X)
  -- Depth: 540mm (Y)
  -- Height: 400mm (Z)
- Motors (x, y, z):  NEMA23
- Movement resolution: 0.01mm (theoretically achievable 0.001mm)
- Motion drive: trapeziodal lead screw, linear rods with ball bearings
- Maximal number of extruders: 3

NOTE: The values above are for a default setup. Extrudes can be mounted on any 3-axis CNC platform, therefore the working area and maximal number of extruders can be changed if needed.

## Vitaprint extruder:
- Axis: 2
- Motion: Extruder Z movement and E extrusion
- Z motor: NEMA 11
- E motor: NEMA 11 with planetary gearbox
- Z movement resolution: 0.01mm (theoretically achievable 0.001mm)
- Cartridge: 5ml luer-lock syringes (polypropylene)
- Nozzle: Gauge needle
- Heating: room temperature - 250°C
- Extrusion resolution: 0.01mm piston movement (1.2uL for 5ml syringe)

## Control electronics:
- Controller: PlanetCNC MK3 9 axis
- Control software: PlanetCNC CNC USB controller
- Power Requirements: 230/110V AC
- Software: PlanetCNC CNC USB controller
- Operating Systems: Windows / Linux
- Print File Type: G-code

## Printing:
- Printing volume (x,y,z): 200 x 300 x 45mm
- Printing speed: max 2600mm/min, typical 500mm/min
- Print File Type: G-code (generate externally via Slic3r software)

NOTE: printing volume will depend on the amount of extruders used.
