from  tkinter import *
root = Tk()
root.title('Basic Calculator')
result = ''
Array = []
def refresh(body,X,Y,paste):
	l = Label(body,text='                                            ')
	l.place(x=X,y=Y)
	l=Label(root, text=paste)
	l.place(x=X,y=Y)
	return None

def ipt(txt):
	global result
	if '|' in result:
		index = result.index('|')
		result = result[:index+1] + txt + result[index+1:]
		refresh(root,350,100,result)
	else:
		result = result + txt
		refresh(root,350,100,result)

def ADD():
	global result
	if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '^' or result[-1] == '√':
		result = result[:-1] + '+'
		refresh(root,350,100,result)
	else:
		ipt('+')
		refresh(root,350,100,result)

def SUB():
	global result
	if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '^' or result[-1] == '√':
		result = result[:-1] + '-'
		refresh(root,350,100,result)
	else:
		ipt('-')
		refresh(root,350,100,result)

def MUL():
	global result
	if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '^' or result[-1] == '√':
			result = result[:-1] + '*'
			refresh(root,350,100,result)
	else:
		ipt('*')
		refresh(root,350,100,result)
	

def DIV():
	global result
	if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '^' or result[-1] == '√':
		result = result[:-1] + '/'
		refresh(root,350,100,result)
	else:
		ipt('/')
		refresh(root,350,100,result)


def basic_exec(Array):
	index0 = 0
	index = 0
	index2 = 0
	count = 0
	if Array[0] == '√':
		output = float(Array[1])
	else:
		output = float(Array[0])
	while index0 < len(Array):
		c = Array[index0]
		if c == '√':
			if float(Array[index0+1]) < 0:
				l=Label(root, text='try to get the square root of a negative number. return the positive value')
				l.place(x=40,y=250)
				Array[index0] = (float(Array[index0+1]) ** 2) **0.25
				index0 += 1
				del Array[index0]
				print(Array)
			else:
				Array[index0] = float(Array[index0+1])**0.5
				index0 += 1
				del Array[index0]
				print(Array)
		elif c == '^':
			Array[index0-1] = float(Array[index0-1])**float(Array[index0+1])
			del Array[index0]
			del Array[index0]
			print(Array)
		else:
			index0 += 1
	while index < len(Array):
		cur = Array[index]
		if cur == '*':
			Array[index-1] = float(Array[index-1]) * float(Array[index+1])
			del Array[index]
			del Array[index]
		elif cur == '/':
			if Array[index+1] == '0':
				l=Label(root, text='you cannot divide by 0')
				l.place(x=40,y=250)
				l=Label(root, text=result)
				l.place(x=350,y=100)
				return None
			Array[index-1] = float(float(Array[index-1]) / float(Array[index+1]))
			del Array[index]
			del Array[index]
		elif cur == '+' or cur == '-':
			count = 1
			index += 1
		else:
			index += 1
	if count == 0:
		txt = 'the answer is ' + str(Array[0])
		refresh(root,350,80,txt)
		l=Label(root, text=result)
		l.place(x=350,y=100)
		l=Label(root, text='                                                   ')
		l.place(x=40,y=250)
		print(f'the answer is {Array[0]}')
		return Array[0]
	else:
		output = float(Array[0])
		for index2 in range(len(Array)):
			if Array[index2] == '+':
				output += float(Array[index2+1])
				index2 += 1
			elif Array[index2] == '-':
				output -= float(Array[index2+1])
				index2 += 1
		txt = 'the answer is ' + str(output)
		refresh(root,350,80,txt)
		l=Label(root, text='                                                   ')
		l.place(x=40,y=250)
		l=Label(root, text=result)
		l.place(x=350,y=100)
		print(f'the answer is {output}')
		return output

def EXEC():
	global Array
	l=Label(root, text='                                         ')
	l.place(x=350,y=100)
	Array = []
	global result
	print(result)
	if result == '':
		l=Label(root, text='empty input')
		l.place(x=40,y=250)
	elif result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[0] == '+' or result[0] == '-' or result[0] == '*' or result[0] == '/' or result[0] == ')' or result[-1] == '(' or result[0] == '^' or result[-1] == '^' or result[-1] == '√':
		l=Label(root, text='dont start or end with calculation signs')
		l.place(x=40,y=250)
		l=Label(root, text=result)
		l.place(x=350,y=100)
	else:
		if '|' in result:
			id_x = result.index('|')
			result = result[:id_x] + result[id_x+1:]
			l=Label(root, text=result)
			l.place(x=350,y=100)
		Act = False
		for item in result:
			if item == '.':
				if Act == True:
					l=Label(root, text='invalid input')
					l.place(x=40,y=250)
					l=Label(root, text=result)
					l.place(x=350,y=100)
					return None
				else:
					Act = True
			elif item == '+' or item == '-' or item == '*' or item == '/' or item == '(' or item == ')' or item == '^' or item == '^':
				Act = False
		front = 0
		back = 0
		b0 = 0
		b1 = 0
		for fi in result:
			if fi == '(':
				b0 += 1
			elif fi == ')':
				b1 += 1
		if b0 != b1:
			l=Label(root, text='incorrect brackets entered')
			l.place(x=40,y=250)
			l=Label(root, text=result)
			l.place(x=350,y=100)
			return None
		if '(' in result:
			print('find (')
			while front < len(result):
				current_fig = result[front]
				if current_fig == '.':
					if result[front-1] == '.' or result[front+1] == '.':
						l=Label(root, text=result)
						l.place(x=350,y=100)
						l=Label(root, text='invalid input')
						l.place(x=40,y=250)
						return None
				if current_fig == '(' or current_fig == '√':
					if result[back:front] != '' and ')' not in result[back:front]:
						Array.append(result[back:front])
					try:
						int(result[front-1])
						if front-1 >= 0:
							Array.append('*')
					except ValueError:
						pass
					if result[front-1] == ')' and front-1 > 0:
						Array.append('*')
					Array.append(current_fig)
					print(f'stage1: {Array}')
					front += 1
					back = front
					if current_fig == '(':
						b0 += 1
				elif current_fig == ')':
					if result[front-1] == '+' or result[front-1] == '-' or result[front-1] == '*' or result[front-1] == '/' or result[front-1] == '(':
						l=Label(root, text='invalid input')
						l.place(x=40,y=250)
						l=Label(root, text=result)
						l.place(x=350,y=100)
						return None
					if result[front-1] != ')':
						Array.append(result[back:front])
					Array.append(current_fig)
					print(f'stage2:{Array}')
					front += 1
					b1 += 1
				elif current_fig == '+' or current_fig == '-' or current_fig == '*' or current_fig == '/' or current_fig == '^' or current_fig == '√':
					try:
						int(result[back:front])
						Array.append(result[back:front])
					except ValueError:
						pass
					Array.append(current_fig)
					front += 1
					print(f'stage3:{Array}')
					back = front
				else:
					front += 1
			try:
				r = int(result[back:len(result)])
				Array.append(r)
			except ValueError:
				pass
			print(f'the array is {Array}')
		else:
			while front < len(result):
				current_fig = result[front]
				if current_fig == '.' and front != len(result)-1:
					if result[front-1] == '.' or result[front+1] == '.':
						l=Label(root, text='invalid input')
						l.place(x=40,y=250)
						l=Label(root, text=result)
						l.place(x=350,y=100)
						return None
				if current_fig == '+' or current_fig == '-' or current_fig == '*' or current_fig == '/' or current_fig == '(' or current_fig == '^':
					Array.append(result[back:front])
					Array.append(current_fig)
					front += 1
					back = front
				elif current_fig == '√':
					if result[back:front] == '':
						Array.append(current_fig)
						front += 1
						back = front
					else:
						Array.append(result[back:front])
						Array.append('*')
						Array.append(current_fig)
						front += 1
						back = front
				else:
					front += 1
			Array.append(result[back:front])
			print(f'the array is {Array}')
		b_c = b1
		if b_c == 0:
			return basic_exec(Array)
		else:
			while b_c > 0:
				print('( found here, start to solve')
				b0 = 0
				b1 = 0
				Activated = False
				for i in range(len(Array)):
					if i >= len(Array):
						break
					c_fig = Array[i]
					if c_fig == '(':
						Activated = True
						b0 = i+1
					if c_fig == ')':
						if Activated:
							b_c -= 1
							print(f'b_c is {b_c}')
							del Array[i]
							c_list = Array[b0:i]
							del Array[b0-1]
							del Array [b0:i-1]
							Array[b0-1] = basic_exec(c_list)
							Activated = False
							i = 0
			return basic_exec(Array)
	
def clear():
	global result
	result = ''
	l=Label(root, text='                                         ')
	l.place(x=350,y=100)

def DEL():
	global result
	if '|' in result:
		index = result.index('|')
		result = result[:index-1]+result[index:]
		refresh(root,350,100,result)
	else:
		result = result[:-1]
		refresh(root,350,100,result)

def SQRT():
	global result
	if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '^' or result[-1] == '√':
		result = result[:-1] + '√'
		refresh(root,350,100,result)
	else:
		result = result + '√'
		refresh(root,350,100,result)

def PWR():
	global result
	if result[-1] == '+' or result[-1] == '-' or result[-1] == '*' or result[-1] == '/' or result[-1] == '^' or result[-1] == '√':
		result = result[:-1] + '^'
		refresh(root,350,100,result)
	else:
		result = result + '^'
		refresh(root,350,100,result)

def move1():
	global result
	if result == '':
		l=Label(root, text='empty input')
		l.place(x=40,y=250)
		return None
	else:
		if '|' not in result:
			result = result + '|'
			refresh(root,350,100,result)
		else:
			index = result.index('|')
			if index == 0:
				return None
			else:
				cache = result[index-1]
				result = result[:index-1] + '|' + cache + result[index+1:]
				refresh(root,350,100,result)

def move2():
	global result
	if result == '':
		l=Label(root, text='empty input')
		l.place(x=40,y=250)
		return None
	else:
		if '|' not in result:
			result = result + '|'
			refresh(root,350,100,result)
		else:
			index = result.index('|')
			if index == len(result)-1:
				l=Label(root, text='out of index')
				l.place(x=40,y=250)
				return None
			else:
				cache = result[index+1]
				result = result[:index] +  cache + '|' + result[index+2:]
				refresh(root,350,100,result)
 
A = Button(root, text ='1', command = lambda: ipt(txt='1'), padx=20,pady=10)
A.place(x=50, y=200)

B = Button(root, text ='2', command = lambda: ipt(txt='2'), padx=20,pady=10)
B.place(x=120, y=200)

C = Button(root, text ='3', command = lambda: ipt(txt='3'), padx=20,pady=10)
C.place(x=190, y=200)

D = Button(root, text ='4', command = lambda: ipt(txt='4'), padx=20,pady=10)
D.place(x=50, y=130)

E = Button(root, text ='5', command = lambda: ipt(txt='5'), padx=20,pady=10)
E.place(x=120, y=130)

F = Button(root, text ='6', command = lambda: ipt(txt='6'), padx=20,pady=10)
F.place(x=190, y=130)

G = Button(root, text ='7', command = lambda: ipt(txt='7'), padx=20,pady=10)
G.place(x=50, y=60)

H = Button(root, text ='8', command = lambda: ipt(txt='8'), padx=20,pady=10)
H.place(x=120, y=60)

I = Button(root, text ='9', command = lambda: ipt(txt='9'), padx=20,pady=10)
I.place(x=190, y=60)

J = Button(root, text ='+', command = ADD, padx=20,pady=4)
J.place(x=50, y=20)

K = Button(root, text ='-', command = SUB, padx=20,pady=4)
K.place(x=120, y=20)

L = Button(root, text ='*', command = MUL, padx=20,pady=4)
L.place(x=190, y=20)

M = Button(root, text ='/', command = DIV, padx=20,pady=4)
M.place(x=260, y=20)

N = Button(root, text ='0', command = lambda: ipt(txt='0'), padx=20,pady=10)
N.place(x=260, y=200)

O = Button(root, text ='C', command = clear, padx=20,pady=10)
O.place(x=260, y=130)

P = Button(root, text ='DEL', command = DEL, padx=13,pady=10)
P.place(x=260, y=60)

Q = Button(root, text ='(', command = lambda: ipt(txt='('), padx=20,pady=10)
Q.place(x=330, y=200)

R = Button(root, text =')', command = lambda: ipt(txt=')'), padx=20,pady=10)
R.place(x=400, y=200)

S = Button(root, text ='√', command = lambda: ipt(txt='√'), padx=18,pady=10)
S.place(x=330, y=130)

T = Button(root, text ='^', command = lambda: ipt(txt='^'), padx=18,pady=10)
T.place(x=400, y=130)

U = Button(root, text ='.', command = lambda: ipt(txt='.'), padx=18,pady=4)
U.place(x=330, y=20)

V = Button(root, text ='<-', command = move1, padx=15,pady=2)
V.place(x=330, y=260)

W = Button(root, text ='->', command = move2, padx=15,pady=2)
W.place(x=400, y=260)

Out = Button(root, text ='=', command = EXEC, padx=10,pady=4)
Out.place(x=400, y=20)


root.geometry("500x300+600+200")
root.mainloop()