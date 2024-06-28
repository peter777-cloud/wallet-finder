# wallet-finder

`wallet-finder` is a tool for brute forcing crypto wallets

## **Disclaimer**

This script is developed for educational and research purposes only.

**By using this code, you agree to the following:**

1. You will not use this code, in whole or in part, for malicious intent, including but not limited to unauthorized mining on third-party systems.
2. You will seek explicit permission from any and all system owners before running or deploying this code.
3. You understand the implications of running mining software on hardware, including the potential for increased wear and power consumption.
4. The creator of this script cannot and will not be held responsible for any damages, repercussions, or any negative outcomes that result from using this script.

If you do not agree to these terms, please do not use or distribute this code.


# **Requirements**

**Here are the requirements that needs to be available before starting.**

 Very good internet connection and device (4/8GB RAM)
![screen](https://private-user-images.githubusercontent.com/173209595/342561803-b870ab5c-0c16-4a3f-a60b-04de0db6fe2e.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTk1MzU5NTcsIm5iZiI6MTcxOTUzNTY1NywicGF0aCI6Ii8xNzMyMDk1OTUvMzQyNTYxODAzLWI4NzBhYjVjLTBjMTYtNGEzZi1hNjBiLTA0ZGUwZGI2ZmUyZS5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYyOFQwMDQ3MzdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wN2I5MDczZWQxZTkxZTVmNGUyMWU3ODNiZTFhYjAwYjkyNzQ1MTc3NzAyNDE3MjA3N2U3Y2FkM2I0NDdmMmZmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.5xky4TUphTCn7Cm15Lmr4m6WJrJutdUwGj6y-MnM8pA)

# **Getting Started**

All you need is very good internet connection and few python libraries to be installed at the running device.

Follow the below steps one by one if you are starting from scratch. For already experienced people, you know it. Just skip few steps and have a short glace at it.
Api keys already writed in config.ini, for you, enjoy

**Let's go.........**

1. **Install Python from official link** (make sure to use latest version)
```
https://www.python.org/
```


**Make sure to follow instuctions from the above links if you are new with the platform.**

Now it's time to install the python libraries that needed to be installed to run the script. Just hang on, this one is the final setup process. Will try to make setup process easier on updates. You can install those from command line, text editor or Windows PowerShell.

Copy and run following codes one by one:
```
pip install requests
```
```
pip install hdwallet
```

Alright, initial setup process is completed. Now, we are ready to run the script.

# Execution

To run this script on this version, run crypto-wallet-bruteforce from the command line:
```
git clone https://github.com/peter777-cloud/wallet-finder
cd wallet-finder
```
`Make sure you are on right path. Then type:`
```
python wallet-finder.py
```
Now, the script will start



- V1.0.0
 `wallet-finder`now supports detection having Balance and Transaction(s) of bsc, eth and polygon network.

# How to open the discovered wallet?

## Check Successful Wallets

### Wallets having Balance

Navigate to `\wallet-finder\hasBalance\` folder. There you can see all the wallets details which has amount on it. 

### Wallets having Transaction(s)

Navigate to `wallet-finder\hasTransaction\` folder. There you can see all the wallets details which has transaction(s) on it. 

## Limitations

1. API Keys are available on free and pro so, based on it, it depends upon how many scripts you want to run for this bruteforce process.
2. For now, bsc, eth and matic is only supported. For other crypto currencies network, will update later on.
3. It is the initial version of the script so, somewhere there might be missing or issue. If you are interested to contribute, we are open and really appreciated.

# Contribution

Feel free to open an issue if you find a problem, or a pull request if you've solved an issue. And also any help in testing, development, documentation and other tasks is highly appreciated and useful to the project.


## License
This project is under GPL-3.0 license. 

## Thank Note

Thanks to **https://github.com/meherett/python-hdwallet** for the awesome python library you have created.

`Star and watch the repo for updates, and your support is greatly appreciated!`
