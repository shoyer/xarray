Frequently Asked Questions
==========================

xray and pandas
---------------

Why isn't pandas enough?
~~~~~~~~~~~~~~~~~~~~~~~~

[pandas][pandas], thanks to its unrivaled speed and flexibility, has emerged
as the premier python package for working with labeled arrays. So why are we
contributing to further [fragmentation][fragmentation] in the ecosystem for
working with data arrays in Python?

**xray** provides two data-structures that are missing in pandas:

  1. An extended array object (with labels) that is truly n-dimensional.
  2. A dataset object for holding a collection of these extended arrays
     aligned along shared coordinates.

Sometimes, we really want to work with collections of higher dimensional array
(`ndim > 2`), or arrays for which the order of dimensions (e.g., columns vs
rows) shouldn't really matter. This is particularly common when working with
climate and weather data, which is often natively expressed in 4 or more
dimensions.

The use of datasets, which allow for simultaneous manipulation and indexing of
many varibles, actually handles most of the use-cases for heterogeneously
typed arrays. For example, if you want to keep track of latitude and longitude
coordinates (numbers) as well as place names (strings) along your "location"
dimension, you can simply toss both arrays into your dataset.

This is a proven data model: the netCDF format has been around
[for decades][netcdf-background].

Pandas does support [N-dimensional panels][ndpanel], but the implementation
is very limited:

  - You need to create a new factory type for each dimensionality.
  - You can't do math between NDPanels with different dimensionality.
  - Each dimension in a NDPanel has a name (e.g., 'labels', 'items',
    'major_axis', etc.) but the dimension names refer to order, not their
    meaning. You can't specify an operation as to be applied along the "time"
    axis.

Fundamentally, the N-dimensional panel is limited by its context in the pandas
data model, which treats 2D `DataFrame`s as collections of 1D `Series`, 3D
`Panel`s as a collection of  2D `DataFrame`s, and so on. Quite simply, we
think the [Common Data Model][cdm] implemented in xray is better suited for
working with many scientific datasets.

[fragmentation]: http://wesmckinney.com/blog/?p=77
[netcdf-background]: http://www.unidata.ucar.edu/software/netcdf/docs/background.html
[ndpanel]: http://pandas.pydata.org/pandas-docs/stable/dsintro.html#panelnd-experimental

What's the relationship between xray and pandas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A major goal of xray is to provide multi-dimensional generalizations of the
:py:class:`pandas.Series` and  :py:class:`pandas.DataFrame`. To do so, we mimick
the pandas API and build upon the fundamental machinery of pandas, particularly
:py:class:`pandas.Index`. pandas is a hard dependency of xray.

The goal of xray is *not* to replace pandas. Rather, we attempting to make many
of the good ideas from pandas relevant for physical scientists and others who
need to work with multi-dimensionanl data.

When should I use xray instead of pandas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In brief: use xray if your data is fundamentally multi-dimensional. If your
data is unstructured or one-dimensional, stick with pandas, which is a more
developed toolkit for doing data analysis in Python.



Why not Iris?
-------------


Why not CDAT?
-------------

