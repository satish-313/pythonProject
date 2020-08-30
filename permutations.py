def compare(list1,list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            t = True
        else:
            return False
    return t

def permutation(model1,model2,index,check):
    for i,v in enumerate(model1):
        #print(i,":",v)
        if v == model2[index]:
            index = index + 1
            check.append(v)
            model1.pop(i)
            #print(len(model1))
            #print(check)
            if len(check) != len(model2):
                #print(len(check))
                if permutation(model1,model2,index,check):
                    return True
            else:
                break


    if compare(check,model2) and len(model1) == 0:
        #print("correct")
        f = True
    else:
        f = False

    if f:
        return True
    else:
        return False

def stringIntoList(model1):
    model = []
    for i in model1:
        model.append(i)
    return model

def listIntoString(model2):
    str1 = ""
    for ele in model2:
        str1 +=ele
    
    return str1

def main():
    print("If two string are each other permutation are not")
    model1 =  input("enter anything : ")#"abc"
    model1 = stringIntoList(model1)
    model2 = input("enter anything that is permutation of above : ")#"cba"
    model2 = stringIntoList(model2)
    #print(len(model2))
    index = 0
    check = []
    if permutation(model1,model2,index,check):
        model = listIntoString(model2)
        print("The permutation exit : ",model)
    else:
        print("permutaion does not exit")

if __name__ == "__main__":
    main()