def readIn():
    book = open('test.txt','r')
    line = []
    for item in book:
        item = item.lstrip() # 去除左边的空格
        if item != '':
            item = item.rstrip('\n') # 去除右边的换行
            item = item.rstrip() # 去除右边的空格,因为每个人打字习惯不同，有的在最后加空格，有的不
            line.append(item)
    book.close()
    print('book done')
    # 以空格切片
    words_and_punctuation = []
    for item in line:
        words_and_punctuation.extend(item.split(' ', -1 ))
    print('words_and_punctuation done')
    # 得到字母表
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    temp = []
    for item in alphabet:
        temp.append(item.upper())
    alphabet.extend(temp)
    # 去除标点
    words = []
    for item in words_and_punctuation:
        if item.isalpha():
            print(item)
            words.append(item)
        else:
            item = cut_punctuation(item,alphabet)
            if item != []:
                words.append(item)
    print('words done')
    return words
    
# 去掉标点 将 alphabet 导入则不需要每次都生成了，减少时间复杂度
def cut_punctuation(str,alphabet):
    str_to_list = list(str)
    list_to_str = ''
    check_whole_not_alphabet = 0
    while 1: # 但使用 ... 会删除不干净，故循环
        for item in str_to_list:
            if item not in alphabet:
                str_to_list.remove(item)
        list_to_str += "".join(str_to_list)
        if list_to_str.isalpha():
            check_whole_not_alphabet = 1
            break
    if check_whole_not_alphabet == 1:
        return list_to_str
    else:
        return []

words = readIn()
for i in words:
    print(i)



# print(item+"* *")
# print(item,"* *") # 中间有一个空格



class WordCount:
    def __init__(self,line = ''):
        self.line = line
    # def 

