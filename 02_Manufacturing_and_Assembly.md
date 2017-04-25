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
   - two-sided tape
   - scalpel
 
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
   - sliding the ball bearing into the rod holder
   - sliding the M5 threaded rod into the coupler
   - sliding the fi3 stainless steel rod into rod holder at the bottom and N11 motor plate at the top

### 3.2 Assembly Details
    |STEP | PHOTO |
    |------|-------|
    |Collect all parts and tools|<img src="https://www.dropbox.com/sh/y9rqggxodcu15ix/AAA8zSpMS3V4_AwSmWENSvsla?dl=0&preview=DSC_0185.jpg" alt="sectionB" width= "150" >|


## 4 Arduino: Temperature Regulation <a id="CODE"></a>
To download Arduino firmware for temperature regulation please visit [vitaprint_heat_regulator](https://github.com/symbiolab/Vitaprint_heat_regulator). This is an external temperature control system and can be replaced by any system you may have available.


