import time
import pyautogui
import cv2
from datetime import datetime

# 准点进入预约页面

def click_at_specific_time(target_time, button_image_path, screenshot_path1):
    """
    在特定时间点击按钮。

    参数:
    target_time (str): 目标时间，格式为 'HH:MM'。
    button_image_path (str): 按钮图像的路径。
    screenshot_path1 (str): 屏幕截图的路径。
    """
    while True:
        # 获取当前时间
        current_time = datetime.now().strftime('%H:%M')
        # 检查当前时间是否为指定时间
        if current_time == target_time:
            # 定位并点击按钮
            button_location = pyautogui.locateOnScreen(button_image_path, screenshot_path1, confidence=0.9)
            if button_location:
                pyautogui.click(button_location)
                print(f"在 {target_time} 成功点击了按钮。")
                break  # 点击后退出循环
            else:
                print("未能找到按钮位置。")
        # 等待一段时间再次检查时间
        time.sleep(1)  # 每分钟检查一次

# 点击立即预约
def click_booking_on_screenshot(booking_screenshot_path, booking_target_screenshot_path):
    """
    在屏幕截图中找到并点击 "booking" 图像。

    参数:
    booking_screenshot_path (str): 包含 "booking" 图像的屏幕截图路径。
    booking_target_screenshot_path (str): 用于定位 "booking" 图像的目标屏幕截图路径。
    """
    # 确保目标屏幕截图已经加载到内存中
    booking_screenshot = pyautogui.screenshot()

    # 检查是否成功获取当前屏幕截图
    if booking_screenshot is None:
        print("无法获取当前屏幕截图。")
        return

    # 定位 "booking" 图像在当前屏幕截图中的位置
    booking_location = pyautogui.locateOnScreen(booking_target_screenshot_path, confidence=0.5)

    # 如果找到了 "booking" 图像的位置
    if booking_location is not None:
        # 计算并移动鼠标到该位置
        pyautogui.click(booking_location)
        print("已成功点击 'booking' 图像。")
    else:
        print("未能在屏幕上找到 'booking' 图像。")

# 点击预约
def click_image_on_screenshot(image_screenshot_path, target_image_path):
    """
    在屏幕截图中找到并点击目标图像。

    参数:
    image_screenshot_path (str): 包含目标图像的屏幕截图路径。
    target_image_path (str): 要定位的目标图像的路径。
    """
    # 确保目标屏幕截图已经加载到内存中
    screenshot = pyautogui.screenshot()

    # 检查是否成功获取当前屏幕截图
    if screenshot is None:
        print("无法获取当前屏幕截图。")
        return

    # 定位目标图像在当前屏幕截图中的位置
    target_location = pyautogui.locateOnScreen(target_image_path, confidence=0.7)

    # 如果找到了目标图像的位置
    if target_location is not None:
        # 计算并移动鼠标到该位置
        pyautogui.click(target_location)
        print(f"已成功点击 '{target_image_path}' 图像。")
    else:
        print(f"未能在屏幕上找到 '{target_image_path}' 图像。")
# 滚动鼠标滚轮的函数
def scroll_mouse_wheel(scroll_amount):
    """
    滚动鼠标滚轮。

    参数:
    scroll_amount (int): 滚动的单位数，默认为200。
    """
    pyautogui.scroll(scroll_amount)

# 选择预约时间
def click_appointment_time(appointment_time_interface_path, pm_time_slot_path, wechat_screenshot_path):
    """
    定位并点击预约时间中的“14:30-17:30”按钮。

    参数:
    appointment_time_interface_path (str): 预约时间界面模板图片的路径。
    pm_time_slot_path (str): “14:30-17:30”时间按钮模板图片的路径。
    wechat_screenshot_path (str): 微信小程序界面截图的路径。
    """

    # 函数用于在屏幕上查找模板图像的位置
    def find_element_on_screen(template_path, screenshot):
        # 将模板图像转换为灰度图
        gray_template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        # 使用pyautogui的locateOnScreen方法查找模板在截图中的位置
        return pyautogui.locateOnScreen(template_path, screenshot, confidence=0.5)

    # 加载微信小程序界面截图
    wechat_screenshot = cv2.imread(wechat_screenshot_path, cv2.IMREAD_GRAYSCALE)

    # 首先定位预约时间界面
    appointment_time_interface_location = find_element_on_screen(appointment_time_interface_path, wechat_screenshot)
    if appointment_time_interface_location:
        # 如果找到预约时间界面，则点击它
        pyautogui.click(appointment_time_interface_location)
        time.sleep(0.01)  # 等待界面响应

        # 然后定位并点击“14:30-17:30”时间按钮
        pm_time_slot_location = find_element_on_screen(pm_time_slot_path, wechat_screenshot)
        if pm_time_slot_location:
            pyautogui.click(pm_time_slot_location)
            print("已成功点击“14:30-17:30”时间按钮。")
        else:
            print("未能找到“14:30-17:30”时间按钮位置。")
    else:
        print("未能找到预约时间界面。")

# 填充个人信息
def automate_wechat_form(wechat_screenshot_path, name_input_template_path, phone_input_template_path, gender_male_template_path, gender_female_template_path, your_name, your_phone, gender):
    # 缩放因子，根据需要调整
    scale_factor = 0.8

    # 函数用于在屏幕上查找模板图像的位置
    def find_element_on_screen(template_path, screenshot):
        # 将模板图像转换为灰度图
        gray_template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        # 缩放到与屏幕截图相同的大小
        scaled_template = cv2.resize(gray_template, (int(gray_template.shape[1] * scale_factor), int(gray_template.shape[0] * scale_factor)))
        # 使用pyautogui的locateOnScreen方法查找模板在截图中的位置
        return pyautogui.locateOnScreen(template_path, screenshot, confidence=0.9)

    # 加载微信小程序界面截图
    wechat_screenshot = cv2.imread(wechat_screenshot_path, cv2.IMREAD_GRAYSCALE)

    # 定位姓名输入框并填写
    name_input_location = find_element_on_screen(name_input_template_path, wechat_screenshot)
    if name_input_location:
        pyautogui.click(name_input_location)
        #time.sleep(0.005)
        pyautogui.typewrite(your_name)
        pyautogui.press('1')


    else:
        print("未能找到姓名输入框位置")

    # 定位手机号输入框并填写
    phone_input_location = find_element_on_screen(phone_input_template_path, wechat_screenshot)
    if phone_input_location:
        pyautogui.click(phone_input_location)
        #time.sleep(0.005)
        pyautogui.typewrite(your_phone)
    else:
        print("未能找到手机号输入框位置")

    # 根据性别选择相应的模板进行匹配并点击
    gender_template_path = gender_male_template_path if gender == "Male" else gender_female_template_path
    gender_template_location = find_element_on_screen(gender_template_path, wechat_screenshot)
    if gender_template_location:
        pyautogui.click(gender_template_location)
    else:
        print("未能找到性别选项位置")

    # 模拟按下Enter键提交
    pyautogui.press('enter')

# 点击提交
def click_submit_button(submit_button_template_path, wechat_screenshot_path):
    """
    定位并点击“保存并提交”按钮。

    参数:
    submit_button_template_path (str): 提交按钮模板图片的路径。
    wechat_screenshot_path (str): 微信小程序界面截图的路径。
    """
    # 函数用于在屏幕上查找模板图像的位置
    def find_element_on_screen(template_path, screenshot):
        # 将模板图像转换为灰度图
        gray_template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        # 使用pyautogui的locateOnScreen方法查找模板在截图中的位置
        return pyautogui.locateOnScreen(template_path, screenshot, confidence=0.9)

    # 加载微信小程序界面截图
    wechat_screenshot = cv2.imread(wechat_screenshot_path, cv2.IMREAD_GRAYSCALE)

    # 定位“保存并提交”按钮
    submit_button_location = find_element_on_screen(submit_button_template_path, wechat_screenshot)
    if submit_button_location:
        # 移动鼠标到找到的位置并点击
        pyautogui.click(submit_button_location)
        print("已点击“保存并提交”按钮。")
    else:
        print("未能找到“保存并提交”按钮位置。")



# 使用路径

#初始界面等待进入
button_image_path = "not_login2.png"  # 按钮图像的路径
screenshot_path = "wechat_screenshot4.png"


#立即预约
booking_target_screenshot_path = "booking1.png"  # 包含 "booking" 图像的屏幕截图路径
booking_screenshot_path = "wechat_screenshot_booking2.png"  # "booking" 图像的目标屏幕截图路径

#预约
target_image_path = "strat.png"  # 要定位的目标图像的路径
image_screenshot_path = "strat_screenshot.png"  # 包含目标图像的屏幕截图路径
image_prebooking_path = "prebooking1.png"
#个人信息填充
wechat_screenshot_path = "wechat_screenshot5.png"
name_input_template_path = "name_input_template1.png"
phone_input_template_path = "phone_input_template1.png"
gender_male_template_path = "gender_male_template1.png"
gender_female_template_path = "gender_female_template.png"

#点击提交按钮
submit_button_template_path = "submit.png"

#选择预约时间
time_input_interface_path = "time_input2.png"  # 预约时间界面模板图片的路径
time_pm_input_path = "time_pm_input.png"  # “14:30-17:30”时间按钮模板图片的

#填入个人信息
your_name = "XXX"
your_phone = "12345678901"
gender = "Male"

target_time = "20:00"  # 目标时间，格式为 'HH:MM'
# 调用函数填写表单
click_at_specific_time(target_time, button_image_path, screenshot_path)

start_time = time.perf_counter()#运行时间

time.sleep(1.5)
click_booking_on_screenshot(booking_screenshot_path, booking_target_screenshot_path)
time.sleep(1.5)

click_image_on_screenshot(image_prebooking_path, target_image_path)
time.sleep(0.5)
#click_image_on_screenshot(image_screenshot_path, target_image_path)
#time.sleep(0.7)
click_appointment_time(time_input_interface_path, time_pm_input_path, wechat_screenshot_path)
scroll_mouse_wheel(int(-600))
automate_wechat_form(wechat_screenshot_path, name_input_template_path, phone_input_template_path, gender_male_template_path, gender_female_template_path, your_name, your_phone, gender)
click_submit_button(submit_button_template_path, wechat_screenshot_path)
end_time = time.perf_counter()#运行时间
elapsed_time = end_time - start_time#运行时间
print(f"程序运行时间：{elapsed_time} 秒")#运行时间