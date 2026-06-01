def func(p1, *args, K,**kwargs):
    print("positional-or-keyword:.....{},{}".format(p1,p2))
    print("var-positional (*args)...{}".format(args))
    print("keywords:........................{}".format(K))
    print("var-keyword:.....................{}".format(kwargs))


func(10,3,4,5,K=6, Key1=1, Key2=2)
