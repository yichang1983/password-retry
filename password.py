password = 'a123456'
i = 3		# password retry times
while True:
	pwd = input('password: ')
	if pwd == password:
		print('login successfully! ')
		break
	else:
		i = i - 1
		print('wrong password! you have', i, 'time to retry')
		if i == 0:
			break
			
