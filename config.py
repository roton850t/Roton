# config.py - All editable strings, colors, paths, and UI texts for rotonfb.py
# Colors (ANSI escape codes) - Easily change colors here

WHITE = "\033[1;97m"
GREEN = "\033[1;92m"
RED = "\033[1;91m"
DARK_GREEN = "\033[1;32m"
LIGHT_GRAY = "\033[1;37m"
CYAN = "\033[1;96m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
MAGENTA = "\033[1;95m"
ORANGE = "\x1b[38;5;208m"

# Global Labels and Separators
OPT_LABELS = [f"{GREEN}[{RED}{str(i).zfill(2)}{GREEN}]" for i in range(1, 8)]
L0 = f"{GREEN}[{RED}00{GREEN}]"
EKL = f"{CYAN}:{WHITE}"  # Separator like ":"
LINE = f"{CYAN}•{'━'*47}•"  # Separator line

# File Paths (Change folder or file names here)
SXR_FOLDER_NAME = "FB-CREATE"  # Folder name
OK_FILE_NAME = "SxR-OK.txt"    # OK accounts file
ER_FILE_NAME = "SxR-ER.txt"    # Error accounts file

# Logo and Header Texts (Change the entire look here)
LOGO_TEXT = f"""{GREEN}
      .d8888.  db    db  d8888b. 
      88'  YP  `8b  d8'  88  `8D 
      `8bo.     `8bd8'   88oobY' 
        `Y8b.   .dPYb.   88`8b   
      db   8D  .8P  Y8.  88 `88. 
      `8888Y'  YP    YP  88   YD   {ORANGE}V-02
{LINE}
 {GREEN}[{RED}●{GREEN}] OWNER        {CYAN}:{GREEN} Owner Name
 {GREEN}[{RED}●{GREEN}] DEVELOPER    {CYAN}:{GREEN} Masudur Rahman Sifat
 {GREEN}[{RED}●{GREEN}] GITHUB       {CYAN}:{GREEN} github.com/Mr-SxR
 {GREEN}[{RED}●{GREEN}] TOOL         {CYAN}:{GREEN} NV CREATE
 {GREEN}[{RED}●{GREEN}] TOOL STATUS  {CYAN}:{GREEN} PERSONAL
{LINE}"""

# Print Messages and Prompts (All editable texts for output)
MSG_PERMISSION_ERROR = f"{GREEN}Please give sdcard permission to save Accounts{WHITE}"
MSG_FOLDER_CREATE_ERROR = f"{RED}Error: Cannot create directory {{folder}}. Please check permissions."
MSG_NO_DEVICES = f" {WHITE}Please connect ADB and run the tool"
MSG_OFFLINE_DEVICES = f" {WHITE}Please disconnect offline devices (adb disconnect <device>) and connect ADB and run the tool"
MSG_ADB_ERROR = f" {WHITE}Adb error: Run the tool again\n\n Exception: {{e}}"
MSG_PKG_INSTALL = f"{WHITE} Run: pkg install android-tools\n\n Exception: {{e}}"
MSG_KEYBOARD_TIME = " Press Enter and manually enable ADB keyboard within 20 seconds"

MSG_DEVICE_ID = f" {WHITE}Device ID {EKL} {GREEN}{{device_id}}\n\n {GREEN}UserName {EKL} {{user_name}}\n {RED}Expired {EKL} {{expiry}} (Utc)\n{LINE}\n {RED}Your access has expired."
MSG_BUY_TOOL = f" {WHITE}Press enter to buy the tool again"
MSG_NOT_REGISTERED = f" {GREEN}Device ID {EKL} {{device_id}} \n {RED}Your Device ID is not registered.\n Please contact the owner to get access."
MSG_WRONG_OPTION = f"\n{RED} You have selected the wrong option.."

MSG_MAIN_MENU = f" {GREEN}UserName {EKL} {{user_name}}\n {RED}Expired {EKL} {{expiry}} (Utc)\n{LINE}\n {OPT_LABELS[0]} START CREATE NV\n {OPT_LABELS[1]} CONTACT OWNER\n {L0} EXIT TOOL\n{LINE}"
MSG_CHOOSE_OPTION = f"{GREEN} [{RED}●{GREEN}] CHOOSE OPTION {EKL} "

MSG_ENTER_PASS = f"{GREEN} [{RED}●{GREEN}] ENTER 8-16 DIGIT PASS {EKL} "
MSG_NUM_OR_EMAIL = f" {OPT_LABELS[0]} NUMBER\n {OPT_LABELS[1]} EMAIL\n{LINE}"
MSG_WHICH_ONE = f"{GREEN} [{RED}●{GREEN}] WHICH ONE TO USE? {EKL} "
MSG_ENTER_FILE_PATH = f"{GREEN} [{RED}●{GREEN}] ENTER FILE PATH {EKL} "
MSG_FILE_NOT_FOUND = f"{LINE}\n {RED}File location not found\n Enter File agin..."
MSG_TOTAL_LOADED_NUM = f" {GREEN}TOTAL NUMBERS LOADED {EKL} {{total}}\n{LINE}"
MSG_TOTAL_LOADED_EMAIL = f" {GREEN}TOTAL EMAILS LOADED {EKL} {{total}}\n{LINE}"
MSG_PROCESS_COMPLETED = f"{LINE}\n {GREEN}PROCESS COMPLETED...\n TOTAL OK: {{ok}}\n {RED}TOTAL ER: {{er}}\n {GREEN}ALL FILE SAVED IN {{folder}}\n{LINE}"

MSG_ER_ACCOUNT = f"{RED} [●] ER {EKL} {{id}}|{{pw}}"
MSG_OK_ACCOUNT = f"{GREEN} [●] OK {EKL} {{id}}|{{pw}}"

MSG_SERVER_OFF = f"{RED} TOOLS SERVER OFF"
MSG_NET_ERROR = f"{RED} NET CONNECTION ERROR\n"
MSG_SECURITY_ERROR = f"{RED} SECURITY SYSTEM ERROR: {{e}}\n RUN TOOL AGAIN"
ERROR_MSGS = "Fatal Python error: PyThreadState_Get: no current thread\nAborted (core dumped)"

# Constants
CONTACT_URL = "https://wa.me/+8801858094178"
BYPASS_WARNING = "⚠️ Warning: Unauthorized bypass is prohibited."