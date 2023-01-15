---
layout: page
title: Metacalibration
description: for Euclid & Roman
img: assets/img/metacal_Q.png
date:   2021-06-13 17:40:57 -0400
importance: 1
category: work
permalink: /projects/metacalibration-for-Euclid/
---

The complexity and the realism in the image simulations must be increase to calibrate shear as the lensing surveys get better and the precision in our results improve. Metacalibration is a new player in the field which attempts to solve this problem by calibrating shear from the observed image itself. However, this relies on the images being Nyquist sampled. By design, space-based surveys such as Euclid and WFIRST are not Nyquist-sampled.

<figure>
<img src="{{ site.base_url}}/assets/img/metacal_Q.png" width="30%" align="right">
</figure>
We attempted to quantify the impact on shear biases for Euclid if we were to use this approach on the individual exposures. We see clear evidence of biases in galaxy shapes that depend on the size, ellipticity and the orientation of the galaxies! Our preliminary analysis suggests that the bias misestimation can be as hugh as 5% making metacalibration not a viable option for these space-based missions. We are working on getting this paper to its final form. Accurate shear measurement for these missions is going to be challenging task!

In order to circumvent this problem, and to mitigate the issue of introducing a shear-dependent noise correlation, I am developing an alternative approach to metacalibration. In contrast to the original, _active_ metacalibration where the observed data is altered, my approach is _passive_ involving the manipulation of the filter functions (weight functions) used to extract shear from galaxy images.
<div align="right">[<a href="index.html#projectlist">back</a>]</div>
Papers that have come out of this project:
<ol reversed>
<li><a href="https://ui.adsabs.harvard.edu/abs/2020arXiv201004164K/abstract">Mitigating the effects of undersampling in weak lensing shear estimation with metacalibration</a><br>
<b>A. Kannawadi</b>, E. Rosenberg, H. Hoekstra, arXiv:2010:04164</li>
<li><a href="https://ui.adsabs.harvard.edu/abs/2020arXiv201004178H/abstract">Accounting for object detection bias in weak gravitational lensing studies</a><br>
H. Hoekstra, <b>A. Kannawadi</b>, T. D. Kitching, arXiv:2010:04178</li>
</ol>
<hr>
