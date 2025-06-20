input1=input("please enter first number:")
a=float(input1)
input2=input("please enter second number:")
b=float(input2)
operation=input("please enter operation(add,sub,mul,div):")
	
class Calculator:
    def _init_(self,a:float,b:float,op:str):
	      self.a=a
        self.b=b
        self.operation=op.lower()
	        
	  def calculate(self):
	      if self.operation == 'add':
            return self.a + self.b
	       elif self.operation == 'subtract':
	          return self.a - self.b
        elif self.operation == 'multiply':
	          return self.a * self.b
        elif self.operation == 'divide':
            if self.b != 0:
	               return self.a / self.b
	          else:
	              return "Error: Division by zero"
	      else:
	           return "Error: Invalid operation"

	    
calc=Calculator(a,b,operation)
result=calc.calculate()
print(result)
