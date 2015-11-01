## FILE IO
print("training...")
labels = ('spam','ham')
def uniq_words(filename):
   with open(filename) as myfile:
  	return set(myfile.read().split())
bags ={l:[uniq_words(l+str(i)+'.txt')
   	for i in range(5)]
  	for l in labels}



## COMPUTE WORD ASSOCIATIONS
print("word...")
def compute_freqs(baglist):
   freqs={}
   for bag in baglist:
     for word in bag:
       if word not in freqs:
         freqs[word] = 0.0
       freqs[word] += 1.0/len(baglist)
   return freqs
class WordCounter:
   def __init__(self, freqs, num_docs):
  	self.freqs = freqs
  	self.num_docs = num_docs
   def __getitem__(self, word):
     if word not in self.freqs:
      self.freqs[word] = 0.0
     return (1.0+self.freqs[word]) / (1.0+self.num_docs)
freqs = {l:WordCounter(compute_freqs(bags[l]), len(bags[l]))
     	for l in labels}
def words_given_label(wordset, label):
   product = 1.0
   for word in wordset:
   	product *= freqs[label][word]
   return product
def label_given_words(wordset, label,prior):
  ps={l:words_given_label(wordset, l) for l in labels}
  total = sum(ps[l] for l in labels)
  return (ps[label]/total) * prior



## CLASSIFICATION
print("ready!...")
while True:
  wset = uniq_words(input("filename?"))
  prob_spam = label_given_words(wset,'spam',0.25)
  if prob_spam > 0.1:
 	print("SPAM!", prob_spam)
  else:
 	print("ham.", prob_spam)


