from __future__ import absolute_import, division, print_function

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

import numpy as np
import pandas as pd

from . import formatting


class Indexes(Mapping, formatting.ReprMixin):
    """Immutable proxy for Dataset or DataArrary indexes."""

    def __init__(self, indexes):
        """Not for public consumption.

        Parameters
        ----------
        indexes : Dict[Any, pandas.Index]
            Indexes held by this object.
        """
        self._indexes = indexes

    def __iter__(self):
        return iter(self._indexes)

    def __len__(self):
        return len(self._indexes)

    def __contains__(self, key):
        return key in self._indexes

    def __getitem__(self, key):
        return self._indexes[key]

    def __unicode__(self):
        return formatting.indexes_repr(self)


def default_indexes(coords, dims):
    """Default indexes for a Dataset/DataArray.

    Parameters
    ----------
    coords : Mapping[Any, xarray.Variable]
        Coordinate variables from which to draw default indexes.
    dims : iterable
        Iterable of dimension names.

    Returns
    -------
    Mapping[Any, pandas.Index] mapping indexing keys (levels/dimension names)
    to indexes used for indexing along that dimension.
    """
    return {key: coords[key].to_index() for key in dims if key in coords}


def result_indexes(input_indexes, output_coords):
    """Combine indexes from inputs into indexes for an operation result.

    Drops indexes corresponding to dropped coordinates.

    IMPORTANT: Assumes outputs are already aligned!

    Parameters
    ----------
    input_indexes : Sequence[Mapping[Any, pandas.Index]]
        Sequence of mappings of indexes to combine.
    output_coords : Sequence[Mapping[Any, pandas.Variable]
        Optional sequence of mappings provided output coordinates.

    Returns
    -------
    List[Mapping[Any, pandas.Index]] mapping variable names to indexes,
    for each requested mapping of output coordinates.
    """
    output_indexes = []
    for output_coords_item in output_coords:
        indexes = {}
        for input_indexes_item in input_indexes:
            for k, v in input_indexes_item.items():
                if k in output_coords_item:
                    indexes[k] = v
        output_indexes.append(indexes)
    return output_indexes
