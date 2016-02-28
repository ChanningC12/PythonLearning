#is_even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print (is_even(8))

#is_int
def is_int(x):
    x=abs(x)
    if x==0:
        return True
    elif round(x)/x == 1:
        return True
    else:
        return False
print (is_int(98.6))

#digit_sum
def digit_sum(x):
    convert=str(x)
    total=0
    for i in convert:
        i=int(i)
        total += i
    return total
print (digit_sum(4134))

#factorial
def factorial(x):
    if x==1:
        return x
    else:
        return x*factorial(x-1)
print (factorial(4))

#is_prime
def is_prime(x):
    if x<2:
        return False
    for n in range(2,x):
        if x%n == 0:
            return False
        else:
            return True
print (is_prime(5))


#reverse
def reverse(text):
    result=""
    le=len(text)
    for index in range(le):
        result += text[le-1-index]
    return result
print (reverse("abcd"))

#anti_vowel
def anti_vowel(text):
    text=str(text)
    back=[]
    for i in text:
        if i not in "aeiouAEIOU":
            back.append(i)
    return "".join(back)

#scrabble score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    word=word.lower()
    points=0
    for char in word:
        points += score[char]
    return points
print (scrabble_score("cc"))


#censor
def censor(text,word):
    new_text=""
    while len(text)>0:
        check=text[0:len(word)]
        if check==word:
            add_text="*" * len(word)
            text=text[len(word):]
        else:
            add_text=text[0]
            text=text[1:]
        new_text += add_text
    return new_text
print (censor("Qifeng is sb","sb"))

#count
def count(sequence,item):
    total=0
    for i in sequence:
        if item == i:
            total+=1
    return total
print (count([1,2,3,4,5,6,4,3,4,2,3,4,3,4,3],3))

#purify
def purify(x):
    finalist=[]
    for i in x:
        if i % 2 == 0:
            finalist.append(i)
    return finalist
cc=[1,2,3,4,5,6,7]
print (purify(cc))


#product
def product(list_integers):
    total=1
    for i in list_integers:
        total*=i
    return total
print (product([1,2,3,4,5]))

#remove duplicates
def remove_duplicates(text):
    cleaned=[]
    for i in text:
        if i not in cleaned:
            cleaned.append(i)
    return cleaned
print (remove_duplicates("qqqqqqiiiifenggg"))



#median
def median(x):
    l=x
    l.sort()
    if len(l) % 2==0:
        n=len(l)/2
        return (l[n]+l[n-1])/2
    elif len(l)==1:
        return l[0]
    else:
        n=len(l)/2
        return l[n]
print (median([2,3,4,2,42,45,31,43,22,12,41,23,6,72])
