data = 'lucy9150@naver.com'
atpos = data.find('@')
print(atpos)
sppos = data.find('.',atpos)
print(sppos)
host = data[atpos+1:sppos]

k = host.upper()
print(k)
print(k[len(k)-1])
print(ord(k[len(k)-1]))

#k_last = k[len(k)-1]
#print(k_last)
#print(host.upper())
#k=host.upper()[len(host)-1]
#print(k)

