from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class Translate(Function):
    """Translate hbjson file to vtkjs/vtp/vtk format."""

    hbjson_file = Inputs.file(
        description='HBJSON file.',
        path='input.hbjson'
    )

    name = Inputs.str(
        description='Name of the zip file.',
        default='model'
    )

    file_type = Inputs.str(
        description='Choose the type of files to export from: vtkjs, vtp, vtk.',
        default='vtkjs',
        spec={'type': 'string',
              'enum': ['vtkjs', 'vtp', 'vtk']}
    )

    display_mode = Inputs.str(
        description='Set display mode for the model.'
        ' Choose from: shaded, surface, surfacewithedges, wireframe, points.',
        default='shaded',
        spec={'type': 'string',
              'enum': ['shaded', 'surface', 'surfacewithedges', 'wireframe', 'points']}
    )

    grid_options = Inputs.str(
        description='Export sensor grids as either points or meshes.'
        ' Choose from: ignore, points, meshes. Choosing ignore will not load grids.',
        default='ignore',
        spec={'type': 'string',
              'enum': ['ignore', 'points', 'meshes']}
    )

    config_path = Inputs.path(
        description='File path to the config json file which can be used to mount'
        'simulation data on HBJSON.',
        path='config.json',
        optional=True
    )

    @command
    def translate_model(self):
        return 'honeybee-vtk translate --name {{self.name}} --file-type' \
            ' {{self.file_type}} --display-mode {{self.display_mode}}' \
            ' --grid-options {{self.grid_options}}' \
            ' --config config.json input.hbjson --folder target_folder'

    files = Outputs.folder(
        description='Folder location where the files are exported.',
        path='target_folder'
    )
