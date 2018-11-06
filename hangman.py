

####################################################################
#ACADEMY OF TECHNOLOGY
#COPY RIGHT:-ACADEMY OF TECHNOLOGY
#PROGRAM DEVELOPED BY SOUVIK GHOSH
#UNDER THE GUIDANCE OF 
#1.ANAND JAISWAL
#2.SHAKSHI BAID
#3.ZEESHAN MEHBOOB

####################################################################

import time,os,sys#random
##import py_compile
##py_compile.compile('hangman.py')
class score:
	def __init__(self):
		self.wrong=0
		self.crt=0
	def increase(self):
		self.crt+=1
		f=open("highest.txt","r")
		msg=f.read()
		f.close
		if eval(msg)<self.crt:
			f=open("highest.txt","w")
			f.write(str(self.crt))
			f.close
	def decrease(self):
		self.wrong+=1
	def reset(self):
		self.wrong=0
		self.crt=0
score1=score()


class scoreplayer2:
	def __init__(self):
		self.p1c=0
		self.p1w=0
		self.p2c=0
		self.p2w=0
	def reset(self):
		self.p1c=0
		self.p1w=0
		self.p2c=0
		self.p2w=0
	def wp1(self):
		self.p1c+=1
	def wp2(self):
		self.p2c+=1
	def lp1(self):
		self.p1w+=1
	def lp2(self):
		self.p2w+=1

score2=scoreplayer2()



def showchar(word1,s1):
	n=len(word1)
	for i in range(0,n-1):
		if s1[i]=="-":
			print word1[i],
			break

def printHello(word1):
	st=""
	for x in word1:
		
		if x=='\n':
			break
		e=ord(x)
		e-=1
		st=st+chr(e)
	st=st+"\n"
	return st



def play():
	t=time.localtime()
	n=t[5]

	i=1
	while i<n:
	 f.readline()
	 i=i+1
	word=f.readline()
	word=printHello(word)
	s="-"*(len(word)-1)
	print s,":",
	
	life=9


	flag=1
	hlp=1
	while life>1 and flag:
		if hlp==1:
			char=raw_input("(1 for lifehelp)")
		else:
			char=raw_input("")
		if (char.isdigit()==1) and hlp:
			showchar(word,s)
			life=life-1
			hlp=0
			printman(life)
			print s,":",
			continue
		if char in word:
			s=printname(word,s,char)
			print s,":",
		else:
			life=life-1
			printman(life)
			print s,":",
		if strcmp(s,word,len(word)-1):
			print "\n\n\tWelldone You win"
			score1.increase()
			print "\n\n\t Your Present SCORE is: CORRECT: ",score1.crt,",WRONG: ",score1.wrong
			flag=0 
	if life==1:
		print "		Correct answer is ",word
		score1.decrease()
		print "\n\n\t Your Present SCORE is: CORRECT: ",score1.crt,",WRONG: ",score1.wrong
	f.close


def player2(a,b):
	print "\n\n\tEnter the word for ",b,": ",
	x=raw_input("")
	print b," are you to GUESS",
	print ""
	time.sleep(2)
	s="-"*(len(x))
	print s,":",
	
	life=9


	flag=1
	hlp=1
	while life>1 and flag:
		if hlp==1:
			char=raw_input("(1 for lifehelp)")
		else:
			char=raw_input("")
		if (char.isdigit()==1) and hlp:
			showchar(x,s)
			life=life-1
			hlp=0
			printman(life)
			print s,":",
			continue
		if char in x:
			s=printname1(x,s,char)
			print s,":",
		else:
			life=life-1
			printman(life)
			print s,":",
		if strcmp(s,x,len(x)):
			print "\n\n\tWelldone You win"
			score2.wp2()
			print "\n\n\t Your Present SCORE is: CORRECT: ",score2.p2c,",WRONG: ",score2.p2w
			flag=0 
	if life==1:
		print "		Correct answer is ",x
		score2.lp2()
		print "\n\n\t Your Present SCORE is: CORRECT: ",score2.p2c,",WRONG: ",score2.p2w
	


	print "\n\n\tEnter the word for ",a,": ",
	x=raw_input("")
	print a," are you to GUESS",
	print ""
	time.sleep(2)
	s="-"*(len(x))
	print s,":",
	
	life=9


	flag=1
	hlp=1
	while life>1 and flag:
		if hlp==1:
			char=raw_input("(1 for lifehelp)")
		else:
			char=raw_input("")
		if (char.isdigit()==1) and hlp:
			showchar(x,s)
			life=life-1
			hlp=0
			printman(life)
			print s,":",
			continue
		if char in x:
			s=printname1(x,s,char)
			print s,":",
		else:
			life=life-1
			printman(life)
			print s,":",
		if strcmp(s,x,len(x)):
			print "\n\n\tWelldone You win"
			score2.wp1()
			print "\n\n\t Your Present SCORE is: CORRECT: ",score2.p1c,",WRONG: ",score2.p1w
			flag=0 
	if life==1:
		print "		Correct answer is ",x
		score2.lp1()
		print "\n\n\t Your Present SCORE is: CORRECT: ",score2.p1c,",WRONG: ",score2.p1w
	

def timeAttack():
	print "\n\n\tYou have to GUESS within 10 sec"
	t=time.localtime()
	n=t[5]
	tup=0
	i=1
	while i<n:
	 f.readline()
	 i=i+1
	word=f.readline()
	word=printHello(word)
	s="-"*(len(word)-1)
	t=time.localtime()
	n=t[5]
	a=t[4]
	print s,":",
	
	life=9


	flag=1
	hlp=1
	while life>1 and flag:
		if hlp==1:
			char=raw_input("(1 for lifehelp)")
		else:
			char=raw_input("")
		if (char.isdigit()==1) and hlp:
			showchar(word,s)
			life=life-1
			hlp=0
			printman(life)
			print s,":",
			continue
		if char in word:
			s=printname(word,s,char)
			print s,":",
		else:
			life=life-1
			printman(life)
			print s,":",
		if strcmp(s,word,len(word)-1):
			print "\n\n\tWelldone You win"
			score1.increase()
			print "\n\n\t Your Present SCORE is: CORRECT: ",score1.crt,",WRONG: ",score1.wrong
			flag=0 
		t=time.localtime()
		m=t[5]
		b=t[4]
		if (m-n)>=10 or a<b:
			tup=1
			break
		if life==1:
			print "		Correct answer is ",word
			score1.decrease()
			print "\n\n\t Your Present SCORE is: CORRECT: ",score1.crt,",WRONG: ",score1.wrong
	f.close
	if tup==1:
		print "\n\n\tTime Up"
		print "		Correct answer is ",word
		score1.decrease()
		print "\n\n\t Your Present SCORE is: CORRECT: ",score1.crt,",WRONG: ",score1.wrong






def printname1(word1,s1,char1):
	s2=""
	for i in range (0,len(word1)):
		if word1[i]==char1:
			s2=s2+char1
		else:
			s2=s2+s1[i]
	return s2










def printname(word1,s1,char1):
	s2=""
	for i in range (0,len(word1)-1):
		if word1[i]==char1:
			s2=s2+char1
		else:
			s2=s2+s1[i]
	return s2




def strcmp(str1,str2,l):
	for i in range(0,l): 
		if str2[i]!=str1[i]:
			return 0
	return 1




def printman(i):
	if i==8:
		print '''		|
		|
		|
		|
		|
		|
		|
	      _____'''
	elif i==7:
		print '''		 ________
		|
		|
		|
		|
		|
		|
		|
	      _____'''
	elif i==6:
		print '''		 ________
		|  /
		| /
		|/
		|
		|
		|
		|
	      _____'''
	elif i==5:
		print '''		 ________
		|  /    |
		| /     0
		|/      |
		|
		|
		|
		|
	      _____'''
	elif i==4:
		print '''		 ________
		|  /    |
		| /     0
		|/    / | 
		|
		|
		|
		|
	      _____'''
	elif i==3:
		print '''		 _________
		|  /     |
		| /      0
		|/     / | \\
		|
		|
		|
		|
	      _____'''
	elif i==2:
		print '''		 _________
		|  /     |
		| /      0
		|/     / | \\
		|       /
		|
		|
		|
	      _____'''
	else :
		print '''		 __________
		|  /      |
		| /       0 
		|/      / | \\
		|        / \\
		|
		|
		|
	      _____'''
		print "Game Over"

def help():
	print '''	WELCOME TO HANGMAN
HANGMAN-SIMPLE GAME WHERE YOU HAVE TO GUESS HIDDEN WORD
1 PLAYER
ONE PLAYER GAME YOU CAN CHOOSE CATEGORY OF THE WORD(MENU "SETTING")
FEATURES AVAILABLE:
ONE LETTER HINT-YOU CAN REVEAL
ONE LETTER FOR ONE "HANGMAN"
2 PLAYER
GAME FOR TWO PLAYER (ON ONE DEVICE) HRE ONE PLAYER SETS THE WORD FOR OTHER PLAYER
FOR GUESSING THE WORD PLAYER GETS ONE POINT
FEATURES AVAILABLE:
ONE LETTER HINT-YOU CAN REVEAL
ONE LETTER FOR ONE "HANGMAN" 
TIME ATTACK
IN TIME ATTACK YOU  HAVE TO GUESS 10 RANDOM WORDS IN THE SHORTEST TIME
FEATURES AVAILABLE:
ONE LETTER HINT-YOU CAN REVEAL
ONE LETTER FOR ONE "HANGMAN" '''


	
	




print "			WELCOME TO HANGMAN"
f=open("name.txt","r")
fl=0



while True:
	print "1.Play(1 Player)"
	print "2.Play(2 Player)"
	print "3.Time Attack"
	print "4.Score"
	print "5.Setting"
	print "6.Exit"

	n=eval(raw_input(""))
	if n==1:
		if fl==0:
			print "\n\n\tHint:It is your friend's name"
			
		play()
	elif n==2:
		if fl==0:
			print "\n\n\tHint:It is your friend's name"
		x=raw_input("\n\n\tEnter the name of player 1: ")
		y=raw_input("\n\n\tEnter the name of player 2: ")
		score2.reset()		
		while True:			
			player2(x,y)
			ch=eval(raw_input("\n\n\tTo play press <1>: "))
			if ch!=1:
				break
			f.seek(0,0)
	elif n==3:
		if fl==0:
			print "\n\n\tHint:It is your friend's name"
		while True:
			timeAttack()
			ch=eval(raw_input("\n\n\tTo play press <1>: "))
			if ch!=1:
				break
			f.seek(0,0)
	elif n==4:
		print "\n\n\tCorrect Answer: ",score1.crt
		print "\n\n\tWrong Answer: ",score1.wrong
	elif n==5:
		print "1.Choose word category"
		print "2.Help"
		print "3.Reset your score"
		print "4.Highest Score"
		n=eval(raw_input(""))
		if n==1:
			fl=1
			print "1.Country"
			print "2.Dishes"
			print "3.Name"
			print "4.Animal"
			n=eval(raw_input("Enter your choice:"))
			if n==1:
				f=open("country.txt","r")
			elif n==2:
				f=open("dishes.txt","r")
			elif n==3:
				f=open("name.txt","r")
			elif n==4:
				f=open("animal.txt","r")
			else:
				print "Invalid input...Try again"
		elif n==2:
			help()
		elif n==3:
			score1.reset()
		elif n==4:
			g=open("highest.txt","r")
			m=g.read()
			f.close
			print "\n\n\tHighest Score is ",m
		else:
			print "\n\n\t Invalid Choice"
	
	elif n==6:
		sys.exit()
	else:
		print "\n\n\tInvalid Choice...Try again"
	f.seek(0,0)

