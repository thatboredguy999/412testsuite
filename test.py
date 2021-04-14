import requests


#md5test script
def md5test():
  url = ("localhost:5000/md5/test")
  datatest = 0
  data = requests.get(url)
  if data.text == datatest:
    print(True)
    return
  else:
    print(False)
    return
  return

#is-prime test script
def isprimetest():
  url = ("localhost:5000/is-prime/test")
  datatest = 0
  data = requests.get(url)
  if data.text == datatest:
    print(True)
    return
  else:
    print(False)
    return
  return

#factorial test script
def factorialtest():
  url = ("localhost:5000/factorial/5")
  datatest = 0
  data = requests.get(url)
  if data.text == datatest:
    print(True)
    return
  else:
    print(False)
    return
  return


#fibonacci test script
def fibonaccitest():
  url = ("localhost:5000/fibonacci/5")
  datatest = 0
  data = requests.get(url)
  if data.text ==  datatest:
    print(True)
    return
  else:
    print(False)
    return
  return


#slack test script
def slacktest():
  url = ("localhost:5000/slack-alert/test")
  datatest = 0
  data = requests.get(url)
  if data.text == datatest:
    print(True)
    return
  else:
    print(False)
    return
  return

#keyval test scripts
#ORDER: POST, PUT, GET, REMOVE

def keyvalpost():
  url = ("localhost:5000/keyval")
  payload = { "key": "new-key", "value": "new value" }
  data =  requests.post(url, data =  payload)
  if data.status_code == 200:
    print("Value posted")
    return
  else:
    print("ERROR: Code 200 expected")
    return
  return

def keyvalput():
  url = ("localhost:5000/keyval")
  payload = { "key": "new-key", "value": "value2" }
  data = requests.put(url,data = payload)
  if data.status_code == 200:
    print("Value Changed")
    return
  else:
    print("ERROR: Code 2-- expected")
    return
  return

def keyvalget():
  url = ("localhost:5000/keyval/new-key")
  data = requests.get(url)
  datatest = 0
  store =  data.json()
  if store == datatest:
    print("Value retrieved:", store)
    return
  else:
    print("ERROR: Code 200 expected")
    return
  return

def keyvalget():
  url = ("localhost:5000/keyval/new-key")
  data = requests.delete(url)
  datatest = 0
  store = data.json()
  if store == datatest:
    print("Key and Value deleted")
    return
  else:
    Error('Code 200 expected')
    return
  return



