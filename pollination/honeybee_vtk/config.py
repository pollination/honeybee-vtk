from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class Config(Function):
    """Write a config file to be consumed by other commands of honeybee-vtk."""

    input_file = Inputs.file(
        description='Path to the input json file.',
        path='input.json'
    )

    @command
    def write_config(self):
        return 'honeybee-vtk config input.json --name config --folder-path .'

    config = Outputs.file(
        description='Config.json file.',
        path='config.json'
    )
