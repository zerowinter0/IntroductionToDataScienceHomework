import torch
import torch.nn as nn
import os
import torchvision.transforms as transforms
from PIL import Image
# 加载彩色图像
color_image = Image.open("Desktop\\数据科学导论作业\\week7\\pic\\test.jpg")

# 定义转换
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1)  # 将图像转换为灰度，num_output_channels=1表示单通道灰度图
])

# 应用转换
gray_image = transform(color_image)

# 保存灰度图像
gray_image.save('Desktop\\数据科学导论作业\\week7\\pic\\gray.jpg')

# 显示灰度图像
gray_image.show()
