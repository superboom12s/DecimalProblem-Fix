def sum(num1, num2):

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

def min(num1, num2):
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

def String_Sum(num1, num2):
  """
      This function fixes the way to deal with long decimal numbers of Python,
      turning them into strings should avoid the auto-integer transformation
      and this function let you add string numbers to other string numbers.

      Input example: String_Sum("1.913", "14")

      :param num1: number one (String-float or String-integer)
      :param num2: number two (String-float or String-integer)
      :return: Correct result (String-float or String-integer)
    """
  try:
    float(num1)
    float(num2)
  except:
    print("Error with String_Sum inputs, one or both inputs are text\ninstead of String-numbers")

  num1_Separado = num1.split(".")
  num2_Separado = num2.split(".")

  if (len(num1_Separado) == 2):
    num1len = len(num1_Separado[1])
    num1 = num1_Separado[0] + num1_Separado[1]
  else:
    num1len = 0


  if (len(num2_Separado) == 2):
    num2len = len(num2_Separado[1])
    num2 = num2_Separado[0] + num2_Separado[1]
  else:
    num2len = 0

  if num1len >= num2len:
    diff = num1len - num2len
    for i in range(diff):
      num2 = num2 + "0"
  else:
    diff = num2len - num1len
    for i in range(diff):
      num1 = num1 + "0"


  PrePreResult = int(num1) + int(num2)
  PreResult = [letra for letra in str(PrePreResult)]
  PreResult.insert(len(PreResult)-diff, ".")
  Result = "".join(PreResult)

  return Result

def String_Min(num1, num2):
  """
      This function fixes the way to deal with long decimal numbers of Python,
      turning them into strings should avoid the auto-integer transformation
      and this function let you substract string numbers to other string numbers.

      Input example: String_Min("1.913", "14")

      :param num1: number one (String-float or String-integer)
      :param num2: number two (String-float or String-integer)
      :return: Correct result (String-float or String-integer)
    """

  num01 = num1
  num02 = num2

  try:
    float(num01)
    float(num02)
  except:
    print("Error with String_Min inputs, one or both inputs are text\ninstead of String-numbers")

  num01_Separado = num01.split(".")
  num02_Separado = num02.split(".")

  if (len(num01_Separado) == 2):
    num01len = len(num01_Separado[1])
    num01 = num01_Separado[0] + num01_Separado[1]
  else:
    num01len = 0

  if (len(num02_Separado) == 2):
    num02len = len(num02_Separado[1])
    num02 = num02_Separado[0] + num02_Separado[1]
  else:
    num02len = 0

  if num01len >= num02len:
    diff = num01len - num02len
    for i in range(diff):
      num02 = num02 + "0"
  else:
    diff = num02len - num01len
    for i in range(diff):
      num01 = num01 + "0"

  PrePreResult = int(num01) - int(num02)
  PreResult = [letra for letra in str(PrePreResult)]
  PreResult.insert(len(PreResult) - diff, ".")
  Result = "".join(PreResult)

  return Result

def String_Mult(num1, num2):
  """
      This function fixes the way to deal with long decimal numbers of Python,
      turning them into strings should avoid the auto-integer transformation
      and this function let you add multiply numbers to other string numbers.

      Input example: String_Mult("1.913", "14")

      :param num1: number one (String-float or String-integer)
      :param num2: number two (String-float or String-integer)
      :return: Correct result (String-float or String-integer)
    """

  num01 = num1
  num02 = num2

  try:
    float(num01)
    float(num02)
  except:
    print("Error with String_Mult inputs, one or both inputs are text\ninstead of String-numbers")

  num01_Separado = num01.split(".")
  num02_Separado = num02.split(".")

  if (len(num01_Separado) == 2):
    num01len = len(num01_Separado[1])
    num01 = num01_Separado[0] + num01_Separado[1]
  else:
    num01len = 0


  if (len(num02_Separado) == 2):
    num02len = len(num02_Separado[1])
    num02 = num02_Separado[0] + num02_Separado[1]
  else:
    num02len = 0

  if num01len >= num02len:
    diff = num01len - num02len
    for i in range(diff):
      num02 = num02 + "0"
  else:
    diff = num02len - num01len
    for i in range(diff):
      num01 = num01 + "0"


  PrePreResult = int(num01) * int(num02)
  PreResult = [letra for letra in str(PrePreResult)]
  PreResult.insert(len(PreResult)-diff, ".")
  Result = "".join(PreResult)

  return Result

def String_Div(num1, num2):
  """
      This function fixes the way to deal with long decimal numbers of Python,
      turning them into strings should avoid the auto-integer transformation
      and this function let you divide string numbers to other string numbers.

      Input example: String_Div("1.913", "14")

      :param num1: number one (String-float or String-integer)
      :param num2: number two (String-float or String-integer)
      :return: Correct result (String-float or String-integer)
    """

  num01 = num1
  num02 = num2

  try:
    float(num01)
    float(num02)
  except:
    print("Error with String_Div inputs, one or both inputs are text\ninstead of String-numbers")

  num01_Separado = num01.split(".")
  num02_Separado = num02.split(".")

  if (len(num01_Separado) == 2):
    num01len = len(num01_Separado[1])
    num01 = num01_Separado[0] + num01_Separado[1]
  else:
    num01len = 0


  if (len(num02_Separado) == 2):
    num02len = len(num02_Separado[1])
    num02 = num02_Separado[0] + num02_Separado[1]
  else:
    num02len = 0

  if num01len >= num02len:
    diff = num01len - num02len
    for i in range(diff):
      num02 = num02 + "0"
  else:
    diff = num02len - num01len
    for i in range(diff):
      num01 = num01 + "0"


  PrePreResult = int(num01) / int(num02)
  PreResult = [letra for letra in str(PrePreResult)]
  PreResult.insert(len(PreResult)-diff, ".")
  Result = "".join(PreResult)

  return Result

def help(function=""):

  """
    This is a library that deals with decimal problems in Python 3.
          For getting help you can use the help() function but you have to
          enter an input inside of help() (Example: help(\"sum()\")).
          This is the 1.3.0 version and these are the functions:
          sum()
          min()
          String_Sum()
          String_Min()
          String_Mult()
          String_Div()
          help()
  :param function: any library function (Example: "sum()")
  :return: Prints the help
  """
  if function:
    if function == "sum()":
      print("This function fixes the way to add decimal numbers of Python.\nParameter 1: number one (integer or float)\n number two (integer or float)\nCorrect result (can be an integer or a float) Example: sum(0.1,0.2)")
    elif function == "min()":
      print("This function fixes the way to add decimal numbers of Python.\nParameter 1: number one (integer or float)\nParameter 2: number two (integer or float)\nCorrect result (can be an integer or a float) Example: min(0.1,0.2)")
    elif function == "String_Sum()":
      print("This function fixes the way to deal with long decimal numbers of Python,\nturning them into strings should avoid the auto-integer transformation\nand this function let you add string numbers to other string numbers.\n\n      Input example: String_Sum(\"1.913\", \"14\")\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "String_Min()":
      print("This function fixes the way to deal with long decimal numbers of Python,\nturning them into strings should avoid the auto-integer transformation\nand this function let you substract string numbers to other string numbers.\n\n      Input example: String_Min(\"1.913\", \"14\")\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "String_Mult()":
      print("This function fixes the way to deal with long decimal numbers of Python,\nturning them into strings should avoid the auto-integer transformation\nand this function let you multiply string numbers to other string numbers.\n\n      Input example: String_Mult(\"1.913\", \"14\")\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "String_Div()":
      print("This function fixes the way to deal with long decimal numbers of Python,\nturning them into strings should avoid the auto-integer transformation\nand this function let you divide string numbers to other string numbers.\n\n      Input example: String_Div(\"1.913\", \"14\")\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "help()":
      print("This is a library that deals with decimal problems in Python 3.\n"
            "For getting help you can use the help() function but you have to\n"
            "enter an input inside of help() (Example: help(\"Sum()\")).\n\n"
            "This is the 1.4.4 version and these are the functions:\n"
            "sum()\n"
            "min()\n"
            "String_Sum()\n"
            "String_Min()\n"
            "String_Mult()\n"
            "String_Div()\n"
            "help()\n")
    elif function == "Test" or "test" or "test()" or "sum_Test()" or "min_Test()" or "String_Sum_Test()" or "String_Min_Test()" or "String_Mult_Test()" or "String_Div_Test()":
      print("\n\n\nAny test function will print the library result with Python's one."
            "\nThese are the test functions:"
            "\nsum_Test()"
            "\nMin_Test()"
            "\nString_Sum_Test()"
            "\nString_Min_Test()"
            "\nString_Mult_Test()"
            "\nString_Div_Test()"
            "\nEverything_Test()"
            "\n\nFor using this, you can introduce two values (example: sum_Test(1, 3.2))\n\n")
    else:
      print("The help input has to be one of the actual functions, try with\n"
            "these ones:"
            "sum()\n"
            "min()\n"
            "String_Sum()\n"
            "String_Min()\n"
            "String_Mult()\n"
            "String_Div()\n"
            "help()\n")

  else:
    print("This is a library that deals with decimal problems in Python 3.\n"
          "For getting help you can use the help() function but you have to\n"
          "enter an input inside of help() (Example: help(\"sum()\")).\n\n"
          "This is the 1.3.0 version and these are the functions:\n"
          "sum()\n"
          "min()\n"
          "String_Sum()\n"
          "String_Min()\n"
          "String_Mult()\n"
          "String_Div()\n"
          "help()\n"
          "test\n")


def sum_Test(num1=0.1, num2=0.2):
  print(f"\n\nLibrary says that {num1} + {num2} equals to: "+str(sum(num1, num2))+"\nand Python 3 says that it equals to: "+str(num1 + num2))

def min_Test(num1=0.1, num2=0.2):
  print(f"\n\nLibrary says that {num1} - {num2} equals to: "+str(min(num1, num2))+"\nand Python 3 says that it equals to: "+str(num1 - num2))

def String_Sum_Test(num1=0.1, num2=0.2):
  print(f"\n\nLibrary says that [str] {num1} + {num2} equals to: "+str(String_Sum(num1, num2))+"\nand Python 3 says it this equals to: "+str(float(num1) + float(num2)))

def String_Min_Test(num1=0.1, num2=0.2):
  print(f"\n\nLibrary says that [str] {num1} - {num2} equals to: "+str(String_Min(num1, num2))+"\nand Python 3 says that it equals to: "+str(float(num1) - float(num2)))

def String_Mult_Test(num1=0.1, num2=0.2):
  print(f"\n\nLibrary says that [str] {num1} * {num2} equals to: "+str(String_Mult(num1, num2))+"\nand Python 3 says that it equals to: "+str(float(num1) * float(num2)))

def String_Div_Test(num1=0.1, num2=0.2):
  print(f"\n\nLibrary says that [str] {num1} / {num2} equals to: "+str(String_Div(num1, num2))+"\nand Python 3 says that it equals to: "+str(float(num1) / float(num2)))

def Test_Test(num1="", num2=""):
  print("\n\n\nYou are really smart, dont you are?")

def Library_Test(num1=0.1, num2=0.2):
  sum_Test(num1, num2)
  min_Test(num1, num2)
  String_Sum_Test(num1, num2)
  String_Min_Test(num1, num2)
  String_Mult_Test(num1, num2)
  String_Div_Test(num1, num2)
