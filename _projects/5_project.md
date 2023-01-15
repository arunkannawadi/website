---
layout: page
title: Mass mapping
description:
img: assets/img/massmap2.jpg
importance: 3
category: work
permalink: /projects/massmapping/
---

Dark matter haloes, which host large clusters of galaxies, also contain sub-haloes that are relics of various mergers over the cosmic eons.
Hierarchical ΛCDM structure formation model makes definite predictions on the statistics of sub-haloes.
The sub-halo mass function is therefore a powerful test of this theory in small scales (∼ 10kpc).
For this project, I propose to produce detailed mass maps of the galaxy clusters in <a href="https://home.strw.leidenuniv.nl/~hoekstra/Projects/MENeaCS.html">MENeaCS</a>.
Because these are nearby galaxy clusters, the higher angular resolution makes it possible to map detailed sub-structures in their mass distributions.
This project will be the first application of the GPU version of SaWLens3 software to real data.
The method is non-parametric and does not assume any functional form for the mass distribution.
The rationale behind this choice over the classic Kaiser-Squires inversion technique is that SaWLens is well-adapted to handle real data that include masks.
The algorithm is based on mesh-free free-form lensing reconstruction and has been shown on simulations to recover the true mass distribution.
An added advantage of this method is that it combines strong lensing features, such as arcs or multiple images whenever available. This work is at its infancy stage.
<figcaption> <center> <font size=3>Image credits: Clowe et al., (2006) </font></center> </figcaption>
![Bullet cluster](/images/massmap2.png){:width="100%"}

<hr>
