# coding=utf-8

from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu

candidate = "There are the Haarrnes and six-point racing seat belts in the interior, and also with the intercom system."
reference1 = "The interior has racing seats and six-point harness belts, as well as an intercom system."
reference3 = "The interior is equipped with racing seats and six-point harness belts, and an intercom system."
reference2 = "The interior features racing seats and six-point seat belts, as well as an intercom system."
reference4 = "The interior has racing seats, six-point seat belts and also an intercom system."

c= word_tokenize(candidate)
r1= word_tokenize(reference1)
r2= word_tokenize(reference2)
r3= word_tokenize(reference3)
r4= word_tokenize(reference4)

weights = (0.4,0.3,0.2,0.1)

ref=[r1]
ref1=[r1,r2]
ref2=[r1,r2,r3]
ref3=[r1,r2,r3,r4]

bleu = sentence_bleu(ref,c,weights)
bleu1 = sentence_bleu(ref1,c,weights)
bleu2 = sentence_bleu(ref2,c,weights)
bleu3 = sentence_bleu(ref3,c,weights)

print ("\nBLEU score with single Reference sentence = ", bleu*100)
print ("BLEU score with one extra Reference sentence = ", bleu1*100)
print ("BLEU score with two extra Reference sentences = ", bleu2*100)
print ("BLEU score with three extra Reference sentences = ", bleu3*100)

print ("\n")



