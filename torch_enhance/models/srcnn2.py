import torch
import torch.nn as nn

from .base import BaseModel
from .baseline import Bicubic


class SRCNN2(BaseModel):
    """ Re-implementation of the SRCNN model, variation 2

    Parameters
    ----------
    scale_factor : int
        Super-Resolution scale factor. Determines Low-Resolution downsampling.
    channels: int
        Number of input and output channels
    """

    def __init__(self, scale_factor: int, channels: int = 3):
        super().__init__()

        self.upsample = Bicubic(scale_factor)

        self.model = nn.Sequential(
            nn.Conv2d(
                in_channels=channels,
                out_channels=256,
                kernel_size=9,
                stride=1,
                padding=4,
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=256,
                out_channels=128,
                kernel_size=1,
                stride=1,
                padding=0,
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=128,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=1,
            ),
            nn.ReLU(),
            nn.Conv2d(
                in_channels=64,
                out_channels=channels,
                kernel_size=5,
                stride=1,
                padding=2,
            ),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Super-resolve Low-Resolution input tensor

        Parameters
        ----------
        x : torch.Tensor
            Input Low-Resolution image as tensor

        Returns
        -------
        torch.Tensor
            Super-Resolved image as tensor

        """
        x = self.upsample(x)
        x = self.model(x)
        return x
