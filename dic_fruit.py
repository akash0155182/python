def remove_print(fname,dic_fruit):
    if fname in dic_fruit:
        print(fname,dic_fruit[fname])
        dic_fruit.pop(fname)


if __name__=="__main__":
    fname=input("enter the fruit name::")
    dic_fruit={"apple":20,"pineapple":30,"banana":40}
    remove_print(fname,dic_fruit)
    print(dic_fruit)
