def Dadd(num1, num2):

  """
  This function fixes the way to add decimal numbers of Python.

  :param num1: number one (integer or float)
  :param num2: number two (integer or float)
  :return: Correct result (can be an integer or a float)
  """
  num_Count = 1

  while num1 != int(num1) or num2 != int(num2):

    num1 *= 10
    num2 *= 10
    num_Count *= 10

  return (num1 + num2) / num_Count

def Dsub(num1, num2):
  """
    This function fixes the way to subtract decimal numbers of Python

    :param num1: number one (integer or float)
    :param num2: number two (integer or float)
    :return: Correct result (can be an integer or a float)
  """

  num_Count = 1

  while num1 != int(num1) or num2 != int(num2):

    num1 *= 10
    num2 *= 10
    num_Count *= 10

  return (num1 - num2) / num_Count


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
    else:
      print("This is a library that deals with decimal problems.\n"
          "For getting help you can use the help() function but you have to\n"
          "enter an input inside of help() (Example: help(\"sum()\")).\n\n"
          "This is the 1.9 version and these are the functions:\n"
          "Dadd()\n"
          "Dsub()\n")
