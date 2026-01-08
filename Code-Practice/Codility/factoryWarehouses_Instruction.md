Your factory has a number of warehouses, and all the

warehouses start empty. If a warehouse is empty before

goods are put into it for one day, it will be filled with

goods. If a warehouse is already full before goods are put

into it, it will overflow. Your goal is to prevent any

warehouse from overflowing.



You are given an integer array **puts** where



· **puts\[i] > 0** : represents that on the day i+1, the warehouse **puts\[i]** will receive goods and become full.

· **puts\[i] == 0** \[ represents that on the day i+1, no warehouse will receive goods, and you can choose a delivery fleet to empty one warehouse.



Please return an array **ans**

conditions:



. **len(ans) == len(puts)**

. If **puts\[i] > 0** ,then **ans\[i] == -1**

. If **puts\[i] == 0**, then **ans\[i]** is the warehouse you may choose to empty on the day i+1.



Note that if you choose to empty a full warehouse, it

becomes empty. However, if you choose to empty an

empty warehouse, nothing happens. If there are multiple

valid solutions, you may return any of them. If it is not

possible to prevent any warehouse from overflowing,

return an empty array.







###### Example 1:

Input: puts = \[1, 2, 3, 4]

Output: \[-1,-1,-1,-1]

Explanation:



· After the first day, the full warehouses are \[1].

· After the second day, the full warehouses are \[1, 2].

· After the third day, the full warehouses are \[1, 2, 3].

. After the fourth day, the full warehouses are \[1, 2, 3, 4]. No

warehouse can be emptied on any day, and no warehouse

will overflow.



###### Example 2:

Input: puts = \[1, 2, 0, 0, 2, 1]

Output: \[-1,-1,2,1,-1,-1]

Explanation:



· After the first day, the full warehouses are \[1].

. After the second day, the full warehouses are \[1, 2].

. After the third day, we emptied warehouse 2. So the

remaining full warehouses are \[1].

. After the fourth day, we emptied warehouse 1. So

temporarily, there are no full warehouses.

· After the fifth day, the full warehouses are \[2].

. After the sixth day, the full warehouses are \[1, 2]. In this

scheme, no warehouse will overflow. Additionally,

\[-1,-1,1,2,-1,-1] is another valid solution without any

warehouse overflow.



###### Example 3:

Input: puts = \[1, 2, 0, 1, 2]

Output:

Explanation:



. After the second day, the full warehouses are \[1, 2]. We can

empty one warehouse on the third day. But after the third

day, both warehouse 1 and warehouse 2 will receive goods

again. So no matter which warehouse we empty on the third

day, the other warehouse will overflow.



Constraints:



. 1 < puts.length <= 1000

· 0 <= puts\[i] <= 2000

