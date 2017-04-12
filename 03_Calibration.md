# Extruder calibration
To ensure the stepper movement translates into the piston movement accordingly to the g-code, it needs to be calibrated properly.

## Calibration set-up
In principle, the calibration set-up requires:
- CNC control of the piston powering motor (we use Nema 11 with a planetary reductor)
- the assembled extruder (at least the moving parts)
- a precise displacement measurement device (calipers, etc., high precision indicators are preferrable)

The calibration protocol requires a set-up, where the piston translation, can be precisely measured in the axis of extrusion. For this purpose, the measurement device is fixed on the extruder in a way, that the extruder movement is translated directly into the measurement.

## Calibration procedure
1. adjust the steps/unit value of the motor settings in the cnc control software (or use default values)
2. command piston movement for an exact distance
3. measure the real movement distance and compare
4. repeat steps 1-3, until the g-code value coincides with the measured value

For a Nema 11 motor (with a planetary reductor) + an M5 spindle (0.5mm pitch/rotation), the default STEPS/UNIT value is 37914.30.
