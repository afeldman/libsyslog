# waf project directories
top="."
out="build"

# Global definitions
SOURCES='src/*.cpp'
CXXFLAGS=['-fopenmp','-Wall','-Werror','-std=c++11','-Wl,--no-as-needed']

# Variant specific build flags
DEBUG_CXXFLAGS=CXXFLAGS+['-g']
RELEASE_CXXFLAGS=CXXFLAGS+['-O3','-DNDEBUG']

import glob
import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

if sys.platform.lower() in ["linux"]:#check for darwin. dows darwin support syslog.h?
    print("only on linux")
    sys.exit(1)

def configure(ctx):

    ctx.setenv('debug')
    ctx.load('compiler_cxx')
    ctx.env.CXXFLAGS=DEBUG_CXXFLAGS
    ctx.env.SOURCES=glob.glob(SOURCES)


    ctx.setenv('release')
    ctx.load('compiler_cxx')
    ctx.env.CXXFLAGS=RELEASE_CXXFLAGS
    ctx.env.SOURCES=glob.glob(SOURCES)