def demo():
    global i
    print("Sagar Shinde Karad Training Sir 27 September",i)
    i=i+1
    if(i==50):
        return i
    demo()
i=0
demo()

