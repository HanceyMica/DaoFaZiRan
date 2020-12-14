# -*- coding: utf-8 -*-
import tkinter as tk
import base64
import re,os
from PIL import Image, ImageTk

class lib(linker,num,where):
    def lib():
        pass
    
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

    def showImg(self.linker, self.num, self.where):
        linker = self.linker
        num = self.num
        where = self.where

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