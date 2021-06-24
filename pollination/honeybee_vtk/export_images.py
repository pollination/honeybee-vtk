from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class ExportImages(Function):
    """Export images from am hbjson file."""

    hbjson_file = Inputs.file(
        description='HBJSON file.',
        path='input.hbjson'
    )

    name = Inputs.str(
        description='Name of image files.',
        default='Camera'
    )

    folder = Inputs.folder(
        description='Target folder where the images will be written.',
        path='output_folder',
        default='.'
    )

    image_type = Inputs.str(
        description='Choose the type of image file.',
        default='jpg'
    )

    image_width = Inputs.int(
        description='Width of images in pixels.',
        default=2500
    )

    image_height = Inputs.int(
        description='height of images in pixels.',
        default=2500
    )

    display_mode_model = Inputs.str(
        description='Set display mode fro the model.',
        default='shaded'
    )

    grid_options = Inputs.str(
        description='Export sensor grids as either points or meshes.',
        default='ignore'
    )

    display_mode_grid = Inputs.str(
        description='Set display mode for the Sensorgrids.',
        default='shaded'
    )

    view_path = Inputs.path(
        description='File path to the radiance view file.',
        path='view_file',
        default='.'
    )

    config_path = Inputs.path(
        description='File path to the config json file which can be used to mount'
        'simulation data on HBJSON.',
        path='config.json'
    )

    @command
    def export_images(self):
        return 'honeybee-vtk input.hbjson output_folder {{self.name}}'\
            ' {{self.image_type}} {{self.image_width}} {{self.image_height}}'\
            ' {{self.display_model_mode}} {{self.grid_options}}'\
            ' {{self.display_mode_grid}} view_file config.json'

    images = Outputs.folder(
        description='Folder location where the images are exported.',
        path='target_folder'
    )
