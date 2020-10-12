# 元素定位与元素操作说明
#### 参考文档
https://www.cnblogs.com/yoyoketang/p/6123890.html

#### 详细流程
1.浏览器的操作
2.八大元素的定位
```
id、name、class、tag、link、patail_link、xpath、css.、xpath
```
3.多窗口、句柄(handle)
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
4. xpath元素定位 文件ElementXpath.py

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

