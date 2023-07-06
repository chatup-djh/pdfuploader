import lightgbm as lgb
import numpy as np
import os

# 打印当前工作目录
print(os.getcwd())

# 加载模型
loaded_gbm = lgb.Booster(model_file='D:\project\Python\project2\djangoy\model\model.model')

# 定义特征列顺序
col=['price_area', 'tube_distance', 'convenience', 'floor_encode', 'latitude', 'longitude', 'towards_encode']

# 定义特征数据
new_data = np.array([[1.2, 3.4, 5.6, 0, 40.0, 116.0, 1]])

# 进行预测
pred = loaded_gbm.predict(new_data)

# 输出预测结果
print(pred)
