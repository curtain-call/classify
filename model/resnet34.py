import torch
import torch.nn as nn
from .basicmodule import BasicModule


class ResBlock(torch.nn.Module):
    def __init__(self, inchannel, outchannel, stride=1, shortcut=None):
        super(ResBlock, self).__init__()
        self.left = self.left = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, 3, stride, 1, bias=False),
            nn.BatchNorm2d(outchannel),
            nn.ReLU(inplace=True),
            nn.Conv2d(outchannel, outchannel, 3, 1, 1, bias=False),
            nn.BatchNorm2d(outchannel))
        self.right = shortcut
        '''
        resnet34的mainpath是两层卷积，shortcut是单层卷积
        '''

    def forward(self, x):
        out = self.left(x)
        residual = x if self.right is None else self.right(x)
        '''
        有没有残差路径，没有的话就正常输出
        '''
        out += residual
        return torch.nn.functional.relu(out)


class ResNet34(BasicModule):
    def __init__(self, num_classes=2):
        super(ResNet34, self).__init__()
        # 定义网络名
        self.model_name = 'resnet34'

        # 图像转换
        self.pre = nn.Sequential(
            nn.Conv2d(3, 64, 7, 2, 3),  # 三通道,输出64个特征,7x7卷积,步长为2,padding三个像素
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(3, 2, 1)
        )

        # 重复的layer，分别有3，4，6，3个residual block
        self.layer1 = self._make_layer(64, 128, 3)
        self.layer2 = self._make_layer(128, 256, 4, stride=2)
        self.layer3 = self._make_layer(256, 512, 6, stride=2)
        self.layer4 = self._make_layer(512, 512, 3, stride=2)

        # 分类用的全连接
        self.fc = nn.Linear(512, num_classes)
        # self.softmax = nn.Softmax() 用不用softmax分类器??

    def _make_layer(self, inchannel, outchannel, block_num, stride=1):
        '''
        构建layer,包含多个残差块
        :param inchannel:
        :param outchannel:
        :param block_num:
        :param stride:
        :return:
        '''

        shortcut = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, 1, stride, bias=False),
            nn.BatchNorm2d(outchannel)
        )

        layers = []
        layers.append(ResBlock(inchannel, outchannel, stride, shortcut))

        for i in range(1, block_num):
            layers.append(ResBlock(outchannel, outchannel))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.pre(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = nn.functional.avg_pool2d(x, 7)
        x = x.view(x.size(0), -1)
        # x = self.fc(x)
        return self.fc(x)
