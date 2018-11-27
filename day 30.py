def big_row():
	m,n=map(int,input().split());
	a=[];
	for i in range(m):
		a.append(sum(list(map(int,input().split()))));
	maxy=max(a);
	for i in range(m):
		if(maxy==a[i]):
			print("Row "+str(i+1));
			break;
big_row()
