"""Extension to holoviews.plotting.bokeh."""
from holoviews.core import Store
from holoviews.plotting.bokeh import associations

from ...element import ImagePoints
from .chart import ImagePointPlot

associations[ImagePoints] = ImagePointPlot
Store.register(associations, "bokeh")

__all__ = []
