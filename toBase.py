

def toBase(number,base):
	if number < 0:
		return '-' + toBase(-number,base)

	(d,m) = divmod(number,base)
	if d:
		return toBase(d,base) + digit_to_char(m)
	return digit_to_char(m)

def digit_to_char(digit):
	if digit < 10: return chr(ord('0') + digit)
	else: return chr(ord('a') + digit - 10)
