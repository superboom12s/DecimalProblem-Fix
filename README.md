# Pydepo
## A solution for Decimal problems in python 3

This library **fixes these two decimal problems** in Python 3:

- Precission.
    - Increases python precision with floats, but keeps using a hardware based decimal flotating point.
- Memory allocation.
    - Usually, floats have a limit of decimal characters of. But with this library, you will be able to use up to `2⁶³ - 2` digits, both integers and decimal places.

## Precision
When python operates decimal numbers, the result may not be the expected one, as it has its inprecissions.
An example of this, may be `0.1 + 0.2`. Despite being a simple operation, python returns `0.30000000000000004`.
This could affect equivalences, as `0.1 + 0.2 == 0.3` outputs `False`, so this could be a huge problem, but it is worse when lots of float operations are made, as this effect would accumulate.

Thankfully, this library is here to fix this, as `Dadd()` and `Dsub` allows you to add and substract decimal values while keeping the preccision on the result.

### Usage:
-  `Dadd( number1 , number2 ) == The correct result of number1 + number2`
-  `Dsub( number1 , number2 ) == The correct result of number1 - number2`

The numbers used for those methods can be both floats or integers and the output can also be both floats or integers.
> [!TIP]
> There isn't any functions for multiplications or divisions, as they aren't needed. Python's built in operations are good enough, even if the divisions may cause huge inprecissions when the amount of numbers it has to generate is a bit big.

## Memory Allocation:
Floats with long decimal characters will be rounded, as they do have a limit for their allocation. This makes operations that require long decimal values to be unable to be done or allocated in a variable. To prevent this, this library uses strings _(As they won't be rounded)_ to allocate floats and operate with them.  
An example of this problem could be `4.9999999999999999`, that would be instantly converted into `5.0`.

This will let the user to save up to `2⁶³ - 2` digits on a single variable (or `2³¹ - 2` on 32 bit systems), instead of the usual `15` decimal places python lets us to store.
> [!NOTE]
> You can obtain the maximun size of the decimal number for your computer with the method `sys.getsizeof()` _(not from this library)_.

### Usage:
-  `String_add( number1 , number2 ) == The correct result of number1 + number2`
-  `String_sub( number1 , number2 ) == The correct result of number1 - number2`
-  `String_mul( number1 , number2 ) == The correct result of number1 * number2`

The numbers used for those methods can be floats, integers or String-numbers and the output will be a String-number.
> [!IMPORTANT]
> I am working on a function to divide two String-numbers, but as python's built in method is extremely inexact upon creating more than `15` numbers, I may take some days to desing a beta function or a working method.  
> That would make posible the creation of large decimal numbers that could take advantage of this library.  
> See issue https://github.com/superboom12s/Pydepo/issues/4

🧃🧃🧃
