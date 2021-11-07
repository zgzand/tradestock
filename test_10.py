import codecs
import os
import shutil
from time import sleep

from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

from autotrade.credit_trade import AutoTrade


def opn_fg():
    src = r'C:\海王星金融终端-中国银河证券\T0002\hq_cache\block_fg.dat'
    dst = r'D:\PycharmProjects\autotrade\db\block_fg.dat'
    dst_1 = r'D:\PycharmProjects\autotrade\db\block_fg.txt'

    shutil.copy(src, dst)  # 复制文件
    os.remove(dst_1)  # 删除文件
    os.rename(dst, dst_1)  # 重命名

    # gbk -> utf-8
    # f = codecs.open(dst_1, 'r', 'gbk')
    # ff = f.read()
    # os.remove(dst_1)  # 删除文件
    # d = codecs.open(dst_1, 'w', 'utf-8')
    # d.write(ff)

    app_1 = Application(backend="uia").start('notepad.exe')
    # dlg = app.window(title=u"无标题 - 记事本", best_match=u"记事本")
    sleep(0.01)

    app_1[' 无标题 - 记事本 '].menu_select("文件(F)->打开(O)")
    app = Desktop()
    dlg = app.window(title=u"打开", best_match=u"打开")
    # dlg.Edit.type_keys('D:\PycharmProjects\\autotrade\db\\block_fg.txt') # 键盘效果输入
    dlg.Edit.set_text(dst_1)
    sleep(0.01)
    dlg.打开.click()
    app_1['block_fg.txt - 记事本 '].menu_select("文件(F)->另存为(A)")
    app = Desktop()
    dlg = app.window(title=u"另存为", best_match=u"另存为")
    sleep(0.05)
    dlg.ComboBox3.select('UTF-8')
    # dlg.ComboBox3.dump_tree()  # 查看窗口控件
    # dlg.print_control_identifiers()
    dlg.button1.click()
    app = Desktop()
    dlg_1 = app.window(title=u"确认另存为", best_match=u"确认另存为")
    sleep(0.01)
    dlg_1.是.click()
    sleep(0.05)
    # app_1.kill()  # 关闭窗口
    app_1['block_fg.txt - 记事本 '].关闭.click()  # 效果等同app_1.kill()


def flash_trading(code, amount='0', ratio=0, sty='211'):
    """
       21 闪电买入  211 闪电融资买入  221 普通买入
       23 闪电卖出  299 闪电卖券还款  223 普通卖出
       22 撤单查询

       """

    src = r'C:\海王星金融终端-中国银河证券\TdxW.exe'
    app = Application(backend="uia").connect(path=src)
    dlg = app.window(best_match=u"Dialog")
    dlg.set_focus()
    # dlg.print_control_identifiers()
    # dlg.dump_tree()  # 查看窗口控件

    send_keys(code + '{ENTER}', pause=0.1)  # 个股票窗口
    # sleep(0.1)
    send_keys(sty + '{ENTER}', pause=0.2)  # 闪电买入

    app = Desktop()
    dlg = app.window(best_match='Dialog')
    # dlg.ComboBox2.select('五档即成剩撤')
    # if code.startswith('6'):
    #     dlg.ComboBox2.select('五档即成剩撤')
    # else:
    #     dlg.ComboBox2.select('对方最优价格')
    # sleep(0.1)

    # RadioButton=1/2  RadioButton2=1/3  RadioButton3=1/4  RadioButton4=1/5
    if ratio == 1:
        # dlg.全部.click()
        dlg.Button2.click()
    elif ratio == 2:
        dlg.RadioButton.click()
    elif ratio == 3:
        dlg.RadioButton2.click()
    elif ratio == 4:
        dlg.RadioButton3.click()
    elif ratio == 5:
        dlg.RadioButton4.click()
    else:
        dlg.Edit2.set_text(amount)
        sleep(0.01)

    dlg.Button3.click()
    # sleep(0.1)

    app = Desktop()
    dlg = app.window(best_match=u"Dialog")
    dlg.Button.click()


# flash_trading('300297', '2500', 0, '211')
flash_trading('600733', '1000', 0, '211')
# trade = AutoTrade()
# trade.get_data_frozen()
