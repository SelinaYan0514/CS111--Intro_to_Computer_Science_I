
#function 1
def double(s,c):
   """ return a new string in which all occurrences of c in s are doubled
       inputs s and c: an arbitrary string s and and a single-character string c
   """
   if s == '':
        return ''
   else:
        rest_double = double(s[1:],c)
        if s[0] == c:
            return 2 * s[0] + rest_double
        else:
            return s[0] +rest_double
        

#function 2
def process(vals,x):
    """ return a new list in which each element of the original list that is 
    larger than x is replaced with a 0
        inputs: a list of 0 or more integers vals and a single integer x
    """
    if vals == []:
        return []
    else:
        rest_process = process(vals[1:],x)
        if vals[0] > x:
            return [0] + rest_process
        else:
            return [vals[0]] + rest_process
        
        
#function 3
def mul_pairs(vals1, vals2):
   """  return a new list in which each element is the product of the elements
   at the corresponding positions in the original lists
       inputs: two lists of numbers, vals1 and vals2
   """
   if len(vals1) != len(vals2):
        return []
   elif len(vals1) == 0 or len(vals2) == 0:
        return []
   else:
        mul_rest = mul_pairs(vals1[1:], vals2[1:])
        return [vals1[0] * vals2[0]]+ mul_rest
    

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    #function 1
    print("double('banana','a') returns", double('banana','a'))
        
    #function 2
    print("process([5,8,3,12],15) returns", process([5,8,3,12],15))
    
    #function 3
    print("mul_pairs([5,2,3,4],[20,30,50,80]) returns", mul_pairs([5,2,3,4],[20,30,50,80]))
    
