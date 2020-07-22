#ifndef __SYSYLOG_LEVEL_HXX__
#define __SYSYLOG_LEVEL_HXX__

#include <syslog.h>

namespace slog{
    enum level {
        emergency   = LOG_EMERG     ,
        alert       = LOG_ALERT     ,
        critical    = LOG_CRIT      ,
        error       = LOG_ERR       ,
        warning     = LOG_WARNING   ,
        notice      = LOG_NOTICE    ,
        info        = LOG_INFO      ,
        debug       = LOG_DEBUG     ,
    };
};

#endif
