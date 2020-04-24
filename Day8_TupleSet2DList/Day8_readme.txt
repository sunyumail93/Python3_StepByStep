8, 2020-04-24
Aim: Besides list and dictionary, there are more objects/data structures: tuple, set and two dimensional list (array)
Tuple: (1,2,3,¡¯string¡¯,1,2,3), different to List, Tuple is unmutable, so you cannot append or change values. Same as List, Tuple and can store repeated, different types of values.
    But Tuple can only be created directly, or converted from a List (or Set). Looping through a Tuple is 10 times faster than looping a List. You can iterate Tuple by t[0]
Set: {'Idrish', 'Archi', 'Jay¡¯}, non-repetitive list, faster then list. Set doesn¡¯t have order, and it will display by a default order. You cannot iterate set by s[0]
    Set can be modified, or converted from a List or Tuple.
2D List/Nested List: Can be used to represent matrix, 2D, 3D, etc.
Here is the question: 
1, Import ATACseq peaks and store chromosome and length information using Tuples
2, Count how many chr appeared using Set
3, Get a distribution of peak lengths using 2D list (count by every 100 nt window from 0-1000 nt, and then >1000 nt)

Some notes:
1, When creating 2D Lists, every list need to be different, rather than a repeating of same list:
Histogram=[0]*(len(Windows)-1)
for i in range(len(Chr)):
    Matrix.append(Histogram)    #This means the same list Histogram repeats len(Chr) times, so every time all the Lists will change at the same time
Here is the correct way:
for i in range(len(Chr)):
    Matrix[i]=[0]*(len(Windows)-1)    #They are true 0, rather than same List
2, When using Set, you can add each value every time, or you can create a List, and convert to Set
3, 2D List can be converted to Pandas DataFrame directly, which will provide a better look of the format
    Day8_TupleSet2DList.py ATACseq.Peaks.txt Output.csv
