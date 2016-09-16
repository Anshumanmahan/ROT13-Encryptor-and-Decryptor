#Thanks to Mr. Robot S02E11
#Made by Anshuman Dixit
#happy messaging.
import time as t
s = ''
print "1 for Encryption || 2 for Decryption"
z = raw_input()
#Entering the sentence.
print "Enter the word/sentence"
a = raw_input()
if z == '1':
	print "\nEncrypting!!\n"
else:
	print "\nDecrypting!!\n"
#Using ROT13 Algorithm.
t.sleep(2)
for i in range(len(a)):
	if(a[i] <= 'm'):
		s += chr(ord(a[i]) + 13)
	else:
		s += chr(ord(a[i]) - 13)
print s
