from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class ExportImages(Function):
    """Export images from am hbjson file."""
    input_hbjson = Inputs.file(

    )
