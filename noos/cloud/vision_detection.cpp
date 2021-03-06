#include "vision_detection.hpp"
namespace noos {
namespace cloud {

//service names
const std::string face_detection::uri   = "face_detection";
const std::string human_detection::uri  = "human_detection";
const std::string gender_detection::uri = "gender_detection";
const std::string age_detection::uri    = "age_detection";
const std::string orb_add_model::uri = "orb_add_model";
const std::string orb_del_model::uri = "orb_del_model";
const std::string orb_query::uri = "orb_query";
const std::string object_detection::uri   = "object_detection";

face_detection::face_detection(noos::object::picture image)
: http_request(make_http_uri(uri)),
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    nlohmann::json json_doc = {{"fast", true}};
    http_request::add_content("json", json_doc.dump(-1), true);
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}

face_detection::face_detection()
: http_request(make_http_uri(uri)),
  cloud_base(false)
{
    nlohmann::json json_doc = {{"fast", true}};
    vision_base::json = json_doc.dump(-1);
}

human_detection::human_detection(noos::object::picture image)
: http_request(make_http_uri(uri)), 
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}

human_detection::human_detection()
: http_request(make_http_uri(uri)), 
  cloud_base(false)
{
    nlohmann::json json_doc = {{"no_param", ""}};
    vision_base::json = json_doc.dump(-1);
}

gender_detection::gender_detection(noos::object::picture image)
: http_request(make_http_uri(uri)),
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}

gender_detection::gender_detection()
: http_request(make_http_uri(uri)),
  cloud_base(false)
{
    nlohmann::json json_doc = {{"no_param", ""}};
    vision_base::json = json_doc.dump(-1);
}

age_detection::age_detection(noos::object::picture image)
: http_request(make_http_uri(uri)),
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}

age_detection::age_detection()
: http_request(make_http_uri(uri)),
  cloud_base(false)
{
    nlohmann::json json_doc = {{"no_param", ""}};
    vision_base::json = json_doc.dump(-1);
}

orb_add_model::orb_add_model(noos::object::picture image,
                                   const std::string name)
: http_request(make_http_uri(uri)), 
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    nlohmann::json json_doc = {{"name", name}};
    http_request::add_content("json", json_doc.dump(-1), true);
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}
    
orb_add_model::orb_add_model(const std::string name)
: http_request(make_http_uri(uri)), 
  cloud_base(false)
{
    nlohmann::json json_doc = {{"name", name}};
    vision_base::json = json_doc.dump(-1);
}

orb_del_model::orb_del_model(const std::string model)
: http_request(make_http_uri(uri)), 
  cloud_base(true)
{
    http_request::make_multipart_form();
    nlohmann::json json_doc = {{"model", model}};
    http_request::add_content("json", json_doc.dump(-1), true);
    http_request::close();
}

/// Class orb_query
orb_query::orb_query(noos::object::picture image,
                                   const std::string model,
                                   const float threshold)
: http_request(make_http_uri(uri)), 
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    nlohmann::json json_doc = {{"model", model},
                               {"theta", threshold}};
    http_request::add_content("json", json_doc.dump(-1), true);
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}

orb_query::orb_query(const std::string model,
                                   const float threshold)
: http_request(make_http_uri(uri)), 
  cloud_base(false)
{
    nlohmann::json json_doc = {{"model", model},
                               {"theta", threshold}};
    vision_base::json = json_doc.dump(-1);
}

object_detection::object_detection(noos::object::picture image,
                                   const float threshold)
: http_request(make_http_uri(uri)),
  cloud_base(true)
{
    http_request::make_multipart_form();
    std::string fname = noos::misc::random_boundary() + "." + image.type();
    nlohmann::json json_doc = {{"threshold", threshold}};
    http_request::add_content("json", json_doc.dump(-1), true);
    http_request::add_content("file", fname, image.bytearray());
    http_request::close();
}

object_detection::object_detection(const float threshold)
: http_request(make_http_uri(uri)),
  cloud_base(false)
{
    nlohmann::json json_doc = {{"threshold", threshold}};
    vision_base::json = json_doc.dump(-1);
}

}
}
