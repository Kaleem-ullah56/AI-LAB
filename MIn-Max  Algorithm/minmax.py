# Here Math FUNCTION was imported by me so that i can use mathematical functions
import math

#if leaf node is reached in code return the value
def minmax(Dep, node_index, maxi,value,targetdep):
    if Dep==targetdep:
        return value[node_index]
    if maxi:
       #IF PLAYER PICK HIGH VALUE(MAXIMIZE)
       #Dep +1 adds new level to depth, node_index*2 tells us about left child if we 
       #add 1 in it will tell right child 
       # True means max player turn False means min player turn
       left_area = minmax(Dep +1 , node_index*2, False, value,targetdep)
       # its for right side
       right_area= minmax(Dep+1, node_index*2+1, False , value, targetdep)
       return max(left_area, right_area)
    else:
        # MINIMIZE IF PLAYER PICK LOW VALUE
        #node*2 tells about left side
        left_area = minmax(Dep +1, node_index*2, True, value, targetdep)
        #addition of 1 in node*2 tells about right side
        right_area=minmax(Dep+1 , node_index*2+ 1, True , value,targetdep)
        return min(left_area, right_area)
value= [3,5,2,9,3,5,2,9]
# Here we used a logrithm where the value of 2 will have power that will be equal to 8. 
# so 2's power 3 is 8. so tree depth is3 
treedep= math.log(len(value), 2) 
result=minmax(0,0,True,value,treedep)
print("The value is",result)