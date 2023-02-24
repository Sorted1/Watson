
# Watson

A Osint Mini Suite For Beginner And Advanced Users

## Features

- Carrier Clerk (Carrier Lookup)
- Email Investigator
- Custom Command Handler
- IP Lookup
## Setup
To Setup Watson Do The Following

 * Get API Key From Sites Stated in ```config.json```
 * Place API Keys In config
 * Get pip Packages `pip install -r requirements.txt`
 * Then Run Script By Typing This `python3 main.py` or `python main.py`
## Custom Commands
* When making Custom Commands Place Then In `./commands` Folder
* It is Open Game With Making Commands Do What you Want!
* For Config Just Call To It With Json Doing This 
```py
with open("config.json") as f:
    config = json.load(f)
    foo = config.get('foo')
    bar = config.get('bar')
```
## Authors

- [@Sorted1](https://www.github.com/sorted1)
- [@node-digital](https://www.github.com/node-digital)
- [@0wls3c](https://www.github.com/0wls3c)
## License

[MIT](https://choosealicense.com/licenses/mit/)

