"""Holoviews elements to display images as point markers."""
import param
from holoviews.core import Dimension
from holoviews.element.geom import Points


class ImagePoints(Points):
    """Set of coordinates in 2D space associated with images.

    ImagePoints represents a set of coordinates in 2D space associated
    with images, which may optionally be associated with any number of value
    dimensions.
    """

    group = param.String(default="ImagePoints", constant=True)

    vdims = param.List(default=[Dimension("Image")], bounds=(1, None))
