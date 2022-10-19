password = 'a123456'
x = 3
while True:
    pwd = input('please enter your code')
    if pwd == password:
	    print('log in successful')
	    break
    else:
        x = x-1
        print('password incorrect, you still have', x ,'time to try')
        if x == 0:
            break