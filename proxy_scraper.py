import requests
import json
import time

print('Run this only in IDLE')

url = "https://www.proxy-list.download/api/v1/get"

type_proxy = input("Which Proxies You Want?\n1.Http\n2.Https\n3.Socks4\n4.Socks5\n: ")

#HTTP
if type_proxy == "1" or type_proxy.lower() == "http":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":

        r = requests.get(url + "?type=http&anon=transparent")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")


    elif anon == '2' or anon.lower() == "anonymous":

        r = requests.get(url + "?type=http&anon=anonymous")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")



    elif anon == '3' or anon.lower() == "elite":

        r = requests.get(url + "?type=http&anon=elite")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")




#HTTPS
elif type_proxy == "2" or type_proxy.lower() == "https":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":

        r = requests.get(url + "?type=https&anon=transparent")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")


    elif anon == '2' or anon.lower() == "anonymous":

        r = requests.get(url + "?type=https&anon=anonymous")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")



    elif anon == '3' or anon.lower() == "elite":

        r = requests.get(url + "?type=https&anon=elite")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")



#SOCKS4
elif type_proxy == "3" or type_proxy.lower() == "socks4":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":

        r = requests.get(url + "?type=socks4&anon=transparent")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")


    elif anon == '2' or anon.lower() == "anonymous":

        r = requests.get(url + "?type=socks4&anon=anonymous")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")



    elif anon == '3' or anon.lower() == "elite":

        r = requests.get(url + "?type=socks4&anon=elite")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")




#SOCKS5
elif type_proxy == "4" or type_proxy.lower() == "socks5":
    anon = input("Anonymity?\n1.Transparent\n2.Anonymous\n3.Elite\n: ")

    if anon == '1' or anon.lower() == "transparent":

        r = requests.get(url + "?type=socks5&anon=transparent")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")


    elif anon == '2' or anon.lower() == "anonymous":

        r = requests.get(url + "?type=socks5&anon=anonymous")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")



    elif anon == '3' or anon.lower() == "elite":

        r = requests.get(url + "?type=socks5&anon=elite")

        text = r.text
        text = text.replace("\r",",")
        text = text.replace("\n","")

        with open ("proxy_scraper.json","w") as f:
            json.dump(text,f)


        print("Proxies are saved in this file's directory as 'proxy_scraper.json'")
        time.sleep(1)
        print("Double tap on 'Squeezed text' to see proxies in IDLE")
        time.sleep(1)
        print(f"===Proxies===\n{r.text}===End===")

    
        
