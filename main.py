'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

# from typing import List
def peren(n):
    output = []
    s = [("",0,0)]
    
    while s:
        now,open_p,close_p = s.pop()
        
        if len(now) == 2*n:
            output.append(now)
            continue
        
        if open_p<n:
            s.append((now +'(',open_p +1 , close_p ))
        
            
        if close_p<open_p:
            s.append((now +')', open_p, close_p+1))
        
    return output


a =  peren(3)  
print(a)
