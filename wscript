#project name
major  = 1
minor  = 0
bugfix = 0
name="libsyslog"
application = name
version='%d.%d.%d' % (major, minor, bugfix)
name_version = '%s-%d.%d.%d' % (name, major, minor, bugfix)

# waf project directories
top="."
out="build"

# Global definitions
SOURCES='src/*.cxx'
CXXFLAGS=['-fopenmp','-Wall','-Werror','-std=c++11','-Wl,--no-as-needed']

# Variant specific build flags
DEBUG_CXXFLAGS=CXXFLAGS+['-g']
RELEASE_CXXFLAGS=CXXFLAGS+['-O3','-DNDEBUG']

import glob
import sys

if sys.platform.lower() not in ["linux"]:#check for darwin. dows darwin support syslog.h?
    print("only on linux")
    sys.exit(1)

def configure(ctx):

    ctx.load('compiler_cxx')

    from waflib import Options
    if Options.options.debug:
        ctx.env.CXXFLAGS=DEBUG_CXXFLAGS
    else:
        ctx.env.CXXFLAGS=RELEASE_CXXFLAGS

    ctx.env.SOURCES=glob.glob(SOURCES)


def options(opt):
    opt.load('compiler_cxx')

    #Add configuration options
    syslog = opt.add_option_group ("%s Options" % name.upper())

    syslog.add_option('--debug',
                      action='store_true',
                      default=False,
                      help='build with debug information')

def build(ctx):
    ctx.shlib(
        source=ctx.env.SOURCES,
        target=name,
        includes=['./include'],
        install_path='${PREFIX}/lib')

    ctx.install_files(
        '${PREFIX}/include/%s/' % name, 
        ctx.path.ant_glob(['**/*.hxx'], 
        remove=False))

    from waflib import Options
    pcf = ctx(
        features = 'subst',
        source = '%s.pc.in' % name,
        target = '%s.pc' % name,
        install_path = '${PREFIX}/lib/pkgconfig/'
        )

    pcf.env.table.update(
        {'LIBS':'',
         'VERSION': version,
         'NAME': name,
         'PREFIX': '%s' % Options.options.prefix,
         'INCLUDEDIR': 'include/%s' % name}
        )
