在Git中創建一個README.md檔步驟
	在專案目錄中創建README.md文件
	打開命令列終端,導航到你的Git專案目錄,然後執行以下命令來創建一個名為README.md的文件
		touch README.md
		這將在專案目錄中創建一個空的README.md文件
	編輯README.md文件
	使用文字編輯器(如Visual Studio Code、Sublime Text、Notepad++等)
		打開README.md檔,然後在其中添加專案的說明、文檔、示例代碼或其他資訊
		Markdown語法通常用於創建README檔,因為它支援格式化文字、添加連結、插入圖像等
		你可以在Markdown中編寫內容,然後保存檔
	以下是一個簡單的Markdown示例

# My Awesome Project

測試 Bootstrap theme (外購或免費) 如何與 Flask Bootstap 專案結合

## Installation

1. 將 Bootstrap theme 解壓縮後,放在 static 目錄中.
2. 將 theme 中的 index.html copy to templates/. 修改其中 src & href 的連結路徑
3. src 直接指向本地路徑; href 則使用 url_for("static", filename="theme 的目錄路徑")
4. 使用 render_template("index.html")

## Usage

和平常的 flask 標準做法相同