import colorama
from colorama import Fore,Back, Style


f=input("ENTER THE PASSWORD TO PROCCED :-")

if 'stark' in f:
    colorama.init()
    
  

    print( Fore.GREEN+'''
    ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
   ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
   ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
   ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                   ''')
    print(Fore.BLUE+"          ","MADE BY ANSHUMAAN SHARMA @ STARK IN INDIA")
    print(Fore.RESET)
    print(Fore.YELLOW)
   

      
      

    print("THIS TOOL HAS FOLLOWING FUNCTION WHICH ONE DO YOU WANT TO USE:-")
    print("1: CALCULATOR")
    print("2: TABLE OF ANY NUMBER")
    

    q=input("WHICH FUNCTION DO YOU WANT TO USE:-")
    print()
    if "1" in q:
        
        
        z=0
        while z<=100:
            a=int(input("enter a number :"))
            b=int(input("enter a number :"))
            c=input("enter task to be performed: ")
           
             
            if 'm' in c:
              
               d=a*b
               print("your required product is: ",d)
               print("")
               x=input("IF YOU WANT TO USE TABLES THEN ENTER:- T")
               if 't' in x:
                  z=0
                  while z<=100:
                 

                    a=int(input("Enter the number for Table : "))
                    b=int(input("Enter no.of Times you want the Table : "))
                    k=1
                    while k<=b:
                     
                       s=k*a
                       print("table of ",a,"*",k, "=", s)
                       k=k+1
            if 'd'  in c:
                n=a/b
                print("your required quotient is: ",n)
                print("")
                x=input("IF YOU WANT TO USE TABLES THEN ENTER:- T")
                if 't' in x:
                  z=0
                  while z<=100:
                    a=int(input("Enter the number for Table : "))
                    b=int(input("Enter no.of Times you want the Table : "))
                    c=1
                    while c<=b:
                       s=c*a
                       print("table of ",a,"*",c, "=", s)
                       c=c+1
        
            if 'su' in c:
               f=a-b
               print("your required difference is: ",f)
               print("")
               x=input("IF YOU WANT TO USE TABLES THEN ENTER:- T")
               if 't' in x:
                  z=0
                  while z<=100:
                      a=int(input("Enter the number for Table : "))
                      b=int(input("Enter no.of Times you want the Table : "))
                      c=1
                      while c<=b:
                         s=c*a
                         print("table of ",a,"*",c, "=", s)
                         c=c+1
            if 'a' in c:
              g=a+b
              print("your required sum is: ",g)
              print("")
              x=input("IF YOU WANT TO USE TABLES THEN ENTER:- T")
              if 't' in x:
                z=0
                while z<=100:
                   a=int(input("Enter the number for Table : "))
                   b=int(input("Enter no.of Times you want the Table : "))
                   c=1
                   while c<=b:
                       s=c*a
                       print("table of ",a,"*",c, "=", s)
                       c=c+1
if "2" in q:
   z=0
   while z<=100:
       a=int(input("Enter the number for Table : "))
       b=int(input("Enter no.of Times you want the Table : "))
       c=1
       while c<=b:
             s=c*a
             print("table of ",a,"*",c, "=", s)

             c=c+1
    

        
        
        
    
    


        
         
    
         
        
        
    
        
        
