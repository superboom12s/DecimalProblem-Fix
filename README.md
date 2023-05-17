# Python-decimal-problem-fix

This library fixes two decimal problems of Python 3:

# Adding or substracting decimal numbers:
An example of this decimal problem is 0.1 + 0.2 = 0.30000000000000004, its obviously 0.3 but python says that is 0.30000000000000004. This library fixes that; when using the library funtions (sum() or min()) it will always return the correct result.
# Using laaaaarge decimals:
When saving a large float into a variable or simply operating with it it will automactly round itself, for example, 4.99999999999999999999999999999999999999999999999 would be stored as a 5.0 or a 5 (depending on your decimal library), the solution is store it as a string but you cant operate with strings, and if you turn it into a decimal it will be rounded into 5, but with this library you can operate with string-numbers to get the most exact result (String_Sum() to add, String_Min() to substract, String_Mult() to multiply and String_Div() to divide).
# Getting help with the library
If you dont know how to use something, just use help() and it should help you.
You can also specify on what to get help, just use help(parameter).
Also you can type the name of a function in your IDE and the IDE will help you with that function if you put you mouse on the function.
If you still have any doubts you can ask me personally :>
