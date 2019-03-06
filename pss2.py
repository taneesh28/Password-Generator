import random

vocab = ['hiljmklzdbn', 'hello', 'khdczcsdfvsdg', 'czxcsdxcfgvfsdf', 'ascfcsddffgvdf', 'accsaddfvbxc', 'asdcsdxcvbxc', 'adasasdvbxcas', 'sadxvbxcdasd', 'dasxfcfvxda',
         'adavbxvsd', 'asdasxvxcas', 'axvbxdasdas', 'xcvxcxcvxxcv']
splchar = ['!', '@', '#', '$', '%', '^', '&', '*', '~']
vo = random.choice(vocab)
sp = random.choice(splchar)
sp1=random.choice(splchar)
pas = sp + vo + sp1
#print(pas)
x=int(input("Enter number of password you want to see: "))
def jumble(new):
    new_word = list(new)        # converting string value into list item
    '''
    s=len(new_word)
    print(s)
    '''
    random.shuffle(new_word)    #shuffle  list item
    #print( ''.join(new_word))
    h=new_word[0:7]              #making condition to have 7 charater
    print( ''.join(h))           #again convert list item into string


for i in range(x):
    jumble(pas)


     

