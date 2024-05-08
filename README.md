# **DecimalProblem-Fix 1.7**

This library **fixes two decimal problems** with Python 3:

## Adding or substracting decimal numbers:
An _example_ of this decimal problem is _0.1 + 0.2 = 0.30000000000000004_, its obviously _0.3_ but **python says that is _0.30000000000000004_**. **This library fixes that**; when using the library funtions (`Dadd( number1, numer2 )` or `Dsub( number1, number2 )`) it will always return the **correct result**.
## Using laaaaarge decimals:
When saving a **large float** into a variable or simply operating with it **it will automactly round itself**, for example, _4.99999999999999999999999999999999999999999999999_ would be stored as a _5.0_ or a _5_ (depending on your decimal library), **the solution is stored as a string but you cant operate with strings**, and if you turn it into a decimal it will be rounded into 5, but **with this library you can operate with _string-numbers_** to get the most exact result (`String_add()` to add, `String_add()` to substract, `String_Mult()` to multiply and `String_Div()` to divide).
# Why using this library
This library is meant for people who just doesnt like maths but still need them, specifically decimals.
If you are more skilled at maths, you can just use fractions, but you can still using this library for irrational numbers, for example, as them require various values if you dont wanna use simple decimal numbers.

I _should_ make this library compatible with fractions _(the divide feature is bugged and doesnt work)_, but im way too lazy and no one is going to use this library anyway, im so sure that i bet that if you are really reading this, is because you are just very curius with computer's decimal problem and if you download this library, is just for testing that it actually works. If this is your case, i appreciate it anyways, thanks!
# Getting help with the library
**If you dont know how to use something, just use `help()` and it should help you.**
You can also specify on what to get help, just use `help(parameter)`.
Also you can type the name of a function in your **IDE** and the **IDE will help you with that function** if you put you mouse on the function.
If you still have any doubts or you find another decimal problem you can pubish an issue with your problem and ill reply as fast as i can.

🧃🧃🧃
