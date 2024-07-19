import numpy as np 
import pandas as pd
import tensorflow as tf 
from konlpy.tag import Okt
from keybert import KeyBERT
from test_text_subject import extract_topics #test_text_subject.py에서 extraact_topics import 


importance_map = {} #주제 : 중요도(정수형으로 저장) 
#중요도 논의 방법 
'''
1. 설문조사 : 설문조사 돌려서 학생들 인식대로
2. 국가적/국제적 지표 
3. 
'''


class Jaenan_moonja() : 

    def __init__(self,text):
        '''
        text : 문자내용을 인자로 받음
        subject 변수 생성 -> 이후 find_subject method를 통해 subject 변수 업데이트 필요 
        '''
        self.text = text 
        subject = None
        self.subject = subject

    def find_subject(self) : 
        '''
        자연어 처리를 통한 주제 찾기 method 
        return은 없습니다. 
        
        ### 고민 ###
        self.subject를 바로 업데이트 가능한데 subject가 필요할까?
        '''
        self.subject= extract_topics(self.text)
         
        
    def sebject_of_message(self) : 
        return self.subject #return subject

    def is_important(self) : 
        '''
        중요도 판단 메서드입니다. 
        중요도에 따른 재난을 분류할 기준은 데이터 분석 이후 정리하는 것을 목표로 합니다. 
        '''
        importance = importance_map[self.find_subject()]
        std_level = 5 #임의적 설정. 이후에 논의 후 변경
        if importance >= std_level : 
            return '아주 큰 재난'
        else : return '별거 아닌듯?' 
    

    

    
