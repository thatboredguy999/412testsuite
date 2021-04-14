import requests

def md5test():
  url = ("localhost:5000/md5/test")
  datatest = 0
  data = request.get(url)
  if data.text = datatest:
    print(True)
    return
  else:
    print(False)
    return
  return

def isprimetest():
  url = ("localhost:5000/isprime/test")
  datatest = 0
  data = request.get(url)
  if data.text = datatest:
    print(True)
    return
  else:
    print(False)
    return
  return


