invalid_msg="invalid values being entered"
def rgb_hex():
  red = int(input("Enter red (R) value: "))
  if(red not in range(0,256)):
    print(invalid_msg)
    return
  green = int(input("Enter green (g) value: "))
  if(green not in range(0,256)):
    print(invalid_msg)
    return
  blue = int(input("Enter blue (B) value: "))
  if(blue not in range(0,256)):
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print("%s" % (hex(val)[2:]).upper())
  

def hex_rgb():
  hex_val = input("Enter the hex value: ")
  if(len(hex_val) != 6):
    print(invalid_msg)
    return
  else:
    hex_val =int(hex_val,16)
  two_hex_digit = 2**8
  blue = hex_val % two_hex_digit
  hex_val= hex_val >> 8
  green = hex_val % two_hex_digit
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digit
  print(f"Red:{red} Green:{green} Blue:{blue}")
  # print "Red: %s Green: %s Blue: %s" % (red, green, blue)

def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      print("RGB to HEX...")
      rgb_hex()
    elif option == '2':
      print("HEX to RGB...")
      hex_rgb()
    elif option == 'x' or option == 'X':
      break
    else:
      print(invalid_msg)

convert()