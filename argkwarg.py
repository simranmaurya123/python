def funargs(nope ,*args,**kwargs):

    print(nope)
    for item in args:
        print(item)

    print("\nnow i would like to introduce some of the members")
    for key, value in kwargs.items():
        print(f"{key} is  {value}")


har = ["simran", "hanna", "scarlet", "33", "vhvvhvh"]
nope = "This is a normal argument"
kw = {"scarlet": "co-owner", "martha": "secretary", "helan": "director", "sarah": "founder", "sam": "bsds"}
funargs(nope, *har, **kw)

