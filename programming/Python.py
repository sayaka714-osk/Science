

########################## 一：数据 ##########################
### （一）数据类型(type) ###    # 所有的数据类型都是类
    # 基本
        # 数字型
                # 不可变
            # 布尔型
            bool()  # 非0=True,0=False（空列表，空元组，空字典）;True=1,False=0
            # 整型
            int()   # 八进制（0o，0O开头），十六进制（0x，0X开头），二进制（0b，0B开头）
                    # 字符型会转换成0
            # 浮点型
            float() # 必须要有小数点
                    # 科学记数法：2e+33，2e33，2E33
            # 复数
            complex()  # 例：myComplex = 4.17-6.5j
                .real  # 实数
                .imag  # 虚数，虚数要有后缀j/J
                .conjugate() # 共轭复数
        # 字符型
                # 可变
            str()   # 可以使用单引号、双引号、三引号（允许换行）;myCourse[3],允许使用负值
                string
                # 字符转换
                    .capitalize()  # 首字母大写
                    .title()	# 所有单词首字母大写
                    .lower()	# 大写转小写
                    .upper()	# 小写转大写
                # 字符匹配
                    .isalnum()	# string至少有一个字符且所有字符都是字母或数字时返回True
                    .isalpha()	# string至少有一个字符且所有字符都是字母时返回True
                    .isdigit()  # string只含数字返回True
                    .islower()	# 如果string中至少包含一个区分大小写的字符且这些字符都是小写，则返回True，否则返回False
                    .isupper()	# 如果string中至少包含一个区分大小写的字符且这些字符都是大写，则返回True，否则返回False
                    .isspace()	# string只包含空格时返回True，否则返回False
                    .startswith(obj, beg=0,end=len(string))	# 如果在string中beg和end范围内以obj开始，则返回True，否则返回False
                    .endswith(obj, beg=0,end=len(string))	# 如果在string中beg和end范围内以obj结束，则返回True，否则返回False
                # 字符查找
                    .find(str,beg=0,end=len(string))	    # 在string中beg和end范围内查找str，如果没找到返回-1，如果找到，返回开始的下标
                # 字符统计
                    .count(str,beg=0,end=len(string))  # str在beg和end范围内出现的次数
                # 字符拆合
                    .join(seq)  # 以string为分隔符，将seq中的所有元素合并为一个字符串
                    .split('str',num=string.count(str))	# 以str为分隔符切片string，分隔出num个子串
                    .partition(str) # 从str出现的第一个位置起，把string分成一个三元组(string_pre_str,str,string_post_str)
                # 字符增删
                    .strip(x)	# 去掉string开头和末尾的x
                    .lstrip(x)	# 去掉string开头的x
                    .rstrip(x)  # 去掉string末尾的x
                    .replace(str1,str2,num=string.count(str1))	# 把string中的str1替换成str2，替换次数不超过num次
    # 复合
        # 列表(list)
                # 顺序存储，元素可变
            # 对象方法
            .append(a)	# 末尾插入a
            .extend(a)  # 末尾插入a的所有元素
            .insert(3,'English') # 按位插入
            .pop(4)	    # 按位删除元素（默认删末尾），返回删除值
            .remove()   # 按值删除元素
            .sort()	    # 永久升序排序(降序要加入reverse=True)
            .index()	# 按值查找，返回下标
            .count()	# 统计元素出现次数
            .reverse()  # 元素转置
            .len()    	# 返回列表长度
            .min()	    # 列表中最小的元素
            .max()  	# 列表中最大的元素
            .sum()  	# 各元素之和
            # 函数
            sorted()	# 返回升序排序列表(降序要加入reverse=True)，不改变原别表
            reversed()	# 返回列表元素转置，但不是列表，需要list()
            list()	    # 强制转换为列表
            # 语句
            列表名 = [元素1,元素2]  # 创建列表
            列表名[下标]       # 访问，索引访问
            del 列表名[下标]   # 删除（元素或列表皆可）
            列表名[k1:k2]        # 切片
            # 列表表达式
            y = [math.sin(each) for each in x]
        # 元组
                # 顺序存储，元素不可变（元组中的列表可改）
            # 对象方法
            .index()	# 按值查找
            .count()	# 统计元素出现次数
            # 函数
            tuple()     # 转换为元组
            # 语句
            t=(元素1,元素2) # 创建元组:可无括号;单元素元组需要一个','
            对象[下标]      # 访问，索引访问
            (元素1,元素2)=t # 解压元组
            t[k1:k2]       # 切片
        # 字典
                # 哈希存储，元素可变，键不可变
            # 对象方法
            .get()     # 返回键值，键不存在返回None
            .items()   # 返回键值对列表
            .keys()	   # 返回键列表
            .values()  # 返回值列表
            .pop()     # 返回给定键的对应值，后删除键对
            .clear()   # 清楚所有项（与赋值清除不同）
            .copy()	   # 返回一个具有相同项的新字典
            .update()  # 用一个字典更新另一个字典
            # 函数
            dict()	   # 通过其他映射或者键值对的序列创建字典；通过关键字参数创建字典
                gradelist=[('刘达',89),('王尔',95),('李珊',67),('陈思',75),('张悟',89)]
                grade=dict(gradelist)
            # 语句
            d={键1:值1,元键2:值2}  # 创建字典
            del 字典名[k]            # 删除键为k的项
            字典名[k]               # 访问，键访问
            字典名[k]=v	          # 添加键值对，值v关联到键k;更新键值对
        # 集合(set)
                # 哈希存储，元素可变
            # 对象方法
            .add()     # 将括号内的元素添加至集合
            .pop()	   # 随机删除元素并返回该元素
            .remove()  # 删除指定元素
            .clear()   # 将集合清除为空集
            .copy()	   # 复制集合
            # 函数
            set()	   # 创建空集（{}是空字典）
            # 语句
            s = {元素1,元素2}  # 创建集合
            A | B   # 并集，A或B
            A & B   # 交集，A和B
 
### （二）变量(variable) ###
    '''
    (1)	声明
        ①不需要预先声明变量
        ②globe：声明为全局变量，一般不用
    (2)	命名规则：字母、数字、下划线
        ①字母区分大小写
        ②不能以数字开头
        ③不能用空格
        ④要有描述性，提高代码可读性
        ⑤不可以使用关键字命名：False，None，True，and，as，assert，break，class，continue，def，del，elif，else，except，finally，for，from，global，if，import，in，is，lambda，non，local，not，or，pass，raise，return，try，while，with，yield
    '''


########################## 二：符号 ##########################
    # (一)数理运算符
        # 算数运算符
        **(指数)＞+(正号)＞-(负号)＞*(乘法)＞/(除法)＞//(整除，向下取整)＞%(取余)＞+(加法)＞-(减法)
        # 比较运算符
        <, >, ==, !=, <=, >=  # 允许3<4<5
        # 逻辑运算符
        not ＞ and ＞ or 
    # (二)字符串运算符
        # 连接运算符
        +                # 文本合并，可以操作字符或数字，但类型要相同
        *                # 文本重复，'s'*3=sss
        # 切片运算符
        s[start:stop:step]  # 从start开始到stop范围内按step步长选出字符而形成的字符串;0表示第一个字符，-1表示最后一个字符。可对对象进行操作
        s[start:end] # 左闭右开
        # 成员运算符
        in, not in	     # 判断是否是其成员
        # 格式化运算符
        %        # e.g.
                "-/-"%(10,1) = '10/ 1'
                "%s's birthday:%2d/%02d"%("Ming Li",10,1) = "Ming Li's birthday:10/01"
            %c    # 单个字符
            %s    # 字符串
            %d,%i # 十进制整数
            %f,%F # 浮点型
            %e,%E # 浮点型科学记数法
            %%    # 输出百分号
            m.n   # m为最小总宽度，n为小数点后的位数
            0     # 辅助符号，位数显示不够时填充
        #
        ~    # 按位取反
    # (三)转义字符
        '\n' # 换行符
        '\r' # 回车符
        '\t' # 制表符
        '\'' # 单引号
        '\"' # 双引号
        '\\' # 反斜线
    # (四)通配符
        *    # 一个或多个元素


########################## 三：语句 ##########################
    # 赋值语句
        a,b = 2,3  # a=2,b=3
        a,b = b,a  # a,b值互换
    # 控制语句
        # 选择语句
            if 条件表示式1：  # 单分支，双分支，多分支
                XXX 
            elif 条件表达式2：
                XXX
            else：
                XXX
        # 循环语句
            for 对象元素 in 对象:
                XXX
            while XXX：
                XXX
            # continue　# 当if后的条件表达式满足时，不执行continue后的剩余代码，进入下一次循环
            # break	　#　当if的条件表达式满足时不执行break后的剩余代码，直接终止循环
            # pass      # 空语句，是为了保持程序结构完整性，不做任何事情，一般用做占位语句
    # 注释语句
        #          # 该行内容都是注释
        '''abc'''  # 多行注释，help()的返回


########################## 四：函数 ########################## 
    # 自定义
    def 函数名(参数):
        函数体
	    return 语句  # 返回值，可无 
    def main():       # 主函数
        函数体
        # 形参
            def build(keys,*a,**b,name='Lee')
                # 可变长度的形参放在形参列表的最后，但遇到默认值参数时，必须将默认值的形参和实参均放在参数列表的最后。
                *a  # 形参为任意参数，实质为元组，但不能直接将元组作为参数
                **b # 形参为任意关键字参数，传递键值对，实质为字典，但不能直接将字典作为参数
                name='Lee' # 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参
    # lambda
    lambda x: x.max()-x.min()

    # 常用
    input()	 # 输入；返回结果都是字符串
    print(obj, end='\n')  # 输出字符串
        end # 默认以换行符结尾
    type()	# 返回对象的数据类型
    help()  # 帮助
    len()   # 计算字符串中字符个数/数据结构的元素个数，整型值


    # 数学函数
    abs(a)	　　 #　绝对值
    max(a,b,…)   # 最大值
    min(a,b,…)   # 最小值
    divmod(a,b)　# 返回元组(a//b,a%b)
    pow(a,b,c=1) # 幂函数，返回a的b次方，再对c取余
    round(a,b=0) # 对a四舍五入，保留b位小数（如果保留的小数位数为0，round()遇5时向偶数取整）
    range(start,end,step)  # 产生[start,end)的数序列，间隔为step
    
    # 格式化
    formate()
    f'string'           # e.g.  f'number{C:2f}'
    string.formate()    # e.g.  "number{:2f}G{}".format(C,name)
        {} # 按顺序输出，可有下标
            {:2f}    # 保留小数点后两位
            {:,}     # 千分位隔开
            {:2%}    # 百分比格式
            {:2e}    # 指数
            {:b}     # 二进制转换
            {:10d}   # 右对齐（默认），宽度为10
            {:x<10d} # 左对齐，其余填充x，宽度为10
            {:x^10d} # 居中对齐，两侧填充x，宽度为10
        () # 
            (**dict) # 字典匹配，{}中用键名


    # 字符串
    eval()	# 去掉最外侧的(单双)引号

    # 类型转换
    chr()	 # 将ASCII码值转换为字符；A（65），a（97），0（48）
    ord()	 # 将一个字符转换为ASCII码值
    zip(a,b) # 多个构造列表，其元素为元组

    # 文件处理
    open(file, mode=’r’,encoding=None,errors=None,newline=None, buffering=-1,closefd=True,opener=None)    # 打开文件，返回文件对象
        file # 路径（少用绝对路径，相对路径）
            ..  # 回到上一级目录
        mode # 可同时使用多种模式，‘bw’
            'r' # 只读方式打开文件，文件必须存在，否则打开出错
            'w' # 写入方式打开文件，若文件不存在则创建，若存在则覆盖已有文件
            'a' # 写入模式打开，若文件存在则在末尾追加写入
            'b' # 二进制方式打开文件
            't' # 文本模式打开文件
            '+' # 同时可读写模式。‘r+’与‘w+’都是可读写模式，但‘r+’必须保证文件存在才可以使用
        encoding # 符号编码：'utf-8',
        # 对象方法
        .close()                    #关闭文件对象
        .read(size=-1)              #读取size个字符，默认读取整个文件
        .readline(size=-1, /)       #读取文件中的一行字符串
            /   # 只接受位置参数，不接受关键字参数
        .readlines(hint=-1, /)      #读取所有行，每行保存为一个列表
        .write(buffer, /)           #将内存中的内容写入文件
        .writelines(lines, /)       #向文件写入序列集合（字符串、列表、元组、字典等）
        .tell()                     #返回游标在文件中的位置，数字表示
        .seek(cookie, whence=0, /)  # 移动游标
            whence # 游标起始位置，0表示文件首部，1表示游标当前位置，2表示文件的尾部
            cookie # 游标的相对距离，正数表示向后移动，负数表示向前移动
    with open('test.txt',mode='w') as f:  # 不访问时可自动关闭文件
	    while Ture:
	     	content=f.readline()
	    	if not content:
		    	break
		    print(content, end=None)


########################## 五：类 ########################## 
    # 定义
    class 类名1(object):                  # 类名一般首字母大写
        属性名1=属性值1                    # 类属性
         …
        def __init__(self, 属性名1, …):   # 对象属性，实例属性
            self.属性名A= 属性值A
             …
	    def 自定义方法名1(self, 其它参数):  # 对象方法，实例方法
            语句序列1
         …
	    @classmethod
	    def 自定义方法名A(cls, 其它参数):   # 类方法：每个类方法前都需声明@classmethod
            语句序列
         …

    # 继承
    class 类名2(类名1):
        def __init__(self, 属性名1, … , 属性名a, …):
            类名1.__init__(self.属性名1, …)
            self.属性名a=属性值a
             …
        def 自定义方法名1(self, 其它参数):    # 重写（override），会覆盖原方法
            语句序列2
            …
        def 自定义方法名a(self, 其它参数):
            语句序列
             …
        @classmethod
    	def 自定义方法名α(cls, 其它参数):
            语句序列
             …


########################## 六：文件结构 ##########################
    ### （一）模块（module） ###
        # 命名空间的基本单位，物理上是.py文件
        # 导入模块时必须在同一目录下
        # 以模块名作为空间的隔断，可同时使用重复的变量、函数以及类的名称
    import <模块名> [as <别名>]
    from <模块名> import {变量名|函数名|类名|*}[as <别名>],…  # 后续代码的库名可以省略，但可能会重名
    模块名.变量名|函数名|类名    #引用模块内容
    .__name__   # 属性，判断语句是否可被执行。由本模块调用时，“__name__”的值为“__main__”；由其他模块调用时，“__name__”的值为被调用模块的模块名

    ### （二）包（package） ###
        # 物理上是存储模块的文件夹
    import <包名.模块名> [as <别名>]
    from <包名> import {模块名}[as <别名>]
    from <包名.模块名> import {变量名|函数名|类名}[as <别名>]…
    from <包名> import * # 需要在所用包的文件夹中添加__init__.py文件，并在文件中定义一个__all__=[‘模块名1’,‘模块名2’，…]，这些模块都在包文件夹中


########################## 七：程序调试 ##########################
    # 错误记录
    traceback  # 一条记录，异常对象，指出何处发生错误；没有编写异常处理代码时，遇到异常会停止并显示记录
        Exception # 错误基类
            # 语法错误
                AttributeError # 尝试访问未知的对象属性
                IndexError     # 索引超出序列的范围
                KeyError       # 字典中关键字不存在
                NameError      # 尝试访问一个不存在的变量
                OSError        # 操作系统产生的异常
                    FileNotFoundError # 打开不存在的文件
                SyntaxError    # 语法出错
            # 运行错误
                TypeError          # 不同类型间的无效操作
                ZeroDivisionError  # 除数为0
            # 逻辑错误
    # 内部错误
        添加监视变量
        print()   # 简单语句，打印中间变量
        设置断点+单步跟踪
        工具：调试器
            step # 单步跟踪
            over # 单步跟踪，遇到函数直接执行
            out  # 跳出
    # 外部错误：异常测试
            # 异常：在程序运行过程中发生的异常事件，通常是由外部问题（如硬件错误、输入错误）所导致的
        try：
            检测范围
        except 错误类型 [as reason]：  # except可用多次
            出现异常（Exception）后的处理代码
        else：
            不出现异常的处理代码
        finally：
            无论是否出现异常，均执行的代码


########################## 库(Libiary) ############################

################ 标准库 ################
    # 一组包和内部模块的集合


# 文本处理服务
import re
    # 编译
    re.compile(pattern,flags=0)         # 将正则表达式编译为正则表达式对象（方便面向对象编程，此时匹配参数无需pattern）
        # 常用操作符
        .	# 表示任何单个字符	
        []	# 字符集，单个字符取值范围, [abc]
        [^]	# 非字符集，单个字符排除范围, [^abc]
        *	# 前一个字符0次或无限次扩展, abc*：ab，abc，abcc等
        +	# 前一个字符1次或无限次扩展, abc+：abc，abcc等
        ?	# 前一个字符0次或1次扩展, abc?：ab，abc
        |	# 或，左右表达式任意一个, abc|def：abc，def
        {m}	# 扩展前一个字符m次, ab{2}c：abbc
        {m,n}	# 扩展前一个字符m至n次（含n次）, ab{1,2}c：abc，abcc
        ^	# 匹配字符串开头, ^abc：abc在字符产开头
        $	# 匹配字符串结尾, $abc：abc在字符串结尾
        ()	# 分组标记，内部只能使用|操作符, (abc)：abc；(abc|def)：abc，def
        \d  # 数字，等价于[0-9]	
        \D  # 非数字	
        \s	# 任何不可见字符，包括空格、制表符、换页符等
        \S	# 任何可见字符
        \w	# 单词字符，等价于[A-Za-z0-9_]
        \W	# 非单词字符
        \A	# 仅匹配字符串开头
        \Z	# 仅匹配字符串结尾
        \b	# 匹配一个单词边界，也就是指单词和空格间的位置
        \B	# 匹配非单词边界
        # 最小匹配操作符
        *？	    # 前一个字符0次或无限次扩展，最小匹配
        +？ 	# 前一个字符1次或无限次扩展，最小匹配
        ??   	# 前一个字符0次或1次扩展，最小匹配
        {m,n}?	# 扩展前一个字符m至n次（含n次），最小匹配
        # 例
        '^[A-Za-z]+$'         # 26个字母组成的字符串
        '^-?\d+$'             # 整数形式的字符串
        '^[0-9]*[1-9][0-9]*$' # 正整数形式的字符串.
        '[\u4e00-\u9fa5]'     # 匹配中文字符
        '[1-9]\d{5}'          # 中国境内邮政编码
        '[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)'  # 邮箱地址
    # 查找
    re.search(pattern,string,flags=0)   # 从string中匹配pattern第一个位置，返回match对象
    re.match(pattern,string,flags=0)    # 从string的开始位置起匹配pattern，返回match对象
    re.findall(pattern,string,flags=0)  # 搜索字符串，返回全部匹配的子串列表
    pattern.findall(string[ pos[ endpos]])   # 在字符串中找到匹配的所有子串，并返回一个列表
        string # 待匹配的字符串；
        pos    # 可选，指定字符串的起始位置，默认为 0；
        Endpos # 指定字符串的结束位置，默认为字符串的长度
    re.finditer(pattern,string,flags=0)  # 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象（方便对每个结果单独处理）
    # 删改拆换
    re.split(pattern,string,maxsplit=0,flags=0)  #将字符串按照匹配结果进行分割，返回列表
        pattern  # 正则表达式的字符串或原生字符串表示
        string   # 待匹配字符串
        maxsplit # 最大分割数，剩余部分作为一个元素输出
        flags # 使用时的控制标记
            re.I # re.IGNORECASE，忽略正则表达式的大小写
            re.M # re.MULTILINE，正则表达式中的^操作符能将给定字符串的每行当作匹配开始
            re.S # re.DOTALL，正则表达式的.操作符能匹配所有字符（包括换行符）
    re.sub(pattern,repl,string,flags=0)  #替换字符串中所有匹配的子串，返回替换后的字符串
        pattern # 待替换的字符串
        repl    # 替换匹配字符串的正则表达式字符串
        count=0 # 匹配的最大替换次数
    # match对象
        # 对象属性
        .string	  # 待匹配的文本
        .re	      # 匹配时使用的pattern对象（正则表达式）
        .pos	  # 正则表达式搜索文本的开始位置
        .endpos	  # 正则表达式搜索文本的结束位置
        # 对象方法
        .group(0) # 获得匹配后的字符串，默认贪婪匹配（输出最长匹配）
        .start()  # 匹配字符串在原始字符串的开始位置
        .end()	  # 匹配字符串在原始字符串的结束位置
        .span()	  # 返回(.start(),.end())

# 数据类型

# 数字与数学模块
import math    # 数学函数
import random  # 生成伪随机数

# 数据持久化
import pickle  # Python对象序列化
    pickle.dump(obj, file, protocol=None, *, fix_imports=True)  #将对象以二进制表示并存储到文件中
        obj   # 对象名称
        file  # 文件对象，必须可write
        *     # 其后的参数必须为关键字参数
    pickle.load(file, *, fix_import=True, encoding=‘ASCII’, errors=‘strict’)  #提取由dump函数存入的文件对象
        file  # 文件对象，必须可二进制方式read/readline

# 文件格式
import csv
    # 写入
    csv.writer(fileobj [dialect=’excel’], [optional keyword args])  #写入csv文件
        fileobj  # 需写入的文件对象
    # 读取
    csv.reader(iterable [,dialect=’excel’], [optional args])    #读取csv文件内容并保存到一个迭代器中
        iterable # 读取的文件对象/列表对象
        dialect  # 默认兼容Excel格式

# 互联网数据处理
import json
    # 写入
    json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False **kw)  #将数据存储到文件中
        obj # 具有JSON格式的Python对象
        fp  # 文件对象，可write
    # 读取
    json.load(fp)   #从文件中读取数据，返回JSON格式的Python对象
        fp  # 已打开的文件对象，可read

# 程序框架
import turtle
    # 绘图窗体布局
    turtle.setup(width,height,[starts],[starty])	# 窗体的长宽，左上角相对于屏幕(0,0)的位置（默认在屏幕正中心）
    turtle.done()	# 完成后程序窗体不会自动退出，需要手工
    # 画笔控制
    turtle.penup()  # 抬起画笔
    turtle.pu()	
    turtle.pendown()  # 落下画笔
    turtle.pd()	
    turtle.pensize(width)
    turtle.width(width)	   # 画笔宽度
    turtle.pencolor(color) # 颜色字符串penvolor("purple")，RGB小数值pencolor(0.63,0.13,0.94)，RGB元组值pencolor((0.63,0.13,0.94))
    turtle.colormode(mode) # 红绿蓝三原色，1.0(小数值表示)；255(整数值表示)
    # 运动控制
    turtle.go(10,80)	根据多个goto(绝对)坐标（窗体正中心）可以画线  # 运动距离都以像素单位
    turtle.forward(d)  # 相对坐标，向正前方走直线
    turtle.fd(d)
    turtle.bk(d)	# 相对坐标，向正后方运动
    turtle.circle(r,extent=None) # 相对坐标，以左侧距离半径r画extent角度的弧形
    # 方向控制
    turtle.setheading(angle)  # 绝对角度，x轴正方向0/360，y轴正方向90/-270  # 改变行进方向，但不运动
    turtle.seth(angle)	 
    turtle.left(angle)	    # 相对角度
    turtle.right(angle)	# 相对角度

# 通用操作系统服务
import os

# Python运行时服务
import sys 
    sys.platform	# 获取当前执行环境的平台
    sys.version	    # 查看当前Python的版本号

################ 第三方库 ################
#     pip install 库名  # 安装第三方库
#     pip3 install 库名

# 异步Web服务库
import aiohttp

# 网页开发
import django

# 阻塞式HTTP请求库
import requests
# 类属性
requests.ConnectionError	# 网络连接异常，如DNS查询失败、拒绝连接等
requests.HTTPError      	# HTTP错误异常
requests.URLRequired    	# URL缺失异常
requests.TooManyRedirects	# 超过最大重定向次数，产生重定向异常
requests.ConnectTimeout  	# 连接远程服务器超时异常
requests.Timeout	        # 请求URL超时（整个过程），产生超时异常
# 构造网页请求
requests.request(method,url,**kwargs)	# 构造请求，支撑以下方法
    method  # 请求方式，'GET'，'HEAD'，'POST'，'PUT'，'PATCH'，'DELETE'，'OPTIONS'
        'POST'     # 请求向URL位置的资源后附加新的数据
        'PUT'      # 请求向URL位置存储一个资源，覆盖原URL的资源；如需局部申请，必须所有资源一起提交
        'PATCH'    # 局部修改申请，相对PUT能节省网络带宽
    **kwargs # 13个控制访问的参数
        params          # 字典或字节序列，作为参数增加到url中，根据参数筛选资源
        data            # 字典、字节序列或文件对象，作为Request的内容
        json            # JSON格式的数据，作为request的内容
        headers         # 字典，HTTP定制头
        cookies         # 字典或CookieJar，Request中的cookie
        auth            # 元组，支持HTTP认证功能
        files           # 字典，传输文件
        timeout         # 设置等待响应的时间，秒为单位
        proxies         # 字典，设置访问代理服务器（防止爬虫逆追踪），可增加登录认证
        allow_redirects # True/False，默认True，时间内未收到响应是重发请求
        stream          # True/False，默认True，获取内容立即下载开关
        verity          # True/False，默认True，认证SSL证书开关
        cert            # 本地SSL证书路径
    # 对象属性
    .url	            # 返回当前请求的url
    .status_code        # HTTP请求的返回状态，200成功，404失败
    .text	            # HTTP响应内容的字符串形式，即url对应的页面内容（最好约定范围）
    .json	            # 返回json格式的结果
    .encoding           # 从HTTP header中猜测的响应内容编码方式，如果header无charset，默认IOS-8859-1
    .apparent_encoding	# 从内容中分析出来的响应内容编码方式（备选）
    .context	        # HTTP响应内容的二进制形式
    .history	        # 返回重定向状态码
    # 对象方法
    .raise_for_status()   # 如果不是200，产生异常request,HTTPError
requests.get(url,params=None,**kwargs)          # 获取HTML页面＝HTTP的GET
requests.head(url,**kwargs)                     # 获取HTML网页头信息＝HTTP的 HEAD
requests.post(url,data=None,json=None,**kwargs) # 向HTML网页提交POST请求＝HTTP的POST
requests.put(url,data=None,**kwargs)            # 向HTML网页提交PUT请求＝HTTP的PUT 
requests.patch(url,data=None,**kwargs)          # 向HTML网页提交局部修改申请＝HTTP的PATCH
requests.delete(url,**kwargs)                   # 向HTML网页提交删除请求＝HTTP的DELETE

# 网站级爬虫
import scrapy
     # 功能结构
        engine         # 控制数据流（已有实现）
        spiders        # （用户编写（配置））
        scheduler      # 爬取请求调度管理（已有实现）
        downloader     # 下载网页（已有实现）
        item pipelines # （用户编写（配置））
     # 文件结构
         自定义目录名
            scrapy.cfg    # 部署Scrapy爬虫的配置文件
            自定义目录名   # Scrapy框架的用户自定义代码
                _init_.py      # 初始化脚本
                items.py       # Items代码模版（继承类）
                middlewares.py # Middlewares代码模版（继承类）
                pipelines.py   # Pipelines代码模板（继承类）
                setting.py     # Scrapy爬虫的配置文件
                spiders        # Spiders代码模板目录（继承类）
                    __init__.py     # 初始文件，无需修改
                    __pycache__     # 缓存目录，无需修改
    # 命令
        scrapy startproject <name> [dir]	        # 创建一个新工程
        scrapy genspider [options] <name> <domin>	# 创建一个爬虫；domin域名 
        scrapy settings [options]	                # 获得爬虫配置信息
        scrapy crawl <spider>   	                # 运行一个爬虫
        scrapy list	                                # 列出工程中的所有爬虫
        scrapy shell [url]	                        # 启动URL调试命令行


# 自动化测试，模拟浏览器
import selenium
    # WebDriver实例
    browser = webdriver.Chrome()    # 声明浏览器
    browser = webdriver.Firefox()
    browser = webdriver.Edge()
    browser = webdriver.PhantomJS()
    browser = webdriver.Safari()	
        # 对象属性
        .page_source    	# 网页源代码
        # 对象方法
        .implicitly_wait()	# 设置隐式等待的时间
        .get()	            # 获取网页
        .click()	        # 点击
        .back()         	# 后退
        .forward()	        # 前进
        .send_keys()        # 输入文字
        .clear()	        #　清空文字
        .execute_script()	# 模拟运行JavaScript
        .switch_to.frame()	# 切换到Frame
        .close()	        # 关闭网页
        .find_element(By.method, ‘’)   # 查找单个元素,返回WebElement节点
            method
                ID                # 相当于find_element_by_id()
                NAME              # 相当于find_element_by_name()
                XPATH             # 相当于find_element_by_xpath()
                LINK_TEXT         # 相当于find_element_by_link_text()
                PARTIAL_LINK_TEXT # 相当于find_element_by_partial_link_text()
                TAG_NAME          # 相当于find_element_by_tag_name()
                CLASS_NAME        # 相当于find_element_by_class_name()
                CSS_SELECTOR      # 相当于find_element_by_css_selector()
        .find_elements(By.method, ‘’)   # 查找多个元素,返回WebElement节点
            method
                ID                # 相当于find_elements_by_id()
                NAME              # 相当于find_elements_by_name()
                XPATH             # 相当于find_elements_by_xpath()
                LINK_TEXT         # 相当于find_elements_by_link_text()
                PARTIAL_LINK_TEXT # 相当于find_elements_by_partial_link_text()
                TAG_NAME          # 相当于find_elements_by_tag_name()
                CLASS_NAME        # 相当于find_elements_by_class_name()
                CSS_SELECTOR      # 相当于find_elements_by_css_selector()
        .get_cookies()	        # 获取所有的cookies
        .delete_all_cookies()	# 删除所有的cookies
        # ActionChains实例
        .ActionChains()   	 # 将具体的webdriver浏览器对象换成ActionChains对象，以便进行动作链
            .drag_and_drop() # 拖拽并放置
            .perform()    	 # 执行
    # WebElement实例
        .id	       # 节点ID
        .location  # 节点在页面的相对位置
        .tag_name  # 标签名称
        .size	   # 节点大小，即宽高
        .text	   # 节点内部文本信息
        .get_attribute()	# 获取结点属性

# 解析库（HTML、XML）
import lxml

# 网页解析
from bs4 import BeautifulSoup
    soup = BeautifulSoup()   # BeautifulSoup实例
        # 对象属性
            # 基本元素
                .<tag>  # 标签（Tag），<>和</>标明首尾
                .name	# 标签名字（Name），<p>...</p>
                .attrs	# 标签属性（Attributes），字典
                .string	#　标签内非属性字符串（NavigableString），<>...</>中字符串
	                    # 标签内字符串的注释（Comment），特殊的Comment类型
            # 遍历方式
                .parent	            # 结点的父亲标签
                .parents	        # 结点先辈标签的迭代类型，用于循环遍历先辈节点
                .contents	        # 子节点的列表，将<tag>所有的儿子节点存入列表
                .children	        # 子节点的迭代列表，用于循环遍历儿子节点
                .descendants    	# 子孙结点的迭代列表，包含所有子孙节点，用于循环遍历
                .next_sibling	    # 返回按照HTML文本顺序的下一个平行节点标签
                .previous_sibling	# 返回按照HTML文本顺序的上一个平行节点标签
                .next_siblings   	# 迭代类型，返回按照HTML文本顺序的所有后续平行节点标签
                .previous_siblings	# 迭代类型，返回按照HTML文本顺序的所有前续平行节点标签
        # 对象方法
        .find_all(name,attrs,recursive,string,**kwargs)	# 返回列表类型，存储查找结果
            name     # 对标签名称的检索字符串
            attrs    # 对标签属性值的检索字符串，可标注属性检索
            reursive # 是否对子孙全部检索，默认True
            string   # <>...</>中字符串区域的检索字符串
            #　等价于<tag>(name,attrs,recursive,string,**kwargs)
        .find()	　　　　　          #　搜索且只返回一个结果，返回字符串。find('table',{'id':'giftlist'})
        .find_parents()	　　　　　　#　在先辈节点中搜索，返回列表
        .find_parent()	　　　　　　#　返回字符串
        .find_next_siblings()　    #　返回列表
        .find_next_sibling()	　 #　返回字符串
        .find_previous_siblings()  #　返回列表
        .find_previous_siblings()  #　返回字符串
        # 
        .select()	　　　　　      #　Css选择器
        .prettify()                # 格式化HTML语言，换行显示

# 网页解析（jQuery，css）
import pyquery
    pyquery.PyQuery(url)  # PyQuery对象
        url      # 网址
        filename # 本地文件
 
# 数组处理
import numpy as np   # Numerical Python
        # 实际数据（尽量使用同质数据，便于性能发挥）＋数据描述（维度，类型等）
        # 元素类型：bool，int，uint，complex
    # 创建数组
        np.array(x,dtype=)  # 直接赋值
            x         # 数组对象，列表或元组
            .ndim     # 秩，即轴的数量或维度的数量（矩阵是 二维）
            .shape    # 对象的尺度，对于矩阵n行m列,(n,m)
            .size     # 元素总个数
            .dtype    # 元素类型
                .name
            .itemsize # 每个元素的大小，以字节为单位
        np.arange(start=0,end=n,step=1) # 等差赋值
        np.linspace(start=0,end,num)    # 等差赋值
            num      # 元素个数
            .endpoint=True # 结束值是否包括在生成的数据内
        np.full(shape,val)                # 全是val
        np.ones(shape,dtype=np.float64)   # 全是1
        np.zeros(shape,dtype=np.float64)  # 全是0
        np.empty(x)                       # 全是0
    # 数组对象
    x = np.array()
        .flat # 迭代器(每一个元素)
        # 形状操作
        .transpose()    # 转置(改变数组本身)
        .reshape(shape) # 重排形状(改变参数并返回)
        .resize(shape)  # 重排形状(改变数组本身)
        .ravel()        # 展平数组(改变参数并返回)
        # 运算
        .sum()    # 求和
        .max()    # 最小值
        .min()    # 最小值 
        .cumsum() # 累加和 
            .axis  # 指定轴：0(按列),1(按行)
    # 其他
        # 索引:一维同切片,不同维度按逗号隔开
            x[0:5,1]    # 第1-5行第2列
            a[ : :-1]   # reversed a
            x[-1]       # 最后一行
            # ...的使用
            x[1,2,…]   # 等同于 x[1,2,:,:,:]
            x[…,3]     # 等同于 x[:,:,:,:,3]
            x[4,…,5,:] # 等同于 x[4,:,:,5,:]  
        # 运算
        A*B         # 每个点相乘
        A**3        # 每个点次方运算
        np.add(A,B) # 加法
        np.dot(A,B) # 矩阵相乘
        np.exp(x)   # e^x
        np.sqrt(x)  # 开根号
        np.ceil(x)  # 向上取整
        np.floor(x) # 向下取整
        np.around(x) # 四舍五入
        np.fromfunction(f,shape,dtype) # 自定义函数运算
        # 随机数
        np.random.random() # 生成随机数
        np.random.randint()
        # 数据导入
        np.loadtxt() # 导入txt文件
        # 数组合并
        np.vstack()  # 上下组合((a,b))
        np.hstack()  # 左右组合  
        np.column_stack() # 左右组合
        np.c_[a,b]
        np.row_stack()    # 上下组合 
        np.r_[a,b]
        np.concatenate()  # 
        np.ndarray.flatten() # 嵌套列表扁平化
        # 数组拆分
        np.hsplit(x,3) # 拆分
    np.eye(n)          # n*n单位矩阵


# 数值运算
from scipy.stats import uniform, norm
    uniform.rvs() # 均匀分布随机变量
    norm.rvs()    # 正态分布随机变量


# 统计分析
import statsmodels as sm
import statsmodels.api as sm # 线性模型
    # 回归模型       
        sm.OLS()	        # 普通最小二乘模型
        sm.GLS(endog,exog,family=None)	        # 具有一般协方差结构的广义最小二乘模型
        sm.WLS()         # 具有对角但非标识协方差结构的回归模型
        sm.GLSAR()       # 具有AR（p）协方差结构的回归模型
        sm.yule_walker()	# 使用Yule-Walker方程从序列X估计AR（p）参数
        sm.QuantReg()	# 分位数回归
        sm.Logit()
        sm.RecursiveLS()	# 递归最小二乘法
            endog # Y
            exog  # X
    # 方差分析
    # 时间序列分析
        anova_lm()	# Anova table for one or more fitted linear models
        AnovaRM()	# Repeated measures Anova using least squares regression

    # 非参数方法

    results = model.fit() # 拟合结果
        .params  # 
        .summary() # 总结输出结果
        .predict() # 预测值
from statsmodels.iolib import smpickle
smpickle.save_pickle(obj, fname) # 模型保存
smpickle.load_pickle(fname)	     # 加载模型


# 计算机视觉
import opencv

# 数据分析
import pandas as pd
        # 空值 NaN
    # Series：系列（一维），左边是index索引，右边是element值
    se = pd.Series(sdata) 
        sdata # 可以为列表,字典
        # 对象属性
        .index   # 索引(不可变); 传入列表; 返回列表
            .name  # 轴名
        .values  # 值,f=返回array
        .name    # Series对象名
        # 索引里可以通过筛选数据
        # 多个索引访问要传递列表
        # 函数对每个元素进行处理,直接运算
        se1 + se2 # Series加法元素操作
        # 对象方法
            se.isnull()
    # DataFrame：数据帧（二维），表格数据结构
    df = pd.DataFrame(dfdata))  # 生成DataFrame数据结构
        """
            给不存在的列赋值会创建新列   
            任何Series上的就地修改会影响DataFrame
            嵌套字典：外部键解析为列索引，内部键解析为行索引 
            使用标签切片会包含结束点，切片可以筛选数据
            可进行加减乘除运算，只运算能运算的，其余为NaN
        """
        # 对象属性
            # 可以将列名作为属性查看数据(不推荐)
            .dtypes  # 列数据的类型
            .index   # 行变量名(序号); 传入列表
                .name # 行名
                .is_unique # 索引是否唯一，不唯一返回
            .columns # 列变量名; 传入列表
                .name # 列名
            .values  # 所有数据
            # 
            .T  # 转置
        # 对象方法
                axis = 0 # 默认对行操作; axis=1,axis='columns'对列操作

            # 查看数据
                .head(5)   # 从头查看数据
                .tail(5)   # 从尾查看数据
                .count()   # 非空值数量
                .loc[x,y]  # 索引成员(标签)
                .iloc[x,y] # 索引成员(下标)
                .at[label_i,label_j] # 标签位置的值
                .iat[i,j] # 某个位置的值
                .value_counts() # 每个元素出现次数
                .unique()
                .isnull()
                .notnull()
            # 
                .isin() # 采样
            #
                .reindex(rownames)  # 重排索引，生成新对象
                    colnames
                    method  # 'ffill'/'pad'(前向填充,向下), 'bfill'/'backfill'(后向填充)
                    fill_value	# 代替重新索引时引入的缺失数据值
                    limit	# 当前向或后向填充时，最大的填充间隙
                    level	# 在多层索引上匹配简单索引，否则选择一个子集
                    copy	# 如果新索引与就的相等则底层数据不会拷贝。默认为True(即始终拷贝）
                .set_index()
                .reset_index()
            # 空缺值处理
                .dropna()  # 删除空值
                    how # 删除包含空值的行
                        = 'all' # 只删除全为空的行
                    thresh  # 指定删除缺失数量大于等于指定数量的行
                .fillna() # 填充空值，可传入字典指定每一列填充值
                    method
                    inplace # 是否原地修改
            # 层次化索引
                .unstack() # 变成DataFrame    
                .stack() # 变成Series

            # 数学运算
                .add(df2) # 加法:df+df2
                .radd(df2) # df2+df
                .sub(y) # 减法
                .rsub(y) # df2-df
                .div(y) # 除法
                .rdiv(y)
                .mul(y) # 乘法
                .rmul(y)
                .floordiv(y) #
                .rfloordiv(y) 
                .pow(y) # 
                .rpow(y)
                    fill_value=0 # 空值填充
                    axis # "index"行，"column"列
            # 增删改
                .apply(func) # 对指定行列操作函数
                .applymap(func) # 对每个元素操作函数
                .drop(data,axis=0)  
                    axis=0 # =0删除行，=1、="columns"删除列
                    inplace=True # 原地修改原始数据，不返回值
            # 统计
                .describe()  # 描述性统计：count,mean,std,min,25%,50%,75%,max
                .sum()
                .corr()  # 相关系数(矩阵)
                .cprrwith()
                .cov()  # 协方差(矩阵)
            # 排序
                .sort_index()  # 索引排序
                .sort_values()  # 按值排序
                    ascending=True # 排序方法，默认升序
                    axis=0   # 默认列
                    by=  # 根据指定列(列名)排序
                .rank() # 排名
                    method # 平级关系处理：'max','min','average','first','dense'
            # 分组
                .groupBy()
            # 文件操作
                .to_csv('文件名.csv')  # 导出为csv
                    index=True  # 行索引
                    header=True # 变量名
                .to_excel('文件名',sheet_name='表名')
        # 
        df['列名']  # 子列对象
            .max()  # 列最大值
        # 语句
        del df['列名'] # 删除子列
    # 类方法
        # 索引
        labels = pd.Index() # 生成索引对象，允许重复(多重索引需要)
            .
        # 数据生成
        pd.data_range()
        # 数据读取
        pd.read_csv('filepath',header,names)  # 读入csv
            names # 若header=None则以此为变量名，列表
        pd.read_excel('文件名',sheet_name='表名') # 读入excel
        # 数据情况
        pd.isnull()   # 判断是否为空,返回bool
        pd.notnull()  # 
        # 数学操作
        np.exp()
        # 数据合并
        pd.merge(df1,df2,how='inner',on='键') # 根据键以how方式合并，df1为主要数据集
            how # 合并方式
                left   # 左连接：合并后显示df1所有行
                right  # 右连接：合并后显示df2所有行
                outer  # 外连接：合并所有值，空缺为NaN
                inner  # 内连接：合并所有共有值
        pd.concat(,axis=0) # 连接
            axis # 连接的轴
                axis=0 # 会得到更长的Series,左右拼接
                axis=1 # DataFrame列连接,横向连接
    

# 静态绘图
import matplotlib.pyplot as plt   
    # 折线图      
    plt.plot(*args, **kwargs)   # 例：plt.plot(x1, y1, "r+", x2, y2, "bo"), plt.plot(x1, y1, x2, y2, linestyle='dashed', color='green', marker='*')
        linestyle = "dashed"(虚线),"","","",""
        color     = "r"(red),"b"(blue),"g"(green),"e"(蓝绿色),"m"(品红色),"y"(yellow),"k"(黑色),"w"(white)
        marker    = "-"(实线),"--"(破折号虚线),"-."(破折号-点虚线),":"(细点虚线),"."(粗点虚线),","(像素点虚线),"o"(圆圈虚线),"v"(下三角虚线),"^"(上三角虚线),"<"(左三角虚线),">"(右三角虚线),"1"(上三角菱虚线),"2"(下三角菱虚线),"3"(左三角菱虚线),"4"(右三角菱虚线),"s"(矩形虚线),"p"(五角形虚线),"*"(星形虚线),"h"(六角形虚线),"+"(加号虚线),"x"(叉号虚线),"D"(钻石形虚线),"d"(细钻石虚线),"|"(竖线虚线),"_"(横线虚线)
    # 散点图
    plt.scatter(x, y, s=None, c=None, marker=None, cmap=None,norm=None, vmin=None, vmax=None, alpha=None, linewidths=None,verts=None, edgecolors=None, hold=None, data=None, **kwargs)
            x,y    # x,y轴的一维数组
            s      # 点的大小
            c      # 点的颜色
            marker # 点的形状
            cmap   # Colormap实例
            norm   # 数据亮度
            alpha  # 透明度
            **kwargs
                label # 图例     
    # 绘制子图
    plt.figure(num=None, figsize=None, dpi=None, facecolor=None,edgecolor=None, frameon=True, FigureClass=<class'matplotlib.figure.Figure'>, clear=False, **kwargs)   # Figure对象
            num       # 生成图像的数量
            figsize   # 图像大小
            dpi       # 像素大小
            facecolor # 背景颜色
            edgecolor # 边界颜色
        .add_subplot(rowsnum,columnsnum,plotposition) # 添加折线子图的对象
            .plot()
            .set_xlabel()  # 子图X轴标题
            .set_ylabel()  # 子图Y轴标题
            .set_title()   # 子图图标题
            .legend()      # 子图图例
    plt.xlabel()	# X轴标题
    plt.ylabel()	# Y轴标题
    plt.title()	    # 图标题
    plt.legend()	# 图例
    plt.show()      # 展示图片
    plt.savefig()   # 保存图片

# 动态绘图
import pygal as pg
    # 直方图
    bar = pg.Bar() # 直方图实例
        bar.title    # 图标题
        bar.x_title
        bar.y_title  # y轴标题
        bar.x_labels # x轴标签
        #
        bar.add('sin(x)',y)  # 将Y轴数据的值加载到直方图
            sin(x)  # 图例,数据标题
        bar.render_to_file()  # 保存为svg格式的图形文件
   
# 世界地图(中国地图有问题！！！)
from pygal_maps_world import maps
from pygal_maps_world.i18n import COUNTRYS   # 国家字典,双字符代码
    maps.World()  # 地图对象
        # 方法属性同pygal

# 三维可视化
import vtk






    

####################  机器学习  #################### 
import sklearn
    # 示例
    x_train,y_train,x_test,y_test=getData() # 训练集和测试集
    model = somemodel()                     # 定义模型
    model.fit(x_train,y_train)              # 拟合模型 
    predictions = model.predict(x_test)     # 模型预测
    model.get_params()                      # 获得这个模型的参数
    score = model.score(x_test,y_test)      # 为模型进行打分

# 模型保存与读取
    #  pickle已有建好的模型model
    import pickle
    with open('model.pickle','wb') as f:
        pickle.dumps(model,f)  # 保存
    with open('model.pickle','rb') as f:
        clf = pickle.loads(f)  # 读取
    # joblib
    from  sklearn.externals import joblib
    joblib.dump(model, 'filename.pkl')  # 保存
    model = joblib.load('filename.pkl') # 导入

# 加载数据
import sklearn.datasets
    # 示例数据集
    datasets.load_iris()	# 分类
    datasets.load_boston()	# 回归
    datasets.load_didits()	# 分类(数字图片)
    # 创建数据
    datasets.make_classification() # 创建分类数据集
    datasets.make_regression()     # 创建回归数据集

# 预处理(Pre-Processing)
import sklearn.preprocessing
    # 标准化
    preprocessing.scale() # 标准化
    # 非线性转换（无参数转化）
    quantile_transformer = preprocessing.QuantileTransformer(random_state=0)
    x_train_trans = quantile_transformer.fit_transform(x_train)
    x_test_trans  = quantile_transformer.transform(x_test)
    # 归一化
    x_normalized = preprocessing.normalize(x, norm='l2')
    # 二值化
    binarizer = preprocessing.Binarizer(threshold=0.0)
    binarizer.transform(x)
    # 分类特征编码
    enc = preprocessing.OneHotEncoder(n_values='auto', categorical_features='all')
    enc.fit(x_train)
    enc.transform(x_test).toarray()
    # 缺失值插补
    imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(x_train)
    imp.transform(x_test)

# 模型选择
    # 数据集拆分
    from sklearn.model_selection  import train_test_split
    X_train, X_test, y_train,   y_test = train_test_split(X, y,     test_size=None,train_size=None)
    # 交叉验证-单指标(cross_val_score)
    scores=model_selection.cross_val_score(model,X,y,
      scoring=None,cv=None,
      n_jobs=1,verbose=0,fit_params=None)
    scores.mean()
    # 交叉验证-多度量评估(cross_validate)：用法同cross_val_score
    # 通过交叉验证获取预测(cross_val_predict)
    predicted = cross_val_predict(model,X,y,cv=None)

# 特征选择
from sklearn.feature_selection import VarianceThreshold,SelectKBest,GenericUnivariateSelect
    VarianceThreshold()       # 移除低方差特征，单变量特征选择
    SelectKBest()             # 移除那些除了评分最高的 K 个特征之外的所有特征
    SelectPercentile()        # 移除除了用户指定的最高得分百分比之外的所有特征
    GenericUnivariateSelect() # 允许使用可配置方法来进行单变量特征选择。它允许超参数搜索评估器来选择最好的单变量特征
    RFECV()                   # 递归式特征消除

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer,TfidfVectorizer
    # 自然语言处理(特征提取)
    count_vect = CountVectorizer() # 词频向量
    x_train_counts = count_vect.fit_transform(x_train)
    tfidf_transformer = TfidfTransformer() # TF-IDF向量
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
    # 合并
    tfidf_vect = TfidfVectorizer()
    x_train_tfidf =  tfidf_vect.fit_transform(x_train)


# 回归与分类（Regression and Classification）
    # 线性模型
    from sklearn.linear_model import LinearRegression,Ridge,Lasso,MultiTaskLasso,LogisticRegression,SGDRegressor,SGDClassifier,ElasticNetCV,MultiTaskElasticNet
        LinearRegression()     # 普通最小二乘回归
        Ridge()	               # 岭回归
        Lasso()	               # 估计稀疏系数的线性模型回归
        MultiTaskLasso()	   # 多任务 Lasso 回归
        LogisticRegression()   # logistic 回归
        SGDRegressor()	       # 随机梯度下降回归
        SGDClassifier()	       # 随机梯度下降分类
        ElasticNetCV()	       # 弹性网络回归
        MultiTaskElasticNet()  # 多任务弹性网络回归
    # 支持向量机
    from sklearn.svm import SCR
        SVC()  # 支持向量机分类
        SVR()  # 支持向量机回归
    # 最近邻算法
    from sklearn.neighbors import NearestNeighbors
        NearestNeighbors()          # 无监督最近邻
        KNeighborsClassifier()      # k-近邻分类
        RadiusNeighborsClassifier() # 固定半径近邻分类
        KNeighborsRegressor()       # 最近邻回归
        RadiusNeighborsRegressor()	
        NearestCentroid()           # 最近质心分类
    # 高斯过程
    from sklearn.gaussian_process import GaussianProcessRegressor
        GaussianProcessRegressor()  # 高斯过程回归（GPR）
        GaussianProcessClassifier() # 高斯过程分类（GPC）
        Kernel()                    # 高斯过程内核
    # 决策树
    from sklearn.tree import DecisionTreeClassifier
        DecisionTreeClassifier() # 决策树分类
        DecisionTreeRegressor()  # 决策树回归
    # 内核岭回归
    from sklearn.kernel_ridge import kernelRidge
        KernelRidge() # 内核岭回归
    # 等式回归
    from sklearn.isotonic.IsotonicRegression
        IsotonicRegression	
    # 多类多标签算法
    from sklearn.multiclass import multiclass
        multiclass
    # 朴素贝叶斯分类器
    from sklearn.naive_bayes import GaussianNB
        GaussianNB()   # 高斯朴素贝叶斯
        MultinomialNB() # 多项分布朴素贝叶斯
        BernoulliNB()   # 伯努利朴素贝叶斯
    # 集成方法
    from sklearn.ensemble import BaggingClassifier
        BaggingClassifier()          # Bagging
        BaggingRegressor()           # 
        RandomForestClassifier()     # 随机森林
        RandomForestRegressor()      # 
        ExtraTreesClassifier()       # 极限随机树
        ExtraTreesRegressor()        # 
        AdaBoostClassifier()         # AdaBoost
        AdaBoostRegressor()          # 
        GradientBoostingClassifier() # Gradient Tree Boosting (梯度树提升)
        GradientBoostingRegressor()  # 
        VotingClassifier()           # 投票分类器
    # 神经网络
    from sklearn.neural_network import MLPClassifier
        MLPClassifier() # 多层感知器(MLP)
        MLPRegressor()
    # 高斯混合模型
    from sklearn.mixture import GaussianMixture
        GaussianMixture()         # 高斯混合
        BayesianGaussianMixture() # 变分贝叶斯高斯混合

# 降维（Dimensionality Reduction）
    # 矩阵分解
    from sklearn.decomposition import PCA
        # 主成分分析（PCA）	
        PCA()            # 准确的PCA和概率解释
        IncrementalPCA() # 增量PCA
        KernelPCA()      # 核 PCA
        SparsePCA()      # 稀疏主成分分析
        MiniBatchSparsePCA() # 小批量稀疏 PCA
        # 截断奇异值分解	
        TruncatedSVD() 
            # 词典学习
            SparseCoder()                 # 带有预计算词典的稀疏编码
            DictionaryLearning()          # 通用词典学习
            MiniBatchDictionaryLearning() # 小批量字典学习
        # 因子分析	
        FactorAnalysis() # 高斯分布
        FastICA()        # 隐变量基于非高斯分布
        # 独立成分分析（ICA）	
        FastICA()	
        # 非负矩阵分解(NMF 或 NNMF)	
        NMF()
        # 隐 Dirichlet 分配（LDA）	
        LatentDirichletAllocation()
    # 流形学习：非线性降维方法
    from sklearn.manifold import Isomap
        Isomap()                 # 等距映射（Isometric Mapping）
        LocallyLinearEmbedding() # 局部线性嵌入
        SpectralEmbedding()      # 谱嵌入
        MDS()                    # 多维尺度分析
        TSNE()                   # t 分布随机邻域嵌入（t-SNE）

# 聚类（Clustering）
    # 聚类
    from sklearn.cluster import
        KMeans() # K-means聚类
        AffinityPropagation() # AP聚类
        MeanShift() # 
        SpectralClustering() # 
        AgglomerativeClustering() # 层次聚类
        DBSCAN() # 
        Birch()
    # 双聚类
    from sklearn.cluster.bicluster import SpectralCoclustering
        SpectralCoclustering()
        SpectralBiclustering()

# 其他
    # 协方差估计
    from sklearn.covariance import empirical_covariance
        empirical_covariance() # 经验协方差
    # 特征提取(sklearn.feature_extraction)可用于提取符合机器学习算法支持的特征，比如文本和图片。
    # 概率校准()
    from sklearn.calibration import CalibratedClassifierCV
        CalibratedClassifierCV()





import scikit-plot
import keras

# 深度学习
import tensorflow as tf
import pytorch

####################### 自然语言处理 ######################
import nltk
    nltk.sent_tokensize() # 对文本进行句子分割
    nltk.word_tokenize() # 对句子进行分词

    nltk.pos_tag(tokens) # 词性标注 tokens句子分词后的结果
    nltk.ne_chunk(tags) # 命名实体标注 tags句子词性标注后的结果

    nltk.download()  #  下载模型

import polyglot  # 海量文本，多语言

import spacy  # 速度最快，最先进，工业级别
    python -m spacy download en # 下载数据与模型
    nlp=spacy.load('en')
    doc=nlp(open().read())

import montylingua # 英文

import jieba  # 中文分词
    # 分词
    jieba.cut()   # 分词：返回generator
    jieba.lcut()  # 分词：返回list
        cut_all = False # False=精确模式, True=全模式
    jieba.cut_for_search() # 搜索引擎模式
    # 
    jieba.add_word()  # 添加词典
    jieba.del_word()  # 


import pyltp  # 哈工大中文LTP(Language Technology Platform)


# 社会网络
import networkx

# 
import pytesseract # OCR
import PILLOW      # 图像处理
import seaborn as sns


# 音乐
import music21
us['lilipondPath'] = "D:"
us['musescoreDirectPNGPath'] = "D:/OneDrive - email.cufe.edu.cn/APP/MuseScore3(64-bit)/bin/MuseScore3.exe"
us['musicxmlPath'] = "D:/OneDrive - email.cufe.edu.cn/APP/MuseScore3(64-bit)/bin/MuseScore3.exe"

####################### 业务 ##########################

######## 网络爬虫 ########
    # 爬虫限制
    1.	来源审查
        (1)	作用：检查来访HTTP协议头的User-Agent域，只响应浏览器或友好爬虫的访问
        (2)	查看：
            r.request.headers  # 查看反馈给网站的头部信息
            kv={'user-agent':'Mozilla/5.0'}   # 在try中添加，修改headers
    2.	发布公告： 
        (1)	作用：Robots协议（Robots Exclusion Standard）告知所有爬虫网站的爬取策略，要求爬虫遵守（建议、非约束性，有法律风险；类人行为（如每日访问量小）可不参考）
        (2)	形式：在网站根目录下的robots.txt文件（如http://www.jd.com/robots.txt）
        (3)	语法：
            User-agent:*  # “*”代表所有
            Disallow:/    # “/”代表根目录
    # 爬虫框架库
    Requests：爬取网页，小规模，数据量小，爬取速度不敏感
    Scrapy库：爬取网站/系列网站，中规模，数据规模较大，爬取速度敏感
    定制开发：爬取全网，大规模，搜索引擎，爬取速度关键

######## 文本分析 ########
    (1)	分词：
    (2)	转换为数字化矩阵：独热表示法（不考虑语序和语法），词嵌入技术
    (3)	信息提取：
        ①无监督学习：词典法（统计次数，选择加权方法），主题分类模型
        ②有监督学习：
            经典：朴素贝叶斯（Naïve Bayes），支持向量机（Support Vector Machine），决策树，K近邻算法，adaboost，最大熵法
            深度学习：深度神经网络（deep neural nets, DNN），卷积神经网络（convolutional neural network, CNN），循环神经网络（recurent neural network, RNN）
    (4)	应用：
        ①经济学：经济政策不确定性指数(EPU)，行业分类，经济周期的度量与预测，媒体政治倾向
        ②关注度指数：投资者关注度，媒体关注度
        ③文本情绪：媒体情绪，管理层语调，投资者情绪，新闻隐含波动率指数，投资者分歧


Web库
    Flask 是一个轻量级的 Web 服务程序，简单、易用、灵活，在本书中我们主要用它来做一些 API 服
    Tornado 是一个支持异步的Web框架，通过使用非阻塞 I/O 流，它可以支撑成千上万的开放连接，效率非常高
爬虫框架库
    PySpider 是国人 binux 编写的强大的网络爬虫框架，它带有强大的 WebUI、脚本编辑器、任务监控器、项目管理器以及结果处理器，同时它支持多种数据库后端、多种消息队列，另外它还支持 JavaScript 渲染页面的爬取
    ScrapyRedis 是 Scrapy 分布式的扩展模块，有了它我们可以方便地实现 Scrapy 分布式爬虫的搭建
        pip3 install scrapy-redis
数据存储库
    (1)	文件存储：txt，json，csv
    (2)	关系型数据库存储：MySql
    (3)	非关系型数据库存储：MongoDB，Redis
    PyMongo（存储库）
    PyMySql（存储库）
    Redis（存储库：支持非关系Redis）
Ajax数据爬取
Ajax，全称为 Asynchronous JavaScript and XML，即异步的 JavaScript 和 XML。
Ajax 不是一门编程语言，而是利用 JavaScript 在保证页面不被刷新、页面链接不改变的情况下与服务器交换数据并更新部分网页的技术


