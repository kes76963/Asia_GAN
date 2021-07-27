from konlpy.tag import Kkma

kkma = Kkma()

kkma.morphs  # 형태소 분석
kkma.nouns  # 명사 분석
kkma.pos  # 형태소 분석 태깅
kkma.sentences  # 문장 분석

# 사용예시
print(kkma.morphs(u'공부를 하면할수록 모르는게 많다는 것을 알게 됩니다.'))
#['공부', '를', '하', '면', '하', 'ㄹ수록', '모르', '는', '것', '이', '많', '다는', '것', '을', '알', '게', '되', 'ㅂ니다', '.']

print(kkma.nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만...'))
#['대학', '통계학', '이산', '이산수학', '수학', '등']

print(kkma.pos(u'다 까먹어버렸네요?ㅋㅋ'))
#[('다', 'MAG'), ('까먹', 'VV'), ('어', 'ECD'), ('버리', 'VXV'), ('었', 'EPT'), ('네요', 'EFN'), ('?', 'SF'), ('ㅋㅋ', 'EMO')]

print(kkma.sentences(u'그래도 계속 공부합니다. 재밌으니까!'))
#['그래도 계속 공부합니다.', '재밌으니까!']