#include <cstring>
#include <ostream>

#include "libsyslog/slog_stream.hxx"

slog::syslog_stream::syslog_stream(
        const std::string& name = std::string(), 
        slog::type type = slog::user ):
        std::basic_ostream<char>(&streambuf),
        streambuf(name, type)
    { }

slog::syslog_stream& slog::syslog_stream::operator<<(slog::level level){
        streambuf.set_level(level);
        return (*this);
}