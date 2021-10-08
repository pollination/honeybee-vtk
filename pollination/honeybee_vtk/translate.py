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

    data = Inputs.folder(
        description='Input data folder. This folder must include a config.json file',
        path='input_data', optional=True
    )

    @command
    def translate_model(self):
        return 'honeybee-vtk translate --name {{self.name}} --file-type' \
            ' {{self.file_type}} --display-mode {{self.display_mode}}' \
            ' --grid-options {{self.grid_options}}' \
            ' --config input_data/config.json input.hbjson --folder target_folder'

    output_file = Outputs.file(
        description='Created file.',
        path='target_folder/{{self.name}}.{{self.file_type}}'
    )
