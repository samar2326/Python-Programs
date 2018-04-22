"""WAP to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically."""
freq = {}   
line = input("enter the words :")
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words = sorted(words)

for w in words:
 print("%s:%d" % (w,freq[w]))
