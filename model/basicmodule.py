import torch
import torch.nn as nn
import time


class BasicModule(nn.Module):
    def __init__(self):
        super(BasicModule, self).__init__()
        self.model_name = str(type(self))  # 默认名称

    def load(self,path):
        self.load_state_dict(torch.load(path))

    def save(self, name=None):
        '''
            保存模型，默认使用“模型名字+时间”作为文件名
        对不同的时间保存一个checkpoint.pth记录已经训练的模型'''
        if name is None:
            prefix = 'checkpoints/' + self.model_name + '_'
            name = time.strftime(prefix + '%m%d_%H:%M:%S.pth')
        torch.save(self.state_dict(), name)
        return name

    def get_optimizer(self,lr,weight_decay):
        '''
        选取优化器,adam算法
        '''
        return torch.optim.Adam(self.parameters(),lr=lr,weight_decay=weight_decay)


class Flat(nn.Module):
    """
    把输入reshape成（batch_size,dim_length）
    """

    def __init__(self):
        super(Flat, self).__init__()
        # self.size = size

    def forward(self, x):
        return x.view(x.size(0), -1)
