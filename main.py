# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:06:57 2020

@author: Wajahat's
"""
import SentenceGenerator


def Print():
    m =  SentenceGenerator.Sentence_Generator()
    return(m.generate_sentence(("am","9","44","work"),sentence_type='declaration',tense='present',s_dtnum=('I am',1),o1_dtnum=('',1),o2_dtnum=('',1),o3_dtnum=('',1)))
print(Print())    
