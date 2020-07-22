#ifndef __SYSYLOG_SLOG_STREAMBUF_HXX__
#define __SYSYLOG_SLOG_STREAMBUF_HXX__

#include <streambuf>
#include "type.hxx"
#include "level.hxx"

namespace slog{
    class syslog_stream;

    class syslog_streambuf: public std::basic_streambuf<char>
    {
    public:
        explicit syslog_streambuf(const std::string&, slog::type);
        ~syslog_streambuf() override;

    protected:
        int_type overflow(int_type c = traits_type::eof()) override{
            if(traits_type::eq_int_type(c, traits_type::eof())){
                this->sync();
            }
            else{
                this->buffer += traits_type::to_char_type(c);
            }

            return c;
        }
        int sync() override;

        friend class syslog_stream;
        void set_level(slog::level) noexcept;
    private:
        static constexpr slog::level ini_level = slog::info;
        slog::level level = ini_level;
        std::string buffer;
    };
};

#endif
