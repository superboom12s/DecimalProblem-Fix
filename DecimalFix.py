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

def String_add(num1, num2):
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

def String_sub(num1, num2):
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
      print("This function fixes the way to deal with long decimal numbers,\nthis function let you substract string numbers to other string numbers.\n\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "String_Mult()":
      print("This function fixes the way to deal with long decimal numbers,\nthis function let you multiply string numbers to other string numbers.\n\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
    elif function == "String_Div()":
      print("This function fixes the way to deal with long decimal numbers,\nthis function let you divide string numbers to other string numbers.\n\n      Parameter1: numberer one (String-float or String-integer)\n      Parameter number two (String-float or String-integer)\n      Return: Correct result (String-float or String-integer)")
  else:
    print("This is a library that deals with decimal problems.\n"
          "For getting help you can use the help() function but you have to\n"
          "enter an input inside of help() (Example: help(\"sum()\")).\n\n"
          "This is the 1.7 version and these are the functions:\n"
          "Dadd()\n"
          "Dsub()\n"
          "String_add()\n"
          "String_sub()\n"
          "String_Mult()\n"
          "String_Div()\n")
