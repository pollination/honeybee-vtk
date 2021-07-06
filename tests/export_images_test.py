from pollination.honeybee_vtk.export_images import ExportImages
from queenbee.plugin.function import Function


def test_export_images():
    function = ExportImages().queenbee
    assert function.name == 'export-images'
    assert isinstance(function, Function)
