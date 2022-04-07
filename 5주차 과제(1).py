words = 'When God Close One Door, He Opens Another.'
# 문자열 속 대문자는 몇 번째 인덱스에 있는지 모두 구하시오.
# 오지영 문제 
for c in words :
    if c>='A' and c<='Z' :
        print(words.index(c),end=',')
