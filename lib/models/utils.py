import torch


def channel_shuffle(x, groups):
    batchsize, num_channels, height, width = x.size()
    assert num_channels % groups == 0, (
        f"channels ({num_channels}) should be divisible by groups ({groups})")
    channels_per_group = num_channels // groups
    x = x.view(batchsize, groups, channels_per_group, height, width)
    x = x.transpose(1, 2).contiguous()
    x = x.view(batchsize, -1, height, width)
    return x
