SELECT      MAX(num) as num
FROM        MyNumbers
WHERE       2 > (SELECT    COUNT(num)
                 FROM      MyNumbers as MyNums2
                 WHERE     MyNums2.num = MyNumbers.num);