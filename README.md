# Brainbow

Brainbow provides simple wrapper functions for 8-bit color terminal escape
sequences.

    print bg_green(fg_red('I am red with a green background.'))


## Supported Colors

**Foreground:**

    black
    red
    green
    yellow
    blue
    magenta
    cyan
    white

**Background:**

    black
    red
    green
    yellow
    blue
    magenta
    cyan
    white


**Special:**

    RESET
    BOLD_ON
    FAINT             # Not widely supported
    ITALICS_ON
    UNDERLINE_ON
    BLINK_ON          # Blink slowly
    BLINK_RAPID_ON    # Blink rapidly
    INVERSE_ON
    CONCEAL           # Not widely supported
    STRIKETHROUGH_ON
    DEFAULT_FONT
    BOLD_OFF
    ITALICS_OFF
    UNDERLINE_OFF
    BLINK_OFF
    INVERSE_OFF
    STRIKETHROUGH_OFF

## Disclaimer

1. Since there are no tests yet, the code is not on any package index.
2. Since this is not on any package index yet, there is no hardened public
   interface - yet.
3. If you still wish to use it, see `test.py` (manual smoke tests, **NOT**
   real unit tests!).
