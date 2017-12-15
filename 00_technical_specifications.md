# Vitaprint hardware technical specifications

## CNC XYZ mechanics: 3020T
- Axis: 3
- Height: 400mm
- Width: 400mm
- Depth: 550mm
- Motors (xyz):  NEMA23
- Movement resolution: 0.01mm (theoretically achievable 0.001mm)
- Positioning accuracy: 0.05mm
- Maximal number of extruders: 3

## Vitaprint extruder:
- Axis: 2
- Motion: Extruder Z movement and E extrusion
- Z motor: NEMA 11
- Z movement resolution: 0.01mm (theoretically achievable 0.001mm)
- Z positioning accuracy: 0.05mm
- Cartridge: 5ml luer-lock syringes (polypropylene)
- Nozzle: Gaugle needle
- Heating: room temperature - 250°C
- Extrusion motor: NEMA 11 with planetary reductor
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
- Print File Type: G-code (generate externally via slicer software, not included)
