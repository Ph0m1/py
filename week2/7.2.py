from functools import reduce
def method_1():
    try:
        #Transforming string to list type directly,it will include the char of ' ', but it isn't a trouble for this question's context.
        s=list(input())
        deleteChar=input().strip()
        print("result",reduce(lambda x,y:x+y,map(lambda x:'' if x.upper().__eq__(deleteChar.upper()) else x,s)).strip(),sep=":")
    except Exception as e:
        print("inputing error!",e,sep="\n")
def method_2():
    s=input()
    dec=input().strip()
    s=s.replace(dec.upper(),'')
    s=s.replace(dec.lower(),'')
    print("result:",s.strip())                                                                                                 
def method_3():
    i=0
    s=list(input())                                                                                                                          
    dec=input().strip()
    while i<len(s):
        if s[i].__eq__(dec.upper()) or s[i].__eq__(dec.lower()):
            s.remove(s[i])
            i-=1
        i+=1
    print("result:",reduce(lambda x,y:x+y,s).strip())
#-------
#method_1()
#method_2()
method_3()
