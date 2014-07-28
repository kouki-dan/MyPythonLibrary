
def confirm(text):
  success = False
  while True:
    print(text + " Y/n:", end="")
    text = input()
    if text == "Y":
      success = True
      break
    elif text == "n" or text == "N":
      break
  return success
