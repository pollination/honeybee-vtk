from pollination.honeybee_vtk.config import Config
from queenbee.plugin.function import Function


def test_write_config():
    function = Config().queenbee
    assert function.name == 'config'
    assert isinstance(function, Function)
