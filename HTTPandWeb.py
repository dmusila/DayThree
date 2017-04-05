import re
import urllib.request

# target web is https://github.com/dmusila

targeturl="htts://github.com/dmusila"

urlrequest = urllib.request.urlopen(targeturl).read()

datatodisplay=urlrequest.decode("utf-8") #decode to utf-8


print(datatodisplay)