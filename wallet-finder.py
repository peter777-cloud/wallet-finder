# -------------------------------------
# Program Starts from here
# ------------------------------------- 
                                                                                                            
                    

import os
import configparser
import time
import datetime
import requests # pip install requests
from hdwallet import BIP44HDWallet # pip install hdwallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
import subprocess
import tempfile
import urllib3
import setuptools
from src.modules import init


def check_connection():

    url='https://www.google.com/'
    try:
        requests.get( url, timeout = 10 )
        return True
    except requests.exceptions.HTTPError as errh:
        # print ( "Http Error:", errh )
        return False
    except requests.exceptions.ConnectionError as errc:
        # print ( "Error Connecting:", errc )
        return False
    except requests.exceptions.Timeout as errt:
        # print ( "Timeout Error:", errt )
        return False
    except requests.exceptions.RequestException as err:
        # print ( "OOps: Something Else", err )
        return False
    except Exception as e:
        time.sleep(5)
        return False

def mainnet_url( mainnet ):

    if mainnet == "bsc":
        mainnet_url = "https://api.bscscan.com/"
    elif mainnet == "eth":
        mainnet_url = "https://api.etherscan.io/"
    elif mainnet == "polygon":
        mainnet_url = "https://api.polygonscan.com/"
    else:
        mainnet_url = "https://api.bscscan.com/"
    return mainnet_url

def mainnet_api( mainnet ):

    # read config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    mainnet_api = config['api'][mainnet]
    return mainnet_api

def req_trnx( mainnet, address ):

    mainnet_url_link = mainnet_url( mainnet )
    mainnet_api_key = mainnet_api( mainnet )
    module = "account"
    action = "txlist"
    page_no = 1
    display_per_page = 1
    sort = "desc"
    connection_count = 1
    while True:
        if check_connection() is True:
            trnx_response = requests.get(f"{mainnet_url_link}api?module={module}&action={action}&address={address}&page={page_no}&offset={display_per_page}&sort={sort}&apikey={mainnet_api_key}", timeout = None)
            if trnx_response:
                trnx_info = trnx_response.json()
                return trnx_info
            break
        else:
            print(f"-------->>> Trying to establish a connection!!! || Checked: {connection_count} time(s) <<<--------\n")
            time.sleep(10)
            connection_count+= 1
            os.system('cls')
            pass
            
def req_balance( mainnet, address ):

    mainnet_url_link = mainnet_url( mainnet )
    mainnet_api_key = mainnet_api( mainnet )
    module = "account"
    action = "balance"
    connection_count = 1
    while True:
        if check_connection() is True:
            balance_response = requests.get(f"{mainnet_url_link}api?module={module}&action={action}&address={address}&apikey={mainnet_api_key}", timeout = None)
            if balance_response:
                balance_info = balance_response.json()
                return balance_info
            break
        else:
            print(f"-------->>> Trying to establish a connection!!! || Checked: {connection_count} time(s) <<<--------\n")
            time.sleep(10)
            connection_count+= 1
            os.system('cls')
            pass

def main():

    os.system('cls')
    # list of mainnet to check
    check_mainnet = ['bsc', 'eth', 'polygon']

    # path of the directory
    hasTransactionPath = "hasTransaction"
    hasBalancePath = "hasBalance"

    # creating the date object of today's date
    todays_date = datetime.date.today()

    looper_count = 0
    balanceFound_count = 0
    trnxFound_count = 0
    init_run_time = time.monotonic()
    run_time = 0
    execution_time = 0
    looper = True
    while looper:

        start_time = time.monotonic()

        print(f"Total Checked: {looper_count} || Execution Per Time: {execution_time} || Elapsed Time: {run_time}")
        print(f"Transaction Found: {trnxFound_count} || Balance Found: {balanceFound_count}")

        # Generate english mnemonic words
        MNEMONIC: str = generate_mnemonic(language="english", strength=128)
        # Secret passphrase/password for mnemonic
        PASSPHRASE: Optional[str] = None

        # Initialize Ethereum mainnet BIP44HDWallet
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
        # Get Ethereum BIP44HDWallet from mnemonic
        bip44_hdwallet.from_mnemonic(
            mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
        )
        # Clean default BIP44 derivation indexes/paths
        # bip44_hdwallet.clean_derivation()

        print("Checking Mnemonic:", bip44_hdwallet.mnemonic())

        # Get Ethereum BIP44HDWallet information's from address index
        for address_index in range(1):
            # Derivation from Ethereum BIP44 derivation path
            bip44_derivation: BIP44Derivation = BIP44Derivation(
                cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
            )
            # Drive Ethereum BIP44HDWallet
            bip44_hdwallet.from_path(path=bip44_derivation)
            # Print address_index, path, address and private_key
            # print(f"{bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}")

            print(f"Wallet Address: {bip44_hdwallet.address()}" )

            for mainnet in check_mainnet:
                wallet_trnx_status = req_trnx( mainnet, bip44_hdwallet.address() )
                print(f"---->>> Checking Transaction(s) on {mainnet}")
                if wallet_trnx_status["status"] == "1":
                    trnxFound_count+= 1
                    print(f"************ Found Transaction on {mainnet}")
                    with open(r"{}\hasTransaction-{}.txt".format(hasTransactionPath, todays_date), "a") as hb:
                        hb.write( mainnet )
                        hb.write( " - " )
                        hb.write( " || Mnemonic : " )
                        hb.write( bip44_hdwallet.mnemonic() )
                        hb.write( " || " )
                        hb.write( bip44_hdwallet.address() )
                        hb.write( " " )
                        hb.write( '\n' )
                        hb.close()
                    print(f"-------->>> Checking Balance on {mainnet}")
                    wallet_trnx_balance = req_balance( mainnet, bip44_hdwallet.address() )
                    if wallet_trnx_balance["result"] != "0":
                        balanceFound_count+= 1
                        print(f"************ Found Balance on {mainnet}")
                        with open(r"{}\hasBalance-{}.txt".format(hasBalancePath, todays_date), "a") as hb:
                            hb.write( mainnet )
                            hb.write( " - " )
                            hb.write( wallet_trnx_balance["result"] )
                            hb.write( " || Mnemonic : " )
                            hb.write( bip44_hdwallet.mnemonic() )
                            hb.write( " || " )
                            hb.write( bip44_hdwallet.address() )
                            hb.write( " " )
                            hb.write( '\n' )
                            hb.close()
                    else :
                        print(f"xxxxxxxx Not Found Balance on {mainnet}")
                else:
                    print(f"xxxxxxxx No Transactions Found on {mainnet}")
            
        looper_count+= 1
        end_time = time.monotonic()
        execution_time = datetime.timedelta(seconds=end_time - start_time)
        run_time = datetime.timedelta(seconds=end_time - init_run_time)
        # Clean derivation indexes/paths
        bip44_hdwallet.clean_derivation()
        os.system('cls')

if __name__ == '__main__':
        
    main()