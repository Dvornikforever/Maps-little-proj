import PIL.Image as Image
import io
import base64
from byte_array import byte_data
from get_map import turn_into_image

b = base64.b64decode(turn_into_image())