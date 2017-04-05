import re
import urllib.request

# target web is https://github.com/dmusila?tab=repositories

username=input("Enter you git user name:") #dmusila

targeturl="https://github.com/"+username+"?tab=repositories"

urlrequest = urllib.request.urlopen(targeturl).read()

datatodisplay=urlrequest.decode("utf-8") #decode to utf-8


print(datatodisplay)

knowrepos=re.search()