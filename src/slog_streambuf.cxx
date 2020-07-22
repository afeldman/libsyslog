#include <string>
#include <ostream>
#include <syslog.h>

#include "libsyslog/type.hxx"
#include "libsyslog/level.hxx"
#include "libsyslog/slog_streambuf.hxx"

slog::syslog_streambuf::syslog_streambuf(
    const std::string& name,
    slog::type type):std::basic_streambuf<char>(){
        openlog(name.size() ? name.data() : nullptr, LOG_PID, type);
};
        
slog::syslog_streambuf::~syslog_streambuf(){
    closelog(); 
}

int slog::syslog_streambuf::sync() {
    if(this->buffer.size()){
            syslog(level, "%s", this->buffer.data());

            this->buffer.clear();
            this->level = ini_level;
        }
        return 0;
}

void slog::syslog_streambuf::set_level(slog::level new_level) noexcept{
    this->level = new_level;
}
