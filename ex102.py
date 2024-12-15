def fat(n, b):

	if(n > 0):
		if(b == True):
			print(end ='' f'{n} x ' if n > 1 else f'{n} = ');
			return n * fat(n - 1, True);
		else:
			return n * fat(n - 1, False);
	else:
		return 1;

print(fat(5, True));