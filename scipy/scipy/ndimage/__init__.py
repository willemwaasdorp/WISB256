"""
=========================================================
Multi-dimensional image processing (:mod:`scipy.ndimage`)
=========================================================

.. currentmodule:: scipy.ndimage

This package contains various functions for multi-dimensional image
processing.


Filters :mod:`scipy.ndimage.filters`
====================================

.. module:: scipy.ndimage.filters

.. autosummary::
   :toctree: generated/

   convolve - Multi-dimensional convolution
   convolve1d - 1-D convolution along the given axis
   correlate - Multi-dimensional correlation
   correlate1d - 1-D correlation along the given axis
   gaussian_filter
   gaussian_filter1d
   gaussian_gradient_magnitude
   gaussian_laplace
   generic_filter - Multi-dimensional filter using a given function
   generic_filter1d - 1-D generic filter along the given axis
   generic_gradient_magnitude
   generic_laplace
   laplace - n-D Laplace filter based on approximate second derivatives
   maximum_filter
   maximum_filter1d
   median_filter - Calculates a multi-dimensional median filter
   minimum_filter
   minimum_filter1d
   percentile_filter - Calculates a multi-dimensional percentile filter
   prewitt
   rank_filter - Calculates a multi-dimensional rank filter
   sobel
   uniform_filter - Multi-dimensional uniform filter
   uniform_filter1d - 1-D uniform filter along the given axis

Fourier filters :mod:`scipy.ndimage.fourier`
============================================

.. module:: scipy.ndimage.fourier

.. autosummary::
   :toctree: generated/

   fourier_ellipsoid
   fourier_gaussian
   fourier_shift
   fourier_uniform

Interpolation :mod:`scipy.ndimage.interpolation`
================================================

.. module:: scipy.ndimage.interpolation

.. autosummary::
   :toctree: generated/

   affine_transform - Apply an affine transformation
   geometric_transform - Apply an arbritrary geometric transform
   map_coordinates - Map input array to new coordinates by interpolation
   rotate - Rotate an array
   shift - Shift an array
   spline_filter
   spline_filter1d
   zoom - Zoom an array

Measurements :mod:`scipy.ndimage.measurements`
==============================================

.. module:: scipy.ndimage.measurements

.. autosummary::
   :toctree: generated/

   center_of_mass - The center of mass of the values of an array at labels
   extrema - Min's and max's of an array at labels, with their positions
   find_objects - Find objects in a labeled array
   histogram - Histogram of the values of an array, optionally at labels
   label - Label features in an array
   labeled_comprehension
   maximum
   maximum_position
   mean - Mean of the values of an array at labels
   minimum
   minimum_position
   standard_deviation - Standard deviation of an n-D image array
   sum - Sum of the values of the array
   variance - Variance of the values of an n-D image array
   watershed_ift

Morphology :mod:`scipy.ndimage.morphology`
==========================================

.. module:: scipy.ndimage.morphology

.. autosummary::
   :toctree: generated/

   binary_closing
   binary_dilation
   binary_erosion
   binary_fill_holes
   binary_hit_or_miss
   binary_opening
   binary_propagation
   black_tophat
   distance_transform_bf
   distance_transform_cdt
   distance_transform_edt
   generate_binary_structure
   grey_closing
   grey_dilation
   grey_erosion
   grey_opening
   iterate_structure
   morphological_gradient
   morphological_laplace
   white_tophat

Utility
=======

.. currentmodule:: scipy.ndimage

.. autosummary::
   :toctree: generated/

   imread - Load an image from a file

"""

# Copyright (C) 2003-2005 Peter J. Verveer
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
# 3. The name of the author may not be used to endorse or promote
#    products derived from this software without specific prior
#    written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import division, print_function, absolute_import

from .filters import *
from .fourier import *
from .interpolation import *
from .measurements import *
from .morphology import *
from .io import *

__version__ = '2.0'

__all__ = [s for s in dir() if not s.startswith('_')]
from numpy.testing import Tester
test = Tester().test
