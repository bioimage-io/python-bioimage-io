from typing import Sequence, Tuple

import numpy

from pybio.core.readers.base import PyBioReader
from pybio.spec.node import OutputArray, Axes


class DummyReader(PyBioReader):
    def __init__(self):
        x_shape = (15, 4)
        y_shape = (15,)
        self.X = numpy.arange(60).reshape(x_shape)
        self.Y = numpy.array([i < 7 for i in range(y_shape[0])])

        super().__init__(
            outputs=(
                OutputArray(
                    name="dummyX",
                    axes=Axes("bx"),
                    data_type="int",
                    data_range=(0, 60),
                    shape=x_shape,
                    halo=(0,) * len(x_shape),
                ),
                OutputArray(
                    name="dummyY",
                    axes=Axes("b"),
                    data_type="bool",
                    data_range=(0, 1),
                    shape=y_shape,
                    halo=(0,) * len(y_shape),
                ),
            )
        )

    def __getitem__(self, rois: Tuple[Tuple[slice, ...], ...]) -> Sequence[numpy.ndarray]:
        assert len(rois) == 2
        return tuple(data[roi] for data, roi in zip([self.X, self.Y], rois))
