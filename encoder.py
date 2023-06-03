from key import *

# Returns a code based on the original text's character
def returnEncodedChar(char):
  if (char == 'a'):
    return lowA
  elif (char == 'b'):
    return lowB
  elif (char == 'c'):
    return lowC
  elif (char == 'd'):
    return lowD
  elif (char == 'e'):
    return lowE
  elif (char == 'f'):
    return lowF
  elif (char == 'g'):
    return lowG
  elif (char == 'h'):
    return lowH
  elif (char == 'i'):
    return lowI
  elif (char == 'j'):
    return lowJ
  elif (char == 'k'):
    return lowK
  elif (char == 'l'):
    return lowL
  elif (char == 'm'):
    return lowM
  elif (char == 'n'):
    return lowN
  elif (char == 'o'):
    return lowO
  elif (char == 'p'):
    return lowP
  elif (char == 'q'):
    return lowQ
  elif (char == 'r'):
    return lowR
  elif (char == 's'):
    return lowS
  elif (char == 't'):
    return lowT
  elif (char == 'u'):
    return lowU
  elif (char == 'v'):
    return lowV
  elif (char == 'w'):
    return lowW
  elif (char == 'x'):
    return lowX
  elif (char == 'y'):
    return lowY
  elif (char == 'z'):
    return lowZ
  elif (char == 'A'):
    return capA
  elif (char == 'B'):
    return capB
  elif (char == 'C'):
    return capC
  elif (char == 'D'):
    return capD
  elif (char == 'E'):
    return capE
  elif (char == 'F'):
    return capF
  elif (char == 'G'):
    return capG
  elif (char == 'H'):
    return capH
  elif (char == 'I'):
    return capI
  elif (char == 'J'):
    return capJ
  elif (char == 'K'):
    return capK
  elif (char == 'L'):
    return capL
  elif (char == 'M'):
    return capM
  elif (char == 'N'):
    return capN
  elif (char == 'O'):
    return capO
  elif (char == 'P'):
    return capP
  elif (char == 'Q'):
    return capQ
  elif (char == 'R'):
    return capR
  elif (char == 'S'):
    return capS
  elif (char == 'T'):
    return capT
  elif (char == 'U'):
    return capU
  elif (char == 'V'):
    return capV
  elif (char == 'W'):
    return capW
  elif (char == 'X'):
    return capX
  elif (char == 'Y'):
    return capY
  elif (char == 'Z'):
    return capZ
  elif (char == ' '):
    return space
  elif (char == '.'):
    return period
  elif (char == ','):
    return comma
  elif (char == '?'):
    return question
  elif (char == '!'):
    return exclamation
  elif (char == '1'):
    return one
  elif (char == '2'):
    return two
  elif (char == '3'):
    return three
  elif (char == '4'):
    return four
  elif (char == '5'):
    return five
  elif (char == '6'):
    return six
  elif (char == '7'):
    return seven
  elif (char == '8'):
    return eight
  elif (char == '9'):
    return nine
  elif (char == '~'):
    return tilda
  elif (char == '`'):
    return single
  elif (char == '\\'):
    return backslash
  elif (char == '/'):
    return frontslash
  elif (char == '\`'):
    return single
  elif (char == '='):
    return equals
  elif (char == '-'):
    return dash
  elif (char == '+'):
    return plus
  elif (char == '_'):
    return underscore
  elif (char == '@'):
    return at
  elif (char == '#'):
    return hashtag
  elif (char == '$'):
    return dollar
  elif (char == '%'):
    return percentage
  elif (char == '^'):
    return rig
  elif (char == '&'):
    return andsign
  elif (char == '*'):
    return asterisk
  elif (char == '('):
    return leftpar
  elif (char == ')'):
    return rightpar
  elif (char == '{'):
    return leftcurly
  elif (char == '}'):
    return rightcurly
  elif (char == '['):
    return leftsquare
  elif (char == ']'):
    return rightsquare
  elif (char == ':'):
    return colon
  elif (char == ';'):
    return semicolon
  elif (char == '\''):
    return singlequote
  elif (char == '\"'):
    return doublequote
  elif (char == '<'):
    return leftcompar
  elif (char == '>'):
    return rightcompar
  elif (char == '|'):
    return absolute
  elif (char == '0'):
    return zero
  else:
    return None