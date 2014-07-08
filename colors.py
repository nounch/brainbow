#!/usr/bin/env python

from core import colorize


###########################################################################
# Color functions
###########################################################################

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


###########################################################################
# Manager classn
###########################################################################

class ColorManager(object):
  def __init__(self, colorize=True, colorize_fg=True, colorize_bg=True):
    self.colorize = colorize
    self.colorize_fg = colorize_fg
    self.colorize_bg = colorize_bg

  #======================================================================
  # Foreground (without prefixes)
  #======================================================================

  def black(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_BLACK'], str(string))
    else:
      s = string
      return s

  def red(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_RED'], str(string))
    else:
      s = string
      return s

  def green(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_GREEN'], str(string))
    else:
      s = string
      return s

  def yellow(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_YELLOW'], str(string))
    else:
      s = string
      return s

  def blue(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_BLUE'], str(string))
    else:
      s = string
      return s

  def magenta(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_MAGENTA'], str(string))
    else:
      s = string
      return s

  def cyan(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_CYAN'], str(string))
    else:
      s = string
      return s

  def white(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_WHITE'], str(string))
    else:
      s = string
      return s


  #======================================================================
  # Foreground (with prefixes)
  #======================================================================

  def fg_black(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_BLACK'], str(string))
    else:
      s = string
      return s

  def fg_red(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s =colorize(['FG_RED'], str(string))
    else:
      s = string
      return s

  def fg_green(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_GREEN'], str(string))
    else:
      s = string
      return s

  def fg_yellow(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s =colorize(['FG_YELLOW'], str(string))
    else:
      s = string
      return s

  def fg_blue(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_BLUE'], str(string))
    else:
      s = string
      return s

  def fg_magenta(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_MAGENTA'], str(string))
    else:
      s = string
      return s

  def fg_cyan(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s =colorize(['FG_CYAN'], str(string))
    else:
      s = string
      return s

  def fg_white(self, string):
    s = ''
    if self.colorize and self.colorize_fg:
      s = colorize(['FG_WHITE'], str(string))
    else:
      s = string
      return s

  #======================================================================
  # Background
  #======================================================================

  def bg_black(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_BLACK'], str(string))
    else:
      s = string
      return s

  def bg_red(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_RED'], str(string))
    else:
      s = string
      return s

  def bg_green(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_GREEN'], str(string))
    else:
      s = string
      return s

  def bg_yellow(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_YELLOW'], str(string))
    else:
      s = string
      return s

  def bg_blue(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_BLUE'], str(string))
    else:
      s = string
      return s

  def bg_magenta(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_MAGENTA'], str(string))
    else:
      s = string
      return s

  def bg_cyan(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_CYAN'], str(string))
    else:
      s = string
      return s

  def bg_white(self, string):
    s = ''
    if self.colorize and self.colorize_bg:
      s = colorize(['BG_WHITE'], str(string))
    else:
      s = string
      return s
