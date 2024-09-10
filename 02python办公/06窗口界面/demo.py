import tkinter as tk

# 创建窗口
root = tk.Tk()
root.title("My Window")

# 定义变量
power = tk.IntVar()
voltage = tk.IntVar()









# 获取屏幕分辨率
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口大小为屏幕的一半
window_width = int(screen_width / 2)
window_height = int(screen_height / 2)
root.geometry(f"{window_width}x{window_height}")

# 创建输入框和输出框
label1 = tk.Label(root, text="电动机功率 单位KW")
label2 = tk.Label(root, text="工作电压 单位KV")
label3 = tk.Label(root, text="额定电流")
# entry = tk.Entry(root, textvariable=A, validate="key")
input1 = tk.Entry(root, width=30, textvariable=power, validate="key") 
input2 = tk.Entry(root, width=30, textvariable=voltage, validate="key")
output = tk.Text(root, height=10, width=30)

# 创建按钮
button1 = tk.Button(root, text="开始计算")
button2 = tk.Button(root, text="清空数据")
button3 = tk.Button(root, text="Button 3")

# 定义一个函数来响应Entry控件中值的变化
def on_entry_changed(*args):
    print("输入框中的值变更为：", power.get())

# 将on_entry_changed函数与Entry控件关联
power.trace("w", on_entry_changed)
voltage.trace("w", on_entry_changed)

# 放置控件
label1.place(relx=0.3, rely=0.2, anchor=tk.CENTER)
input1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
label2.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
input2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
label3.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
output.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button1.place(relx=0.3, rely=0.8, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
button3.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

# 运行窗口
root.mainloop()