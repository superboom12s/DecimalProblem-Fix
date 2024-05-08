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
  def sumaTotal(integer1, integer2, decimal1 = 0, decimal2 = 0):
    integer1 = int(integer1)
    integer2 = int(integer2)

    #Si no hay decimales
    if not decimal1:
      return str(integer1+integer2)

    #Si hay decimales
    else:
      decimal1 = int(decimal1)
      decimal2 = int(decimal2)

      #Lista para operar
      operationList = [integer1+integer2, decimal1+decimal2]

      #En caso de llevar algun numero. Lo detecta cuando el resultado es mas largo que el mas grande de los originales.
      if len(str(operationList[1])) > len(str(max(decimal1, decimal2))):
        operationList[1] -= pow(10, len(str(operationList[1]))-1)
        operationList[0] += 1

      #Devuelve el numero final.
      return '.'.join([str(operationList[0]), str(operationList[1])])

  try:
    float(num1)
    float(num2)
  except:
    raise ValueError("Error with String_add inputs")

  #1
  #Si ambos numeros son decimales
  if len(num1.split(".")) == 2 and len(num2.split(".")) == 2:
    #1.1 - obtener los decimales y ordenarlos de menor a mayor
    provisionalList = sorted([int(num1.split(".")[1]), int(num2.split(".")[1])])

    #1.2 - Diferencia entre los largos de cada uno
    decimalDiff = len(str(provisionalList[1]))-len(str(provisionalList[0]))

    #1.3 igualar numeros
    provisionalList[0] = provisionalList[0] * pow(10, decimalDiff)

    return sumaTotal(num1.split(".")[0], num2.split(".")[0], provisionalList[0], provisionalList[1])

  #1 B
  #Si uno de los dos es decimal, su parte decimal es el decimal total.
  elif len(num1.split(".")) == 2:
    return sumaTotal(num1.split(".")[0], int(num2.split(".")[0]), num1.split(".")[1])
  elif len(num2.split(".")) == 2:
    return sumaTotal(num1.split(".")[0], int(num2.split(".")[0]), num2.split(".")[1])

  #1 C
  #Si ninguno es decimal, el decimal total es 0
  else:
    sumaTotal(num1.split(".")[0], int(num2.split(".")[0]))


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
  else:
    print("This is a library that deals with decimal problems.\n"
          "For getting help you can use the help() function but you have to\n"
          "enter an input inside of help() (Example: help(\"sum()\")).\n\n"
          "This is the 1.9 version and these are the functions:\n"
          "Dadd()\n"
          "Dsub()\n"
          "String_add()\n")
