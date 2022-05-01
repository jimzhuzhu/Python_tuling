# 常用模块
 - calendar
 - time
 - datetime
 - os
 - shutil
 - zip
 - math
 - string
 - 上述所有模块使用理论上都应该先导入，string是特例
 - calendar,time,datetime的区别参考中文意思
 
# calendar
 - 跟日历相关的模块
 - 使用前需要先导入
 
        import calendar
 - claendar: 获取一年的日历字符串
 -  参数
    - w = 每个日期之间的间隔字符串
    - l = 每周所占用的行数
    - c = 每个月之间的间隔字符数
 - 详细案例 p01.py
 - calendar.isleap(x):
    - 判断某一年是否闰年
    - 返回一个布尔值
    - 案例 p02.py
 - calendar.leapdays(y1, y2):
    - 获取指定年份之间闰年个数
    
## month() 获取某个月的日历字符串
 - 格式：calendar.month(year, month)
 - 回值： 某年某月的日历字符串
 - 案例 p03.py
## monthrange() 获取一个月的周几开始即天数
 - 格式： calendar.monthrange(year, month)
 - 回值： 返回两个值，元组 tuple(周几开始，总共天数)
 - 参数：
    - w, 代表这个月周几开始
    - t, 代表这个月总共多少天
 - 注意： 周默认 0-6 表示周一到周日
 - 案例 p04.py
 
## monthcalendar()
 - 返回一个月每天的矩阵列表
 - 格式： calendar.monthcalendar(year, month)
 - 回值： 矩阵中没有天数用0表示
 - 案例 p04.py
## prcal: print calendar 
 - 直接打印日历
        
        calendar.prcal(2020)
## prmonth() 直接打印整个月的日历
 - 格式： calendar.prmonth(year, month)
 - 返回值：无
        
        calendar.prmonth(2020, 5)
## weekday() 获取周几
 - 格式： calendar.weekday(year, month, day)
 - 返回值： 周几对应的数字
        
        calendar.weekday(2020, 5, 21)
     
# time 模块
## 时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能够支持到2038年

## UTC时间
    - UTC又称为世界协调时间，以英国的格林尼治天文所在地区的时间作为
    参考时间，也叫做世界标准时间
    - 中国时间是 UTC+8 东八区
 
## 夏令时
    - 夏令时就是在夏天的时候将时间调快一小时，本意是督促大家早睡早起，每天变成25小时
    实质还是24小时
    
## 时间元组
    - 一个包含时间内容的普通元组
    
        索引  内容    属性       值
        0     年     tm_year  （例如，1993）
        1     月     tm_mon    range [1, 12]
        2     日     tm_mday   range [1, 31]
        3     时     tm_hour   range [0, 23]
        4     分     tm_min    range [0, 59]
        5     秒     tm_sec    range [0, 61] 60代表闰秒 61保留值
        6     周几    tm_wday   range [0, 6] ，周一为 0
        7     第几天  tm_yday   range [1, 366]
        8     夏令时  tm_isdst0, 1 或 -1（表示夏令时）
        N/A    tm_zone时区名称的缩写
        N/A    tm_gmtoff以秒为单位的UTC以东偏离
 - 需要单独导入 import time
 - 案例 p05.py    
 - 时间模块的属性
    - timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔
    - 东八区的间隔是-2880
    - altzone: 获取当时时区与UTC时间相差的秒数，在有夏令时的情况下
    - daylight: 测当前是否是夏令时时间状态，0表示是
        print(time.timezone)
        结果是-28800
 - 得到时间戳
    time.time()
 - localtime, 得到当前的时间结构获得目前的具体时间
 - 可以通过点号操作符得到相应的属性元素的内容
    t = time.localtime()
 - asctime() 返回元组的正常字符串化之后的时间格式
    - 格式：time.asctime() 时间元组
    - 返回值：字符串 Tue Jun 6 11：11：00 2020
 - ctime 获取字符串化的当前时间
 - mktime() 使用时间元组获取对应的时间戳
    - 格式： time.mktime (时间元组)
    - 返回值： 浮点数时间戳
 - clock: 获取cpu时间， 3.0-3.3版本直接使用，3.6调用这个有问题
 - sleep: 使程序进入睡眠，n秒后继续
    
        for i in range(10):
            print(i)
            time.sleep(1)
  
## strftime: 将时间元组转化为自定义的字符串格式
     ‘’‘
     格式  含义  备注
     %a  本地（locale）简化星期名称
     %A  本地完整星期名称
     %b  本地简化月份名称
     %B  本地完整月份名称
     %c  本地相应的日期和时间表示
     %d  一个月中的第几天（01 - 31）
     %H  一天中的第几个小时（24 小时制，00 - 23）
     %I  一天中的第几个小时（12 小时制，01 - 12）
     %j  一年中的第几天（001 - 366）
     %m  月份（01 - 12）
     %M  分钟数（00 - 59）
     %p  本地 am 或者 pm 的相应符 
     %S  秒（01 - 61）
     %U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周
     %w  一个星期中的第几天（0 - 6，0 是星期天）
     %W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始 
     %x  本地相应日期 
     %X  本地相应时间 
     %y  去掉世纪的年份（00 - 99）
     %Y  完整的年份 
     %z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）
     %%  %号本身
     ’‘’
     
 - 把时间表示成， 2020 5，24 22：30
 - 案例 p06.py
    - 如果格式中使用中文，尽量使用format进行格式化
    
# datetime 模块
 - datetime 提供日期和时间的运算和表示
 - 程序案例 p07.py
 - 常见属性
    - datetime.date:一个理想和的日期，提供year, month, day属性
    - datetime.time:提供一个理想和的时间，居于hour, minute, second, microsecond等内容
    - datetime.datetime: 提供日期跟时间的组合
    - datetime.timedelta: 提供一个时间差，时间长度
 - datetime.datetime
        
        from datetime import 
    - 常用类方法：
        - today
        - mow
        - utcnow
        - fromtimestamp: 从时间戳中返回本地时间
 - timeit-时间测量工具
 - 测量程序运行时间间隔实验
 - 案例 po8.py
 - timeit 可以执行一个函数，来测量一个函数的执行时间
 - 案例 p09.py
 

# os - 操作系统相关
 - 跟操作系统相关，主要是文件操作
 - 于系统相关的操作，主要包含在三个模块里
    - os, 操作系统目录相关
    - os.path ， 系统路径相关操作
    - shutil, 高级文件操作，目录树的操作，文件赋值，删除和移动
 - 路径：
    - 绝对路径： 总是从根目录上开始
    - 相对路径： 基本以当前环境为开始的一个相对地方
    
# os模块
 - 常见操作系统
    - dos, windows,unix,linux,ios,Andriod
 - 先导入 import os
 - getcwd() 获取当前的工作目录
    - 格式： os.getcwd()
    - 返回值： 当前工作目录的字符串
    - 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
 - chdir() 改变当前的工作目录
    - change directory
    - 格式： os.chdir(路径)
    - 返回值： 无
 - listdir() 获取一个目录中所有子目录和文件的名称
    - 格式: os.listdir(路径)
    - 返回值： 所有子目录和文件名称的列表
 - makedirs() 递归创建文件夹
    - 格式： os.makedirs(递归路径)
    - 返回值：无
    - 递归路径：多个文件夹层层包含的路径就是递归路径，例如 a/b/c
 -system() 运行系统shell命令
    - 一般推荐使用subprocess代替
    - 格式： os.system(系统命令)
    - 返回值：打开一个shell或者终端界面
    - 在当前目录下创建一个zhuzhu.liuliu 的文件夹
 - getenv() 获取指定的系统环境变量值
 - 相应还有putenv
    - 格式： is.getenv('环境变量名’)
    - 返回值：指定环境变量名对应值
 - exit() 推出当前程序
    - 格式： exit()
    - 返回值：无
    
# 值部分
 - os.curdir: curretn dir, 当前目录
 - os.pardir: parent dir, 父亲目录
 - os.sep: 当前系统的路径分隔符
    - windows: "\"
    - linux: "/"
 - os.linesep: 当前系统的换行符号
    - window: "\r\n"
    - unix,linux,macos: "\n"
 - os.name: 当前系统名称 
    - window: nt
    - mac,unix,lunix: posix
 - 在路径相关的操作中，尽量不要手动拼写，不具有移植性
 
# os.path 模块，跟路径相关的模块
 - abspath() 将路径转换为绝对路径
 - abselute 绝对
    - 格式： os.path.abspath("路径")
    - 返回值： 路径的绝对路径形式
 - 在linux中
    - . 点好，代表当前目录
    - .. 双点，代表父目录
 - basename() 获取路径中的文件名部分
    - 格式： os.path.basename(路径)
    - 返回值：文件名字符串
 - join() 将多个路径拼合成一个路径
    - 格式： os.path.join(路径1，路径2，路径3...)
    - 返回值：组合之后的新路径字符串
 - split() 将路径切割为文件夹部分和当前文件夹部分
    - 格式： os.path.split(路径)
    - 返回值：路径和文件名组成的元组
 - isdir() 检测是否是目录
    - 格式： os.path.isdir(路径)
    - 返回值：布尔值
 - exists() 检测文件或者目录是否存在
    - 格式： os.path.exists(路径)
    - 返回值：布尔值
  
# shutil 模块
 - copy() 复制文件
    - 格式： shutil.copy(来源路径，目标路径)
    - 返回值：返回目标路径
    - 拷贝的同时，可以给文件重命名
 - copy2() 复制文件，保留元数据(文件信息)
    - 格式：shutil.copy2(来源路径，目标路径)
    - 返回值：返回目标路径
 - copyfile() 将一个文件中的内容复制到另一个文件当中
    - 格式：shutil.copyfile('源路劲‘，'目标路径')
    - 返回值：无
 - move() 移动文件/文件夹
    - 格式：shutil.move(来源路径，目标路径)
    - 返回值：目标路径！
 
# 归档和压缩
 - 归档： 把多个文件或者文件夹合并到一个文件当中
 - 压缩： 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中
 - make_archiv() 归档操作
    - 格式：shutil.make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
    - 返回值：归档之后的地址
 - unpack_archive()解包操作
    - 格式：shutil.unpack_archive('归档文件地址','解包之后的地址')
    - 返回值：解包之后的地址
    
# zip - 压缩包
 - 模块名称叫 zipfile
 - zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
    - 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或类文件对象
 - ZipFile.getinfo(name):
    - 获取zip文档内指定文件的信息。返回一个zipfile.Zipfile对象，包括文件的详细内容
 - ZipFile.namelist()
    - 获取zip文档内所有文件的名称列表
 - ZipFile.extractall([path[, members[, pwd]]])
    - 解压zip文档中所有文件到当前目录。参数members的默认值为zip文档内所有的文件名称列表
    
# random 随机数
 - import random
 - 案例p11.py
 - 所有的随机模块都是伪随机
 - rnadom() 获取0-1之间的随机小数
    - 格式： random.random()
    - 返回值： 随机0-1之间的小数
 - choice() 随机返回序列的某个值
    - 格式：random.choice(序列)
    - 返回值：序列中的某个值
 - shuffle() 随机打乱列表
    - 格式： random.shuffle(列表)
    - 返回值：打乱顺序之后的列表
 - randint(a,b) 返回a到b的随机整数，包含a，b
 