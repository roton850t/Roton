# Installation

### Firsi Time Installation

```
pkg update -y && pkg upgrade -y
pkg install python git curl wget nano openssl android-tools -y
termux-setup-storage
pip install requests faker python-dateutil pycryptodome
```
### Run Tools

```Bash
cd $HOME
rm -rf Roton
git clone --depth=1 https://github.com/roton850/Roton.git
cd Roton
git pull
python roton.py
```
