# prog-part-2
Perfilova Ganna IR-11 nomer 1
variant 3 skladnist' 3
ymova:
Write a function that takes an unsorted array of integers and returns the length of the longest peak subsequence. A minimum of 3 numbers is required to form a peak subsequence. A peak subsequence is defined as a sequence of numbers that starts with a smaller number, after which each subsequent number is strictly greater than the previous one until they reach the peak (the maximum value in the subsequence). All values after reaching the peak must always be strictly less than the previous one.
For example, a peak sequence can look like this:
1 7 2
Where 7 is the peak of the sequence.
1 2 3 - is not a peak sequence (missing the decreasing part).
3 2 1 - is also not a peak sequence (missing the increasing part).
-1 -5 -1 - is also not a peak sequence (you need to find a peak, not a valley).
There can be multiple peak subsequences in the array; you need to find the length of the longest one.
Example:
For the input array: [1, 3, 5, 4, 2, 8, 3, 7], the longest peak subsequence found has a length of 5 (1, 3, 5, 4, 2).
To verify the correctness of the implemented algorithm, you should use the unittest library and test the scenarios where:
• All array elements are sorted in ascending order.
• All array elements are sorted in descending order.
• The array consists of exactly 2 elements.
• The array does not contain any peak subsequences.
• The array contains 3 peak subsequences
(Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає довжину
найдовшої пікової підпослідовностію Для формування пікової підпослідовності
необхідно мінімум 3 числа. Пікова підпослідовність визначається як послідовність
чисел, яка починається з меншого числа, після чого наступне число строго більше
попереднього, поки вони не досягнуть вершини (максимального значення у
підпослідовності). Всі значення після досягнення вершини мають бути завжди меншими
від попередника. Наприклад, пікова послідовність може мати вигляд:
1 7 2
Де 7 - є вершиною послідовності
1 2 3 - не є піковою послідовністю (немає лівої частки)
3 2 1 - також не є піковою полідовністю (немає правої частки)
-1 -5 -1 - теж не є піковою послідовністю (необхідно знайти вершину, а не впадину)
У масиві може бути декілька пікових підпослідовностей, необхідно знайти довжину
максимальної
Приклад
Для вхідного масиву: 1, 3, 5, 4, 2, 8, 3, 7, знайдена найдовша пікова
підпослідовність має довжину 5 - 1, 3, 5, 4, 2
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку
`unittest` та перевірити сценарії коли:
всі елементи масиву посортовані за зростанням,
посортовані за спаданням,
масив з 2х елементів,
не містять пікових підпослідовностей,
містять 3 пікові послідовності)
