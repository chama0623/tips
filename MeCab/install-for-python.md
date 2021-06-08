# Pythonで扱えるMeCabのインストール 2021-06-09

実行環境
- Windows10 Pro
- Anaconda仮想環境
- Python3.8

手順
1. mecab-pythonのインストール
2. unidic-lite(辞書)のインストール
3. MeCabがインストールできたか確認

## 1. mecab-pythonのインストール
まず, python用のMeCabをインストールする. Anaconda Promptに次のように入力する. これでpython用のMeCabをインストールすることができた.

```
pip install mecab-python
```

## 2. unidic-lite(辞書)のインストール
次にunidic-lite(辞書)をインストールする. Anaconda Promptに次のように入力する.
```
pip instlal unidic-lite
```

## 3. MeCabがインストールできたか確認
Anaconda PromptからPythonを起動して, 次のコードを実行する.
```python
import MeCab

mecab = MeCab.Tagger()
sent = "人類に栄光あれ"
print(mecab.parse(sent))
```

実行すると次に示すように, 形態素解析の結果が得られる. 正常にMeCabをインストールできた.
```
人類    ジンルイ        ジンルイ        人類    名詞-普通名詞-一般                      1
に      ニ      ニ      に      助詞-格助詞
栄光    エーコー        エイコウ        栄光    名詞-普通名詞-一般                      0
あれ    アレ    アレ    彼れ    代名詞                  0
EOS

>>>
```