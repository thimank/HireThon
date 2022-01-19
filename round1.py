items=input("Enter the vegetables/fruits available (item1,item2,..) :").split(",")
weights=list(map(int,input("Enter the respective weights (weight1,weight2,..) :").split(",")))
profits=list(map(int,input("Enter the respective profits (profit1,profit2,..) :").split(",")))
maxWeight=int(input("Max carrying weight :"))

pList=[]

#Calculating the list of profit from each item and Storing in pList
for i in range(len(items)):
    x=int(maxWeight/weights[i])*profits[i]
    pList.append(x)

#pIndex indicates the index of most profitable item
pIndex=pList.index(max(pList))
print("Maximum Profit from :",int(pList[pIndex]/profits[pIndex]),items[pIndex])