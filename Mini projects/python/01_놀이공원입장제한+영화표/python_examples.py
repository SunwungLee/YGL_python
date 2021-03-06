# -*- coding: utf-8 -*-
"""python_examples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l_bcmhIMu7lMoomijqOTB0m1rWIpxCo3

# Python examples

## 1. 놀이공원 입장
"""

limit_height = 100
limit_age = 5
age = int(input("나이를 입력하세요: "))
if age >= limit_age:
    height = int(input("키를 입력하세요(cm): "))
    if height >= limit_height:
        print("놀이기구 탑승 가능")
    else:
        print("탑승 불가, 키 제한")
else:
    print("탑승 불가, 나이 제한")

"""## 2. 영화 요금제 만들기
- 일반 / 학생 여부
- 요일 / 시간
- 변수 입력시에는 가급적 범용적 변수

https://namu.wiki/w/CGV


"""

weekdays = ['월요일', '화요일', '수요일', '목요일']
weekend = ['금요일', '토요일', '일요일']
movie_type = ['일반', 'imax', '4dx']
movie_dimension = ['2D', '3D']
timetable = ['모닝', '브런치', '일반']
cost = [[9, 10, 13, 16, 12, 15], 
        [11, 12, 16, 20, 16, 21],
        [13, 14, 17, 21, 17, 22],
        [10, 11, 13, 16, 13, 16],
        [14, 15, 18, 23 ,18, 22],
        [14, 15, 18, 23 ,18, 22]]
time_f = 0
type_f = 0
while True:
    sel_day = input("희망하는 날짜를 입력하세요(e.g. 월요일): ")
    if sel_day in weekdays:
        # print('주중')
        time_f = 0
        break
    elif sel_day in weekend:
        # print("주말")
        time_f = 3
        break
    else:
        print("날짜 다시입력")
while True:
    sel_movie_type = input("희망하는 영화 타입을 입력하세요(e.g. 일반, imax, 4dx): ")
    if sel_movie_type == '일반':
        # print('일반')
        type_f = 0
        break
    elif sel_movie_type.lower() == 'imax':
        # print('아맥')
        type_f = 2
        break
    elif sel_movie_type.lower() == '4dx':
        # print('포디엑')
        type_f = 4
        break
    else:
        print('타입 다시입력')
while True:
    sel_dimension = input("희망하는 차원을 입력하세요(2D/3D): ")
    if sel_dimension.lower() == '2d':
        # print('2d')
        break
    elif sel_dimension.lower() == '3d':
        # print('3d')
        type_f += 1
        break
    else:
        print('차원 다시입력')
while True:
    sel_time = int(input("희망 시간을 입력하세요: "))
    if 6 <= sel_time < 10:
        # print('모닝')
        break
    elif 10 <= sel_time < 13:
        # print('브런치')
        time_f += 1
        break
    elif 13 <= sel_time < 24:
        # print('일반')
        time_f += 2
        break
    else:
        print('시간 다시입력')

print(f"선택하신 옵션은: {sel_day} {sel_time}시, {sel_movie_type}/{sel_dimension}")
print(f"영화 가격: {(cost[time_f][type_f]) * 1000}원")

