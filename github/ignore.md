# Gitの管理下に置きたくないファイルを設定する.
``.gitignore``というファイルにGitの管理下に置きたくないファイルを書いておく.
次のようなディレクトリ構造でmain_org.c,tmp.c,projectB(で)をGit管理下に置きたくない場合を考える.
```
workingdir
|
|---projectA/
|   |
|   |-main.c
|   |-main_org.c
|
|---projectB/
| 
|---readme.md
|---tmp.c
```

``.gitignore``ファイルの中には次のように記述する.
```
tmp.c
projectA/main_org.c
projectB/
```

``git status``コマンドで管理表示を行ったとき,gitignoreファイルに
記述したファイルは表示されない.  
``git add .``コマンドを実行したときも,もちろんgitignoreファイルに
記述したファイルはステージングされない.