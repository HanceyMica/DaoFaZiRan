# -*- coding: utf-8 -*-
import tkinter as tk
import base64
import re
from PIL import Image, ImageTk
from ico2py import img

traditional_table = {
    '乾'  :'A',
    '坤'  :'B',
    '屯'  :'C',
    '蒙'  :'D',
    '需'  :'E',
    '訟'  :'F',
    '師'  :'G',
    '比'  :'H',
    '小畜':'I',
    '履'  :'J',
    '泰'  :'K',
    '否'  :'L',
    '同人':'M',
    '大有':'N',
    '謙'  :'O',
    '豫'  :'P',
    '隨'  :'Q',
    '蠱'  :'R',
    '臨'  :'S',
    '觀'  :'T',
    '噬咳':'U',
    '贲'  :'V',
    '剝'  :'W',
    '複'  :'X',
    '無妄':'Y',
    '大畜':'Z',
    '頤'  :'a',
    '大過':'b',
    '坎'  :'c',
    '離'  :'d',
    '鹹'  :'e',
    '恒'  :'f',
    '遯'  :'g',
    '大壯':'h',
    '晉'  :'i',
    '明夷':'j',
    '家人':'k',
    '睽'  :'l',
    '蹇'  :'m',
    '解'  :'n',
    '損'  :'o',
    '益'  :'p',
    '夬'  :'q',
    '姤'  :'r',
    '萃'  :'s',
    '升'  :'t',
    '困'  :'u',
    '井'  :'v',
    '革'  :'w',
    '鼎'  :'x',
    '震'  :'y',
    '根'  :'z',
    '漸'  :'0',
    '歸妹':'1',
    '豐'  :'2',
    '旅'  :'3',
    '巽'  :'4',
    '兌'  :'5',
    '渙'  :'6',
    '節'  :'7',
    '中孚':'8',
    '小過':'9',
    '既濟':'+',
    '未濟':'/',
}

simplified_table = {
    '乾'  :'A',
    '坤'  :'B',
    '屯'  :'C',
    '蒙'  :'D',
    '需'  :'E',
    '讼'  :'F',
    '师'  :'G',
    '比'  :'H',
    '小畜':'I',
    '履'  :'J',
    '泰'  :'K',
    '否'  :'L',
    '同人':'M',
    '大有':'N',
    '谦'  :'O',
    '豫'  :'P',
    '随'  :'Q',
    '蛊'  :'R',
    '临'  :'S',
    '观'  :'T',
    '噬咳':'U',
    '贲'  :'V',
    '剥'  :'W',
    '复'  :'X',
    '无妄':'Y',
    '大畜':'Z',
    '颐'  :'a',
    '大过':'b',
    '坎'  :'c',
    '离'  :'d',
    '咸'  :'e',
    '恒'  :'f',
    '遁'  :'g',
    '大壮':'h',
    '晋'  :'i',
    '明夷':'j',
    '家人':'k',
    '睽'  :'l',
    '蹇'  :'m',
    '解'  :'n',
    '损'  :'o',
    '益'  :'p',
    '夬'  :'q',
    '姤'  :'r',
    '萃'  :'s',
    '升'  :'t',
    '困'  :'u',
    '井'  :'v',
    '革'  :'w',
    '鼎'  :'x',
    '震'  :'y',
    '根'  :'z',
    '渐'  :'0',
    '归妹':'1',
    '丰'  :'2',
    '旅'  :'3',
    '巽'  :'4',
    '兑'  :'5',
    '涣'  :'6',
    '节'  :'7',
    '中孚':'8',
    '小过':'9',
    '既济':'+',
    '未济':'/',
}

# 编译失败时可尝试此处改为绝对路径
favicon = r"./img/favicon.ico"
img_title = r"./img/img_title.png"
footer = r"./img/footer.png"

window = tk.Tk()
window.title('道法自然')
window.geometry('640x640')
window.iconbitmap(favicon)

def showImg(linker, num, where):
    load = Image.open(linker)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(where, image=render)
    img.image = render
    if num == 1:
        img.pack(side='top')
    elif num == 2:
        img.pack(side='bottom')
    elif num == 3:
        img.pack(side='left')
    elif num == 4:
        img.pack(side='right')

showImg(img_title, 1, window) 

def coding_sim():
    output_text.delete('0.0', 'end')
    source = input_text.get("0.0", "end")
    pattern = re.compile('.{1,1}')
    source = ('\x00'.join(pattern.findall(source)))
    sou_base = str(base64.b64encode(source.encode('utf-8'))
                   )[2:-1].replace('=', 'A')
    for (k, v) in simplified_table.items():
        sou_base = sou_base.replace(v, k)
    output_text.insert('insert', sou_base)

def decoding_sim():
    output_text.delete('0.0', 'end')
    cipher = input_text.get("0.0", "end")
    for (k, v) in simplified_table.items():
        cipher = cipher.replace(k, v)
    source = str(base64.b64decode(cipher))[2:-1].replace('\\x00', '')
    # print(source)
    output_text.insert('insert', source)

def coding_tra():
    output_text.delete('0.0', 'end')
    source = input_text.get("0.0", "end")
    pattern = re.compile('.{1,1}')
    source = ('\x00'.join(pattern.findall(source)))
    sou_base = str(base64.b64encode(source.encode('utf-8'))
                   )[2:-1].replace('=', 'A')
    for (k, v) in traditional_table.items():
        sou_base = sou_base.replace(v, k)
    output_text.insert('insert', sou_base)

def decoding_tra():
    output_text.delete('0.0', 'end')
    cipher = input_text.get("0.0", "end")
    for (k, v) in traditional_table.items():
        cipher = cipher.replace(k, v)
    source = str(base64.b64decode(cipher))[2:-1].replace('\\x00', '')
    # print(source)
    output_text.insert('insert', source)

def delete_t():
    input_text.delete('0.0', 'end')
    output_text.delete('0.0', 'end')

input_text = tk.Text(window, height=5)
input_text.pack(pady=10)

fm1 = tk.Frame(window)
b1 = tk.Button(fm1, text='今法悟道', width=10, height=2, command=coding_sim).pack(
    side='left', padx=10, fill='both')
b2 = tk.Button(fm1, text='今法解惑', width=10, height=2, command=decoding_sim).pack(
    side='left', padx=10, fill='both')
b1 = tk.Button(fm1, text='古典悟道', width=10, height=2, command=coding_tra).pack(
    side='left', padx=10, fill='both')
b2 = tk.Button(fm1, text='古典解惑', width=10, height=2, command=decoding_tra).pack(
    side='left', padx=10, fill='both')
b5 = tk.Button(fm1, text='无上清净', width=10, height=2,
               command=delete_t).pack(side='left', fill='both')
fm1.pack(pady=10)

output_text = tk.Text(window, height=5)
output_text.pack()

fm2 = tk.Frame(width=500)
l2 = tk.Label(window, text='P.s.:\n1)暂时未开发右键菜单，请使用Ctrl+C,Ctrl+V进行复制粘贴操作。\n2)古典奥术解不开今法之道，今法之密不贯通古典疑惑。',
              font=('Microsoft Yahei', 8), width=500, height=3).pack()
showImg(footer, 2, fm2)
fm2.pack(side='bottom')


window.mainloop()
 