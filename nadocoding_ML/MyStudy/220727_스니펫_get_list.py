'''
나도코딩 머신러닝 공부중에
데이터프레임내에 리스트에 딕셔너리 값중에서 name만을 추출하여 리스트로 만들기
'''

def get_list(x):
    if isinstance(x, list):		# x가 리스트인 경우에
        names = [i['name'] for i in x]	# 리스트내에서 딕셔너리를 돌면서 name값난 추출
        if len(names) > 3:		# names의 리스트 값이 3개 이상인 경우에는
            names = names[:3]	# 처음 3개의 값만 리스트에 담기
        return names
    return []