#coding=utf-8


if __name__ == "__main__":
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")   
 
    # 用 - 将t中元素合并成一个新的字符串8
    str_demo = '-'.join(t)
    print(str_demo)    
 
    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)    
    
    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)

    source_str=u"it's my book, please show it, wa ka ka, yo yo yo!"
    print(source_str.find("please"))
    print(source_str.index("my"))

    print(source_str.rfind("please"))
    print(source_str.rindex("my"))

    des_str=source_str.replace("yo","ha",2)
    print(des_str)

    demo_str=" 前有空格 中 后  啊 "
    print(demo_str.lstrip())
    print(demo_str.rstrip())
    print(demo_str.strip())

    tuple1=[u"2018年加油",1,"deeptest"]
    tuple2=(10,5,18,100)
    tuple3=("a","d","g","b")
    print(len(tuple2))
    print(max(tuple3))
    print(tuple(tuple1))

    tuple_demo=("hello","appium","python3","test","good")
    print(tuple_demo[1])
    print(tuple_demo[-2])
    print(tuple_demo[1:])
    print(tuple_demo[1:4])
    print(tuple2+tuple3)
    # del tuple3
    # print(tuple3)
    print(tuple2*2)
    print(1 in tuple2)

    for t in tuple2:
        print(t)

    print("list操作")
    list1=[1,2,3,"test",u"朴慧尚",2]
    list2=[4,1,6,8]
    print(len(list1))
    list1.append("两三次")        
    print(list1.count("1"))
    list1.extend("10086")
    print(list1.index(2))
    list1.insert(-1,"中国")
    list1.pop()
    list1.remove(2)
    list1.reverse()
    list2.sort()
    list2.clear()
    list1.copy()
    list1[0]="哈哈"
    print(list1,list2)
    dict1={"name":"lilei","age":"18","kg":120}
    tup1=[1,2,3,4]
    print(len(dict1))
    str_d=str(dict1)
    print(str_d)
    print(type(str_d))

    dict_cp=dict1.copy()
    print(dict_cp)
    
    dict_new=dict.fromkeys(tup1,"啦啦")
    print(dict_new)

    v1=dict_new.get(12,u"我是默认值")
    print(v1)



