from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs
from queenbee.io.common import ItemType


@dataclass
class ExportImages(Function):
    """Export images from am hbjson file."""

    hbjson_file = Inputs.file(
        description='HBJSON file.',
        path='input.hbjson'
    )

    image_type = Inputs.str(
        description='Choose the type of image file.'
        'Choose from: png, jpg, ps, tiff, bmp, pnm.',
        default='png',
        spec={'type': 'string',
              'enum': ['png', 'jpg', 'ps', 'tiff', 'bmp', 'pnm']}
    )

    image_width = Inputs.int(
        description='Width of images in pixels. If not set, x dimension of view will be'
        ' used.',
        default=0
    )

    image_height = Inputs.int(
        description='Height of images in pixels.If not set, y dimension of view will be'
        ' used.',
        default=0
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

    selection = Inputs.str(
        description='Select what to export.',
        default='model',
        spec={'type': 'string',
              'enum': ['model', 'grid', 'timestep']}
    )

    grid_filter = Inputs.list(
        description='Filter sensor grids by their identifiers. If specified, grids with'
        ' only these identifiers will be exported.',
        default=[],
        items_type=ItemType.String
    )

    text_content = Inputs.str(
        description='Text to be displayed on an image of a grid. This will put this'
        ' same text on all of the images.',
        default='',
        optional=True
    )

    text_height = Inputs.int(
        description='The height of the text in pixels for the text that will be'
        ' added to the image of a grid.',
        default=15,
    )

    text_color = Inputs.str(
        description='The text color of the text that will added to the image of'
        ' a grid.',
        default='0 0 0',
    )

    text_position = Inputs.str(
        description='The position of the text to be added to the images. This'
        ' setting is applied at the lower left point of the text. (0,0) will give you'
        ' the lower left corner of the image. (1,1) will give you the upper right'
        ' corner of the image.',
        default='0.05 0.05',
    )

    text_bold = Inputs.str(
        description='A flag to indicate whether to make the text bold or not for the text'
        ' that will be added to the image of a grid.',
        default='text-normal',
        spec={'type': 'string', 'enum': ['text-bold', 'text-normal']}
    )

    time_step_file_name = Inputs.str(
        description='File name for the timestep file without its extension.',
        default='',
        optional=True
    )

    periods_file = Inputs.file(
        description='File Path to the Periods json file which can be used'
        ' to define time periods and colors. A period is composed of two Ladybug DateTime'
        ' objects. First is the start DateTime and second is the End DateTime. Think of'
        ' these periods as filters of time steps. Images will be generated for'
        ' these periods only. You can also define colors for corresponding periods.',
        path='periods.json',
        optional=True
    )

    flat_gradient = Inputs.str(
        description=' A flag to indicate whether to use flat transparency or gradient'
        ' transparency in generating time step images. If flat is chosen, all the'
        ' images wil have the same level of transparency. If gradient is chosen, the'
        ' transparency of an image will be lower than the transparency of the image'
        ' coming above.',
        default='flat',
        spec={'type': 'string', 'enum': ['flat', 'gradient']}
    )

    transparent_images = Inputs.str(
        description='A flag to indicate whether to generate transparent images of each'
        ' timestep or not.',
        default='transparent-images',
        spec={'type': 'string', 'enum': ['transparent-images', 'no-images']}
    )

    gif_name = Inputs.str(
        description='File name for the gif file without its extension.',
        default='output',
        optional=True
    )

    gif_duration = Inputs.int(
        description='Duration of the gif in milliseconds.',
        default=1000,
    )

    gif_loop_count = Inputs.int(
        description='Number of times the gif will be looped.',
        default=0,
    )

    gif_linger_last_frame = Inputs.int(
        description='A number that will make the last frame linger for longer than'
        ' the duration by this multiple.',
        default=3
    )

    image_transparency = Inputs.float(
        description='Set the transparency of the image. 0.0 is fully transparent and'
        ' 1.0 is fully opaque.',
        default=0.5
    )

    @ command
    def export_images(self):
        return 'honeybee-vtk export-images --image-type'\
            ' {{self.image_type}} --image-width {{self.image_width}} --image-height'\
            ' {{self.image_height}} --background-color {{self.background_color}}'\
            ' --model-display-mode {{self.model_display_mode}} --grid-options'\
            ' {{self.grid_options}} --grid-display-mode {{self.grid_display_mode}}'\
            ' --config config.json --selection {{self.selection}}'\
            ' --grid-filter {{self.grid_filter}} --text-content {{self.text_content}}'\
            ' --text-height {{self.text_height}} --text-color {{self.text_color}}'\
            ' --text-position {{self.text_position}} --{{self.text_bold}}'\
            ' --time-step-file-name {{self.time_step_file_name}}'\
            ' --periods-file periods.json --{{self.flat_gradient}}'\
            ' --{{self.transparent_images}} --gif-name {{self.gif_name}}'\
            ' --gif-duration {{self.gif_duration}}'\
            ' --gif-loop-count {{self.gif_loop_count}} --gif-linger-last-frame'\
            ' {{self.gif_linger_last_frame}} --image-transparency'\
            ' {{self.image_transparency}} input.hbjson --folder target_folder'

    images = Outputs.folder(
        description='Folder location where the images are exported.',
        path='target_folder'
    )
