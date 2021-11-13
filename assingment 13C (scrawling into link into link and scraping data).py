'''Assignment: Following Links in HTML Using BeautifulSoup   ( week 4)'''
#every time the names changing positions every time we repeat click

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

u = input("Enter url- ")  # http://py4e-data.dr-chuck.net/known_by_Crystyn.html
p = int(input("Position- "))
r = int(input("Repeat- "))
count = 0
namelist = list()
linklist = list()
url = u

while count <= r-1 :  #definite loop for definite values
      namelist.clear() # imp to use to get fesh values for every loop value
      linklist.clear()
      html = urllib.request.urlopen(url).read()
      s = BeautifulSoup(html,"html.parser")
      print(s)

      tags = s('a') #makes list of tags we want #its like split() on web page
      print(tags)
      count = count + 1

      for tag in tags :
         link = tag.get("href",None)  #in html #where it take us when we click string link
         name = tag.string            #string which is act like link
         namelist.append(name) 
         linklist.append(link)
      url = linklist[p-1]  #as index of list starts from 0
   
print(namelist[p-1]) #for Ex. the name at the postion 10 after 5 repetion on the same position's link
    
