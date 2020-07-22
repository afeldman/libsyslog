#ifndef __SYSYLOG_SLOG_STREAM_HXX__
#define __SYSYLOG_SLOG_STREAM_HXX__

#include <ostream>
#include <string>
#include "type.hxx"
#include "level.hxx"
#include "slog_streambuf.hxx"


namespace slog{
    class syslog_stream: public std::basic_ostream<char>
    {
    public:
        explicit syslog_stream(const std::string&, 
                            slog::type  );

        syslog_stream& operator<<(slog::level) noexcept;

    private:
        syslog_streambuf streambuf;
    };
};

#endif
