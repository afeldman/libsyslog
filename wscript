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

    ctx.setenv('debug')
    ctx.load('compiler_cxx')
    ctx.env.CXXFLAGS=DEBUG_CXXFLAGS
    ctx.env.SOURCES=glob.glob(SOURCES)

    ctx.setenv('release')
    ctx.load('compiler_cxx')
    ctx.env.CXXFLAGS=RELEASE_CXXFLAGS
    ctx.env.SOURCES=glob.glob(SOURCES)

def options(opt):
    opt.load('compiler_cxx')

def init(ctx):
    # Setup contexts build_debug, build_release, clean_debug, ...
    from waflib.Build import BuildContext, CleanContext, InstallContext, UninstallContext
    for x in (BuildContext, CleanContext, InstallContext, UninstallContext):
        for y in ['debug','release']:
            class tmp(x):
                variant=y
                cmd=x.__name__.replace('Context','').lower()+'_'+y

def build(ctx):
    if not ctx.variant:
        import waflib.Options
        for x in ['debug','release']:
            waflib.Options.commands.insert(0,ctx.cmd+'_'+x)    
    else:
        ctx.shlib(source=ctx.env.SOURCES,target=name,includes=['./include'],install_path='${PREFIX}')

    ctx.install_files('${PREFIX}/include/%s/' % name, ctx.path.ant_glob(['**/*.hxx'], remove=False))

    from waflib import Options
    # process libshm.pc.in -> libshm.pc - by default it use the task "env" attribute
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
