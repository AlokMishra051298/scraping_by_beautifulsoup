import bs4
import requests
import csv
import lxml
res=requests.get("https://engineering.careers360.com/colleges/list-of-aerospace-engineering-colleges-in-india")
soup=bs4.BeautifulSoup(res.text,"lxml")
csv_file=open("lists.xls",'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Title','Link'])
for div in soup.find_all('div', class_='title'):
    for a in div.find_all('a'): 
        name=a.string 
        print('Name: '+ name)
        link=a['href']
        if link[:1]=='/':
            link='https://www.careers360.com/university'+link
        print('Link'+ link)
res1=requests.get("https://engineering.careers360.com/colleges/list-of-aerospace-engineering-colleges-in-india?page=1")
soup1=bs4.BeautifulSoup(res1.text,"lxml")
for div in soup1.find_all('div', class_='title'):
    for a in div.find_all('a'): 
        name=a.string 
        print('Name: '+ name)
        link=a['href']
        if link[:1]=='/':
            link='https://www.careers360.com/university'+link
        print('Link'+ link)
        csv_writer.writerow([name,link])
csv_file.close()
