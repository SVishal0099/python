s="{()[}("
lst=[]
if len(s) % 2 != 0:
    print("Invalid Sequence")
else:
     for b in s:
        if b=="(" or b=="{" or b=="[":
            lst.append(b)
        elif b==")" or b=="}" or b=="]":
            cnt=len(lst)-1
            if b==")":
                if lst[cnt]=="(":
                    lst.pop()
                else:
                    print("Invalid Sequence")
            break
if b=="}":
 if lst[cnt]=="{":
  lst.pop()