import torch
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
import torch_geometric.transforms as T
from torch_geometric.nn import GCNConv
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

dataset = Planetoid(root='data/Cora', name='Cora', transform=T.NormalizeFeatures())
data = dataset[0]

import torch.optim as optim

# 定义GCN模型
class GCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# 初始化模型
model = GCN(in_channels=dataset.num_features, hidden_channels=16, out_channels=dataset.num_classes)

# 选择损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 训练模型
model.train()
for epoch in range(200):
    optimizer.zero_grad()
    output = model(data)
    loss = criterion(output[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()

# 评估模型
model.eval()
with torch.no_grad():
    pred = model(data).argmax(dim=1)
    acc = pred[data.test_mask].eq(data.y[data.test_mask]).sum().item() / data.test_mask.sum().item()
    print(f'Test Accuracy: {acc:.4f}')

# 使用PCA进行降维处理
pca = PCA(n_components=2)
data.x = pca.fit_transform(data.x)

# 绘制二维散点图
colors = [data.y[i] for i in range(len(data.y))]
plt.scatter(data.x[:, 0], data.x[:, 1], c=colors, cmap='viridis')
plt.colorbar()
plt.show()