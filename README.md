# No IP Automation
## Description
Free NoIP domains require confirmation every 30 days to prevent them going into redemption. Normally an E-Mail is sent 7 days prior to this action but this can be easily missed leading to issues accessing your domains. This simple script uses selenium to automate the login procedure and check to see if any hostname requires confirmation, if so it simply confirms the hostname.

## Features
- Simple python script built using python3.8 and selenium4.3.0
- Reads credentials from json file (find instructions below)
- Can be used with CronJobs in Linux to automate the running of script every day.

## Credential File
The python script uses a json file to read in your NoIp credentials.
1) Create a file in the root directory of the project called "credentials.json"
2) Copy the following extract into that file:
```
{
  "username": "YOUR_USERNAME",
  "password": "YOUR_PASSWORD"
}
```
3) Replace "YOUR_USERNAME" and "YOUR_PASSWORD" with your NoIP credentials.

## Prerequisites
- Python 3 (Built using 3.8)
- Pip 3 (Install pip packages using requirements.txt. For example on Linux "pip3 install -r requirements.txt")
- Firefox (Selenium requires Firefox to be installed. For example on Linux "sudo apt-get install firefox")

## CronJob
This script is useful when its combined with CronJobs in linux to run automatically on a server.
