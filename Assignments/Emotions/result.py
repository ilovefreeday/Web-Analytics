import operator

f = open('result.txt','r')
alltext = f.read().split('\n')
text,count,num = [],[],[]

for i in alltext:
	if len(i) > 30:
		text.append(i)

for i in text:
	count.append(i.split(', ')[:-1])
for i in range(len(count)):
	# print len(count[i])
	dic = dict()
	print dic
	for j in range(len(count[i])):
		tmp = count[i][j].split(':')[0]
		num = int(count[i][j].split(':')[1])
		if tmp not in dic:
			dic[tmp] = num
	print '@'
	for key, value in sorted(dic.iteritems(), key=lambda (k,v): (v,k)):
	 	print key,value
		
