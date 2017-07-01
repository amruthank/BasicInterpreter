import os
import sys


'''
Token formats:
	Token(INTEGER,10)
	Token(PLUS,+)

'''
class Token(object):

	def __init__(self,type,value):
		self.type = type
		self.value = value
		
	def __str__(self):
		return 'Token ({type},{value})'.format(type = self.type,value=self.value)
		
	def __repr__(self):
		return self._str_()
		
		
class Interpreter(object):
	
	def __init__(self,text):
		self.text = text
		self.pos = 0
		self.cur_token = None
		
	def error(self):
		raise Exception("Error while parsing")
		
		
	def get_next_token(self):
		text = self.text
		
		if self.pos>len(text)-1:
			return Token("EOF",None)
		
		cur_char = text[self.pos]
		
		if cur_char.isdigit():
			token = Token("INTEGER", int(cur_char))
			self.pos += 1
			return token
		
		if cur_char == "+":
			token = Token("PLUS",cur_char)
			self.pos += 1
			return token
		
		if cur_char == "-":
			token = Token("MINUS",cur_char)
			self.pos += 1
			return token

		if cur_char == "*":
			token = Token("STAR",cur_char)
			self.pos += 1
			return token	

		if cur_char == "/":
			token = Token("DIV",cur_char)
			self.pos += 1
			return token		
			
		self.error()	
		
		
	def eat(self,type):
		if self.cur_token.type == type:
			self.cur_token = self.get_next_token()
		else:
			self.error()
			
			
	def expr(self):
		self.cur_token = self.get_next_token()
		
		left = self.cur_token
		self.eat("INTEGER")
		
		op = self.cur_token
		if op.type != "INTEGER":
			if op.type == "PLUS":
				self.eat("PLUS")
			elif op.type == "MINUS":
				self.eat("MINUS")
			elif op.type == "STAR":	
				self.eat("STAR")
			elif op.type == "DIV":	
				self.eat("DIV")	
				
		right = self.cur_token
		self.eat("INTEGER")
		
		if op.type == "PLUS":
			result = left.value + right.value
		elif op.type == "MINUS":
			result = left.value - right.value
		elif op.type == "STAR":
			result = left.value * right.value
		else:
			result = left.value / right.value
		
		return result
		
		
def main():
	while True:
		try:
			text = input('Expression> ')
		except EOFError:
			break
	
		if not text:
			continue
	
		interpreter = Interpreter(text)
		result = interpreter.expr()
			
		print(result)	
			

if __name__ == '__main__':
	main()