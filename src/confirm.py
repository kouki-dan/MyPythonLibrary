


def confirm(text):
  success = False
  while True:
    answer = input(text + " Y/n:")
    if answer in ["Y"]:
      success = True
      break
    elif answer in ["n", "N"]:
      break
  return success
