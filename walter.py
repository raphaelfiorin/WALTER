import bs4, requests
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
from requests import HTTPError
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def verf():
            # Test acessible host
    for url in ['{domain}'.format(**entry)]:
        try:
            response = requests.get('https://'+url , timeout=1.25)

            response.raise_for_status()
        except HTTPError as http_err:
            print(f'\033[1;31mHTTP error occurred\033[m: {http_err} \n')
        except Exception as err:
            print(f'\033[1;31mHost not Reachable\033[m: {err} \n') 
        else:
            print('\033[1;32mReachable Host\033[m')

            # Grepping JS files
            print("\033[1;34mJS Parsing:\033[m")
            web_url = 'https://'+'{domain}'.format(**entry)
            html = requests.get(web_url).content
            soup = bs4.BeautifulSoup(html, "html.parser")
            js_files = []
            for script in soup.find_all("script"):
                if script.attrs.get("src"):
                    script_url = urljoin(url, script.attrs.get("src"))
                    js_files.append(script_url)
                    print (js_files, '\n')


print("""\033[1;32m
            ⠄⠄⠄⠄⠄⠄⠄⢀⣠⣶⣾⣿⣶⣦⣤⣀⠄⢀⣀⣤⣤⣤⣤⣄⠄⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⢀⣴⣿⣿⣿⡿⠿⠿⠿⠿⢿⣷⡹⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄
            ⠄⠄⠄⠄⠄⣾⣿⣿⣿⣯⣵⣾⣿⣿⡶⠦⠭⢁⠩⢭⣭⣵⣶⣶⡬⣄⣀⡀⠄⠄
            ⠄⠄⠄⡀⠘⠻⣿⣿⣿⣿⡿⠟⠩⠶⠚⠻⠟⠳⢶⣮⢫⣥⠶⠒⠒⠒⠒⠆⠐⠒
            ⠄⢠⣾⢇⣿⣿⣶⣦⢠⠰⡕⢤⠆⠄⠰⢠⢠⠄⠰⢠⠠⠄⡀⠄⢊⢯⠄⡅⠂⠄
            ⢠⣿⣿⣿⣿⣿⣿⣿⣏⠘⢼⠬⠆⠄⢘⠨⢐⠄⢘⠈⣼⡄⠄⠄⡢⡲⠄⠂⠠⠄
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣥⣀⡁⠄⠘⠘⠘⢀⣠⣾⣿⢿⣦⣁⠙⠃⠄⠃⠐⣀
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣵⣾⣿⣿⣿⣿⣦⣀⣶⣾⣿⣿⡉⠉⠉
            ⣿⣿⣿⣿⣿⣿⣿⠟⣫⣥⣬⣭⣛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄
            ⣿⣿⣿⣿⣿⣿⣿⠸⣿⣏⣙⠿⣿⣿⣶⣦⣍⣙⠿⠿⠿⠿⠿⠿⠿⠿⣛⣩⣶⠄
            ⣛⣛⣛⠿⠿⣿⣿⣿⣮⣙⠿⢿⣶⣶⣭⣭⣛⣛⣛⣛⠛⠛⠻⣛⣛⣛⣛⣋⠁⢀
            ⣿⣿⣿⣿⣿⣶⣬⢙⡻⠿⠿⣷⣤⣝⣛⣛⣛⣛⣛⣛⣛⣛⠛⠛⣛⣛⠛⣡⣴⣿
            ⣛⣛⠛⠛⠛⣛⡑⡿⢻⢻⠲⢆⢹⣿⣿⣿⣿⣿⣿⠿⠿⠟⡴⢻⢋⠻⣟⠈⠿⠿
            ⣿⡿⡿⣿⢷⢤⠄⡔⡘⣃⢃⢰⡦⡤⡤⢤⢤⢤⠒⠞⠳⢸⠃⡆⢸⠄⠟⠸⠛⢿
            ⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸\033[m""")
print("\033[1;34mHACKER MAN\033[m".center(65))
print("\033[1;31mW.A.L.T.E.R v2\033[m".center(65))
print("By: Raphael Fiorin, Daniel Mizael & Kayky Vinicius\n".center(55))

domain = input('\033[1;34mTarget:\033[m ')

res = DNSDumpsterAPI(False).search(domain)

print("\n\033[1;34mDNS Servers:\033[m")
for entry in res['dns_records']['dns']:
    print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

print("\n\033[1;34mMX Records\033[m")
for entry in res['dns_records']['mx']:
    print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

print("\n\033[1;34mHost Records (A):\033[m")
for entry in res['dns_records']['host']:
    if entry['reverse_dns']:
        print(("\n{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
        verf()

print("\033[1;34mTXT Records:\033[m")
for entry in res['dns_records']['txt']:
	print(entry)