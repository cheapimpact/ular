import requests

import webbrowser

# webbrowser.open('https://inventwithpython.com/')

res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
    print(type(res))
    print(len(res.text))
    print(res.text[:250])

except Exception as exc:
    print("There was a problem: %s" % (exc))
