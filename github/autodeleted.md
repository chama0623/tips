## git statusでdeletedと表示されるファイルを一括でrmするコマンド

```
git rm $(git ls-files --deleted)
```