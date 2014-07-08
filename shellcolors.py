#!/usr/bin/env python

from colors import colorize


#==========================================================================
# Foreground (without prefixes)
#==========================================================================

def black(string):
  return colorize(['FG_BLACK'], str(string))

def red(string):
  return colorize(['FG_RED'], str(string))

def green(string):
  return colorize(['FG_GREEN'], str(string))

def yellow(string):
  return colorize(['FG_YELLOW'], str(string))

def blue(string):
  return colorize(['FG_BLUE'], str(string))

def magenta(string):
  return colorize(['FG_MAGENTA'], str(string))

def cyan(string):
  return colorize(['FG_CYAN'], str(string))

def white(string):
  return colorize(['FG_WHITE'], str(string))


#==========================================================================
# Foreground (with prefixes)
#==========================================================================

def fg_black(string):
  return colorize(['FG_BLACK'], str(string))

def fg_red(string):
  return colorize(['FG_RED'], str(string))

def fg_green(string):
  return colorize(['FG_GREEN'], str(string))

def fg_yellow(string):
  return colorize(['FG_YELLOW'], str(string))

def fg_blue(string):
  return colorize(['FG_BLUE'], str(string))

def fg_magenta(string):
  return colorize(['FG_MAGENTA'], str(string))

def fg_cyan(string):
  return colorize(['FG_CYAN'], str(string))

def fg_white(string):
  return colorize(['FG_WHITE'], str(string))

#==========================================================================
# Background
#==========================================================================

def bg_black(string):
  return colorize(['BG_BLACK'], str(string))

def bg_red(string):
  return colorize(['BG_RED'], str(string))

def bg_green(string):
  return colorize(['BG_GREEN'], str(string))

def bg_yellow(string):
  return colorize(['BG_YELLOW'], str(string))

def bg_blue(string):
  return colorize(['BG_BLUE'], str(string))

def bg_magenta(string):
  return colorize(['BG_MAGENTA'], str(string))

def bg_cyan(string):
  return colorize(['BG_CYAN'], str(string))

def bg_white(string):
  return colorize(['BG_WHITE'], str(string))
