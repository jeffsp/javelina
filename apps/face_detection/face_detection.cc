/// @file face_detection.cc
/// @brief get faces from a list of images
/// @author Jeff Perry <jeffsp@gmail.com>
/// @version 1.0
/// @date 2013-12-18

#include "face_detection.h"
#include "version.h"
#include "opencv2/highgui/highgui.hpp"

using namespace std;
using namespace cv;
using namespace javelina::face_detection;

const char *usage = "face_detection <fn.png|fn.jpg>";

int main (int argc, char **argv)
{
    try
    {
        clog << "face detection version " << version << endl;
        if (argc != 2)
            throw runtime_error (usage);

        string fn = argv[1];

        face_detector fd;

        clog << "reading " << fn << endl;
        Mat img = imread (fn, CV_LOAD_IMAGE_COLOR);
        if (img.data == NULL)
            throw runtime_error ("can't read image");

        // find faces
        faces faces = fd.get_faces (img);

        // print face and eye rects
        for (auto i : faces)
        {
            // face rect
            cout
                << "face"
                << " " << i.get_rect ().x
                << " " << i.get_rect ().y
                << " " << i.get_rect ().x + i.get_rect ().width
                << " " << i.get_rect ().y + i.get_rect ().height
                << endl;
            // eye rects
            for (auto j : i.get_eyes ())
                cout
                    << "eye"
                    << " " << i.get_rect ().x + j.x
                    << " " << i.get_rect ().y + j.y
                    << " " << i.get_rect ().x + j.x + j.width
                    << " " << i.get_rect ().y + j.y + j.height
                    << endl;
        }

        return 0;
    }
    catch (const exception &e)
    {
        cerr << e.what () << endl;
        return -1;
    }
}

