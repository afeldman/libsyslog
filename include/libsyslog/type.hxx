#ifndef __SYSYLOG_TYPE_HXX__
#define __SYSYLOG_TYPE_HXX__

#include <syslog.h>

namespace slog{
    enum type {
        auth   = LOG_AUTH   ,
        cron   = LOG_CRON   ,
        daemon = LOG_DAEMON ,
        local0 = LOG_LOCAL0 ,
        local1 = LOG_LOCAL1 ,
        local2 = LOG_LOCAL2 ,
        local3 = LOG_LOCAL3 ,
        local4 = LOG_LOCAL4 ,
        local5 = LOG_LOCAL5 ,
        local6 = LOG_LOCAL6 ,
        local7 = LOG_LOCAL7 ,
        print  = LOG_LPR    ,
        mail   = LOG_MAIL   ,
        news   = LOG_NEWS   ,
        user   = LOG_USER   ,
        uucp   = LOG_UUCP   ,
    };
};

#endif