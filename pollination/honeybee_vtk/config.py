from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class Config(Function):
    """Write a config file to be consumed by other commands of honeybee-vtk."""

    input_file = Inputs.file(
        description='Path to the input json file.',
        path='input.json'
    )
    name = Inputs.str(
        description='Name of the config file.',
        default='config'
    )

    @command
    def write_config(self):
        return 'honeybee-vtk config input.json --name {{self.name}}'\
            ' --folder-path target_folder'

    config = Outputs.folder(
        description='Folder location where the config json is written.',
        path='target_folder'
    )
