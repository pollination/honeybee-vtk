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

    image_type = Inputs.str(
        description='Choose the type of image file.'
        'Choose from: png, jpg, ps, tiff, bmp, pnm.',
        default='png',
        spec={'type': 'string',
              'enum': ['png', 'jpg', 'ps', 'tiff', 'bmp', 'pnm']}
    )

    image_width = Inputs.int(
        description='Width of images in pixels.',
        default=2500
    )

    image_height = Inputs.int(
        description='Height of images in pixels.',
        default=2500
    )

    background_color = Inputs.str(
        description='Background color for the images as a string of rgb values.',
        default='255 255 255'
    )

    model_display_mode = Inputs.str(
        description='Set display mode for the model.'
        'Choose from: shaded, surface, surfacewithedges, wireframe, points.',
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

    grid_display_mode = Inputs.str(
        description='Set display mode for the Sensorgrids.'
        'Choose from: shaded, surface, surfacewithedges, wireframe, points',
        default='shaded',
        spec={'type': 'string',
              'enum': ['shaded', 'surface', 'surfacewithedges', 'wireframe', 'points']}
    )

    config_path = Inputs.path(
        description='File path to the config json file which can be used to mount'
        'simulation data on HBJSON.',
        path='config.json',
        optional=True
    )

    @command
    def export_images(self):
        return 'honeybee-vtk export-images --name {{self.name}} --image-type'\
            ' {{self.image_type}} --image-width {{self.image_width}} --image-height'\
            ' {{self.image_height}} --background-color {{self.background_color}}'\
            ' --model-display-mode {{self.display_model_mode}} --grid-options'\
            ' {{self.grid_options}} --grid-display-mode {{self.display_mode_grid}}'\
            ' --config config.json input.hbjson --folder target_folder'

    images = Outputs.folder(
        description='Folder location where the images are exported.',
        path='target_folder'
    )
