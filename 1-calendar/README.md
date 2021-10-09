# 1-calendar

Status:
Incomplete

Type:
Function

Description:
A function that helps orient the first day of a calendar month and structures the rest of the month accordingly. 

Details:
This function does not account for the change in days in other months and uses only 31 days. This is why the status is "Incomplete". I will consider it complete once the function can account for the change in days depending on the month, year, and if it is a leap year.

Currently, ```startDay``` is the first day of the month ranging from 1 to 7 with 1 being a Sunday and 7 being a Saturday.

For example:

```
$ calendar(6)

        January

                1  2 

 3  4  5  6  7  8  9 

10 11 12 13 14 15 16 

17 18 19 20 21 22 23 

24 25 26 27 28 29 30 

31

$ calendar(1)

        January

 1  2  3  4  5  6  7 

 8  9 10 11 12 13 14 

15 16 17 18 19 20 21 

22 23 24 25 26 27 28 

29 30 31 

```