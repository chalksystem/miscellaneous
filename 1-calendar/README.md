# 1-calendar

Status:
Complete (Virtually)

Type:
Class

Description:
A class that returns a full calendar for any specified year. 

Details:
When initializing the class, the only input required is the desired calendar year. For example (using ipython):

```
In [1]: from main import calendar                                             

In [2]: thisYear = calendar(2021)                                             

In [3]: thisYear.getDays()                                                    

In [4]: thisYear.getCalendar()                                                


        January 

 S  M  T  W  T  F  S 

                1  2 

 3  4  5  6  7  8  9 

10 11 12 13 14 15 16 

17 18 19 20 21 22 23 

24 25 26 27 28 29 30 

31 


       February 

 S  M  T  W  T  F  S 

    1  2  3  4  5  6 

 7  8  9 10 11 12 13 

14 15 16 17 18 19 20 

21 22 23 24 25 26 27 

28 


          March 

 S  M  T  W  T  F  S 

    1  2  3  4  5  6 

 7  8  9 10 11 12 13 

14 15 16 17 18 19 20 

21 22 23 24 25 26 27 

28 29 30 31 


          April 

 S  M  T  W  T  F  S 

             1  2  3 

 4  5  6  7  8  9 10 

11 12 13 14 15 16 17 

18 19 20 21 22 23 24 

25 26 27 28 29 30 


            May 

 S  M  T  W  T  F  S 

                   1 

 2  3  4  5  6  7  8 

 9 10 11 12 13 14 15 

16 17 18 19 20 21 22 

23 24 25 26 27 28 29 

30 31 


           June 

 S  M  T  W  T  F  S 

       1  2  3  4  5 

 6  7  8  9 10 11 12 

13 14 15 16 17 18 19 

20 21 22 23 24 25 26 

27 28 29 30 


           July 

 S  M  T  W  T  F  S 

             1  2  3 

 4  5  6  7  8  9 10 

11 12 13 14 15 16 17 

18 19 20 21 22 23 24 

25 26 27 28 29 30 31 


         August 

 S  M  T  W  T  F  S 

 1  2  3  4  5  6  7 

 8  9 10 11 12 13 14 

15 16 17 18 19 20 21 

22 23 24 25 26 27 28 

29 30 31 


      September 

 S  M  T  W  T  F  S 

          1  2  3  4 

 5  6  7  8  9 10 11 

12 13 14 15 16 17 18 

19 20 21 22 23 24 25 

26 27 28 29 30 


        October 

 S  M  T  W  T  F  S 

                1  2 

 3  4  5  6  7  8  9 

10 11 12 13 14 15 16 

17 18 19 20 21 22 23 

24 25 26 27 28 29 30 

31 


       November 

 S  M  T  W  T  F  S 

    1  2  3  4  5  6 

 7  8  9 10 11 12 13 

14 15 16 17 18 19 20 

21 22 23 24 25 26 27 

28 29 30 


       December 

 S  M  T  W  T  F  S 

          1  2  3  4 

 5  6  7  8  9 10 11 

12 13 14 15 16 17 18 

19 20 21 22 23 24 25 

26 27 28 29 30 31 

```

