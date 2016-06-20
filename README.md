# free-parrot

#### FUNCTIONAL DESCRIPTION:
Software PoC that scans for parrot drones' networks, connect to them, hijack all the connected hosts and pilot the drone away from the "local" position (keep them far) 
<br/>
The _pilot.py_ file contains the routine that pilot the drone, using [this] (https://github.com/venthur/python-ardrone) python library. The **routine** if fully customizable.<br/>
The basic behavior is that the pilot tries to fly the parrot away by using a simple _robot algorithm_ that moves it in a direction and then checks if it is more far or more near with the wifi's signal strength and then decide the next move based on the result of the new signal strength.

#### REQUIREMENTS:
This program runs on the **python** interpreter.<br/>
This program uses _arpspoof_ and _nmap_ to find and hijack the hosts connected to the victim parrot.
To install the packets on a Debian based system, type as **root**:<br/>```apt-get install nmap dsniff```
<br/>
To use this program you actually need 2 **NICs** (Network Interface Card). One is used as _controller_ for the parrot; the other is used to _scan_ for wifi networks (and update RSSI values)<br/><br/>
This software has been developed on a Debian system and it requires _iwconfig_, _iwlist_, _dhclient_, _grep_ to effectively work.

#### CONFIGURATION:
Configure the **gloval_vars.py** file with your Network Intefaces (if you have a NIC that is more accurate than another, put it as secondary so it will be used for scanning; improving RSSI sampled values)
<br/>
Same file contains other parameters to tweak; like _power_threshold_, after which the drone is taken over the control of the owner.
<br/>
**VERY IMPORTANT:** If your _secondary_net_interface_ (as configured in global_vars.py) through iwlist return "Signal level" value in negative *dbm* it's ok.<br/>
If it returns a *fraction base 100*, you need to apply the 2 patches in the root directory.<br/>
```patch net.py net.patch```<br/>
```patch pilot.py pilot.patch```<br/><br/>
To test if your network card is affected, type: ```iwlist $secondary_net_interface scan | grep "Signal level"```

#### RUN:
```python main.py```<br/>
It crashes on parsing incomplete results from _iwlist_ (it happened)<br/>
Trivial way to fix with a bash script, assuming you've only one instance of _python_ running:<br/>
```while [ 1=1 ]; do if [[ $(pgrep python) = "" ]]; then python main.py \&; fi; sleep 1; done```


<br/><br/>
#####ENJOY!!
