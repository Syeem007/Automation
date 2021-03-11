
frequencies={}
file_contents=file_contents.split()
str1=''


for word in file_contents:
    str1=''.join(ch for ch in word if ch.isalnum())
    if str1.lower() not in uninteresting_words:
        if str1.lower() not in frequencies:
            frequencies[str1.lower()]=1
        else:
            frequencies[str1.lower()]+=1
