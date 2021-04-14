import requests


#md5test script
def md5test():
  url = ('http://localhost:5000/md5/test')
  datatest = '{"input":"test","output":"098f6bcd4621d373cade4e832627b4f6"}'
  data = requests.get(url)
  datat = data.text
  if datatest in datat:
    print(True)
    return
  else:
    print(False)
    return
  return

#is-prime test script
def isprimetest():
  url = ("http://localhost:5000/is-prime/5")
  datatest = '{"intput":5,"output":true}'
  data = requests.get(url)
  datat = data.text
  if datatest in datat:
    print(True)
    return
  else:
    print(False)
    return
  return

#factorial test script
def factorialtest():
  url = ("http://localhost:5000/factorial/5")
  datatest = '{"input":5,"output":120}'
  data = requests.get(url)
  if datatest in data.text:
    print(True)
    return
  else:
    print(False)
    return
  return


#fibonacci test script
def fibonaccitest():
  url = ("http://localhost:5000/fibonacci/5")
  datatest = '{"input":5,"output":[0,1,1,2,3,5]}'
  data = requests.get(url)
  if datatest in data.text:
    print(True)
    return
  else:
    print(False)
    return
  return


#slack test script
def slacktest():
  url = ("http://localhost:5000/slack-alert/test")
  datatest = '{"input":"test","output":true}'
  data = requests.get(url)
  if datatest in data.text:
    print(True)
    return
  else:
    print(False)
    return
  return

#keyval test scripts
#ORDER: POST, PUT, GET, REMOVE

def keyvalpost():
  url = ("http://localhost:5000/keyval")
  payload = { 'key': 'new-key', 'value': 'new value' }
  data =  requests.post(url, json = payload)
  if data.status_code == 200:
    print("Value posted")
    return
  else:
    print("ERROR: Code 200 expected")
    return
  return

def keyvalput():
  url = ("http://localhost:5000/keyval")
  payload = { "key": "new-key", "value": "value2" }
  data = requests.put(url, json = payload)
  if data.status_code == 200:
    print("Value Changed")
    return
  else:
    print("ERROR: Code 2-- expected")
    return
  return

def keyvalget():
  url = ("http://localhost:5000/keyval/new-key")
  data = requests.get(url)
  datatest = 0
  store =  data.json()
  if datatest in store:
    print("Value retrieved:", store)
    return
  else:
   # print("ERROR: Code 200 expected")
    print(data.json())
    return
  return

def keyvaldelete():
  url = ("http://localhost:5000/keyval/new-key")
  data = requests.delete(url)
  datatest = 0
  store = data.json()
  if datatest in store:
    print("Key and Value deleted")
    return
  else:
    print('Code 200 expected')
    return
  return



md5test()
isprimetest()
factorialtest()
fibonaccitest()
slacktest()
keyvalpost()
keyvalput()
keyvalget()
keyvaldelete()
