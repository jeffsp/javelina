/// @file face_detection.h
/// @brief face detection
/// @author Jeff Perry <jeffsp@gmail.com>
/// @version 1.0
/// @date 2013-12-18

#ifndef FACE_DETECTION_H
#define FACE_DETECTION_H

#include <cassert>
#include <vector>
#include <iostream>
#include <stdexcept>
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/imgproc/imgproc.hpp"

namespace javelina
{

namespace face_detection
{

typedef std::vector<cv::Point2f> points;
typedef std::vector<cv::Rect> rects;

rects fix_eyes (const rects &e, const cv::Rect &f)
{
    rects eyes (e);
    // make sure right eye comes first
    if (eyes.size () > 1 && eyes[0].x > eyes[1].x)
        std::swap (eyes[0], eyes[1]);
    return eyes;
}

class face
{
    private:
    const cv::Rect rect;
    const rects eyes;
    public:
    face (const cv::Rect &rect, const rects &eyes)
        : rect (rect)
        , eyes (eyes)
    {
    }
    cv::Rect get_rect () const
    {
        return rect;
    }
    rects get_eyes () const
    {
        return eyes;
    }
};

typedef std::vector<face> faces;

class face_detector
{
    private:
    cv::CascadeClassifier face_cascade;
    cv::CascadeClassifier eyes_cascade;
    public:
    face_detector (const std::string &fcn = "haarcascade_frontalface_alt.xml",
        const std::string &ecn = "haarcascade_eye_tree_eyeglasses.xml")
    {
        std::clog << "loading " << fcn << std::endl;
        if (!face_cascade.load (fcn))
            throw std::runtime_error ("Error loading face cascade");
        std::clog << "loading " << ecn << std::endl;
        if (!eyes_cascade.load (ecn))
            throw std::runtime_error ("Error loading eyes cascade");
    }
    faces get_faces (const cv::Mat &img)
    {
        // Search within grayscale
        cv::Mat gs;
        cvtColor (img, gs, cv::COLOR_BGR2GRAY);

        rects f;
        face_cascade.detectMultiScale (gs, f, 1.1, 2);

        faces faces;
        for (auto i : f)
        {
            rects e;
            eyes_cascade.detectMultiScale (img (i), e, 1.1, 2);
            faces.push_back (face (i, fix_eyes (e, i)));
        }
        return faces;
    }
};

}

}

#endif
