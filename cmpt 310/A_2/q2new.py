$

d = [
    ['t','f'], ['t','f'],['t','f']
]

def isValid(x,y,z=None):

   if(x==y):
       return False
   if(z!=None):
       if(y==z):
        return False
   return True

a = True
def solution(d):
    for i in d[0]:
        for m in d[1]:
            if (isValid(i,m)== False):
                print("X ="+i+" Y = "+m+" Failure")
                a = False
                # break
            else:
                a = True
            if(a == True):
                for k in d[2]:
                    if (isValid(i,m,k)== False):
                        print("X ="+i+" Y = "+m+" Z = "+k +" Failure")   
                    else:
                        print("X ="+i+" Y = "+m+" Z = "+k+" Solution")
                  

solution(d)


 

