# d41274_15ja20_esp-me3-user-manual-advanced-dom_en-en.pdf

--- Page 1 ---
ESP-ME3 Controller
Advanced User Manual
LNKTM Ready

--- Page 2 ---
ESP-ME3 Controller · Advanced User Manual
EN
Contents Appendix .....................................................15
Troubleshooting .........................................................15
Technical Support .........................................................2
Error Detection .................................................................15
Introduction ..................................................3
Programming Errors (blinking LED) ..........................15
Welcome to Rain Bird® .................................................3
Electrical Errors (non-blinking LED) ..........................15
The Intelligent Use of Water® .........................................3
Flow Alarms .......................................................................16
ESP-ME3 Controller Features ......................................3 Watering Issues.................................................................16
WiFi Enabled .........................................................................3 Electrical Issues (solid LED illuminated)...................17
Installation ...................................................4 Certifications ...............................................................18
Mount Controller ..........................................................4 Safety Information .....................................................18
Connect Valves ....................................................................4
Connect Master Valve (optional) ...................................4
Connect Pump Start Relay (optional) ..........................5
Connect Flow Sensor (optional) ....................................5 Hazardous Warnings
Connect Weather Sensor (optional) .............................6
C WARNING
Connect Power ....................................................................6
Station Expansion Modules ........................................7 Indicates a hazardous situation that, if not avoided,
Install Modules ....................................................................7 could result in death or serious injury.
Station Numbering ............................................................8
C CAUTION
Complete Controller Installation ...............................8
Normal Operation ........................................8 Indicates a hazardous situation that, if not avoided,
could result in minor or moderate injury.
Controls and Features ..................................................8
AUTO .......................................................................................9
NOTICE
OFF ...........................................................................................9
Display Indicators .........................................................9 Indicates information considered important, but not
Basic Programming ....................................10 hazard-related (e.g., messages relating to property
damage).
1. Set Date and Time ..................................................10
2. Set Watering Start Times ......................................10
SAFETY INSTRUCTIONS
3. Set Station Run Times ...........................................10
Specific safety-related instructions or procedures
4. Set Water Days ........................................................10
are described.
Custom Days of the Week .............................................10
Program-Based Scheduling ......................................11 Symbols & User Operation
Common Programming Error .....................................11 a NUMBERS define a series of steps for the user to
Manual Watering Options ..........................11
follow in order to operate the controller.
Test All Stations ...........................................................11 B
NOTE: Notifies the user of important operating
Run a Single Station ...................................................11 instructions related to controller functionality,
Run a Single Program ................................................12 installation or maintenance.
Advanced Programming ............................12 H
REPEAT: Indicates that a repetition of previous
Odd or Even Calendar Days ......................................12 steps or actions may be required for further oper-
Cyclic Days ....................................................................12 ation, or to complete a process.
Seasonal Adjust ...........................................................13 Technical Support
Delay Watering ............................................................13
Questions?
Permanent Days Off ...................................................13
Call Rain Bird toll free Technical Support at
Special Features..........................................14 1-800-724-6247 (USA and Canada only)
Options .......................................................14
Reset Button ................................................................14
Remote Accessories ....................................................14
Detached Programming ............................................15
Battery Life ...................................................................15
2 ESP-ME3 Controller

--- Page 3 ---
Introduction WiFi Enabled
EN
The LNKTM WiFi Module allows remote connection to
Welcome to Rain Bird®
a Rain Bird ESP-ME3 Controller using an Apple® iOS® or
AndroidTM compatible smart device. The mobile appli-
Thank you for choosing Rain Bird’s ESP-ME3 controller.
cation allows remote access and configuration of one
In this manual are step by step instructions for how to
or more irrigation controllers.
install and operate the ESP-ME3.
* Apple is a trademark of Apple Inc, IOS is a trademark
of Cisco Systems Inc, and Android is a trademark of
Google LLC.
For more information on the LNKTM WiFi Module and
the value this product can provide for your ESP-ME3
controller, please visit: http://wifi-pro.rainbird.com
LNKTM WiFi Module
The Intelligent Use of Water® (sold separately)
We believe it is our responsibility at Rain Bird to
develop products that use water efficiently.
ESP-ME3 Controller Features
Feature Description
Maximum Stations 22 (with optional Station
Modules)
Master Valve or Pump Supported
Start Relay
Start Times 6
Programs 4
Program Cycles Custom Days, Odd, Even and
Cyclic
Permanent Days Off By program
Master Valve Control On/Off per station
Rain Delay Supported
Rain/Freeze Sensor Supported
Rain Sensor Control Global or by station
Seasonal Adjust Global or by program
Manual Watering Run Yes
Manual Program Run Yes
Manual Test All Stations Yes
Short Detect Yes
Delay Between Stations Set by program
Accessory Port Yes (5 pin)
Save & Restore Program- Yes
ming Manage Sites Remotely
Station Advance Yes
LNKTM WiFi Module Supported
Flow Sensor Supported
Cycle+SoakTM Supported in Rain Bird App
via LNKTM WiFi Module
3 ESP-ME3 Controller

--- Page 4 ---
Installation Connect Valves
EN
a Route all field wires through the opening at the
Mount Controller
bottom or back of the unit. Attach conduit if
B desired, as shown.
NOTE: Choose a suitable mounting location close
to a 120VAC wall outlet. C WARNING
a Drive a mounting screw into the wall, leaving an
Do not route valve wires through the same opening
1/8 inch gap between the screw head and the
as power wires.
wall surface (use the supplied wall anchors if
necessary), as shown. b Connect one wire from each valve to the terminal
on the Base Module or Station Module that
b Locate the keyhole slot on back of the controller
corresponds to the desired station number (1-22).
unit and hang it securely on the mounting screw.
c Connect a field common wire to the COM
a b
(common)terminal on the Base Module. Then
connect the remaining wire from each valve to
1/8 IN.
the field common wire, as shown.
d To perform a Valve Test, connect the common wire
to the COM terminal and the power wire to the VT
terminal. This will immediately turn the valve ON.
Connect Master Valve (optional)
e Connect a wire from the master valve to the MV
(master valve) terminal on the Base Module.
Then connect the remaining wire from the master
c Open the front panel, and drive three additional
valve to the field common wire, as shown.
screws through the open holes inside the
controller and into the wall, as shown.
e c
c b
a
22
11
SSEENNSS
MMVV
MASTER
VALVE
CCOOMM
4 ESP-ME3 Controller

--- Page 5 ---
Connect Pump Start Relay (optional) Connect Flow Sensor (optional)
EN
B
a Connect a wire from the PSR (pump start relay) NOTE: Install the flow sensor in the field accord-
to the MV (master valve) terminal on the Base ing to the manufacturer’s instructions.
Module. Then connect another wire from the a Run the flow sensor wires to the controller.
pump start relay to the field common wire, as
shown. C WARNING
b To avoid the possibility of damage to the pump, Do not route valve wires through the same open-
connect a short jumper wire from any unused ing as power wires.
terminal(s) to the nearest terminal in use, as
b Connect both flow sensor wires to the Flow
shown.
terminals, as shown. Be sure to connect the
NOTICE positive (sometimes red) sensor wire to the
red (+) terminal and the negative (sometimes
The ESP-ME3 controller DOES NOT provide power for
black) sensor wire to the grey (-) terminal.
a pump. The relay must be wired according to manu-
facturer instructions.
Only the following Rain Bird pump start relay models
are compatible with the ESP-ME3:
Description Note Model
No.
Universal Pump Relay 110 volt PSR110IC b
only
Universal Pump Relay 220 volt PSR220IC
only
B a
NOTE: Connection to
pump and external Flow Sensor Settings
power not shown.
Set the controller to obey or ignore a flow sensor.
Refer to pump instal-
lation instructions. When set to Sensor ON, automatic irrigation will
be suspended per station if detected flow exceeds
learned flow by more than 30%. When set to Sensor
OFF, all stations will ignore the flow sensor.
b
Turn the dial to Flow Sensor.
• Press or to select SENS ON (sensor on) or SENS
OFF (sensor off).
Sensor ON Sensor OFF Flow detected
(flashing)
22
B
NOTE: When switching from Sensor OFF to Sen-
11
sor ON, the controller will begin to LEARN FLOW.
PPSSRR It will run each station for short period to set the
expected station flow.
PUMP START
B
RELAY NOTE: See Troubleshooting section of the Appen-
dix for Flow Alarms information.
CCOOMM
5 ESP-ME3 Controller

--- Page 6 ---
Connect Weather Sensor (optional) Connect Power
EN
a Remove the yellow jumper wire from the SENSOR C WARNING
terminals on the controller.
DO NOT plug in the transformer or connect external
NOTICE power until you have completed and checked all
wiring connections.
Do not remove the yellow jumper wire unless con-
necting a rain sensor.
Installation with Pre-attached Cord
b Connect both rain sensor wires to the SENSOR
• Plug the attached power cord into a nearby 120VAC
terminals as shown.
electrical outlet.
C WARNING
Do not route the rain sensor wires through the same
opening as the power wiring
B
NOTE: Rain Bird ESP-ME3 controllers are only
compatible with normally closed rain sensors.
B
NOTE: For wireless rain/freeze sensors, refer to
the sensor installation instructions.
b
Weather Sensor Settings
Set the controller to obey or ignore a weather sensor.
When set to Sensor ON, automatic irrigation will be
suspended if rainfall is detected. When set to Sensor
OFF all stations will ignore the rain sensor.
Turn the dial to Weather Sensors.
• Press or to select SENS ON (sensor on) or SENS
OFF (sensor off).
Sensor ON Sensor OFF Rain detected
(flashing)
6 ESP-ME3 Controller

--- Page 7 ---
Outdoor Installation with Direct Wiring Station Expansion Modules
EN
C WARNING Optional Station Modules can be installed in the empty
slots to the right of the Base Module to increase the
Electric shock can cause severe injury or death. Make
station capacity up to 22 stations.
sure power supply is turned OFF before connecting
B
NOTE: 6-Station Modules are compatible with
power wires.
ESP-ME3 and ESP-Me. They are not backwards
compatible with the ESP-M vintage controller.
POWER WIRING CONNECTIONS 120VAC
B
NOTE: For ideal station sequencing, insert 3-Sta-
Black supply wire (hot) to the black transformer wire
tion module after inserting all 6-station modules.
White supply wire (neutral) to the white transformer For more details see the Station Numbering sec-
wire tion.
Green supply wire (ground) to the green transformer Base Module Expansion Modules
wire (included) (sold separately)
a Locate the transformer wiring compartment in
the lower left corner of the controller unit. Use a
screwdriver to remove the cover and expose the
transformer connection wires.
b Route the three external power source wires
through the conduit opening at the bottom of
the unit and into the wiring compartment.
3-STATION
c Using the provided wire nuts, connect the
(ESPSM3) 6-STATION
external power source wires (two power and one
(ESPSM6)
ground) to the transformer connection wires
inside the wiring compartment.
Install Modules
C WARNING a Verify the securing lever on the module is in the
Ground wire must be connected to provide electrical unlocked position (slide to the left).
surge protection. Permanently mounted conduit b Place the module under the desired slot between
shall be used for connecting main voltage to the the plastic rails.
controller c Push the module up into the slot until secure.
d Verify that all wiring connections are secure, d Slide the securing lever to the locked position
then replace the wiring compartment cover and (slide to the right).
secure it with the screw.
c
bcd
a
a
H
REPEAT for additional modules.
b B
NOTE: Modules can be installed or removed with
OR without AC power connected. They are con-
sidered “hot-swappable”.
B
NOTE: It take about 30 seconds for stations to
become available for configuration after install-
ing a new module.
7 ESP-ME3 Controller

--- Page 8 ---
Station Numbering • A 3-Station Module is installed in Bay Three and
EN
uses stations 11 through 13.
The controller is configured with “fixed station num-
bering”, meaning that Bays Two, Three and Four can During programming, the controller will skip any
accept either a 3 or a 6-Station Module. If a 6-Station unused stations, creating a gap in station numbering.
Module is NOT installed then the unused stations are The unused stations will show on the display as 8SKIP,
reserved for future use. 9SKIP, etc.
Example of Station Numbering when using two
3-Station Modules. A total of 10 stations are installed.
Bay One Bay Two Bay Three Bay Four
If the screen displays 20NOMOD where the 20 is flash-
ing, then there is no module installed for that station
number.
Complete Controller Installation
a Reinstall and reconnect the front panel.
b Apply power to the controller and test the system.
B
NOTE: The electrical connections can be checked
• The Base Module is installed in Bay One and uses
even if water is not available. If water is available
Stations 1 through 4.
and you would like to test some or all of your
• A 3-Station Module is installed in Bay Two and stations, use the Test All Stations feature of the
uses stations 5 through 7. Stations 8 through 10 are controller.
skipped and will be unavailable.
Normal Operation
Controls and Features
Start Times Program
AUTO Date/Time Up to 6 Start Select Button
Watering occurs Set the current Times per Select Program
automatically Date and Time program A, B, C or D
OFF
Disables automatic
ALARM
irrigation
Indicator
Manual Watering
Start watering for
one or all stations
Hold to Start
Manual
irrigation
Flow Sensor
Set the controller to
obey or ignore
a flow sensor
Seasonal Adjust
Adjust Run Times
from 5% up to 200% Back/Next – / + Buttons
Weather Sensors Water Days Run Times Buttons Adjust feature
Set controller to Select days to Set station Select settings
obey or ignore a allow watering Run Times programming
weather sensor options
8 ESP-ME3 Controller

--- Page 9 ---
Display Indicators
EN
AUTO
Display Func- Description
tion
AUTO is the normal operating mode. Return the dial to
AUTO when programming is complete. ALL ALL All stations
During Watering: CLEARED CLEARED Programming was
cleared
The display shows a blinking sprinkler symbol, the
active Station Number or Program, and the Remaining Watering occurs at
Run Time. CYCLIC CYCLIC specific intervals, such
as every 2 days
DELAY DELAY Delay Watering Active
EVEN EVEN Even days watering
FLOW FLOW Flow Sensor
Master or Pump-start
MV ON MV ON
relay is active
• To cancel watering, turn the dial to OFF for three NOMOD NOMOD No station modules
seconds until the screen shows OFF. installed for that station
To Manually Start a Program: ODD ODD Odd days watering
a Press the Program Select button to select a OFF OFF Controller will not
water
program.
Permanent days off
b Press and hold the Hold to Start button to
PERMOFF PERMOFF for Odd, Even, Cyclic
immediately start manual watering for the
watering
selected program.
RAIN RAIN Rain Sensor
RESTORD RESTORD Programming restored
SAVED SAVED Save programming
Sensor will function if
SENS ON SENS ON
wired
Sensor is ignored even
SEN OFF SEN OFF
if wired
Station not used due to
SKIP SKIP station module config-
uration
Soak time between wa-
tering times - support-
OFF SOAK SOAK
ed through the Rain
Bird app.
Turn the dial to OFF to stop automatic irrigation or to
cancel all active watering immediately.
NOTICE
Watering will NOT occur if the controller remains in
the OFF position.
B
NOTE: Manual watering can be started using
mobile apps or LIMR when dial is in OFF position.
9 ESP-ME3 Controller

--- Page 10 ---
Basic Programming 4. Set Water Days
EN
Custom Days of the Week
1. Set Date and Time
Set watering to occur on specific days of the week.
Turn the dial to Date / Time
Turn the dial to Water Days
a Press or to select the setting to change.
a Press Program Select to choose the desired
b Press or to change the setting value.
Program (if necessary).
c Press and hold or to accelerate adjustments. b Press or to set the selected (blinking) day as
To change the time format (12 hour or 24 hour): either ON or OFF, and to automatically move to
d With Day of Month blinking, press . the next day.
e Press or to select the desired time format, c Press or at any time to move the cursor to the
previous or next day.
then press to return to the time setting.
B
NOTE: With Sunday selected, press the button
2. Set Watering Start Times
to enter and activate Cyclic Watering (see the
Up to six Start Times are available for each program. Advanced Programming section). If this is not
desired, press the button to return to watering
Turn the dial to Start Times by Custom Days.
a Press Program Select to choose the desired
Program (if necessary).
b Press or to select an available Start Time.
c Press or to set the selected Start Time
(ensure the AM/PM setting is correct).
d Press to set additional Start Times.
e To turn off a start time press until 12:00 AM
(00:00 in 24 HR), then press one more time for
OFF.
B
NOTE: The OFF Position for any start time is
between 11:45 PM and 12:00 AM.
3. Set Station Run Times
Run Times can be set from one minute up to six hours.
Turn the dial to Run Times
a Press Program Select to choose the desired
Program (if necessary).
b Press or to select a Station.
c Press or to set the Run Time for the selected
Station.
d Press to set additional Station Run Times.
B
NOTE: Only assign Run Times in a Program for
stations you want to water. If you do not want a
specific station to run in a selected program then
set the Run Time to zero.
B
NOTE: Rain Bird recommends that the maximum
irrigation station cycle time be less than the time
required for runoff to begin and that there be
adequate soak time before the next irrigation
cycle of that same station begins again.
10 ESP-ME3 Controller

--- Page 11 ---
Program-Based Scheduling Manual Watering Options
EN
The ESP-ME3 uses a programmed-based scheduling
Test All Stations
method to create irrigation schedules. This means all
stations with a run time on the program will run in Start watering immediately for all programmed
numerical order. stations.
Common Programming Error Turn the dial to Manual Watering
The most common programming error for any pro-
a Press or to set a Run Time.
gram-based controller is to set multiple Program Start
Times that cause watering cycles to repeat. b Press the Hold to Start button.
c Turn the dial to AUTO after display shows
As an example: Program A has a 1st Start Time set to
STARTED.
run at 8:00 AM. But then a 2nd Start Time has mistak-
enly been set for 8:15 AM, which means that all sta- During Testing:
tions would water a 2nd time. The display shows a blinking sprinkler symbol, the
active Station Number and the remaining Run Time.
In this example, a 3rd Start Time has mistakenly been
set for 8:30 AM. Which means all stations would water
a 3rd time. The desired watering time was 45 minutes,
or 15 minutes per station. The actual is 2 hours and 15
minutes, which is excessive watering!
Incorrect: Multiple Start Times set by mistake
Program Station
Program Program Station
Watering Watering d To cancel the test, turn the dial to OFF for three
Letter Start Time Number
Time Duration
seconds until the screen shows OFF.
1 15 MIN
A 1st 8:00 AM 2 15 MIN Run a Single Station
3 15 MIN
1 15 MIN Start watering a single station, or set multiple stations
A 2nd 8:15 AM 2 15 MIN to water in order.
3 15 MIN
1 15 MIN
Turn the dial to Manual Watering
A 3rd 8:30 AM 2 15 MIN
3 15 MIN
a Press or to select the desired station.
b Press – or + to set a Run Time.
Correct: Only one Start Time
c Press the Hold to Start button.
Program Program Program Station Station d Irrigation will begin and STARTED will appear on
Watering Watering
Letter Start Time Number the display.
Time Duration
1 15 MIN e Turn the dial back to AUTO
A 1st 8:00 AM 2 3 1 1 5 5 M M I I N N H REPEAT process as desired to add more stations
4 15 MIN to the queue. When one station finishes watering
then the next station will start.
B
NOTE: Manual Watering (Test All, Run Single Sta-
tion and Manual Program) will start even when a
weather sensor is set to SENS ON (sensor on).
11 ESP-ME3 Controller

--- Page 12 ---
Run a Single Program Advanced Programming
EN
Start watering immediately for one program.
Odd or Even Calendar Days
Turn the dial to AUTO.
Set watering to occur on all ODD or EVEN calendar days.
a Press Program Select to choose the desired Turn the dial to Water Days
Program (if necessary).
b Press the Hold to Start button to begin a Press Program Select to choose the desired
watering the selected Program. Program (if necessary).
c Irrigation will begin and STARTED will appear on b Press and hold and until ODD or EVEN is
the display. displayed.
d Press the Advance Station button to advance Cyclic Days
to the next station if desired.
Set watering to occur at specific intervals, such as
e NOTE: A maximum of 88 stations can be queued
every 2 days, or every 3 days, etc.
across all four programs.
During Manual Watering (Single-station or Single-program): Turn the dial to Water Days
The display shows a blinking sprinkler symbol, the
a Press Program Select to choose the desired
active Station Number, and the remaining Run Time.
Program (if necessary).
b On the Custom Days of the Week screen, press
until the Cyclic screen is displayed (after SUN).
c Press or to set the desired DAY CYCLE, then
press .
d Press or to set the DAYS REMAINING before
the cycle begins. The NEXT watering day updates
• To cancel manual watering, turn the dial to OFF for
on the display to indicate the day that watering
three seconds until the screen shows OFF.
will start as shown.
To add additional programs to the manual watering queue:
Turn the dial to Manual Watering
a Press and hold Program Select to show program
letter on the display.
b Press Program Select to choose the desired
program (if necessary).
c Press the Hold to Start button to begin watering
the selected program. B NOTE: See Special Features to set Rain Sensor
d Turn the dial to AUTO ON by Station.
12 ESP-ME3 Controller

--- Page 13 ---
Seasonal Adjust Permanent Days Off
EN
Increase or decrease program run times by a selected Prevent watering on selected days of the week (for
percentage (5% to 200%). Odd, Even or Cyclic programming only).
As an example: If the Seasonal Adjust is set to 100%
Turn the dial to Water Days
and the station Run Time is programmed for 10 min-
utes, the station will run for 10 minutes. If the Seasonal
a Press Program Select to choose the desired
Adjust is set to 50%, the station will run for 5 minutes.
Program (if necessary).
b Press and hold Program Select, then press to
Turn the dial to Seasonal Adjust.
set the selected (blinking) day as a Permanent
Day Off or press to leave the day ON.
a Press or to increase or decrease Seasonal
Adjust for all Programs.
b To adjust an individual Program, press Program
Select to choose the desired Program (if
necessary). Press or to increase or decrease
Seasonal Adjust for all Programs.
Delay Watering
Suspend watering for up to 14 days.
Turn the dial to AUTO.
a Press and Hold the button to enter the Rain
Delay screen.
b Press or to set the DAYS REMAINING. The
NEXT watering day will update on the display to
indicate when watering will resume.
c To cancel a Rain Delay, set the DAYS REMAINING
back to 0.
B
NOTE: When the delay expires, automatic irriga-
tion resumes as scheduled.
13 ESP-ME3 Controller

--- Page 14 ---
Special Features
EN
a Turn the dial to the desired position indicated
Save Restore
below for each Special Feature.
Programming Programming
b Press and hold and at the same time.
Set Interstation Delay
by Program
A station delay (from 1
second to 9 hours) ensures
that a valve has completely
closed before the next one
opens. Press Program Select
to set delay for different
programs.
Set Flow Sensor by Station
Turns a flow sensor on or
off by station
Reset to Factory Defaults
Set Master Valve
All programmed schedules
will be erased. Set Rain Sensor by Set to Odd or Even by Station
Station Watering Days Allows a station to be
Tells a station to obey or controlled by a master
ignore a rain sensor. valve or pump start relay.
Options Remote Accessories
A 5 pin accessory port is available for Rain Bird
Reset Button
approved external devices, including:
If the controller is not working properly, you can try • LNKTM WiFi Module
pressing RESET.
• LIMR Receiver Quick Connect harness
• Insert a small tool such as a paper clip, into the
PORT
access hole and press until the controller is reset.
All previously programmed watering schedules will
remain stored in memory.
RESET
14 ESP-ME3 Controller

--- Page 15 ---
Detached Programming Appendix
EN
Program the front panel remotely on battery power.
Troubleshooting
The front panel can be removed from the controller
and programmed remotely using a 9 volt battery for Error Detection
power. Settings can be programmed for all 22 stations
The ESP-ME3 controller has built-in error detection
regardless of which Station Modules are installed in
that can automatically generate an ALARM caused by
the controller.
an essential programming error or if an electrical short
a Remove the front panel. condition is detected.
b Install a 9V battery in the battery compartment. The ALARM LED light on the ESP-ME3 controller front
c Program the controller. panel will light up to indicate an alarm condition:
Programming Errors (blinking LED)
Error Mes-
ALARM
Error sage On
LED
Display
No Start Times are set BLINK NO START TIMES
No Run Times are set BLINK NO RUN TIMES
No Water Days are set BLINK NO WATER DAYS
B
NOTE: Program information is stored in nonvol-
atile memory so it is never lost if the front panel The error will go away when the station is successfully
loses power. run after condition is corrected.
B
d Replace the front panel (refer to Complete NOTE: The dial must be in the AUTO position for
Installation in the Installation section). an ALARM message to appear on the display.
B
NOTE: After the front panel is re-installed, any Electrical Errors (non-blinking LED)
station that does not have a corresponding Sta-
tion Module installed will function as though the ALARM Error Message
Error
run time is zero. LED On Display
Battery Life Master Valve SOLID MASTER VALVE SHORTED
short OR HIGH CURRENT
If the display repeatedly shows “-- -- -- -- --”, or there
is no display when using a 9V battery for remote pro- Station short SOLID STATION “X” WIRE SHORT-
gramming, replace the battery. ED
When an electrical error is detected, irrigation for the
affected station is cancelled and watering advances to
the next operable station in the program.
The controller will attempt to water the affected sta-
tion again at the next scheduled watering. Completion
of a successful watering will clear the error condition
associated with that station.
15 ESP-ME3 Controller

--- Page 16 ---
Flow Alarms Low Flow conditions are also monitored. The limit
EN
for Low Flow is 70% below the learned flow unless
ALARM Error Message
Error changed in the Rain Bird App. A Low Flow alarm is
LED On Display shown at the controller display and the red alarm LED
Flow Sensor - Solid HIGH FLOW ALARM STA- comes on.
High Flow Con- TION "X"
To clear the alarm press the “Hold to Start” right arrow
dition
button during the alarm message.
Flow Sensor - Solid LOW FLOW ALARM STA- B
NOTE: Turning the flow sensor feature off and
Low Flow Con- TION "X"
then back on will cause the controller to learn
dition
new flow levels and ignore previous error condi-
When a flow sensor is in use the ESP-ME3 monitors for tions.
B
High Flow of 130% above regular learned flow. This NOTE: If the flow sensor measures flow when the
percent limit can be adjusted in the Rain Bird App controller is not scheduled for watering, a “HIGH
when used with LNKTM WiFi Module. If a High Flow con- FLOW ZONE” alarm is shown on the display and
dition is detected, a “High Flow Alarm” is shown at the the red alarm LED comes on. To clear the alarm
display and the red alarm LED comes on. To clear the press the “Hold to Start” right arrow button dur-
alarm press the “Hold to Start” right arrow button dur- ing the alarm message.
ing the alarm message.
Watering Issues
Problem Possible Cause Possible Solution
Display shows a Water source not supplying water. Verify there is no disruption to the main water line and
program is active, but that all other water supply lines are open and functioning
system isn’t watering. properly.
Wiring is loose or not properly connect- Check that field wiring and master valve or pump start
ed. relay wiring is securely connected at the controller and in
the field.
Field wires are corroded or damaged. Check field wiring for damage and replace if necessary.
Check wiring connections and replace with watertight
splice connectors if needed.
Loss of AC power. When there is a power loss and a 9 volt battery is in-
stalled, the system does not irrigate but programs show
as remaining active.
NO AC message on No Power detected. Check circuit breaker and that unit is plugged into socket
display. or properly connected to power source.
Controller may be plugged into a GFCI Check power to the outlet or reset the circuit breaker.
outlet or an outlet that is wired to a GFCI
outlet.
It just rained and This is normal operation. The ESP-ME3 This is normal operation.
the alarm light is not does not consider the interruption of
illuminated, why? irrigation due to rainfall as an alarm
condition.
16 ESP-ME3 Controller

--- Page 17 ---
Watering Issues
EN
Problem Possible Cause Possible Solution
Programmed sched- Connected rain sensor may be activat- Set Rain Sensor to Sensor OFF to ignore the rain sensor.
ules do not start. ed. If watering resumes, the sensor is operating properly and
no further correction is needed.
Connected rain sensor may not be oper- Let the rain sensor dry out, or disconnect it from the
ating properly. controller terminal strip and replace it with a jumper wire
connecting the two SENS terminals, or set to Sensor OFF.
If no rain sensor is connected, the Move dial position to Weather Sensors and set to Sensor
jumper wire connecting the two SENS OFF.
terminals on the terminal strip may be
missing or damaged.
Too much irrigation Multiple Start Times in the same pro- Separate start times are not required for each valve. A
gram. program only requires single start time in order to run all
stations in that program.
Multiple programs are running at the Review programming to assure that the same Station is
same time. not active in multiple Programs.
Valve is malfunctioning. Check to see if the ALARM light on the controller is lit
solid, then repair or replace the valve if necessary.
Seasonal Adjust setting is too high. Set Seasonal Adjust to 100%.
Electrical Issues (solid LED illuminated)
Problem Possible Cause Possible Solution
Display is blank or fro- Power not reaching the Verify the main AC power supply is securely plugged in or connect-
zen, the controller will controller. ed and working properly.
not accept program-
ming or is operating
Controller needs to be reset. Press the Reset Button. For details see “Reset Button” section.
abnormally.
An electrical surge may have Unplug the controller for 2 minutes, then plug it back in. If there is
interfered with the control- no permanent damage, the controller should accept programming
ler’s electronics. and resume normal operation.
Automatic error detec- Short circuit or overload Identify and repair the fault in the wiring. Refer to compatible
tion indicates a problem condition in valve, master pump start relays. For details see “Connect Pump Start Relay”
by ALARM LED and valve or pump start relay section.
an error message on wiring.
display.
LED is flashing or solidly Dial not in AUTO RUN Turn dial to AUTO RUN position. Push Reset button or power cycle
illuminated but I see no position. the controller.
message on the LCD.
17 ESP-ME3 Controller

--- Page 18 ---
Certifications Safety Information
EN
Supplier’s Declaration of Conformity C WARNING C CAUTION
47 CFR § 2.1077 Compliance Information
Special precautions must be taken Stationary appliances not fitted
Unique Identifier: ESP-ME3 (ESP4ME3) when valve wires (also known as with means for disconnection from
Responsible Party – U.S. Contact station or solenoid wires) are locat- the supply mains having a contact
Information ed adjacent to, or share a conduit separation in all poles that provide
with other wires, such as those full disconnection under overvolt-
Rain Bird Corporation
used for landscape lighting, other age category III, the instructions
9491 Ridgehaven Court
“low voltage” systems or other state that means for disconnection
San Diego, CA
“high voltage” power. must be incorporated in the fixed
92123
Separate and insulate all conduc- wiring in accordance with the
Ph. (858) 268-2650
tors carefully, taking care not to wiring rules
FCC Compliance Statement damage wire insulation during This appliance can be used by chil-
This device complies with Part 15 of the FCC installation. An electrical “short” dren aged from 8 years and above
Rules. Operation is subject to the following two (contact) between the valve wires and persons with reduced physical,
conditions: (1) This device may not cause harm- and another power source can sensory or mental capabilities or
ful interference, and (2) this device must accept damage the controller and create a lack of experience and knowledge
any interference received, including interfer- fire hazard. if they have been given supervision
ence that may cause undesired operation. All electrical connections and wiring or instruction concerning use of
Note: This equipment has been tested and runs must comply with local build- the appliance in a safe way and
found to comply with the limits for a Class B dig- ing codes. Some local codes require understand the hazards involved.
ital device, pursuant to part 15 of the FCC Rules. that only a licensed or certified Children shall not play with the
These limits are designed to provide reasonable electrician can install power. Only appliance. Cleaning and user
protection against harmful interference in a res- professional personnel should in- maintenance shall not be made by
idential installation. This equipment generates, stall the controller. Check your local children without supervision.
uses and can radiate radio frequency energy building codes for guidance. For controllers not provided
and, if not installed and used in accordance with Outdoor controller shall be with supply cord, the fixed
the instructions, may cause harmful interfer- permanently connected to fixed installation must include a dis-
ence to radio communications. However, there wiring by a flexible cord, and connecting device for all three
is no guarantee that interference will not occur have a cord anchorage. The cord poles suitable for overvoltage
in a particular installation. If this equipment anchorage shall relieve conductors category III protection.
does cause harmful interference to radio or from strain, including twisting,
television reception, which can be determined at the terminals and protect the NOTICE
by turning the equipment off and on, the user is insulation of the conductors from
Use only Rain Bird approved
encouraged to try to correct the interference by abrasion.
accessory devices. Unapproved
one or more of the following measures:
devices may damage the controller
• Reorient or relocate the receiving antenna.
and void the warranty. For a list of
• Increase the separation between the equip- compatible devices go to: www.
ment and receiver. rainbird.com
• Connect the equipment into an outlet on a Changes or modifications not ex-
circuit different from that to which the receiver pressly approved by Rain Bird could
is connected. void the user’s authority to operate
• Consult the dealer or an experienced radio/TV the equipment.
technician for help. Date and time are retained by a
• Changes or modifications not expressly lithium battery which must be
approved by Rain Bird could void the user’s disposed of in accordance with local
authority to operate the equipment. regulations.
ICES-003 Compliance Label/Étiquette de
conformité à la NMB-003
CAN ICES-3(B)/NMB-3(B)
18 ESP-ME3 Controller

--- Page 19 ---
The Intelligent Use of Water®
LEADERSHIP · EDUCATION · PARTNERSHIPS · PRODUCTS
At Rain Bird, we believe it is our responsibility to develop
products and technologies that use water efficiently. Our
commitment also extends to education, training and
services for our industry and community.
The need to conserve water has never been greater.
We want to do even more and with your help we can.
Visit www.rainbird.com for more information about The
Intelligent Use of Water®.
Rain Bird Corporation Rain Bird Corporation Rain Bird International
6991 East Southpoint Road 970 W. Sierra Madre Ave. 1000 W. Sierra Madre Ave.
Tucson, AZ 85756 Azusa, CA 91702 Azusa, CA 91702
USA USA USA
Tel: (520) 741-6100 Tel: (626) 812-3400 Tel: +1 (626) 963-9311
Rain Bird Turkey Rain Bird Europe SNC Rain Bird Deutschland GmbH
Çamlık Mh. Dinç Sokak Sk. No.4 D:59-60 Rain Bird France SNC Königstraße 10c
34760 Ümraniye, İstanbul 240 rue René Descartes 70173 Stuttgart
TÜRKIYE Bâtiment A, parc Le Clamar DEUTSCHLAND
Tel: (90) 216 443 75 23 BP 40072 Tel: +49 (0) 711 222 54 158
rbt@rainbird.eu 13792 AIX-EN-PROVENCE CEDEX 3 rbd@rainbird.eu
www.rainbird.com.tr FRANCE
Tel: (33) 4 42 24 44 61
rbe@rainbird.eu · www.rainbird.eu Rain Bird Brasil Ltda.
Rain Bird Ibérica S.A. rbf@rainbird.eu · www.rainbird.fr Rua Marques Póvoa, 215
C/ Valentín Beato, 22 2ª Izq. fdo Bairro Osvaldo Rezende
28037 Madrid Uberlândia, MG, Brasil
ESPAÑA Rain Bird Australia Pty Ltd. CEP 38.400-438
Tel: (34) 91 632 48 10 Unit 13, Level1 Tel: 55 (34) 3221-8210
rbib@rainbird.eu · www.rainbird.es 85 Mt Derrimut Road www.rainbird.com.br
portugal@rainbird.eu PO Box 183
www.rainbird.pt Deer Park, VIC 3023
Tel: 1800 724 624
info@.rainbird.com.au
www.rainbird.com/au
Technical Services for
U.S. and Canada only:
1 (800) RAINBIRD
1-800-247-3782
www.rainbird.com
) Registered trademark of Rain Bird Corporation
( 2020 Rain Bird Corporation D41274 15JA20