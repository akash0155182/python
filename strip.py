def remove_and_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
this="  akash is a good boy  "
n=remove_and_split(this,"akash")
print(n)
