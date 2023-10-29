# Python-decimal-problem-fix

This library fixes two decimal problems with Python 3:

# Adding or substracting decimal numbers:
An example of this decimal problem is 0.1 + 0.2 = 0.30000000000000004, its obviously 0.3 but python says that is 0.30000000000000004. This library fixes that; when using the library funtions (sum() or min()) it will always return the correct result.
# Using laaaaarge decimals:
When saving a large float into a variable or simply operating with it it will automactly round itself, for example, 4.99999999999999999999999999999999999999999999999 would be stored as a 5.0 or a 5 (depending on your decimal library), the solution is store it as a string but you cant operate with strings, and if you turn it into a decimal it will be rounded into 5, but with this library you can operate with string-numbers to get the most exact result (String_Sum() to add, String_Min() to substract, String_Mult() to multiply and String_Div() to divide).
# Testing tha library
I dont know why would you want to test the library, but you can.
When testing, the library will print the library result and the python's one.
Use help with test (help("test")) for getting help with test. :v
# Why using this library
This library is meant for people who just doesnt like maths but still need them, specifically decimals.
If you are more skilled at maths, you can just use fractions, but you can still using this library for irrational numbers, for example, as them require various values if you dont wanna use simple decimal numbers.

I should make this library compatible with fractions (the divide feature is bugged and doesnt work), but im way too lazy and no one is going to use this library anyway, im so sure that i bet that if you are really reading this, is because you are just very curius with computer's decimal problem and if you download this library, is just for testing that it actually works. If this is your case, i appreciate it anyways, thanks!
# Getting help with the library
If you dont know how to use something, just use help() and it should help you.
You can also specify on what to get help, just use help(parameter).
Also you can type the name of a function in your IDE and the IDE will help you with that function if you put you mouse on the function.
If you still have any doubts or you find another decimal problem you can ask me personally and ill surely reply :>

🧃🧃🧃
