import tkinter as tk

# Canvasに円を描画するプログラム

# ウインドウを作成する
window = tk.Tk()
# キャンバスを作成
canvas = tk.Canvas(window, width=400, height=400, bg="white")
# pack()メソッドは、ウィジェット(Canvasなど)をウインドウ内に配置するメソッドです
# 引数なしの場合は親ウィジェットの中央に配置されます
canvas.pack()

# 現在の円のIDを保持する変数
current_circle = None

# クリックされた時の処理
def on_click(event):
    global current_circle
    # 既存の円があれば白で塗りつぶして「消す」
    if current_circle is not None:
        canvas.itemconfig(current_circle, fill="white")
    
    # クリックされた位置を中心に新しい円を描く
    # 円のサイズは直径100ピクセル 円の線の太さは0
    x, y = event.x, event.y
    radius = 50  # 半径50ピクセル
    current_circle = canvas.create_oval(
        x - radius, y - radius,  # 左上の座標
        x + radius, y + radius,  # 右下の座標
        fill="red",
        width=0
    )

# キャンバスにクリックイベントを紐付け
canvas.bind("<Button-1>", on_click)

# 最初の円を描く（中心に配置）
x = 200  # キャンバスの中心のx座標
y = 200  # キャンバスの中心のy座標
radius = 50
current_circle = canvas.create_oval(
    x - radius, y - radius,
    x + radius, y + radius,
    fill="red",
    width=0
)

# ウインドウを表示する
window.mainloop()