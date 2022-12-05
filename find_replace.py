text= "Firedog"
oldText = "dog"
newText = "man"


def findAndReplace(text, oldText, newText):        
    replacedText = ''
    i = 0
    while i < len(text):
        if text[i:i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText)
        else:
            replacedText += text[i]
            i += 1
    return replacedText

print(findAndReplace(text, oldText, newText))

