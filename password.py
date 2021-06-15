password = 'a123456'
i = 3		# password retry times
while i > 0:
	i = i - 1
	pwd = input('password: ')
	if pwd == password:
		print('login successfully! ')
		break		#jump out from the loop.
	else:
		print('wrong password! ') 
		if i > 0:
			print('you have', i, 'time to retry')
		else:
			print('your account is locked')


