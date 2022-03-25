#리스트의 모든 값을 화면으로 출력하라
data = [32, 14, 55, 23, 12, 67, 44]
for k in data :
    print(k, end=',')
print ("stop")

#리스트의 값 중에서 짝수 값만을 출력하라
data = [32, 14, 55, 23, 12, 67, 44]
for k in data :
    if k%2==0 :
        print(k, end=',')
print("stop")

# 30이상 출력
data = [32, 14, 55, 23, 12, 67, 44]
for k in data :
    if k >= 30 :
        print(k, end=',')
print("stop")

# 40 크고 50 미만 출력
data = [32, 14, 55, 23, 12,67, 44]
for k in data :
    if k>40 and k<50 :
        print(k, end=',')
print("stop")

# 20보다 작거나 50 이상 출력
data = [32, 14, 55, 23, 12, 67, 44]
for k in data :
    if k<=20 or k>=50 :
        print(k, end=',')
print("stop")

#홀수값 출력
data = [32, 14, 55, 23, 12, 67, 44]
for k in data :
    if k%2==1 :
        print(k, end=',')
print("stop")

#30이상 갯수
data = [32, 14, 55, 23, 12, 67, 44]
count =0
for k in data :
    if k>=30 :
        count=count+1
print(count)
print("stop")
