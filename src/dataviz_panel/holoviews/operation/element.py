"""Collection of simple operations."""
import holoviews as hv
import param
from holoviews.operation import Operation
from holoviews.plotting.links import RangeToolLink

minimap_default_opts = hv.opts(
    width=150,
    height=150,
    xaxis=None,
    yaxis=None,
    toolbar=None,
    default_tools=[],
)


class minimap(Operation):  # NOQA
    """Creates a minimap version of an element."""

    axes = param.ListSelector(
        default=["x", "y"],
        objects=["x", "y"],
        doc="""
        Which axes to link the RangeTool to.""",
    )
    rename_dimensions = param.Boolean(
        default=True,
        doc="""
        Change the dimension names so not to interfere with shared axes.
        Dimension labels are not affected.""",
    )
    clone = param.Boolean(
        default=True,
        doc="""
        Clone the source element.""",
    )
    target = param.Parameter(
        default=None,
        doc="""
        Element to use as target for the RangeTool""",
    )

    def _process(self, element, key=None):
        if self.p.rename_dimensions:
            # change the dimension names, but keep the original labels
            dimension_map = {
                dim.name: hv.Dimension((f"{dim.name}_minimap", f"{dim.label}"))
                for dim in element.dimensions()
            }
            element = element.redim(**dimension_map)

        element = element.opts(minimap_default_opts, clone=self.p.clone)

        if self.p.target:
            RangeToolLink(element, self.p.target, axes=self.p.axes)

        return element
