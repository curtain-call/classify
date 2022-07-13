'''
对于网络模型所有超参数的配置
单独放进一个文件
'''

import warnings
import torch as t


class DefaultConfig(object):
    env = "default"  # visdom环境
    vis_port = 8097  # visdom端口

    model = "resnet34"  # 使用的模型

    train_data_root = "/dataset/dogsVScats/data/catvsdog/train/"  # 训练集存放路径
    test_data_root = "/dataset/dogsVScats/data/catvsdog/test/"  # 测试集存放路径

    load_model_path = None  # 加载预训练模型的路径，None表示不加载

    batch_size = 8  # batch_size
    use_gpu = True
    num_workers = 4
    print_freq = 50

    debug_file = ""
    result_file = "./submission.csv"

    max_epoch = 10
    lr = 0.001
    lr_decay = 0.95
    weight_decay = 1e-4  # 损失函数

    """根据字典更新config参数，便于命令行更改参数"""

    def parse(self, kwargs):

        """更新配置参数"""
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning:opt has not attribut %s" % k)
            setattr(self, k, v)

        """打印配置信息"""
        print("user config:")
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                print(k, getattr(self, k))


opt = DefaultConfig()
if __name__ == '__main__':
    new_config = {'lr': 0.1, 'use_gpu': False}
    opt.parse(new_config)
    print("*************", opt.lr, opt.use_gpu)
'''
原值：
lr = 0.001
gpu：true
'''
