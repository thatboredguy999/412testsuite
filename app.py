import requests


#post,put,get,delete


def md5test():
	url = "http://localhost:5000/md5/5"
	data = requests.get(url).json
	testrun = {"input":"test","output":"098f6bcd4621d373cade4e832627b4f6"}
	if data == data-test:
		print (true)
		return true
	else:
		print (false)
		return false


if __name__ == "__main__":
