# 라이브러리 임포트
from konlpy.tag import Okt
from keybert import KeyBERT

# 텍스트 전처리 및 주제 추출 함수
def extract_topics(text):
    okt = Okt()
    # 형태소 분석을 통해 명사만 추출
    nouns = okt.nouns(text)
    # 추출된 명사 리스트를 하나의 문자열로 결합
    noun_text = ' '.join(nouns)
    # KeyBERT를 사용해 키워드 추출
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(noun_text, top_n=5)
    return [keyword[0] for keyword in keywords]

print(extract_topics('지금 화재가 발생했습니다. '))