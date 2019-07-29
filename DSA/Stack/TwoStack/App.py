from TwoStack import TwoStack

ts = TwoStack(5) 
ts.push1(5) 
ts.push2(10) 
ts.push2(15) 
ts.push1(11) 
ts.push2(7) 
  
print("Popped element from stack1 is " + str(ts.pop1())) 
ts.push2(40) 
print("Popped element from stack2 is " + str(ts.pop2()))