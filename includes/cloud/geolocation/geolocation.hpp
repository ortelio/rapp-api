#ifndef RAPP_CLOUD_GEOLOCATION
#define RAPP_CLOUD_GEOLOCATION
#include "includes.ihh"
namespace rapp {
namespace cloud {
/**
 * \brief geolocation service
 * \class geolocation
 * \version 0.7.0
 * \date 15 August 2016
 * \author Alex Gkiokas ,a.gkiokas@ortelio.co.uk>
 */
class geolocation :  public caller, public http_request
{
public:
    /**
     * \param ipaddr: the machine's ip
     * \param engine: the API (default ip-api)
     * \param callback: receives a JSON reply
     */
    geolocation(
                 const std::string ipaddr,
                 const std::string engine,
                 std::function<void(std::string)> callback
               )
	: http_header("POST /hop/geolocation HTTP/1.1\r\n"), 
      http_post(http_header::get_boundary()), 
      delegate_(callback)
	{
        boost::property_tree::ptree tree;
        tree.put("ipaddr", ipaddr);
        tree.put("engine", engine);

        std::stringstream ss;
        boost::property_tree::write_json(ss, tree, false);

        std::string json = ss.str();
        http_post::add_content("json", json, false); 
        http_post::end();
     
    }

    /**
     * \brief handle platform's JSON reply
     */
	void deserialise(std::string json) const
    {
        std::stringstream ss(json);
        delegate_(std::move(json));
    }


    /**
    * \brief method to fill the buffer with http_post and http_header information
    * \param info is the data of the platform    
    */
    boost::asio::streambuf fill_buffer(rapp::cloud::platform info)
    {
           return std::move(http_request::fill_buffer(info));
    }

private:   
    /// 
    std::function<void(std::string)> delegate_;
};
}
}
#endif
