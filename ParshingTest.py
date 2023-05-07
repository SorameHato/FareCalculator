import csv
from os import path
print('파싱 테스트')

# CSV 파일들의 경로
LINE_FILES = [
    'RH1.csv',
    'RH5.csv',
    'RH15.csv'
]

# 각 노선의 이름과 별칭을 저장하는 dict를 생성
line_list = dict()
alias_list = dict()
for filename in LINE_FILES:
    with open(path.join('Table',filename), 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        line = filename[:-4] # 노선의 이름을 파일명에서 .csv를 제외한 부분으로 설정
        line_list[line] = dict()
        alias_list[line] = dict()
        for row in reader:
            if len(row) == 1: # 거리밖에 없는 경우
                print(f'{line} 노선의 csv 파일에 문제가 있습니다. 문제가 있는 부분 : {row[0]}')
                exit()
            elif len(row) == 2: # 별칭이 없는 경우
                distance, station = row
            else: # 별칭이 있는 경우 -> alias들을 alias_list에 추가하는 작업 추가
                distance, station, *alias = row
                alias_list[line][station] = alias
            line_list[line][station] = float(distance) # len이 2인 경우와 3 이상인 경우 둘 다 작동해야 해서 밑으로 뺐음

# 아래에서 역명이 존재하는지, 존재하지 않으면 alias 목록에 있는지 확인 후
# alias 목록에 있으면 올바른 역명으로 교정하는 함수
def stn_check(var, output:str):
    exist = False
    if not any(var in line for line in line_list.values()): # var이 역명 리스트에 없는 경우
        for line in alias_list:
            for correct_name, aliases in alias_list[line].items():
                if var in aliases:
                    exist = True
                    return correct_name
        if not exist:
            print(f"{output}으로 설정한 {var}역은 잘못된 역이거나 여정 별 운임 부과 지역입니다. 다시 한 번 확인해주시기 바랍니다.")
            exit()
    else:
        return var

# 출발역과 도착역을 입력받음
departure = input("출발역: ")
destination = input("도착역: ")

#역명 체크 함수 실행
departure = stn_check(departure, '출발역')
destination = stn_check(destination, '도착역')

print(f'출발역 : {departure}, 도착역 : {destination}')
