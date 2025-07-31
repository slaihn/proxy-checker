from proxychecker_config import proxyType, timeout
from requests import get
from requests import ConnectTimeout, ReadTimeout, ConnectionError

def checkProxy(proxy):
    proxies = {
        "http": f"{proxyType}://{proxy}",
        "https": f"{proxyType}://{proxy}"
    }

    try:
        r = get("http://google.com", proxies=proxies, timeout=timeout)
        if r.status_code == 200:
            return proxy
    except (ConnectTimeout, ReadTimeout, ConnectionError) as e:
        global err
        err = e
        return None
    
if __name__ == "__main__":
    from proxychecker_config import proxiesPath, workingProxiesPath
    from tqdm import tqdm

    ascii = r"""
    ___                     ___ _           _           
    | _ \_ _ _____ ___  _   / __| |_  ___ __| |_____ _ _ 
    |  _| '_/ _ \ \ | || | | (__| ' \/ -_/ _| / / -_| '_|
    |_| |_| \___/_\_\\_, |  \___|_||_\___\__|_\_\___|_|  
                    |__/                               
    """
    print(ascii)

    try:
        with open(proxiesPath, 'r') as file:
            proxyList = file.read().splitlines()
    except FileNotFoundError:
        print("-"*20)
        print("(!) Proxies file not found\nCheck your config")
        print("-"*20)
        exit()

    workingProxies = []

    print("-"*20)
    print(f"Checking {len(proxyList)} proxies")
    print("-"*20)

    for proxy in tqdm(proxyList, desc="Progress", unit="proxies"):
        print(f"\nChecking proxy: {proxy}")
        result = checkProxy(proxy)
        if result:
            print(f"(+) {proxy}: Working\n")
            workingProxies.append(result)
        else:
            print(f"(-) {proxy}: Timed out/Failed ({type(err).__name__})\n")

    print("-"*20)
    print(f"Working: {len(workingProxies)}")

    with open(workingProxiesPath, 'w') as file: # Change to 'a' to append instead of overwriting the file
        for proxy in workingProxies:
            file.write(f"{proxy}\n")
    print(f"Saved to: {workingProxiesPath}")
    print("-"*20)
