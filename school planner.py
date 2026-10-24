from asyncio import gather


print ("smart school planner")
print ("anser three questoin and i will plan your day")
day =input("what day is it? Monday to Sunday").strip().capitalize()
weather=input("what is the weather sunny/rainy/cloudy").strip().lower()
homework=input("is yiur home work done yes or no")
print ("your plan for",day)
print("-"*35)
if day in("Saturday","Sunday"):
    print("day type:enjoy your free time")
     
