#Kerem Kok
#3/7/21
#A function that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs.


mainlist=["pan, paper, idea, rope, groceries"]
debuffs=["slow"]
list1=["rope, coat, first aid kit, notslow"]
list2=["pan, groceries, notsmall"]
list3=["pen, paper, idea, noConfusion"]
if list1 in mainlist:
    print("Task 1 Completed")
else: 
    print("Task 1 Incomplete")
if list2 in mainlist:
    print("Task 2 Completed")
else:
    print("Task 2 Incomplete")
if list3 in mainlist:
    print("Task 3 Completed")
else:
    print("Task 3 Incomplete")
