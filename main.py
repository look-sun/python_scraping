import csv

# from modules import get_p
#
# p = get_p('크로스백')
# print(p)

f = open('크로스백.insta.txt', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    if line[1] != '0':
        print(line[1])

f.close()

# 인스타그램 구조
# 한번에 6개의 div
# 한 개의 div에 3개의 게시물
# 즉 한번에 18개의 게시물들을 불러온다.
# 한개의 게시물에는 사진이 최대 10장 까지 있을 수 있다.

# csv 파일은 list 형태로 저장/읽어올 수 있다.
# 읽어올 때에는 list[1][1]이러한 형태로 리스트 안에 리스트가 또있다.
# 첫 번째 안에있는 리스트에는 ['0', '/p/B4SaUdIlh4m/'] 이러한 형태로,
# 앞에는 열번호, 두번째에는 값이 들어있다.
# 모든 csv 파일의 첫 번째값은 ['', '0'] 이다.
# 그래서 리스트의 10 번째 값을 가져오고 싶다면 list[10][2] 이라고 하면 된다.
