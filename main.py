if __name__ == "__main__":
  # Python Syntax

  ## Whitespace and indentation

  # dedine main function to print out something
  def main():
    i = 1
    max = 10
    while (i < max):
      print(i)
      i += 1

  # call function main
  main()

  # Comments

  # This is a single line comment in Python

  # Continuation of statements

  a, b, c = (True, True, True)

  if (a == True) and  \
    (b == True) and \
    (c == True):
    print("Continuation of statements")

  # Identifiers

  # Keywords

  import keyword

  print(keyword.kwlist)

  # String literals

  s = 'This is a string'
  print(s)

  s = "Another string using double quotes"
  print(s)

  s = '''String can span
multiple line'''
  print(s)
