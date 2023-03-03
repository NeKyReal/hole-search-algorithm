**+=========================================================================================+**

**English:**

**Simple educational search algorithm.** Searches for a hole in a user-defined field. 
From the mandatory conditions of its operation, the two holes must be separated from each other. There can be no holes on the edges (this vulnerability can be circumvented by creating a virtual wall near it, which the algorithm does), and the holes themselves can be of different shapes and sizes. The size of the structural element is 2X2.

The principle of the algorithm is simple - a structural element, 2 by 2 cells in size, walks through the field and counts the number of occupied cells, that is, the number of holes per structural element. Initially there are two null variables - **i** and **j**. When the algorithm is running, a simple condition is met:

+ if **number of holes ** = 1, then i = i + 1
+ if **number of holes** = 3, then j = j + 1, 

after that, the structural element is shifted one cell forward. At the end of the algorithm, the obtained values are entered into the formula: 

**N = (i - j) / 4**, where 
+ N - number of holes, 
+ i and j are the number of fragments of holes found by the structural element.

There are two files in the repository - main and algorithm. The program itself is located in the main file, in algorithm - the basic algorithm showing the essence of the work.

**+=========================================================================================+**

**Russian:**

**Простой учебный алгоритм поиска.** Осуществляет поиск отверстия на заданном пользователем поле. 
Из обязательных условий его работы, два отверстия должны быть разделены между собой. На края не может быть отверстия (данную уязвимость можно обойти, если создать возле нее виртуальную стену, что алгоритм и делает), а сами отверстия могут быть разной формы и размеров. Размер структурного элемента - 2Х2.

Принцип работы алгоритма прост - по полю ходит структурный элемент, размером 2 на 2 клетки, и подсчитывает количество занятых ячеек, то есть количество отверстий на один структурный элемент. Изначально есть две нулевых переменных - **i** и **j**. При работе алгоритма выполняется простое условие:

+ если **количество отверстий** = 1, то i = i + 1
+ если **количество отверстий** = 3, то j = j + 1, 

после чего структурный элемент сдвигается на одну клетку вперед. По окончанию работы алгоритма, полученные значения вносятся в формулу: 

**N = (i - j) / 4**, где 
+ N - количество отверстий, 
+ i и j - число найденных фрагментов отверстий структурным элементом.

В репозитории находится два файла - main и algorythm. Сама программа находится в файле main, в algorythm - базовый алгоритм, показывающий суть работы.

**+=========================================================================================+**
