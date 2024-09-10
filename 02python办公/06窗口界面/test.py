import tkinter as tk

root = tk.Tk()

# 创建一个Label控件来显示文本“电动机功率”
label = tk.Label(root, text="电动机功率")
label.pack()

# 创建一个IntVar对象并将其与变量A关联
A = tk.IntVar()
# 创建一个Entry控件，并将其与A关联，同时指定数据类型为int
entry = tk.Entry(root, textvariable=A, validate="key")
entry.pack()

# 定义一个函数来响应Entry控件中值的变化
def on_entry_changed(*args):
    print("输入框中的值变更为：", A.get())

# 将on_entry_changed函数与Entry控件关联
A.trace("w", on_entry_changed)

root.mainloop()