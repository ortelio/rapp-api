/*
 * Template implementation
 */
template <class cloud_type,
          class callback,
          class socket_type,
          class error_handle>
callable<cloud_type,callback,socket_type,error_handle>::callable(cloud_type object,
                                                                 callback functor)
: object(object), 
  functor(functor), 
  buffer_(std::make_unique<boost::asio::streambuf>())
{ }

template <class cloud_type,
          class callback,
          class socket_type,
          class error_handle>
template <typename... parameters>
callable<cloud_type,callback,socket_type,error_handle>::callable(parameters... args,
                                                                 callback functor)
: object(args...), 
  functor(functor),
  buffer_(std::make_unique<boost::asio::streambuf>())
{}

template <class cloud_type,
          class callback,
          class socket_type,
          class error_handle>
void callable<cloud_type,callback,socket_type,error_handle>::socket(
                                            std::function<void(std::string)> cloud_function,
                                            boost::asio::io_service & io_service,
                                            bool keep_alive)
{
    socket_ = std::make_unique<socket_type>(cloud_function, 
                                            [&](auto e){ error_handle()(e); }, 
                                            io_service, 
                                            keep_alive,
                                            *buffer_.get());
    assert(socket_);
}

template <class cloud_type,
          class callback,
          class socket_type,
          class error_handle>
void callable<cloud_type,callback,socket_type,error_handle>::send(
                                            boost::asio::ip::tcp::resolver::query & query,
                                            boost::asio::ip::tcp::resolver & resolver,
                                            unsigned int timeout,
                                            noos::cloud::platform endpoint)
{
    assert(socket_);
    //buffer_->consume(buffer_->size() + 1); 
    // TODO: we might need to "clear" the buffer first
    object.fill_buffer(boost::ref(*buffer_.get()), endpoint);
    socket_->is_connected() ? 
        socket_->send(query, resolver, timeout, *buffer_.get()) :
        socket_->begin(query, resolver, timeout);
}
