from .base import BaseModel
from .baseline import Bicubic
from .srcnn import SRCNN
from .edsr import EDSR
from .vdsr import VDSR
from .espcn import ESPCN
from .srresnet import SRResNet
from .srcnn1 import SRCNN1
from .srcnn2 import SRCNN2
from .srcnn3 import SRCNN3

__all__ = ["BaseModel", "Bicubic", "SRCNN",
           "SRCNN1", "SRCNN2", "SCRNN3", "VDSR", "EDSR", "ESPCN", "SRResNet"]
