import tkinter as tk
import random
import math

# 図形を描画するプログラム

# ウインドウを作成する
window = tk.Tk()
# キャンバスを作成
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# 図形の基本クラス
class Shape:
    def __init__(self, canvas, color, start_x, start_y, dx, dy):
        self.canvas = canvas
        self.size = 25  # 基本サイズ（円の半径、四角の半分の幅、三角の高さの半分）
        self.x = start_x
        self.y = start_y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.shape = None  # 図形のIDを保持
        self.draw()  # 図形を描画
    
    def draw(self):
        pass  # サブクラスで実装
    
    def move(self):
        # 次の位置を計算
        next_x = self.x + self.dx
        next_y = self.y + self.dy
        
        # 壁との衝突判定
        if next_x - self.size <= 0 or next_x + self.size >= 400:
            self.dx = -self.dx
        if next_y - self.size <= 0 or next_y + self.size >= 400:
            self.dy = -self.dy
        
        # 位置を更新
        self.x += self.dx
        self.y += self.dy
        
        # 図形を移動
        self.update_position()
    
    def update_position(self):
        pass  # サブクラスで実装

# 円クラス
class Circle(Shape):
    def draw(self):
        self.shape = self.canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color,
            width=0
        )
    
    def update_position(self):
        self.canvas.coords(
            self.shape,
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size
        )

# 四角クラス
class Square(Shape):
    def draw(self):
        self.shape = self.canvas.create_rectangle(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color,
            width=0
        )
    
    def update_position(self):
        self.canvas.coords(
            self.shape,
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size
        )

# 三角形クラス
class Triangle(Shape):
    def draw(self):
        # 三角形の頂点を計算
        points = [
            self.x, self.y - self.size,  # 上の頂点
            self.x - self.size, self.y + self.size,  # 左下の頂点
            self.x + self.size, self.y + self.size   # 右下の頂点
        ]
        self.shape = self.canvas.create_polygon(points, fill=self.color, width=0)
    
    def update_position(self):
        # 三角形の頂点を更新
        points = [
            self.x, self.y - self.size,
            self.x - self.size, self.y + self.size,
            self.x + self.size, self.y + self.size
        ]
        self.canvas.coords(self.shape, *points)

# 図形のインスタンスを作成
shapes = [
    Circle(canvas, "red", 100, 100, 2, 3),      # 赤い円
    Square(canvas, "blue", 300, 100, -2, 2),    # 青い四角
    Triangle(canvas, "green", 200, 300, 3, -2)  # 緑の三角
]

# アニメーションの更新処理
def update():
    for shape in shapes:
        shape.move()
    window.after(16, update)  # 約60FPS

# アニメーションを開始
update()

# ウインドウを表示する
window.mainloop()