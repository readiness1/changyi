import numpy as np 
import pandas as pd
import tensorflow as tf 

importance_map = {} #주제 : 중요도(정수형으로 저장) -> 논의 후 작성 


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
        subject를 업데이트합니다. 
        '''
        pass #일시적으로 pass 처리 
        
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
    

    

    
