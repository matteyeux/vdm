# VDM Escape Game

### Archi

<img src="http://collab-mha.nexen.net/vdm_archi.png">

## Virtual Environment

### Dependencies
Ubuntu :
- install `python3-virtualenv` : `sudo apt install python3-virtualenv`

Debian :
- install `python3-pip3` : `sudo apt install python3-pip`
- install `virtualenv`with easy_instal : `sudo easy_install3 virtualenv`

### Setup
In the root directory of the projet create the new env : `virtualenv -p python3 env`. It will create a new directory named `env` with all you need to start coding.

Enable virtual env : `source env/bin/activate`

Install Python modules : `pip3 install -r requirements.txt`
