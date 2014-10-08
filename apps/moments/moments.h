/// @file moments.h
/// @brief compute 1-4 central moments
/// @author Jeff Perry <jeffsp@gmail.com>
/// @version 1.0
/// @date 2014-09-30

#pragma once

#include <cmath>
#include <iostream>
#include <stdexcept>

namespace javelina
{

namespace moments
{

class Moments
{
    private:
    size_t total;
    // moments about the origin
    size_t u1;
    size_t u2;
    size_t u3;
    size_t u4;
    public:
    Moments ()
        : total (0)
        , u1 (0)
        , u2 (0)
        , u3 (0)
        , u4 (0)
    {
    }
    void update (const unsigned char p)
    {
#pragma omp atomic
        ++total;
#pragma omp atomic
        u1 += p;
#pragma omp atomic
        u2 += p * p;
#pragma omp atomic
        u3 += p * p * p;
#pragma omp atomic
        u4 += p * p * p * p;
    }
    double mean () const
    {
        // first moment about the mean
        return static_cast<double> (u1) / total;
    }
    double variance () const
    {
        // second moment about the mean
        return static_cast<double> (u2) / total - mean () * mean ();
    }
    double skewness () const
    {
        // third moment about the mean
        const double m = mean ();
        const double v = variance ();
        const double sd = sqrt (v);
        // skewness = ( E(x^3) - 3 * mean * variance - mean^3 ) /  stddev^3
        const double s = (static_cast<double> (u3) / total - 3 * m * v - pow (m, 3.0)) / pow (sd, 3.0);
        return s;
    }
    double kurtosis () const
    {
        // excess kurtosis = (x4 / s4) - 3.0;
        // x4 = u4p - 4 * u1p * u3p + 6 * u1p^2 * u2p - 3 * u1p^4
        // s4 = variance^2
        const double u1p = static_cast<double> (u1) / total; // mean
        const double u2p = static_cast<double> (u2) / total;
        const double u3p = static_cast<double> (u3) / total;
        const double u4p = static_cast<double> (u4) / total;
        const double x4 = u4p - 4.0 * u1p * u3p + 6.0 * pow (u1p, 2.0) * u2p - 3.0 * pow (u1p, 4.0);
        const double v = variance ();
        const double s4 = v * v;
        return (x4 / s4) - 3.0;
    }
};

}

}
