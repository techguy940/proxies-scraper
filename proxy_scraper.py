import requests
import json
import time

def get_proxies(type_proxy,anon):
    r = requests.get(url + "?type={}&anon={}".format(type_proxy,anon))

    text = r.text
    text = text.replace("\n","")

    with open ("proxy_scraper.txt","w") as f:
        f.write(text)


    print("Proxies are saved in this file's directory as 'proxy_scraper.txt'")
    time.sleep(1)
    

url = "https://www.proxy-list.download/api/v1/get"

type_proxy = input("Which Proxies You Want?\n1.Http\n2.Https\n3.Socks4\n4.Socks5\n: ")


#HTTP
if type_proxy == "1" or type_proxy.lower() == "http":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":
        get_proxies("http","transparent")

    elif anon == '2' or anon.lower() == "anonymous":
        get_proxies("http","anonymous")

    elif anon == '3' or anon.lower() == "elite":
        get_proxies("http","elite")


#HTTPS
elif type_proxy == "2" or type_proxy.lower() == "https":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":
        get_proxies("https","transparent")

    elif anon == '2' or anon.lower() == "anonymous":
        get_proxies("https","anonymous")

    elif anon == '3' or anon.lower() == "elite":
        get_proxies("https","elite")


#SOCKS4
elif type_proxy == "3" or type_proxy.lower() == "socks4":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":
        get_proxies("socks4","transparent")

    elif anon == '2' or anon.lower() == "anonymous":
        get_proxies("socks4","anonymous")

    elif anon == '3' or anon.lower() == "elite":
        get_proxies("socks4","elite")


#SOCKS5
elif type_proxy == "4" or type_proxy.lower() == "socks5":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":
        get_proxies("socks5","transparent")

    elif anon == '2' or anon.lower() == "anonymous":
        get_proxies("socks5","anonymous")

    elif anon == '3' or anon.lower() == "elite":
        get_proxies("socks5","elite")

    
        
