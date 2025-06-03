def Dadd(num1, num2):

  """
  This function fixes the way to add decimal numbers of Python.

  :param num1: number one (integer or float)
  :param num2: number two (integer or float)
  :return: Result (can be an integer or a float)
  """
  #Tries to obtain the exponent of 10 needed to convert the integer and decimal part into an integer. If the value is a float, it will turn the number into a string, split it on the '.' and obtain the lenght of the decimal part. If its an integer, it will set it to 1, as 10**0 is equal to 1. The functions tries it with both numbers separately cause there could be a decimal and an integer number.
  try:
      num1ex = len(str(num1).split('.')[1])
  except:
      num1ex = 1
  try:
      num2ex = len(str(num2).split('.')[1])
  except:
      num2ex = 1
    
  #Now, it checks the number with the highest exponent to convert the numbers into integers, operate with them and then transform them into floats again to return them.      
  if num1ex > num2ex:
      return (num1*10**num1ex + num2*10**num1ex) / 10**num1ex
  else:
      return (num1*10**num2ex + num2*10**num2ex) / 10**num2ex
     
        
def Dsub(num1, num2):
  """
    This function fixes the way to subtract decimal numbers of Python

    :param num1: number one (integer or float)
    :param num2: number two (integer or float)
    :return: Result (can be an integer or a float)
  """
    #Tries to obtain the exponent of 10 needed to convert the integer and decimal part into an integer.
    #If the value is a float, it will turn the number into a string, split it on the '.' and obtain the
    #lenght of the decimal part. If its an integer, it will set it to 1, as 10**0 is equal to 1.
    #The functions tries it with both numbers separately cause there could be a decimal and an integer number.
  try:
      num1ex = len(str(num1).split('.')[1])
  except:
      num1ex = 1
  try:
      num2ex = len(str(num2).split('.')[1])
  except:
      num2ex = 1
    
  #Now, it checks the number with the highest exponent to convert the numbers into integers, operate with them
  #and then transform them into floats again to return them.      
  if num1ex > num2ex:
      return (num1*10**num1ex - num2*10**num1ex) / 10**num1ex
  else:
      return (num1*10**num2ex - num2*10**num2ex) / 10**num2ex

def String_add(Snum1, Snum2):
    """
    This function is used to add a String-number to each other.
    
    Parameters
    ----------
    :param Snum1: Value 1 - Can be a String-number, integer or float.
    :param Snum1: Value 2 - Can be a String-number, integer or float.

    Raises
    ------
    Exception or TypeError
        In case of any value contains text or is not an integer, float or a string.

    Returns
    -------
    String
        The result of adding one number to the other in a String-number.
        
        It can be an integer or a float nested inside a string, but converting the string into any of these may not be the exact number this value contains.
    """
    
    #This block checks both numbers have correct values, if the format is incorrect,
    #it will be corrected unless its a boolean. Any type other than a string that is
    #able to be turned into a number, will return an exception.
    assert not(isinstance(Snum1, bool) or isinstance(Snum2, bool)), "String number expected, boolean value provided instead." #If any value was boolean, raise exception.
    
    Snum1 = str(Snum1) if isinstance(Snum1, (int, float)) else Snum1 #If any value is an integer or a float, convert
    Snum2 = str(Snum2) if isinstance(Snum2, (int, float)) else Snum2 #it to a string.
    
    try:
        float(Snum1) #Check if the number can be turned into a float to make
        float(Snum2) #sure the string is not text, if any is, throws exception.
    except:
        #If any of the strings contained text, throws this exception.
        raise TypeError("String numbers must not contain text.")
        
    #Tries to obtain the exponent of 10 needed to convert the integer and decimal part into an integer.
    #If the value is a float, it will turn the number into a string, split it on the '.' and obtain the
    #lenght of the decimal part. If its an integer, it will set it to 1, as 10**0 is equal to 1.
    #The functions tries it with both numbers separately cause there could be a decimal and an integer number.
    try:
        num1ex = len(str(Snum1).split('.')[1])
    except:
        num1ex = 1
    try:
        num2ex = len(str(Snum2).split('.')[1])
    except:
        num2ex = 1
        
    #Converts both numbers into integers before using an exponent of 10 before equal them.
    Snum1 = int(Snum1.replace('.', ''))
    Snum2 = int(Snum2.replace('.', ''))
        
    #Depending on the number of exponents of 10 of each number, the smaller one is adjusted
    #to be 'equal' to the other one in terms of decimal lenght, so they can be added to each
    #other to equal an integer version of the decimal values of the operation.
    #In case they have the same exponent of 10, they are added to each other and returned
    #to a string value.
    if num1ex > num2ex:
        
        #If the first number has a greater exponent of 10, the seconth number is multiplied by
        #10 to the exponent of the substraction of the exponents to equal the exponents.
        Snum2 *= 10**(num1ex - num2ex)
        
        #The operation is done, turned into an string and allocated on 'raw_result', so its
        #easier to read the code.
        raw_result = str(Snum1+Snum2)
        #The greater exponent is substracted from lenght of raw_result to determine where the
        #float separator has to be put. The result is substracted by the greater exponent, so
        #it will directly make reference to the place the dot has to be.
        #It is allocated on the same variable of the greater exponent for a small optimization,
        # as it is still understandable like this.
        num1ex = len(raw_result)-num1ex
        
        #Finally, the string with the result is returned, adding the semicolon on the exact
        #same line. This uses the index obtained from before to join the string from 0 to the
        #index, a dot and the rest of the string.
        return raw_result[:num1ex] + '.' + raw_result[num1ex:]
        
    elif num1ex < num2ex:
        
        #If the first number has a greater exponent of 10, the seconth number is multiplied by
        #10 to the exponent of the substraction of the exponents to equal the exponents.
        Snum1 *= 10**(num2ex - num1ex)
        
        #The operation is done, turned into an string and allocated on 'raw_result', so its
        #easier to read the code.
        raw_result = str(Snum1+Snum2)
        #The greater exponent is substracted from lenght of raw_result to determine where the
        #float separator has to be put. The result is substracted by the greater exponent, so
        #it will directly make reference to the place the dot has to be.
        #It is allocated on the same variable of the greater exponent for a small optimization,
        # as it is still understandable like this.
        num2ex = len(raw_result)-num2ex
        
        #Finally, the string with the result is returned, adding the semicolon on the exact
        #same line. This uses the index obtained from before to join the string from 0 to the
        #index, a dot and the rest of the string.
        return raw_result[:num2ex] + '.' + raw_result[num2ex:]
    
    else:
        #If they have the exact same exponent, there is no need to equal them, so we skip this step.
        
        #The operation is done, turned into an string and allocated on 'raw_result', so its
        #easier to read the code.
        raw_result = str(Snum1+Snum2)
        #The greater exponent is substracted from lenght of raw_result to determine where the
        #float separator has to be put. The result is substracted by the greater exponent, so
        #it will directly make reference to the place the dot has to be.
        #As both of the exponents are the same, it doesn't really matter to use one or another.
        #It is allocated on the same variable of the greater exponent for a small optimization,
        # as it is still understandable like this.
        num1ex = len(raw_result)-num1ex
        
        #Finally, the string with the result is returned, adding the semicolon on the exact
        #same line. This uses the index obtained from before to join the string from 0 to the
        #index, a dot and the rest of the string.
        return raw_result[:num1ex] + '.' + raw_result[num1ex:]

def String_sub(Snum1, Snum2):
    """
    This function is used to substract a String-number to each other.
    
    Parameters
    ----------
    :param Snum1: Value 1 - Can be a String-number, integer or float.
    :param Snum1: Value 2 - Can be a String-number, integer or float.

    Raises
    ------
    Exception or TypeError
        Iaddn case of any value contains text or is not an integer, float or a string.

    Returns
    -------
    String
        The result of adding one number to the other in a String-number.
        
        It can be an integer or a float nested inside a string, but converting the string into any of these may not be the exact number this value contains.
    """
    
    #This block checks both numbers have correct values, if the format is incorrect,
    #it will be corrected unless its a boolean. Any type other than a string that is
    #able to be turned into a number, will return an exception.
    assert not(isinstance(Snum1, bool) or isinstance(Snum2, bool)), "String number expected, boolean value provided instead." #If any value was boolean, raise exception.
    
    Snum1 = str(Snum1) if isinstance(Snum1, (int, float)) else Snum1 #If any value is an integer or a float, convert
    Snum2 = str(Snum2) if isinstance(Snum2, (int, float)) else Snum2 #it to a string.
    
    try:
        float(Snum1) #Check if the number can be turned into a float to make
        float(Snum2) #sure the string is not text, if any is, throws exception.
    except:
        #If any of the strings contained text, throws this exception.
        raise TypeError("String numbers must not contain text.")
        
    #Tries to obtain the exponent of 10 needed to convert the integer and decimal part into an integer.
    #If the value is a float, it will turn the number into a string, split it on the '.' and obtain the
    #lenght of the decimal part. If its an integer, it will set it to 1, as 10**0 is equal to 1.
    #The functions tries it with both numbers separately cause there could be a decimal and an integer number.
    try:
        num1ex = len(str(Snum1).split('.')[1])
    except:
        num1ex = 1
    try:
        num2ex = len(str(Snum2).split('.')[1])
    except:
        num2ex = 1
        
    #Converts both numbers into integers before using an exponent of 10 before equal them.
    Snum1 = int(Snum1.replace('.', ''))
    Snum2 = int(Snum2.replace('.', ''))
        
    #Depending on the number of exponents of 10 of each number, the smaller one is adjusted
    #to be 'equal' to the other one in terms of decimal lenght, so they can be added to each
    #other to equal an integer version of the decimal values of the operation.
    #In case they have the same exponent of 10, they are added to each other and returned
    #to a string value.
    if num1ex > num2ex:
        
        #If the first number has a greater exponent of 10, the seconth number is multiplied by
        #10 to the exponent of the substraction of the exponents to equal the exponents.
        Snum2 *= 10**(num1ex - num2ex)
        
        #The operation is done, turned into an string and allocated on 'raw_result', so its
        #easier to read the code.
        raw_result = str(Snum1-Snum2)
        #The greater exponent is substracted from lenght of raw_result to determine where the
        #float separator has to be put. The result is substracted by the greater exponent, so
        #it will directly make reference to the place the dot has to be.
        #It is allocated on the same variable of the greater exponent for a small optimization,
        # as it is still understandable like this.
        num1ex = len(raw_result)-num1ex
        
        #Finally, the string with the result is returned, adding the semicolon on the exact
        #same line. This uses the index obtained from before to join the string from 0 to the
        #index, a dot and the rest of the string.
        return raw_result[:num1ex] + '.' + raw_result[num1ex:]
        
    elif num1ex < num2ex:
        
        #If the first number has a greater exponent of 10, the seconth number is multiplied by
        #10 to the exponent of the substraction of the exponents to equal the exponents.
        Snum1 *= 10**(num2ex - num1ex)
        
        #The operation is done, turned into an string and allocated on 'raw_result', so its
        #easier to read the code.
        raw_result = str(Snum1-Snum2)
        #The greater exponent is substracted from lenght of raw_result to determine where the
        #float separator has to be put. The result is substracted by the greater exponent, so
        #it will directly make reference to the place the dot has to be.
        #It is allocated on the same variable of the greater exponent for a small optimization,
        # as it is still understandable like this.
        num2ex = len(raw_result)-num2ex
        
        #Finally, the string with the result is returned, adding the semicolon on the exact
        #same line. This uses the index obtained from before to join the string from 0 to the
        #index, a dot and the rest of the string.
        return raw_result[:num2ex] + '.' + raw_result[num2ex:]
    
    else:
        #If they have the exact same exponent, there is no need to equal them, so we skip this step.
        
        #The operation is done, turned into an string and allocated on 'raw_result', so its
        #easier to read the code.
        raw_result = str(Snum1-Snum2)
        #The greater exponent is substracted from lenght of raw_result to determine where the
        #float separator has to be put. The result is substracted by the greater exponent, so
        #it will directly make reference to the place the dot has to be.
        #As both of the exponents are the same, it doesn't really matter to use one or another.
        #It is allocated on the same variable of the greater exponent for a small optimization,
        # as it is still understandable like this.
        num1ex = len(raw_result)-num1ex
        
        #Finally, the string with the result is returned, adding the semicolon on the exact
        #same line. This uses the index obtained from before to join the string from 0 to the
        #index, a dot and the rest of the string.
        return raw_result[:num1ex] + '.' + raw_result[num1ex:]

def help(function=""):

  """
    Provides some help with the library.
    Best is to read documentation.

  :param function: any library function.
  :return: Prints helping dialogs
  """
  if function:
    if function == "Dadd()":
      print("This function fixes the way to add decimal numbers.\nParameter 1: number one (integer or float)\nParameter 2: (integer or float)\nReturns a correct result (can be an integer or a float) Example: sum(0.1,0.2)")
    elif function == "Dsub()":
      print("This function fixes the way to substract decimal numbers.\nParameter 1: number one (integer or float)\nParameter 2: number two (integer or float)\nReturns a correct result (can be an integer or a float) Example: min(0.1,0.2)")
    elif function == "String_add()":
      print("This function fixes the way to deal with long decimal numbers,\nthis function let you add string numbers to other string numbers.\n\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "String_sub()":
      print("This function fixes the way to deal with long decimal numbers,\nthis function lets you substract string numbers to other string numbers.\n\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")

  else:
    print("This is a library that deals with decimal problems.\n"
          "For getting help you can use the help() function but you have to\n"
          "enter an input inside of help() (Example: help(\"sum()\")).\n\n"
          "This is the 1.9 version and these are the functions:\n"
          "Dadd()\n"
          "Dsub()\n"
          "String_add()\n"
          "String_Sub()\n")
