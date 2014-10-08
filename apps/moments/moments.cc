/// @file moments.cc
/// @brief compute central moments
/// @author Jeff Perry <jeffsp@gmail.com>
/// @version 1.0
/// @date 2014-09-30

#include "moments.h"
#include "version.h"
#include "opencv2/highgui/highgui.hpp"

using namespace std;
using namespace cv;
using namespace javelina::moments;

const char *usage = "moments <fn.png|fn.jpg>";

int main (int argc, char **argv)
{
    try
    {
        clog << "moments version " << version << endl;
        if (argc != 2)
            throw runtime_error (usage);

        string fn = argv[1];

        clog << "reading " << fn << endl;
        Mat img = imread (fn, CV_LOAD_IMAGE_COLOR);
        if (img.data == NULL)
            throw runtime_error ("can't read image");
        if (img.depth () != CV_8U)
            throw runtime_error ("this is not an 8bpp image");
        if (img.channels () != 3 && img.channels () != 4)
            throw runtime_error ("this is not a 3- or 4-channel image");
        Moments mr;
        Moments mg;
        Moments mb;
#pragma omp parallel for schedule (dynamic)
        for (int i = 0; i < img.rows; ++i)
        {
            for (int j = 0; j < img.cols; ++j)
            {
                Vec3b p = img.at<Vec3b>(i, j);
                uchar r = p.val[2];
                uchar g = p.val[1];
                uchar b = p.val[0];
                mr.update (r);
                mg.update (g);
                mb.update (b);
            }
        }
        clog << "R: mean stdev skewness excess_kurt" << endl;
        clog << "G: mean stdev skewness excess_kurt" << endl;
        clog << "B: mean stdev skewness excess_kurt" << endl;
        cout << ' ' << mr.mean ();
        cout << ' ' << sqrt (mr.variance ());
        cout << ' ' << mr.skewness ();
        cout << ' ' << mr.kurtosis ();
        cout << endl;
        cout << ' ' << mg.mean ();
        cout << ' ' << sqrt (mg.variance ());
        cout << ' ' << mg.skewness ();
        cout << ' ' << mg.kurtosis ();
        cout << endl;
        cout << ' ' << mb.mean ();
        cout << ' ' << sqrt (mb.variance ());
        cout << ' ' << mb.skewness ();
        cout << ' ' << mb.kurtosis ();
        cout << endl;

        return 0;
    }
    catch (const exception &e)
    {
        cerr << e.what () << endl;
        return -1;
    }
}

