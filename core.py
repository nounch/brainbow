import sys

DEFAULT           = '\033[m'

# Foreground colors
FG_BLACK          = '\033[30m'
FG_RED            = '\033[31m'
FG_GREEN          = '\033[32m'
FG_YELLOW         = '\033[33m'
FG_BLUE           = '\033[34m'
FG_MAGENTA        = '\033[35m'
FG_CYAN           = '\033[36m'
FG_WHITE          = '\033[37m'

# Background colors
BG_BLACK          = '\033[40m'
BG_RED            = '\033[41m'
BG_GREEN          = '\033[42m'
BG_YELLOW         = '\033[43m'
BG_BLUE           = '\033[44m'
BG_MAGENTA        = '\033[45m'
BG_CYAN           = '\033[46m'
BG_WHITE          = '\033[47m'

# Special attributes
RESET             = '\033[0m'
BOLD_ON           = '\033[1m'
FAINT             = '\033[2m' # Not widely supported
ITALICS_ON        = '\033[3m'
UNDERLINE_ON      = '\033[4m'
BLINK_ON          = '\033[5m' # Blink slowly
BLINK_RAPID_ON    = '\033[6m' # Blink rapidly
INVERSE_ON        = '\033[7m'
CONCEAL           = '\033[8m' # Not widely supported
STRIKETHROUGH_ON  = '\033[9m'
DEFAULT_FONT      = '\033[10m'
BOLD_OFF          = '\033[22m'
ITALICS_OFF       = '\033[23m'
UNDERLINE_OFF     = '\033[24m'
BLINK_OFF         = '\033[25m'
INVERSE_OFF       = '\033[27m'
STRIKETHROUGH_OFF = '\033[29m'

def mapColors(colors):
  for index, color in enumerate(colors):
    # Default (no color)
    if color == 'DEFAULT':
      colors[index] = DEFAULT
    if color == 'NORMAL':                 # 'DEFAULT' and 'NORMAL' are interchangeable
      colors[index] = DEFAULT
      # Foreground colors
    elif color == 'FG_BLACK':
      colors[index] = FG_BLACK
    elif color == 'FG_RED':
      colors[index] = FG_RED
    elif color == 'FG_GREEN':
      colors[index] = FG_GREEN
    elif color == 'FG_YELLOW':
      colors[index] = FG_YELLOW
    elif color == 'FG_BLUE':
      colors[index] = FG_BLUE
    elif color == 'FG_MAGENTA':
      colors[index] = FG_MAGENTA
    elif color == 'FG_CYAN':
      colors[index] = FG_CYAN
    elif color == 'FG_WHITE':
      colors[index] = FG_WHITE
      # Background colors
    elif color == 'BG_BLACK':
      colors[index] = BG_BLACK
    elif color == 'BG_RED':
      colors[index] = BG_RED
    elif color == 'BG_GREEN':
      colors[index] = BG_GREEN
    elif color == 'BG_YELLOW':
      colors[index] = BG_YELLOW
    elif color == 'BG_BLUE':
      colors[index] = BG_BLUE
    elif color == 'BG_MAGENTA':
      colors[index] = BG_MAGENTA
    elif color == 'BG_CYAN':
      colors[index] = BG_CYAN
    elif color == 'BG_WHITE':
      colors[index] = BG_WHITE
      # Special attributes
    elif color == 'RESET':
      colors[index] = RESET
    elif color == 'BOLD_ON':
      colors[index] = BOLD_ON
    elif color == 'FAINT':
      colors[index] = FAINT
    elif color == 'ITALICS_ON':
      colors[index] = ITALICS_ON
    elif color == 'UNDERLINE_ON':
      colors[index] = UNDERLINE_ON
    elif color == 'BLINK_ON':
      colors[index] = BLINK_ON
    elif color == 'BLINK_RAPID_ON':
      colors[index] = BLINK_RAPID_ON
    elif color == 'INVERSE_ON':
      colors[index] = INVERSE_ON
    elif color == 'CONCEAL':
      colors[index] = CONCEAL
    elif color == 'STRIKETHROUGH_ON':
      colors[index] = STRIKETHROUGH_ON
    elif color == 'DEFAULT_FONT':
      colors[index] = DEFAULT_FONT
    elif color == 'BOLD_OFF':
      colors[index] = BOLD_OFF
    elif color == 'ITALICS_OFF':
      colors[index] = ITALICS_OFF
    elif color == 'UNDERLINE_OFF':
      colors[index] = UNDERLINE_OFF
    elif color == 'BLINK_OFF':
      colors[index] = BLINK_OFF
    elif color == 'INVERSE_OFF':
      colors[index] = INVERSE_OFF
    elif color == 'STRIKETHROUGH_OFF':
      colors[index] = STRIKETHROUGH_OFF
      # Omit unwanted unsupported properties (and typos!)
    else:
        del colors[index]
  return colors

def compileOutput(colors, text):
  """
  Compiles the output string."""
  output = ''

  mapColors(colors)

  for attr in colors:
    output += attr
    output += text + DEFAULT
    return output

def cprint(colors, text):
  """
  Print the compiled output string with a trailing newline."""
  print compileOutput(colors, text)

def cprin(colors, text):
  """
  Print the compiled output string without a trailing newline."""
  output = compileOutput(colors, text)
  sys.stdout.write(output)

def colorize(colors, text):
  """
  Returns the compiled output string (without a trailing newline)."""
  return compileOutput(colors, text)
