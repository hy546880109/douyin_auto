#第一次安装软件运行可能有弹窗，请在次运行即可。
#已经适配不同版本的安卓手机和分辨率
from appium import webdriver
import time
import os

vs = os.system('adb shell getprop ro.build.version.release')    #获取手机系统版本
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'douyinjisu.apk')    #安装包路径

result = os.popen("adb shell pm list package")  # 查看手机中已安装的软件包名
if "com.ss.android.ugc.aweme.lite" in result.read():  # 判断此软件包名是否在手机中
    print("应用已安装")
    print('开始执行脚本>>>')
else:
    print("应用未安装,开始进行安装>>>")
    os.system(f'adb install {file_path}')
time.sleep(1)

caps = {}
caps["appPackage"] = "com.ss.android.ugc.aweme.lite"    #包名
caps["appActivity"] = "com.ss.android.ugc.aweme.splash.SplashActivity"  #启动名
# caps['app'] = file_path
caps["platformName"] = "Android"
# 模拟器
caps["deviceName"] = "Android Emulato"  #设备名称
caps["platformVersion"] = vs #安卓版本
# 真机
# caps["deviceName"] = "b68548ed"
# caps["platformVersion"] = "10"
caps["noReset"] = "True"    #不初始化

number = input('输入执行的次数:')
show_time = input('输入视频的观看时间(单位秒):')
count = 0

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
get_h = driver.get_window_size()['height']  # 获取屏幕分辨率
get_w = driver.get_window_size()['width']
# 自适应分辨率
start_h = get_h*0.75
end_h = get_h*0.2
now_w = get_w/2
for s in range(int(number)):
    count += 1
    time.sleep(int(show_time))
    driver.swipe(now_w, start_h, now_w, end_h, 500)  # 自动上滑
    print(f'已执行次数>>>{count}次')

driver.quit()
