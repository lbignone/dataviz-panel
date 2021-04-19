"""Implementation of a PointPlot extension to interface with image_url."""
import numpy as np
from bokeh.transform import jitter
from holoviews.plotting.bokeh.chart import PointPlot


class ImagePointPlot(PointPlot):
    """Interface to image_url."""

    _plot_methods = dict(single="image_url", batched="image_url")
    _batched_style_opts = ["w", "h", "angle"]

    style_opts = [
        "w",
        "h",
        "angle",
        "dilate",
        "anchor",
        "alpha",
        "h_units",
        "w_units",
        "retry_attempts",
        "retry_timeout",
        "visible",
    ]

    def get_data(self, element, ranges, style):
        """Implementation of get_data method."""
        dims = element.dimensions(label=True)

        xidx, yidx = (1, 0) if self.invert_axes else (0, 1)
        mapping = dict(x=dims[xidx], y=dims[yidx], url=dims[2])
        data = {}

        if not self.static_source or self.batched:
            xdim, ydim = dims[:2]
            data[xdim] = element.dimension_values(xdim)
            data[ydim] = element.dimension_values(ydim)
            data[dims[2]] = element.dimension_values(dims[2])
            self._categorize_data(data, dims[:2], element.dimensions())

        if "angle" in style and isinstance(style["angle"], (int, float)):
            style["angle"] = np.deg2rad(style["angle"])

        if self.jitter:
            if self.invert_axes:
                mapping["y"] = jitter(
                    dims[yidx], self.jitter, range=self.handles["y_range"]
                )
            else:
                mapping["x"] = jitter(
                    dims[xidx], self.jitter, range=self.handles["x_range"]
                )

        self._get_hover_data(data, element)

        return data, mapping, style
