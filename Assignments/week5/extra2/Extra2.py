import re

page=open('in.html','r').read()
fw=open('out.txt','w')

chunk = page.split('str-author-box authorbox')

content = ''
content2 = ''
for i in range(1,len(chunk)):
	sname = ''
	scity = ''
	flag1,flag2 = 1,0
	names = re.finditer('<div class="authorsn x-author">(.*?)</div>',chunk[i])
	citys = re.finditer('<a data-t="post-geoip" href=.*?">\n(.*?)\n</a>',chunk[i])
	dates = re.finditer('<span class="x-post-time">(.*?)</span>',chunk[i])
	snames = re.finditer('<a data-t="post-usersntxt" href=.*?">(.*?)</a>',chunk[i])
	scitys = re.finditer('<p class="geoip x-geoip">\n(.*?)\n</p>',chunk[i])
	for sn in snames:
		sname =  sn.group(1)
	for sc in scitys:
		scity = sc.group(1)
	for n in names:
		name =  n.group(1)
	for c in citys:
		city = c.group(1)
	for d in dates:
		date = d.group(1)

	if sname == '':
		if name[0].islower():
			flag1 = 0
		for j in range(1,len(name)):
				if name[j].islower():
					flag2 = 1
		if flag1 and flag2:
			content = name + '\t' + city + '\t' + date + '\n'
			fw.write(content)

	else:
		if sname[0].islower():
			flag1 = 0
		for j in range(1,len(sname)):
				if sname[j].islower():
					flag2 = 1
		if flag1 and flag2:
			content = sname + '\t' + scity + '\t' + date + '\n'
			fw.write(content)

fw.close()