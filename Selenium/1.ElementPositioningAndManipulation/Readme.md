# 元素定位与元素操作说明
#### 参考文档
https://www.cnblogs.com/yoyoketang/p/6123890.html

#### 学习路线
1.浏览器的操作 OperateWeb
```
# 页面等待 sleep()
# 页面刷新 driver.refresh()
# 前进和后退 driver.back() driver.forward()
# 修改浏览器窗口大小 driver.set_windows_size(with, height)
# 浏览器截屏 driver.save_screenshot('路径名 + 文件名 + 后缀')
# 退出浏览器进程 driver.quit()
# 关闭浏览器窗口 driver.close()
```

2.八大元素的定位 ElementEight.py
```
id、name、class、tag、link、patail_link、xpath、css.、xpath
```


3.多窗口、句柄(handle) ElementEightPlus.py
```
执行文件ElementEight.py文件 报错 出现2个页面
原因是 浏览器窗口的属性使用句柄来识别 两个页面也就可以理解为有2个句柄 2个handle
自动化脚本比较呆 没办法知道这2个页面到底要操作哪一个 于是他就混乱了...

解决办法：
1.保存需要获取元素页面的句柄  
this_window_handle =  driver.current_window_handle
2.在需要的时候及时进行切换
driver.switch_to.window(mainwindows)

获取当前所有页面的handle：
all_handles = driver.window_handles
如：['CDwindow-2B8ABDE6A5B019FD1A1325D81E1D0C6A', 'CDwindow-44CBD36A855626879AF42079BFB21FBB']
```
4.xpath元素定位 文件 
```
ElementXpath.py
ElementXpath2.py
```
5.css元素定位
```
ElementCSS.py
```
6.自动化登录案例
7.定位一组元素
```
Elements.py
```
8.键盘和鼠标事件 操作元素
```
MouseAndKeyboard.py
Mouse.py
```
9.iframe
```
switch_to_frame.py
```
10.select下拉框
```
select.py
```
11.alert
```
Alert.py
```
12.JS处理滚动条

- 18种元素定位
# 单元素

1.id定位：find_element_by_id(self, id_)
2.name定位：find_element_by_name(self, name)
3.class定位：find_element_by_class_name(self, name)
4.tag定位：find_element_by_tag_name(self, name)
5.link定位：find_element_by_link_text(self, link_text)
6.partial_link定位find_element_by_partial_link_text(self, link_text)
7.xpath定位：find_element_by_xpath(self, xpath)
8.css定位：find_element_by_css_selector(self, css_selector）

# 复数形式
9.id复数定位find_elements_by_id(self, id_)
10.name复数定位find_elements_by_name(self, name)
11.class复数定位find_elements_by_class_name(self, name)
12.tag复数定位find_elements_by_tag_name(self, name)
13.link复数定位find_elements_by_link_text(self, text)
14.partial_link复数定位find_elements_by_partial_link_text(self, link_text)
15.xpath复数定位find_elements_by_xpath(self, xpath)
16.css复数定位find_elements_by_css_selector(self, css_selector

# 基于PO模式的元素定位
17.find_element(self, by='id', value=None)
18.find_elements(self, by='id', value=None)

