# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
def funargs(normal, *args,**kwargs):
    print(normal)

    for item in args:
        print(item)
    print("\nNow I would introduced some heros")

    for key, value in kwargs.items():
        print(f"{key} is a {value}")

    # print(type(args))
    # print(args)
roh = ["Harry","Rohan","Hamad","Skillf","Shivam","Aayush"]
normal = "I am normal argumant and students are"

kw = {"Rohan":"Monitor","Harry":"Fitness Instructor","Nihal":"Coordinator","Shivam":"Cook"}
funargs(normal,*roh,**kw)

