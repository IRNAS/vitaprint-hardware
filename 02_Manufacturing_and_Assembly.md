# Manufacturing and Assembly

## Table of contents
 - [Overview](#OVER)
 - [Part Manufacturing](#MANUFACTURING)
 - [Assembly Brief](#ASSEMBLY)
 - [Arduino Temperature Regulation](#CODE)
 

## 1 Overview and Toolset <a id="OVER"></a>
Here you can find manufacturing and assembly details for one Vitaprint unit. In this repository you can find STEP files for the Vitaprint unit in both orientations - Left and Right. The procedure is the same for both orientations (the final product is only mirrored) therefore you will find details for assembly for one unit in this repository. 

### 1.1 General
- Manufacturing time: X min
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
 | DESCRIPTION | 
 |------|-------|-------|
 |Collect all parts and tools|<img src="https://cloud.githubusercontent.com/assets/14543226/25372744/edc79336-2996-11e7-8249-ebf960823e0e.jpg" alt="tools_parts" width= "150" >|
 | SECTION A |
 |Take Nema11 motor plate and Nema11 stepper motor and fix them together with four torx screws|<img src="https://cloud.githubusercontent.com/assets/14543226/25372981/177bbb2a-2998-11e7-8505-06f3d0da0ced.jpg" alt="step1a" width= "150" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25372926/d43add28-2997-11e7-8887-940e12599bcf.jpg" alt="step1b" width= "150" >|
 |Take the nut and nut plate and fix them together with two philips screws|<img src="https://cloud.githubusercontent.com/assets/14543226/25373052/586397b6-2998-11e7-80ab-f0d0bd8c4928.jpg" alt="step2a" width= "150" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25373068/663aa6c2-2998-11e7-84b6-38fa4631825c.jpg" alt="step2b" width= "150" >|
 |Take the threaded rod and join it with a coupler. The fit is designed to be tight.|<img src="https://cloud.githubusercontent.com/assets/14543226/25373374/b5b481ae-2999-11e7-8280-a12f8cc03a00.jpg" alt="step3a" width= "150" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25373386/c3dd8ed8-2999-11e7-8a1a-d0fb3adfce9e.jpg" alt="step3b" width= "150" >|
 |Screw the rod with a coupler through the nut M5 center thread. Slide the fi3 rods through the holes. |<img src="https://cloud.githubusercontent.com/assets/14543226/25376284/e063de72-29a3-11e7-94f8-825f228a2164.jpg" alt="step4a" width= "150" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25376309/f4293236-29a3-11e7-832d-61b2ab6464e1.jpg" alt="step4b" width= "150" >|
  |Merge the N11 motor section and the nut-rod section.|<img src="https://cloud.githubusercontent.com/assets/14543226/25376379/37758f6c-29a4-11e7-9715-d70013bed612.jpg" alt="step5a" width= "150" >|<img src="https://cloud.githubusercontent.com/assets/14543226/25376392/4990475a-29a4-11e7-90a8-45d486ae110b.jpg" alt="step5b" width= "150" >|


## 4 Arduino: Temperature Regulation <a id="CODE"></a>


To download Arduino firmware for temperature regulation please visit [vitaprint_heat_regulator](https://github.com/symbiolab/Vitaprint_heat_regulator). This is an external temperature control system and can be replaced by any system you may have available.


