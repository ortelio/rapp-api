#include <noos/noos>
#include <iostream>
// TODO: REMOVE and PLACE IN ROS TUTORIAL
int main()
{
    using namespace noos::cloud;
    /*
     * The image is loaded from its path to a picture class.
     * If you run the example inside examples folder, this path is valid.
     * In other cases, you'll have to change it for a proper one.
     */    
    auto pic = noos::object::picture("data/map_picture.png");

    /*
     * Now construct a lambda, std::function or bind your own functor.
     * This functor will receive the reply from the cloud **asynchronously**!
     * In this example we'll pass an inline lambda as the callback.
     * 
     * In order to use the correct callback, see the "callback" definition in each cloud class.
     * For example, the class `available_services` has a `callback` alias set to:
     *
     *      `using callback = std::function<void(bool)>;`
     *
     */
    std::string map_name = "old_map";
    auto callback = [](bool success) {
         std::cout << "Success uploading a map: " << std::boolalpha << success << std::endl;
     };

    /*
     * Finally we create a callable object and send the information to the platform
     * with a timeout of 2 seconds
     * For more information /see noos::cloud::callable
     *
     * The actual parameter depends on the cloud class you're using,
     * so for a complete list, you need to read and understand how each cloud class functions.
     */
    auto callable_upload = call<upload_map,false>(callback, map_name, pic);
    callable_upload.send();
    
    std::this_thread::sleep_for(std::chrono::milliseconds(100));

    /*
     * Repeat the process for delete the map
     */
    auto callback2 = [](bool success) {
         std::cout << "Success deleting map: " << std::boolalpha << success << std::endl;
     };

    auto callable_delete = call<delete_map,false>(callback2, map_name);
    callable_delete.send();

    return 0;
}
