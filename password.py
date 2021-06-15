password = 'a123456'
i = 3		# password retry times
while i > 0:
	pwd = input('password: ')
	if pwd == password:
		print('login successfully! ')
		break		#jump out from the loop.
	else:
		i = i - 1
		print('wrong password! you have', i, 'time to retry')


