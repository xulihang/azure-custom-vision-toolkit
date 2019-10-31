# azure-custom-vision-toolkit


文件说明：

* yolo2azure.py：将yolo的txt格式标注文件转换为azure需要的x坐标、y坐标、宽度、高度格式的txt。
* upload.py：将标注内容上传到azure。

用法：

将用labelme之类标注软件生成的txt放到yolo文件夹中，将图片放到images文件夹中。

运行yolo2azure.py会在out文件夹里生成保存了azure需要的数据格式的txt文件。

运行upload.py进行上传，需要手动设置endpoint和key，并在azure的网站上建好项目并添加一个标签（项目和标签的指定可以修改代码，默认使用存在的第一个项目和标签）。

