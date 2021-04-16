"""Tests for element operations."""
import numpy as np
from holoviews import Layout
from holoviews import Points
from holoviews.element.comparison import ComparisonTestCase
from holoviews.plotting import bokeh  # NOQA Needed to register backend

from dataviz_panel.operation import minimap


class TestMinimap(ComparisonTestCase):
    """Test minimap operation."""

    def test_points(self):
        """Test minimap creation for Point source."""
        arr = np.arange(4)
        points = Points(arr)
        minimap_points = minimap(points)
        self.assertIsInstance(minimap_points, Points)

    def test_layout(self):
        """Test minimap creation for Layout."""
        arr = np.arange(4)
        layout = Layout([Points(arr) + Points(arr)])
        minimap_points = minimap(layout)
        self.assertIsInstance(minimap_points, Layout)

    def test_rename(self):  # NOQA
        """Test that dimensions are renamed."""
        arr = np.arange(4)
        points = Points(arr)
        minimap_points = minimap(points)
        for dimension in minimap_points.dimensions():
            assert "minimap" in dimension.name

    def test_no_rename(self):
        """Test that dimensions are not changed."""
        arr = np.arange(4)
        points = Points(arr)
        minimap_points = minimap(points, rename_dimensions=False)
        self.assertEqual(points.dimensions(), minimap_points.dimensions())
