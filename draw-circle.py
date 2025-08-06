import tkinter as tk

# Canvasに円を描画するプログラム

# ウインドウを作成する
window = tk.Tk()
# 中心に円を描く
canvas = tk.Canvas(window, width=400, height=400)
# pack()メソッドは、ウィジェット(Canvasなど)をウインドウ内に配置するメソッドです
# 引数なしの場合は親ウィジェットの中央に配置されます
canvas.pack()

# 円を描く
canvas.create_oval(100, 100, 300, 300, fill="red")

# ウインドウを表示する
window.mainloop()