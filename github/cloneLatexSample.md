# tipsリポジトリからlatex-sampleフォルダのみをcloneする方法

レポートとフォルダで次のコマンドを実行します.これによってtipsリポジトリから
latex-sampleフォルダのみをcloneできます. コマンドを実行した後に.gitフォルダを削除すれば
そのまま別のプロジェクトにpushできます.
```
git init 
git config core.sparsecheckout true
git remote add origin https://github.com/yudai0731/tips.git
echo /latex-sample > .git/info/sparse-checkout
git pull origin master
```