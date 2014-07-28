
def confirm(text):
  success = False
  while True:
    answer = input(text + " Y/n:")
    if answer == "Y":
      success = True
      break
    elif answer == "n" or answer == "N":
      break
  return success
