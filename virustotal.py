'''
Known malicious IPs for test:
23.95.35.112
103.59.94.89
185.203.186.242
'''

'''
Known malicious URLs for test:
mp3raid.com/music/krizz_kaliko.html
signin.eby.de.zukruygxctzmmqi.civpro.co.za
retajconsultancy.com
'''

import vt

api_key = "INSERT_YOUR_API_KEY_HERE"




def check_ip(ip_address):
    client = vt.Client(api_key)
    ip_object = client.get_object(f"/ip_addresses/{ip_address}")
    stats = ip_object.last_analysis_stats

    print("\n\n")
    print(f"IP Address: {ip_address}")
    print(f"Owner: {ip_object.as_owner}")
    print(f"IP Country: {ip_object.country}\n")

    print(f"Malicious: {stats.get('malicious')}")
    print(f"Suspicious: {stats.get('suspicious')}")
    print(f"Harmless: {stats.get('harmless')}")

    if stats.get('malicious') > 0:
        print("\nDANGER! Possibly a malicious IP!")
    else:
        print("\nIP seems clean.")
    client.close()
    print("\n\n")





def check_url(url):
    client = vt.Client(api_key)
    url_id = vt.url_id(url)

    url_object = client.get_object(f"/urls/{url_id}")
    stats = url_object.last_analysis_stats # Get the stats from the website

    print("\n\n")
    print(f"URL: {url}")
    print(f"Malicious: {stats.get('malicious')}")
    print(f"Suspicious: {stats.get('suspicious')}")
    print(f"Harmless: {stats.get('harmless')}")


    if stats.get('malicious') > 0:
            print("\nDANGER! Possibly a malicious URL!")
    else:
        print("\nURL seems clean.")
    print("\n\n")

    client.close()



functions = input("What do you want to check? Enter the number:\n1. IP\n2. URL\n")
if functions.endswith("."):
     functions = functions[:-1]
if functions == "1":
    check_ip(input("Enter IP: "))
elif functions == "2":
    check_url(input("Enter URL: "))
else:
    exit


