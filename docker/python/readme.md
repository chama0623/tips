# DockerでPython環境を構築する

Reference : https://zenn.dev/mosamosa/articles/b187cb5380be87

1. docker-Desktopにおいて右上の歯車マーク(setting)からResources>WSL INTEGRATIONでUbuntu-20.04を有効にする. 

2. 次のコマンドを実行してコンテナをインストールする. このコンテナはPythonイメージベースではなくUbuntuイメージベースである. このため, 
pythonの他に頻繁に使う開発ツール(Git, vim)や形態素解析エンジンのインストールを行う. Dockerfileに追記することで他のツールのインストールが可能である. またPythonにおいてインストールするライブラリはrequirements.txtに記述する. さらにmatplotlibの日本語対応のためにIPAexfontを適用する処理を行う. この処理ではおおよそ36GBのファイルをインストールするため時間がかかる.

```
docker build -t ml_base:latest .
```

3. インストールが完了したらコンテナを起動する. コンテナの起動は次のコマンドで行う. 今回は--rmオプションでコンテナの終了時にそのコンテナを削除する(作業内容はセーブされる). そしてコンテナ名は--nameオプションで常に「python3.8」で起動するように設定している. 
```
docker run -it --name python3.8 -p 8888:8888 --gpus all --mount source=mlws,target=/mlws -t  ml_base:latest
```
2回目以降は次のコマンドでコンテナをスタートさせればよい
```
docker start python3.8
```

4. bashを起動して日本語設定を行う. bashの起動コマンドを次に示す.
```
docker exec -it python3.8 bash
```
bashを起動したら, 「/usr/local/lib/python3.8/dist-packages/matplotlib/mpl-data」にある
matplotlibrcを編集する. 具体的には「#font.family:  sans-serif」を「##font.family:  sans-serif」に変更する. 

5. GPUが使用できるか確認する. localhost:8888からJupyterlabを開きConsoleで次のコードを実行する.
```python
from tensorflow.python.client import device_lib
device_lib.list_local_devices()

[name: "/device:CPU:0"
 device_type: "CPU"
 memory_limit: 268435456
 locality {
 }
 incarnation: 5706910557682975930
 xla_global_id: -1,
 name: "/device:GPU:0"
 device_type: "GPU"
 memory_limit: 4120313856
 locality {
   bus_id: 1
   links {
   }
 }
 incarnation: 17555109577345631864
 physical_device_desc: "device: 0, name: NVIDIA GeForce RTX 2060, pci bus id: 0000:0a:00.0, compute capability: 7.5"
 xla_global_id: 416903419]
```

次のコードを実行してtensorflowで実際にGPUが使われていることを確認してもよい.
```python
import tensorflow as tf
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
iris = load_iris()

data_X = iris.data
data_y = to_categorical(iris.target)

train_X, test_X, train_y, test_y = train_test_split(data_X, data_y, test_size=0.3, random_state=0)

model = tf.keras.models.Sequential([
    tf.keras.layers.Input(4),
    tf.keras.layers.Dense(300, activation='relu'),
    tf.keras.layers.Dense(300, activation='relu'),
    tf.keras.layers.Dense(300, activation='relu'),
    tf.keras.layers.Dense(500, activation='relu'),
    tf.keras.layers.Dense(700, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

result = model.fit(train_X, train_y, batch_size=32, epochs=3, validation_data=(test_X, test_y), verbose=1)
```

## その他
jupyterlabのデフォルトディレクトリは/mlwsに設定されている.