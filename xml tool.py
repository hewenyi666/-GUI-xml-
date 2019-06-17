from tkinter import *

import tkinter.filedialog as openfile  # 选择文件的提示框

root = Tk()

with open('./final testcase/result_case.xml', 'w', encoding='utf-8') as f2:
    str4 = '<?xml version="1.0" encoding="utf-8" ?>\n' + '<!-- TODO: xml schema definition -->\n' + '<testcases>\n'
    f2.write(str4)

lable_testcase = Label(root, text='Testcase', font=("楷体, 25"))
lable_testcase.pack(side=TOP)
frame1 = Frame(height=150, width=200)
frame1.pack(side=TOP, expand=YES)
labfra1 = LabelFrame(frame1, text='choose language', padx=10, pady=10)  # choose language的选择框
labfra1.pack(side=LEFT)
langs1 = [('cn', 1), ('tw', 2), ('hk', 3)]
v1 = IntVar()


# v1.set(1)
def get_choose_info():
    # print(v.get())
    print(langs1[v1.get() - 1][0])


for lang, num1 in langs1:
    b = Radiobutton(labfra1, text=lang, variable=v1, value=num1, command=get_choose_info)  # v是控制默认选择的第几个
    b.pack(anchor=W)

# ,padx=10,pady=10
labfra2 = LabelFrame(frame1, text='type')  # type:contextdb的选择框
labfra2.pack(side=LEFT, padx=15, pady=20)
v2 = IntVar()
v2.set(1)


def get_type():
    print('contextdb')


c = Radiobutton(labfra2, text='contextdb', variable=v2, value=1, command=get_type)  # v是控制默认选择的第几个
c.pack(anchor=CENTER)  # anchor,控制按钮上内容的位置。使用N, NE, E, SE, S, SW, W, NW,or CENTER这些值之一。默认值是CENTER

label_input1 = Label(frame1, text='input:')  # input 选择文件获取路径
label_input1.pack(side=LEFT)
char_input = StringVar()
Entry_input = Entry(frame1, textvariable=char_input)
Entry_input.pack(side=LEFT)


def get_filepath():
    fileName = openfile.askopenfilename()
    char_input.set(fileName)
    print(fileName)


Button(frame1, text='选择输入文件路径', command=get_filepath).pack(padx=15, pady=20, side=LEFT)
Button(frame1, text='清空内容', command=lambda: delete_button_content(Entry_input)).pack(padx=5, pady=20, side=LEFT)


def get_shuchupath():
    fileName22 = openfile.askopenfilename()
    tt.set(fileName22)


label_input2 = Label(frame1, text='output:')  # output 选择文件获取路径
label_input2.pack(padx=15, pady=20, side=LEFT)
tt = StringVar()
Entry_output = Entry(frame1, textvariable=tt)  # output的输入框
Entry_output.pack(side=LEFT)
Button(frame1, text='选择输出文件路径', command=get_shuchupath).pack(padx=15, pady=20, side=LEFT)
Button(frame1, text='清空内容', command=lambda: delete_button_content(Entry_output)).pack(padx=5, pady=20, side=LEFT)

label_dict = Label(root, text='Dicts', font=("楷体, 25"))  # dicts的label
label_dict.pack(padx=20, pady=20)

frame2 = Frame(height=150, width=200)
frame2.pack(side=TOP, expand=YES)
label_system = Label(frame2, text='type=system:').pack(side=LEFT, padx=5, pady=10)
e = StringVar()
Entry_system = Entry(frame2, textvariable=e)
Entry_system.pack(side=LEFT)


def get_dict_sys_path():
    dict_sys_path = openfile.askopenfilename()
    e.set(dict_sys_path)
    print(dict_sys_path)


Button(frame2, text='选择system的dict文件', command=get_dict_sys_path).pack(side=LEFT, padx=15, pady=10)


def delete_button_content(which_button):
    # Entry_system.delete(0,END)
    which_button.delete(0, END)


Button(frame2, text='清空内容', command=lambda: delete_button_content(Entry_system)).pack(side=LEFT)


# 使用lambda后,可以使调用函数时候可以传递参数,否则只能将参数写在函数内部

def get_dict_user_path():
    dict_user_path = openfile.askopenfilename()
    e1.set(dict_user_path)
    print(dict_user_path)


frame3 = Frame(height=150, width=200)  # frame3用于存放dict的第2个标签
frame3.pack(side=TOP, expand=YES)
label_user = Label(frame3, text='type=user:').pack(side=LEFT, padx=5, pady=10)
e1 = StringVar()
Entry_user = Entry(frame3, textvariable=e1)
Entry_user.pack(side=LEFT)
Button(frame3, text='选择user的dict文件', command=get_dict_user_path).pack(side=LEFT, padx=15, pady=10)
Button(frame3, text='清空内容', command=lambda: delete_button_content(Entry_user)).pack(side=LEFT)

Label(root, text='Settings', font=("楷体, 25")).pack(padx=20, pady=30)
frame_set1 = Frame(height=300, width=200)
frame_set1.pack()  # 使用frame后,需要使用pack方法,确定frame的位置后,才能显示出来frame上的内容
v3 = IntVar()
v3.set(1)


def get_inputmode():
    print('inputmode')


labfra_set1 = LabelFrame(frame_set1, text='setting type-1')  # choose language的选择框
labfra_set1.pack(side=LEFT, padx=20, pady=10)
ZZ = Radiobutton(labfra_set1, text='inputmode', variable=v3, value=1, command=get_inputmode)  # v是控制默认选择的第几个
ZZ.pack(anchor=W)

label_user1 = Label(frame_set1, text='value:').pack(side=LEFT, padx=5, pady=10)
var1 = StringVar()
Entry_value1 = Entry(frame_set1, textvariable=var1)  # 获取输入框内容,使用entry.get()
Entry_value1.pack(side=LEFT, padx=5, pady=10)
Button(frame_set1, text='清空内容', command=lambda: delete_button_content(Entry_value1)).pack(side=LEFT)

frame_set2 = Frame(height=150, width=200)
frame_set2.pack()  # 使用frame后,需要使用pack方法,确定frame的位置后,才能显示出来frame上的内容
v4 = IntVar()
v4.set(1)


def get_keyboard():
    print('keyboard')


labfra_set2 = LabelFrame(frame_set2, text='setting type-2')  # choose language的选择框
labfra_set2.pack(side=LEFT, padx=20, pady=10)
XX = Radiobutton(labfra_set2, text='keyboard', variable=v4, value=1, command=get_keyboard)  # v是控制默认选择的第几个
XX.pack(anchor=W)

label_user2 = Label(frame_set2, text='value:').pack(side=LEFT, padx=5, pady=10)
var1 = StringVar()
Entry_value2 = Entry(frame_set2, textvariable=var1)  # 获取输入框内容,使用entry.get()
Entry_value2.pack(side=LEFT, padx=5, pady=10)
Button(frame_set2, text='清空内容', command=lambda: delete_button_content(Entry_value2)).pack(side=LEFT)

frame_set3 = Frame(height=150, width=200)
frame_set3.pack()  # 使用frame后,需要使用pack方法,确定frame的位置后,才能显示出来frame上的内容
v5 = IntVar()
v5.set(1)


def get_fuzzy():
    print('fuzzy')


labfra_set3 = LabelFrame(frame_set3, text='setting type-3')  # choose language的选择框
labfra_set3.pack(side=LEFT, padx=20, pady=10)
XX = Radiobutton(labfra_set3, text='fuzzy', variable=v5, value=1, command=get_fuzzy)  # v是控制默认选择的第几个
XX.pack(anchor=W)

label_user2 = Label(frame_set3, text='value:').pack(side=LEFT, padx=5, pady=10)
var3 = StringVar()
Entry_value3 = Entry(frame_set3, textvariable=var3)  # 获取输入框内容,使用entry.get()
Entry_value3.pack(side=LEFT, padx=5, pady=10)
Button(frame_set3, text='清空内容', command=lambda: delete_button_content(Entry_value3)).pack(side=LEFT, padx=10, pady=10)

frame_set4 = Frame(height=150, width=200)
frame_set4.pack()  # 使用frame后,需要使用pack方法,确定frame的位置后,才能显示出来frame上的内容
v6 = IntVar()
v6.set(1)


def get_dict_status():
    print('dict_status')


labfra_set4 = LabelFrame(frame_set4, text='setting type-4')  # choose language的选择框
labfra_set4.pack(side=LEFT, padx=20, pady=10)
CC = Radiobutton(labfra_set4, text='dict_status', variable=v6, value=1, command=get_dict_status)  # v是控制默认选择的第几个
CC.pack(anchor=W)

label_user4 = Label(frame_set4, text='value:').pack(side=LEFT, padx=5, pady=20)
var4 = StringVar()
Entry_value4 = Entry(frame_set4, textvariable=var4)  # 获取输入框内容,使用entry.get()
Entry_value4.pack(side=LEFT, padx=5, pady=10)
Button(frame_set4, text='清空内容', command=lambda: delete_button_content(Entry_value4)).pack()  # side=LEFT


def get_entry_content():
    testcase_lang = langs1[v1.get() - 1][0]
    testcase_type = 'contextdb'

    testcase_input = Entry_input.get()
    testcase_output = Entry_output.get()

    dict_system = Entry_system.get()
    dict_user = Entry_user.get()

    setting_type1 = 'inputmode'
    setting_value1 = Entry_value1.get()

    setting_type2 = 'keyboard'
    setting_value2 = Entry_value2.get()

    setting_type3 = 'fuzzy'
    setting_value3 = Entry_value3.get()

    setting_type4 = 'dict_status'
    setting_value4 = Entry_value4.get()

    #  print(testcase_lang,testcase_type,dict_type1)

    list_value = [testcase_lang, testcase_type, testcase_input, testcase_output, dict_system, dict_user,
                  setting_type1, setting_value1, setting_type2, setting_value2,
                  setting_type3, setting_value3, setting_type4, setting_value4]
    with open('./temporary data/temporary case.xml', 'r+', encoding='utf-8') as f:
        text1 = f.read()
    list_num = []  # 存放000-013 的列表
    for yy in range(14):
        if yy <= 9:
            char1 = "00" + str(yy)
        else:
            char1 = "0" + str(yy)
        list_num.append(char1)

    temp1 = text1.replace(list_num[0], list_value[0]).replace(list_num[1], list_value[1]).replace(list_num[2],
                                                                                                  list_value[
                                                                                                      2]).replace(
        list_num[3], list_value[3]).replace(list_num[4], list_value[4]).replace(list_num[5], list_value[5]).replace(
        list_num[6], list_value[6]).replace(list_num[7], list_value[7]).replace(list_num[8], list_value[8]).replace(
        list_num[9], list_value[9]).replace(list_num[10], list_value[10]).replace(list_num[11], list_value[11]).replace(
        list_num[12], list_value[12]).replace(list_num[13], list_value[13])
    with open('./final testcase/result_case.xml', 'a', encoding='utf-8') as f3:
        f3.write('\n' + temp1)


Button(root, text='开始添加', command=get_entry_content).pack(pady=10)


def add_stop_char():
    # print('hello')
    with open('./final testcase/result_case.xml', 'a', encoding='utf-8') as f3:
        f3.write('\n' + '</testcases>')


Button(root, text='结束添加!!!', command=add_stop_char).pack(pady=15)  # 注意command调用函数时不能加括号,否则会自动调用!


def continue_add():
    with open('./final testcase/result_case.xml', 'r', encoding='utf-8') as f6:
        text6 = f6.read().replace('</testcases>', '')
    with open('./final testcase/result_case.xml', 'w', encoding='utf-8') as f7:
        f7.write(text6)


Button(root, text='继续添加用例', command=continue_add).pack(pady=10)

mainloop()
