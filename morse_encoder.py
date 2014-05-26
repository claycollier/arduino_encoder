__encoder = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
          'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..',
          'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',
          'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...',
          't':'-', 'u':'..-', 'v':'...-','w':'.--', 'x':'-..-', 'y':'-.--',
          'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
          '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
          '0':'-----', ' ':'/', '\n':'//'}

__pre_wrapper = 'int pin = 13;\n\nvoid setup() {\n\tpinMode(pin, OUTPUT);\n}\n\nvoid loop() {\n'
__post_wrapper = '\n}\n\nvoid dot() { digitalWrite(pin, HIGH); delay(250); digitalWrite(pin, LOW); delay(250); }\n\nvoid dash() { digitalWrite(pin, HIGH); delay(1000); digitalWrite(pin, LOW); delay(250); }\nvoid gap() { digitalWrite(pin, LOW);delay(1000);}\n' 

def encode(text):
     """Encodes a single line of text into the Morse alphabet."""
     output = ''
     for character in text.lower():
          output += __encoder.get(character, '')

     return output

def emit(encoded_text):
     output = __pre_wrapper
     for char in encoded_text:
          if char == '.':
               output += '\tdot();\n'
          elif char == '-':
               output += '\tdash();\n'
          elif char == '/':
               output += '\tgap();\n'
     output += __post_wrapper
     return output
