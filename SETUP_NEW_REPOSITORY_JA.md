# GitHub Desktop：既存のAvani共有リポジトリに触れず、新しく作る方法

推奨名：**dog2-agi-predictor**

## 最も安全な作業順序

1. このZIPをMacで展開。`dog2-agi-predictor` フォルダができます。元の `dog2-all56-pwa` フォルダには一切コピーしません。
2. GitHub Desktopを開き、**File → Add Local Repository... → Choose...** から、新しい `dog2-agi-predictor` フォルダを選びます。
3. 「This directory does not appear to be a Git repository. Would you like to create a repository here?」と表示されたら、**Create a repository here** を選びます（GitHub Desktopの表示はバージョンで少し異なる可能性があります）。
4. **Current repository** が `dog2-agi-predictor` であることを、コミットする前に必ず確認してください。`dog2-all56-pwa` になっていたら操作しないでください。
5. 変更一覧に新アプリのファイルが並んでいることを確認し、Summaryに `Initial AGI-branded DOG2 predictor PWA` と入力。**Commit to main**。
6. **Publish repository** を選択。名前を `dog2-agi-predictor` とし、公開範囲を選択します。**公開前に `app.json` 内のモデル/マッピングを公開してよいか、必ず確認**してください。
7. パブリックのGitHub Pages公開を行う場合は、GitHub Webの新リポジトリ → **Settings → Pages** → **Deploy from a branch** → **main** / **(root)** → **Save**。
8. 公開URLは `https://<GitHubユーザー名>.github.io/dog2-agi-predictor/` です。URLが実際に有効になるまで、GitHub PagesのDeployment状況を確認します。
9. Web、iPhoneのSafariとホーム画面追加、TSV/PDF出力、実データでのDFI/OS予測、TARGET表示をそれぞれ試します。

## 重要事項

- ZIPの中にあるファイルを **別の既存リポジトリにコピーしない** でください。
- GitHub Pages用の `index.html` / `.nojekyll` / `app.json` / `shinylive/` / `icons/` / `manifest.webmanifest` は全てリポジトリの直下に置きます。
- これは独立したコピーです。今後新アプリでコミット・Pushしても、Avaniさんと共有している旧リポジトリは変更されません。
- ブラウザ内でRが動くShinylive方式なので、モデル資産は利用者に配布されます。
- 保存済み旧PWAとの干渉を避けるため、**異なるリポジトリ名・URL**で公開してください。

## ターミナルでもチェックできます

```bash
cd ~/Downloads/dog2-agi-predictor  # 実際に展開した場所に変更
python3 verify_site.py
python3 -m http.server 8000
```

GitHubリポジトリそのものをChatGPTが作成・Pushしたわけではありません。公開操作はGitHub Desktopで行ってください。
