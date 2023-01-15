---
layout: page
title: Cosmic shear
description: Shear calibration and parameter inference
date:   2021-06-13 17:40:57 -0400
img: assets/img/sims2.png
importance: 2
category: work
permalink: image-simulations-KiDS
---

Galaxy shapes measured from noisy images are noisy and biased, since the shape is a non-linear function of the pixel values. This in turn leads to biased estimates for the weak lensing shear if not corrected for, and is known as noise bias. The precise value of the noise bias depends on the size and the signal-to-noise ratio of the galaxies, and hence are specific to each survey. The magnitude of the noise bias is typically evaluated through image simulations. And because the bias is survey specific, it is critical that the simulations match the data.

![Plot1]({{ site.base_url }}/images/data2.png){:width="50%"}
![Plot2]({{ site.base_url }}/images/sims2.png){:width="50%" align="right"}

We achieve this by taking the intrinsic galaxy properties from HST and simulating them under KiDS observing conditions. The animation on the right shows our emulations of a part of the COSMOS field. This work has highlighted the importance of accurately capturing the joint distributions, such as that of size-ellipticity, failing which the bias estimates can be very different from the true biases. The emulation also has an advantage that the galaxies can be assigned true photometric and spectroscopic redshifts from data, thereby enabling to quantify the impact of bias in tomographic bins due to errors in redshift.

Papers that have out of this project:
<ol reversed>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2020A%26A...633A..69H/abstract">KiDS+ VIKING-450: Cosmic shear tomography with optical+ infrared data</a><br>
H. Hildebrandt, F. Köhlinger, J. L. van den Busch, B. Joachimi, C. Heymans, <b>A. Kannawadi</b>, A. H. Wright, M. Asgari, C. Blake, H. Hoekstra, S. Joudaki, K. Kuijken, L. Miller, C. B. Morrison, T. Tröster, A. Amon, M. Archidiacono, S. Brieden, A. Choi, J. T.A.  de Jong, T. Erben, B. Giblin, A. Mead, J. A. Peacock, M. Radovich, P. Schneider, C. Sifón, M. Tewes (2019), A&A 633, A89</li>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2019A%26A...624A..92K/abstract">Towards emulating cosmic shear data: revisiting the calibration of the shear measurements for the Kilo-Degree Survey</a><br>
<b>A. Kannawadi</b>, H. Hoekstra, L. Miller, M. Viola, I. Fenech Conti, R. Herbonnet, T. Erben, C. Heymans, H. Hildebrandt, K. Kuijken, M. Vakili, A. H. Wright (2019), A&A 624, A92 </li>
</ol>
<hr>
