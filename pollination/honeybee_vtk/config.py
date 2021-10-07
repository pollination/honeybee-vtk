from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs
from queenbee.io.common import ItemType


@dataclass
class Config(Function):
    """Write a config file to be consumed by honeybee-vtk."""

    paths = Inputs.list(
        description='Paths to the result folders.',
        items_type=ItemType.String
    )

    id = Inputs.list(
        description='List of strings representing identifiers for the data that will be'
        ' mounted on the model.',
        items_type=ItemType.String
    )

    unit = Inputs.list(
        description='List of string representring the units for the data that will be'
        ' mounted on the model.',
        items_type=ItemType.String
    )

    name = Inputs.str(
        description='Name of the config file.',
        default='config'
    )

    @command
    def translate_model(self):
        path_str = ''
        id_str = ''
        unit_str = ''

        for i in range(len(self.paths)):
            path_str += self.paths[i] + ' '
            id_str += '--id=' + self.id[i] + ' '
            unit_str += '--unit=' + self.unit[i] + ' '

        res_str = path_str + id_str + unit_str + \
            '--name {{self.name}} --config-path target_folder'

        return res_str

    config = Outputs.folder(
        description='Folder location where the config json is written.',
        path='target_folder'
    )
