from collections import Counter
from nltk.corpus import wordnet
synonyms = []
import operator
import requests
import pyperclip
from bs4 import BeautifulSoup
url='https://btechgeeks.com/python-programming-examples-with-output/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
data=soup.find('div',class_='entry-content')
c=0
while(1):
    s=list(input('Enter your article name : ').lower().split())
    oris=Counter(s)
    d={}
    e={}
    for i in data.find_all('li'):
        if(c>20):
            temptext=i.text.lower()
            e[temptext]=i
            cnt=0
            testr=Counter(temptext.split())
            synonyms=[]
            
            for u in oris:

                for syn in wordnet.synsets(u):

	                for l in syn.lemmas():

                         if(u!='List' or u!='list'):

                            synonyms.append(l.name())

                synwords=set(synonyms)
                if u in testr.keys():
                    
                    cnt+=1
            
            d[temptext]=cnt               
        c+=1
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))   
    p=0 
    ss='<strong>Related Programs</strong>:\n<ul>'
    for i in sorted_d:
       
        if(p==0):
            p+=1
            continue   
        eee=str(e[i])
        if "href" in eee:
            if(i!=' '.join(s)):
                ss+=str(e[i])
                print(e[i])
                p+=1 
        if(p==8):   
            break  
    ddd=input("Enter no or No to stop = ")
    ss+='\n</ul>'
    if(ddd=='no' or ddd=='No'):
        break    

    pyperclip.copy(ss)

            