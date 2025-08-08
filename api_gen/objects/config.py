from typing import Literal


#######################################################################
##                                                                   ##
##                           Indent Config                           ##
##                                                                   ##
#######################################################################
# Specifies the character used for indentation.
INDENT_CHAR: Literal[' ', '\t'] = ' '

# Specifies the amount of indent characters used per indent level.
INDENT_WIDTH: int = 4



#######################################################################
##                                                                   ##
##                               Misc.                               ##
##                                                                   ##
#######################################################################
# Everything here isn't part of the config, so only change
# if you know what you're doing!

# The config contains global vars, so don't
# pollute the namespace of the importer by
# allowing all symbols to get imported (this
# is a config, so only specific values
# should get imported anyway)
__all__ = []
