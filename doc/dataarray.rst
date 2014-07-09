DataArray
=========

:py:class:`xray.DataArray` is the foundational object for xray: a labeled,
multi-dimensional array.

Adding `dimensions` (names for axes, such as `'time'`) and `coordinates`
(tick labels, such as `'2014-01-01'`) values to numpy's
`ndarray <http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html>`__
makes many powerful operations possible:

-  Apply operations over dimensions by name: ``x.sum('time')``.
-  Select values by label instead of integer location:
   ``x.loc['2014-01-01']`` or ``x.sel(time='2014-01-01')``.
-  Mathematical operations (e.g., ``x - y``) vectorize across multiple
   dimensions (known in numpy as "broadcasting") based on dimension
   names, regardless of their original order.
-  Flexible split-apply-combine operations with groupby:
   ``x.groupby('time.dayofyear').mean()``.
-  Database like aligment based on coordinate labels that smoothly
   handles missing values: ``x, y = xray.align(x, y, join='outer')``.
-  Keep track of arbitrary metadata in the form of a Python dictionary:
   ``x.attrs``.

Comparison to pandas objects
----------------------------

Like a :py:class:`pandas.Series` or :py:class:`~pandas.DataFrame`,
`DataArray` objects have tick labels, termed `coordinates` in xray, that can be
used for alignment and as as an alternative to integer based indexing (via the
:py:class:`pandas.Index` object).

Unlike pandas objects, data arrays keep track of `dimensions` such as
`('x', 'y', 'z')`, and indexing a `DataArray` will always return another
`DataArray`, even if the value is 0-dimensional: data ararys can have any number
of dimensions. Data arrays also store dictionaries of arbitrary metadata
`attrs`.



Data arrays consist of 

The important differences are two



.. ipython:: python
   :suppress:

   import numpy as np
   np.random.seed(123456)

To get started, we will import numpy, pandas and xray:

.. ipython:: python

    import numpy as np
    import pandas as pd
    import xray

``Dataset`` objects
-------------------

:py:class:`xray.Dataset` is xray's primary data structure. It is a dict-like
container of labeled arrays (:py:class:`xray.DataArray` objects) with aligned
dimensions. It is designed as an in-memory representation of the data model
from the `NetCDF`__ file format.

__ http://www.unidata.ucar.edu/software/netcdf/

Creating a ``Dataset``
~~~~~~~~~~~~~~~~~~~~~~

To make an :py:class:`xray.Dataset` from scratch, pass in a dictionary with
values in the form ``(dimensions, data[, attributes])``.

- `dimensions` should be a sequence of strings.
- `data` should be a numpy.ndarray (or array-like object) that has a
  dimensionality equal to the length of the dimensions list.

.. ipython:: python

    foo_values = np.random.RandomState(0).rand(3, 4)
    times = pd.date_range('2000-01-01', periods=3)

    ds = xray.Dataset({'time': ('time', times),
                       'foo': (['time', 'space'], foo_values)})
    ds



You can also insert :py:class:`xray.Variable` or :py:class:`xray.DataArray`
objects directly into a ``Dataset``, or create an dataset from a
:py:class:`pandas.DataFrame` with
:py:meth:`Dataset.from_dataframe <xray.Dataset.from_dataframe>` or from a
NetCDF file on disk with :py:func:`~xray.open_dataset`. See
`Working with pandas`_ and `Serialization and IO`_.
