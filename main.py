from trainer import Trainer

if __name__ == '__main__':
    # trainer = Trainer("models/net.pth")
    # trainer = Trainer("models/net_0.8.pth")
    # trainer = Trainer("models/net_SGD_without_normal.pth")
    # trainer = Trainer("models/test.pth")
    # trainer = Trainer("models/net_Adam_with_normal.pth")
    # trainer = Trainer("models/net_SGD_with_normal.pth")
    # trainer = Trainer("models/net_Adam_with_normal_new_net.pth")# 残差块2层
    trainer = Trainer("models/net_Adam_with_normal_old_net.pth")  # 残差块3层
    trainer.train()
