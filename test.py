#!/usr/bin/env python


from core import *
from colors import *


def _banner(modulename):
  print "#" * 75
  print "# %-71s #" % ("'" + modulename + "' module")
  print "#" * 75
  print

def _separator():
  print('\n')
  print('-' * 75)
  print('\n')

def test_basic():
  """
  Test the 'color' module."""
  _banner('core')

  testString = "This is a test."

  colors = Colors()

  # Simple example
  colors.cprint(['FG_GREEN', 'BG_RED'], testString)

  # Bad example (unsupported font attributes)
  colors.cprint(['FG_CYAN', 'BG_WHITE', 'INVERSE_ON', 'BOLD_ON',
                 'ITALICS_ON', 'NOTHING'], testString)

  # Print without trailing newline
  colors.cprin(['FG_GREEN'], "This ")
  colors.cprin(['UNDERLINE_ON'], "is")
  colors.cprin(['NORMAL'], " ")
  colors.cprin(['NORMAL'], "an ")
  colors.cprin(['BG_RED', 'FG_WHITE'], "ERROR")
  colors.cprin(['NORMAL'], ".")
  print

  # Fancy example
  testNumbers = range(30, 170, 3)
  for index, item in enumerate(testNumbers):
    print "%-30s %-30s" % (
      "" + colors.colorize(['BG_CYAN', 'FG_WHITE'], str(index)),
      "" + colors.colorize(['FG_MAGENTA'],str(item)))

def test_color_functions():
  _banner('colors')

  s = 'test'

  # Foreground (without prefixes)
  print(black(s))
  print(red(s))
  print(green(s))
  print(yellow(s))
  print(blue(s))
  print(magenta(s))
  print(cyan(s))
  print(white(s))

  _separator()
  # Foreground (with prefixes)
  print(fg_black(s))
  print(fg_red(s))
  print(fg_green(s))
  print(fg_yellow(s))
  print(fg_blue(s))
  print(fg_magenta(s))
  print(fg_cyan(s))
  print(fg_white(s))

  _separator()
  # Background
  print(bg_black(s))
  print(bg_red(s))
  print(bg_green(s))
  print(bg_yellow(s))
  print(bg_blue(s))
  print(bg_magenta(s))
  print(bg_cyan(s))
  print(bg_white(s))

  _separator()
  print(bg_green(fg_red(s)))
  print(bg_red(fg_green(s)))
  print(bg_white(fg_blue(s)))
  print(bg_magenta(fg_yellow(s)))
  print(bg_cyan(fg_magenta(s)))
  print(bg_magenta(fg_cyan(s)))
  print(bg_white(fg_black(s)))
  # ...

  _separator()
  print(red('red') + ' ' + green('green' + ' ' + yellow('yellow')))

  import sys
  import string
  _separator()
  fg_functions = [black, red, green, yellow, blue, magenta, cyan, white]
  bg_functions = [bg_black, bg_red, bg_green, bg_yellow, bg_blue,
                  bg_magenta, bg_cyan, bg_white]
  for function in fg_functions:
    for bg_function in bg_functions:
      print(bg_function(function('fg: ' + function.__name__ + ' - bg: ' +
                                 string.strip(string.strip(
                bg_function.__name__, 'bg'), '_'))))

def test_color_manager():
  _banner('color')

  print('ColorManager 1:')
  cm1 = ColorManager()
  print cm1.red('test')

  _separator()
  print('ColorManager 2 (no colors):')
  cm2 = ColorManager(colorize=False)
  print cm2.green('test')
  print cm2.blue('test')
  print cm2.red(cm2.bg_cyan('test'))
  print cm1.red(cm2.bg_cyan('test')) # Foreground should still be red

  _separator()
  print('ColorManager 2 (no foreground colors):')
  cm2 = ColorManager(colorize_fg=False)
  print cm2.green('test')
  print cm2.blue('test')
  print cm2.red(cm2.bg_cyan('test'))
  print cm1.red(cm2.bg_cyan('test')) # Foreground should still be red

def test_termcolor():
  """Test 'termcolor' module as a reference (less features)."""
  _banner('termcolor')

  import termcolor
  print termcolor.colored('hello', 'red'), termcolor.colored('world',
                                                             'green')

def test_colorama():
  """Test 'colorama' module as a reference (more features/different
  featurset).
  """
  _banner('colorama')

  import colorama
  colorama.init()
  print colorama.Fore.RED + "hello " + colorama.Fore .WHITE + colorama.Back.GREEN + "world" + colorama.Style.DIM + "!"
  colorama.deinit()


if __name__ == '__main__':
  test_color_manager()
  print('\n\n')

  test_color_functions()
  print('\n\n')

  # test_basic()
  # print('\n\n')

  # test_termcolor()
  # print('\n\n')

  # test_colorama()
