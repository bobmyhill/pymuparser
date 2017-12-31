# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import os
import sys
import shutil
import time

from distutils.core import Extension
from distutils.core import setup


# =============================================================================
# >> PROJECT SOURCES
# =============================================================================
SOURCES = [
    # muparser binding
    'src/muparser_wrap.cpp',
    
    # MuParser
    'src/thirdparty/musparser/src/muParser.cpp',
    'src/thirdparty/musparser/src/muParserBase.cpp',
    'src/thirdparty/musparser/src/muParserBytecode.cpp',
    'src/thirdparty/musparser/src/muParserCallback.cpp',
    'src/thirdparty/musparser/src/muParserDLL.cpp',
    'src/thirdparty/musparser/src/muParserError.cpp',
    'src/thirdparty/musparser/src/muParserInt.cpp',
    'src/thirdparty/musparser/src/muParserTest.cpp',
    'src/thirdparty/musparser/src/muParserTokenReader.cpp',
]


# =============================================================================
# >> EXTRA INCLUDES
# =============================================================================
INCLUDE_DIRS = [
    'src/thirdparty/musparser/include',
]


# =============================================================================
# >> LIBRARY SEARCH DIRECTORIES
# =============================================================================
LIBRARY_DIRS = [
    'src/thirdparty/musparser/lib',
]


# =============================================================================
# >> LIBRARY NAMES
# =============================================================================
# Windows
if os.name == 'nt':
    LIBRARIES = [
        #'muparser32',
    ]

# Linux
else:
    LIBRARIES = [
        #'muparser',
    ]


# =============================================================================
# >> COMPILER FLAGS
# =============================================================================
COMPILER_FLAGS = [
    # This disables annoying visibility warnings
    #'-Wno-attributes',

    # Disable parentheses suggestions
    #'-Wno-parentheses',

    # Disable "deprecated conversion from string..." warning
    #'-Wno-write-strings',

    # Disable sign compare warnings
    #'-Wno-sign-compare',
]


# =============================================================================
# >> LINKER FLAGS
# =============================================================================
if os.name == 'nt':
    LINKER_FLAGS = [
        #'-static-libgcc',
        #'-static-libstdc++',
    ]
else:
    LINKER_FLAGS = [
    ]


# =============================================================================
# >> MACROS
# =============================================================================
MACROS = [
]


# =============================================================================
# >> MAIN
# =============================================================================
def main():
    # Compile the binary
    print('Compiling the binary...')
    setup(
        name='muparser',
        ext_modules=[
            Extension(
                'muparser',
                sources=SOURCES,
                library_dirs=LIBRARY_DIRS,
                libraries=LIBRARIES,
                include_dirs=INCLUDE_DIRS,
                extra_compile_args=COMPILER_FLAGS,
                extra_link_args=LINKER_FLAGS,
                define_macros=MACROS
            ),
        ]
    )

if __name__ == '__main__':
    now = time.time()
    main()
    print('Time elapsed: %.02f seconds.'% (time.time() - now))