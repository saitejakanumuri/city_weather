import random
print('welcome to passcode generator!!')
charset = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','.','/',';','[',']','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','~','`','_','+','<','>','?',':','"','{','}','|','A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M',',']
l=len(charset)
print(l)
length=int(input("enter your password length: "))
number_of_passwords=int(input("enter how many password samples to generate: "))
l1=[]
while number_of_passwords!=0 :
     l1=random.choices(charset,weights=[1,2,3,4,5,6,7,8,9,10]*9,k=length)
     l1= ''.join(l1)
     print(l1)
     number_of_passwords-=1


