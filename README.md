# TokaiOnAir
この動画の前後に何があった？と思うことありませんか

ということで今回は動画の一覧を抽出してgrepできるようにしました

## 特定チャンネルの動画一覧を取得
APIの登録が必要

2020/10/3時点の東海オンエアの動画一覧はリポジトリに含まれている  
（他の動画関連データも取得すれば良かった気がする）

1. 環境変数`YOUTUBE_API_ACCESS_KEY`を設定

2. get_all_video.pyを実行し標準入力でチャンネルIDを渡す
```shell
$ python get_all_videos.py
[チャンネルID]
```

3. videos.txtに動画のURL一覧が作成日の昇順で吐き出される

## grepする
前後の動画を取得する
```shell
$ cat videos.txt | grep [動画ID] -[前後に表示する本数]
```

いろいろつなげてみたり
```shell
$ cat videos.txt | grep [動画ID] -[前後に表示する本数] | sed -n 1 | xargs open
```
ラップするといいかもね

前の行の取得は`sed`を使わなくても`grep`で取れる気がしている