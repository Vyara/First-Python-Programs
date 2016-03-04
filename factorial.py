#-------------------------------------------------------------------------------
# Name:        factorial.py
# Purpose: A program that evaluates factorials of numbers.
#
# Author:      Vyara
#
# Created:     30/09/2012
# Copyright:   (c) Vyara 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

 print "This program calculates factorials of numbers"
 a = input("Enter a number: ")

 for i in range(1,a):
    a = i * a

 print "The answer is:",(a)
 raw_input ("Press Enter to exit.")
main()
