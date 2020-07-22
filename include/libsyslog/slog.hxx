#ifndef __SYSYLOG_LOG_HXX__
#define __SYSYLOG_LOG_HXX__

#include "type.hxx"
#include "level.hxx"
#include "slog_streambuf.hxx"
#include "slog_stream.hxx"

using systype   = slog::type;
using syslevel  = slog::level;
using syslog    = slog::syslog_stream;
using sysbuffer = slog::syslog_streambuf;

#endif