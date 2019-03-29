#!/bin/python3

"""  Problem Statement
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .

Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Function Description

Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

gradingStudents has the following parameter(s):

grades: an array of integers representing grades before rounding
Input Format

The first line contains a single integer, , the number of students. 
Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.

Constraints

Output Format

For each , print the rounded grade on a new line.

Sample Input 0

4
73
67
38
33
Sample Output 0

75
67
40
33"""

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    j=0
    res = list()                          # Empty list for assigning new grades
    for i in grades:
        if i>=38:                         # Check if the grade is greater then 38
            multiple_five = i+(5-(i%5))   # Find next multiple of 5 for current grade
            a = multiple_five - i         # Defference between next mult of 5 and the current grade
            if a < 3:                     # if the difference is greater than 3 then update the grade with the mult of 5
                res.insert(j,multiple_five)
                j+=1
                a=0
            else:
                res.insert(j,i)           # Otherwise no change in grade
                j+=1
                a=0
        else:
            res.insert(j,i)               # Otherwise no change in grade
            j+=1
            a=0

    return res                            # Return the new grades


if __name__ == '__main__':

    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
