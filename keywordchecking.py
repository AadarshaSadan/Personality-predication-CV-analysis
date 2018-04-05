# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 21:11:54 2018

@author: bajag
"""
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
x = np.random.normal(size = 1000)
plt.hist(x, normed=True, bins=30)
plt.ylabel('Probability');
import re
class Check_keyword():
    def qualification_score(self,words):
        global temp
        uniscore=70
        school=20
        phd=90
        default=10
        #specify other token if necessary example ioe,ku,pu etc
        if "university" in words:
            temp=uniscore
        elif "phd" in words:
            temp=phd
        elif "school" in words:
            temp=school
        elif "school" and "phd "in words:
            temp=250
        else:
            temp=default
        print(temp)
        
        
        
    def expirence_score(self,sentence,name,registration):
        global per
        #print(sentence) #regular grammer for 4 digit number
        #print(sentence)
        print(registration)
        appitude=30

        match = re.findall(r'(\d{4})', sentence)
        if match:
            #print(match)
            intoint = list(map(int, match))
            results= sorted(i for i in intoint if i >=2000 and i<2020)
            #print(results)
            #print(re)
            max_value = max(results)
            min_value = min(results)
            experenceyear=(max_value-min_value)
            per=((experenceyear)/20)*100
            cvScore=((per+temp)/2)
            #print(cvScore)
            #x = np.arange(3)
            #plt.bar(x, height= [cvScore,appitude])
            #plt.xticks(x+10, [cvScore,appitude]);
            if cvScore>50:
                remark="Eligible"
            elif cvScore<50:
                remark="NotEligible"
            connect=sqlite3.connect('details.db')
            connect.execute('''INSERT INTO final(name,regno,cv_score,remarks) VALUES(?,?,?,?)''', (name, registration, cvScore,remark))
            connect.commit()
            
            
    #def lang_spoken_score(self):
    
        
    
    #def appitude_test_score(self):
    
    
    
    #def skill_score(self)

if __name__ == "__main__":
     keyobject=Check_keyword()
     keyobject.qualification_score()
