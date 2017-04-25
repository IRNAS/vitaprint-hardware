# Manufacturing and Assembly

## Table of contents
 - [Overview](#OVER)
 - [Part Manufacturing](#MANUFACTURING)
 - [Assembly Brief](#ASSEMBLY)
 - [Arduino Temperature Regulation](#CODE)
 

## 1 Overview and Toolset <a id="OVER"></a>
Here you can find manufacturing and assembly details for one Vitaprint unit. In this repository you can find STEP files for the Vitaprint unit in both orientations - Left and Right. The procedure is the same for both orientations (the final product is only mirrored) therefore you will find details for assembly for one unit in this repository. 

### 1.1 General
- Manufacturing time: 7h
- Assembly time: 30 min
- Manufacturing skills: high

### 1.2 Tool List and Skills Required
 - 3D printer (ABS)
 - CNC mill
 - CNC router
 - band saw
 - lathe
 - HAND TOOLS:
   - torx srewdriver
   - phillips screwdriver
   - super glue
   - allan key
 
### 1.3 Necessary Steps
 - purchase of raw materials and components
 - manufacturing of parts
 - assembly
 - calibration
 
## 2 Part Manufacturing <a id="MANUFACTURING"></a>
Manufacturing is impossible without advanced CNC milling and lathe skills.

 <img src="https://cloud.githubusercontent.com/assets/14543226/24997531/3aaafcba-2037-11e7-8800-1aba4ec7eacb.png" alt="bubble" width="450" height="400">

<img src="https://cloud.githubusercontent.com/assets/14543226/24997449/fa3d8c7e-2036-11e7-8a56-a97ed070c891.png" alt="table" width="500" height="600">

## 3 Assembly Details <a id="ASSEMBLY"></a>

### 3.1 Assembly Overview
 - manufacture all parts
 - assemble each section separately, then join them together
 
 | SECTION A | SECTION B | SECTION C |
 |-----------|-----------|-----------|
 |<img src="https://cloud.githubusercontent.com/assets/14543226/24998545/c2ab57ce-203a-11e7-9a3c-8f3a5b85e27a.png" alt="sectionB" width= "150" > | <img src="https://cloud.githubusercontent.com/assets/14543226/24998406/4e023a1e-203a-11e7-8f65-00fdcdb5f56f.png" alt="sectionB" width= "150" > |<img src="https://cloud.githubusercontent.com/assets/14543226/24998669/3aab29d4-203b-11e7-93f6-95d102f12aa9.png" alt="sectionB" width= "150">|
 


 - Use philips DIN965 screws wherever you see the hole chamfers, use torx BN6404 screws elsewhere
 - for the following steps gently apply hammer:
   -- sliding the M5 threaded rod into the coupler
   -- sliding the fi3 stainless steel rod into rod holder at the bottom and N11 motor plate at the top

### 3.2 Assembly Details
 | DESCRIPTION | STEP 1 | STEP 2 | 
 |------|-------|-------|
 |Collect all parts and tools|<img src="https://cloud.githubusercontent.com/assets/14543226/25372744/edc79336-2996-11e7-8249-ebf960823e0e.jpg" alt="tools_parts" width= "200" >|
 |Take Nema11 motor plate and Nema11 stepper motor and fix them together with four torx screws|<img src="https://cloud.githubusercontent.com/assets/14543226/25372981/177bbb2a-2998-11e7-8505-06f3d0da0ced.jpg" alt="step1a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25372926/d43add28-2997-11e7-8887-940e12599bcf.jpg" alt="step1b" width= "200" >|
 |Take the nut and nut plate and fix them together with two philips screws|<img src="https://cloud.githubusercontent.com/assets/14543226/25373052/586397b6-2998-11e7-80ab-f0d0bd8c4928.jpg" alt="step2a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25373068/663aa6c2-2998-11e7-84b6-38fa4631825c.jpg" alt="step2b" width= "200" >|
 |Take the threaded rod and join it with a coupler. The fit is designed to be tight.|<img src="https://cloud.githubusercontent.com/assets/14543226/25373374/b5b481ae-2999-11e7-8280-a12f8cc03a00.jpg" alt="step3a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25373386/c3dd8ed8-2999-11e7-8a1a-d0fb3adfce9e.jpg" alt="step3b" width= "200" >|
 |Screw the rod with a coupler through the nut M5 center thread. Slide the fi3 rods through the holes. |<img src="https://cloud.githubusercontent.com/assets/14543226/25376284/e063de72-29a3-11e7-94f8-825f228a2164.jpg" alt="step4a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25376309/f4293236-29a3-11e7-832d-61b2ab6464e1.jpg" alt="step4b" width= "200" >|
  |Merge the N11 motor section and the nut-rod section.|<img src="https://cloud.githubusercontent.com/assets/14543226/25376379/37758f6c-29a4-11e7-9715-d70013bed612.jpg" alt="step5a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25376392/4990475a-29a4-11e7-90a8-45d486ae110b.jpg" alt="step5b" width= "200" >|
  |Take the syringe mount, syringe mount bottom and top plates.|<img src="https://cloud.githubusercontent.com/assets/14543226/25377206/33e6a6ee-29a7-11e7-8bfa-ac163347e28d.jpg" alt="step6" width= "200" >||
  |Mount the bottom plate onto the syringe mount using two torx screws.|<img src="https://cloud.githubusercontent.com/assets/14543226/25377287/6a6a0efe-29a7-11e7-9010-d01c8a2049d9.jpg" alt="step7a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25377350/7eba8e56-29a7-11e7-9904-516d0fddc050.jpg" alt="step7b" width= "200" >|
  |Slide the ceramic heater in one of the bigger slots and place the thermistor in a smaller slot in the middle of syringe mount.|<img src="https://cloud.githubusercontent.com/assets/14543226/25377412/c4120236-29a7-11e7-8542-c983b59c6b93.jpg" alt="step8a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25377437/dc28e0c4-29a7-11e7-980a-3faca9494b64.jpg" alt="step8b" width= "200" >|
  |Glue/weld the short M5 threaded rod onto the 24BYJ-48 shaft and place the 24BYJ-48 nut. Then fix the motor and nut to the backplate.|<img src="https://cloud.githubusercontent.com/assets/14543226/25377633/5fe97914-29a8-11e7-9934-9532626a4b7c.jpg" alt="step9a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25377685/872e3e10-29a8-11e7-93f8-318a6381efbf.jpg" alt="step9b" width= "200" >|
  |Take the syringe mount and close it using torx screws and push the heater and thermistor wires through the wire slot in the backplate.|<img src="https://cloud.githubusercontent.com/assets/14543226/25377811/d7700e44-29a8-11e7-8c68-8fc3003a7f6b.jpg" alt="step10a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25377877/058f6f2c-29a9-11e7-83d3-5e8d1581c92c.jpg" alt="step10b" width= "200" >|
  |Fix the syringe mount with hotend to the backplate.|<img src="https://cloud.githubusercontent.com/assets/14543226/25382638/cec25f3a-29b8-11e7-82e8-de62081f6216.jpg" alt="step11a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25382645/d983b2f2-29b8-11e7-8975-65f7358a795e.jpg" alt="step11b" width= "200" >|
  |Mount the syringe mount - backplate assembly on to the CNC head. Begin with fixing the 24BYJ-48 to the respective motor plate.|<img src="https://cloud.githubusercontent.com/assets/14543226/25382777/5ccf904a-29b9-11e7-9837-8fe4f4b9941e.jpg" alt="step12a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25382867/c252bb68-29b9-11e7-9753-7f6fd9c06507.jpg" alt="step12b" width= "200" >|
  |Continue with fixing the backplate to the rail of the linear bearing system.|<img src="https://cloud.githubusercontent.com/assets/14543226/25382918/fce5939a-29b9-11e7-887e-dcb73cbb3892.jpg" alt="step13a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25382932/1217f366-29ba-11e7-9c19-3107a026c558.jpg" alt="step13b" width= "200" >|
  |Mount the Nema11 assembly with extrusion mechanics (threaded rod, nut, linear sliding rods) to the top of the assembly. First slide the rods into the slods on the syringe mount top, then fix the Nema11 motor plate to the top of the backplacte using torx screws.|<img src="https://cloud.githubusercontent.com/assets/14543226/25383136/fce483aa-29ba-11e7-9ec9-a5fe73751afe.jpg" alt="step14a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25383177/30c0c896-29bb-11e7-8dbd-c1063bc3635b.jpg" alt="step14b" width= "200" >|
  |This is the final appearance.|<img src="https://cloud.githubusercontent.com/assets/14543226/25383196/47870680-29bb-11e7-813d-f982c1aa632a.jpg" alt="step15a" width= "200" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25383224/7061cc34-29bb-11e7-8616-0636fbef9fdc.jpg" alt="step15b" width= "200" >|
  
  


## 4 Arduino: Temperature Regulation <a id="CODE"></a>


To download Arduino firmware for temperature regulation please visit [vitaprint_heat_regulator](https://github.com/symbiolab/Vitaprint_heat_regulator). This is an external temperature control system and can be replaced by any system you may have available.


