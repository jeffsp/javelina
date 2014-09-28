
# Javelina
Content Based Image Retrieval

## Problem Description
* *U*: Dataset of unstructured data points (images).
* *U\[i\]*: Unstructured data point *i*.
* *F()*: Mapping from unstructured data point to structured data point.
* *F\[j\]()*: Mapping function *j*.
* *F\[j\](U\[i\])*: Mapping function *j* applied to image *i*.
* *S\[k\]=F\[j\]\(U\[i\]\)*: Mapping function *j* applied to image *i* yielding structured data point *k*.
* *D(a,b)*: Distance metric applied to two structured data points.

## Structured Data Tree
* Original Path
    * e.g.: "/var/javelina/original/image.jpg"
* Standard Converted Image Path
    * e.g.: "/var/javelina/standard/image.ppm"
* Original MD5Sum
* Standard Converted Image MD5Sum
* Luminance
    * Image
        * Average/Variance/Skew/Kurtosis
    * Segments
        * Average/Variance/Skew/Kurtosis
* Chromaticity
    * Image
        * Average/Variance/Skew/Kurtosis
    * Segments
        * Average/Variance/Skew/Kurtosis
* Geometry
    * Edge Orientation Distribution
        * Image
            * Average/Variance/Skew/Kurtosis
        * Segments
            * Average/Variance/Skew/Kurtosis
    * Edge Pair Distribution
        * Distance, Direction, Orientation
        * Image
            * Average/Variance/Skew/Kurtosis
        * Segments
            * Average/Variance/Skew/Kurtosis
* Texture
    * RMS Contrast Distribution
* Biological
    * Number of Faces
    * Faces
        * Size
        * Color
        * Eyes
* Overlapping Pyramid
    * 3X3 Overlapping Blocks
    * Recursive \(Contains Structured Data Trees\)
* SIFT
* Deep Learning
    * Category
    * Objects

## Tasks
### UI
* Admin
    * Upload
        * Single Image
            * URL
            * Local
        * Zip File of Images
        * URL Scraper
    * Convert Uploads to Standard Size/Format
        * E.g.: 1024x1024 8-bit PPM
        * Display Number of Available Uploads
    * Add Uploads to Database
        * Display Number of Converted Uploads
    * Rebuild Entire Database
        * Are you sure?
* View
    * Upload
        * Local Image
        * Image URL
    * View Images and Scores
    * Radio Buttons for Enabling/Disabling Dimensions

### Server Side Engine
* Convert Unstructured Data to Structured Data
    * Unstructured PPM Input
    * Structured JSON Output
* Mapping function
	* Structured JSON Input, 2 data points
	* Numerical Score Output, \[0.0, 1.0\]

### Implementation

```C++
// for uncorrelated data
class SU : public class S
{
	void update (const unsigned char c)
	{
		// Update 1st-4th moments
		...
	}
	...
};

// for correlated data
class SC : public class S
{
	void update (const image8_t &i)
	{
		// Update edge histogram
		...
	}
	...
};

// For each char in image
for (auto i : img)
{
	// update structured data point
	s.update (i)
	...
}
s.update (img);
...
```

## Support
* OpenStack
* AWS
* [Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_flask.html)
* Chef
* Docker
* VirtualEnv

## Problems/Questions
* How do you measure performance?

## References
* [Content Based Image Retrieval](https://en.wikipedia.org/wiki/Content-based_image_retrieval)
* [Metrics](http://en.wikipedia.org/wiki/Metric_\(mathematics\))
* [THE WINDSURF LIBRARY FOR THE EFFICIENT RETRIEVAL OF MULTIMEDIA HIERARCHICAL DATA](http://www-db.deis.unibo.it/research/papers/SIGMAP11.pdf)
* [ID3 Decision Tree Learning Algorithm](http://en.wikipedia.org/wiki/ID3_algorithm)

## Notes

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

> Examples of "unstructured data" may include books, journals, documents, metadata, health records, audio, video, analog
> data, images, files, and unstructured text such as the body of an e-mail message, Web page, or word-processor document.

[A probabilistic approach to 3-D inference of geons from a 2-D view](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=ABE246E451C1D552AE0B0CA6DB8D26F9?doi=10.1.1.38.729&rep=rep1&type=pdfa)


From [http://www.physicsforums.com](http://www.physicsforums.com/showthread.php?t=141624)

> There are several reasons why entropy, H, is not equivalent to
> variance, V, including:
>
> 1. For (1-D) continuous distributions, one has H <= (1/2) log (2 pi e
> V). This implies that
> (a) variance can be maximum (i.e., V=infinity) when entropy is not, eg,
> the Lorentz distribution
> p(x) = 1/(1+x^2), and
> (b) entropy can be minimum (i.e., H= - infinity) when variance is
> finite, eg, a mixutre of two delta-functions
> p(x) = (1/2) [ delta(x-a)/2 + delta(x-b) ] .
> Hence they are not equivalent as to the degree of uncertainty in a
> continuous distribution, as they do not agree with respect to "minimum"
> and "maximum" uncertainty.
>
> 2. For discrete distributions, such as the colour of a billiard ball,
> variance is totally artificial - eg, one must assign arbitrary numbers
> to each colour, and the variance will depend on the assignment. In
> contrast, entropy is independent of labelling - it is only a function
> of the probabilities.
>
> 3. If one distribution is "flatter" than another (look up
> "majorisation"), then the entropy of the first is greater than the
> entropy of the second. However, this ordering property does not hold
> for variance. Similarly, entropy is a concave function of probability,
> whereas variance is not (this is particularly important as to why
> entropy rather than variance appears in thermodynamics).
>
> 4. The (Shannon) information gained from a member of mixture of
> distributions is the difference of the entropy of the average
> distribution and the average of the entropies of the individual
> distributions. One cannot define an analogous information measure
> using variance that makes sense (essentially for reasons related to
> those given above).
>
> 5, There are some connections between entropy and variance (other than
> the inequality in item 1 above), for *particular classes* of
> distributions (eg, Gaussian distributions, for which the inequality
> becomes an equality). *If* one restricts attention to such a class,
> then there may be a monotonic relation between H and V. In such a
> case, one is simply some function of the other, and so they are in some
> sense equivalent.
