import time

print 'Enter GPIO number:'
gpio = raw_input()
print 'Enter number of blinks'
blinks = raw_input()

#Make sure resource is available
try:
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(gpio))
    f.close()
except IOError as e:
    lol=0

#Export pin number
f= open ('/sys/class/gpio/export','w')
f.write(str(gpio))
f.close()

#Define Pin Direction as Output for LED

path = '/sys/class/gpio/gpio' + gpio + '/direction'
f= open (path,'w')
f.write('out')
f.close()

#Loop through LED 'ON' and 'OFF' for the number of times specified
i=0;
path = '/sys/class/gpio/gpio' + gpio + '/value'
while(i<int(blinks)):
    
    f= open (path,'w')
    f.write('1')
    f.close()

    time.sleep(0.5)

    f= open (path,'w')
    f.write('0')
    f.close()

    time.sleep(0.5)
    i+=1

#Unexport Pin 
f= open ('/sys/class/gpio/unexport','w')
f.write(str(gpio))
f.close()
print 'Cool blinking, huh?'
print 'Have a nice day!'
print 'Best wishes, Semillero ADT'

