r = {'q':'q',
		'w':'q',
		'e':'w',
		'r':'e',
		't':'r',
		'y':'t',
		'u':'y',
		'i':'u',
		'o':'i',
		'p':'o',
		'[':'p',
		'a':'a',
		's':'a',
		'd':'s',
		'f':'d',
		'g':'f',
		'h':'g',
		'j':'h',
		'k':'j',
		'l':'k',
		';':'l',
		'z':'z',
		'x':'z',
		'c':'x',
		'v':'c',
		'b':'v',
		'n':'b',
		'm':'n',
		',':'m',
		'.':',',
		'/':'.',
		"'":';',
		']':'[',
		'\\':']'						
	}
l = {'q':'w',
		'w':'e',
		'e':'r',
		'r':'t',
		't':'y',
		'y':'u',
		'u':'i',
		'i':'o',
		'o':'p',
		'p':'[',
		'a':'s',
		's':'d',
		'd':'f',
		'f':'g',
		'g':'h',
		'h':'j',
		'j':'k',
		'k':'l',
		'l':';',
		'z':'x',
		'x':'c',
		'c':'v',
		'v':'b',
		'b':'n',
		'n':'m',
		'm':',',
		'[':']',
		']':'\\',
		';':"'",
		',':'.',
		'.':'/'
	}
side = str(raw_input())
word = str(raw_input())
b = ''
if(side=='R'):
	for i in word:
		b = b+r[i]
elif(side=='L'):
	for i in word:
		b = b+l[i]
print b
