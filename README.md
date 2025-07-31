# 🕵️‍♂️ Proxy Checker
Extract valid proxies from a list with ease
# ⚙️ Setup
Start by installing the required libraries for **Proxy Checker**
```python
pip install -r requirements.txt
```
Edit your config file: `proxychecker_config.py`
```python
proxiesPath = 'proxies.txt'
# Format: 127.0.0.1:1080 seperated by new lines
proxyType = "socks5"
timeout = 20 # Timeout for each check in seconds
workingProxiesPath = 'workingProxies.txt' # Working proxies will be saved here
```
You may change the path of your proxy list,

Change the proxy type to the protocol of your list

Set the timeout to whatever you prefer

Finally, you can set a path to save valid proxies
# 🚀 Usage
1. Run `proxychecker.py` to start checking your list  
2. Import **proxychecker** into your script
- Example:
```python
from proxychecker import checkProxy
result = checkProxy("127.0.0.1:1080")
if result:
    print("Valid")
else:
    print("Invalid")
```
# 📬 Contact
Have any suggestions or issues?

[Contact me here](https://slain.me)
