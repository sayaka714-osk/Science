



/*************  一、数据  ****************/






/*************  二、函数  ****************/

// 数学函数
gen a1 = int(b)  // 取整，直接抹除小数位
gen a2 = sqrt(b) // 开根号

// 时间函数
gen date    = date(date_variable, "YMD")  // 用date函数，根据string格式的date_variable，生成时间变量date
gen year    = year(date)
gen quarter = quarter(date)
gen month   = month(date)
gen week    = week(date)
gen yq      = yq(year, quarter)

// 字符串函数
gen a = strmatch( b , "*xxx*" ) // 如果字符型变量b包含字符串“xxx”，那么a=1，否则a=0




/*************  三、命令  ****************/


/****   1、数据收集   ****/

此步骤在Stata里面无关紧要。如果是数据库，此步骤为手动下载。如果是爬取数据，不建议使用Stata，Python或其他爬虫的工业化软件明显更方便。如果选择录入数据，直接探索菜单就好。

/****   2、数据导入   ****/

// 因为Stata15及以前的版本只有一张数据表，因此需要对各个数据文件分别导入、导出等。
// 最原始的数据导入建议手动，直接点菜单，然后保存为.dta格式的文件。在Stata里，这种步骤重复性低而可复用性高（在金融里，能用的公开数据就那几个），直接转成dta数据即可。再者，dta数据文件打开速度相较于txt等较快。

（1）如果使用命令导入非Stata的dta文件：
import

（2）如果是Stata文件，则直接：
use "data.dta", clear // 导入目录""中的Stata数据文件

（3）中途数据
// 将内存中的数据生成为暂时文件file_name。这样就不会始终占据磁盘空间，尤其是当合作的数据等需要同步时，不会陷入每一个临时文件都被同步的烦恼
tempfile file_name
// 保存暂时文件file_name。暂时文件的使用需要在前后分别加上`和'符号
save "`file_name'" , replace
// 导入暂时文件
use "`file_name'", clear



/****   3、数据清洗   ****/
// 数据类型转换
tostring a , replace  // 将数值型变量a转化为字符型变量
destring a , replace  // 将字符型变量a转化为数值型变量


/****   4、数据合并   ****/
// 横向键值匹配
merge 1:1 firm year using "data.dta"  // 将data.dta文件与当前数据表根据键值对firm和year进行横向合并
// 纵向键值匹配
append using "data.dta"  // 将新的观测值从尾部追加到当前数据表中


/****   5、数据生成   ****/
（1）增
gen  a = b  // 生成（generate）a使其等于b
egen a = total(b)  // 生成变量a使其等于b变量所有观测值之和
    egen：升级版gen
bysort year: egen a = total(b)  // 根据年份变量year分组，生成变量a使其等于组内b变量所有观测值之和
// 时序变化
gen a1 = F.b // 前推项：生成变量a1，使其等于t+1期的b
gen a2 = L.b // 滞后项：生成变量a2，使其等于t-1期的b
gen a3 = D.b // 差分项：生成变量a3，使其等于t期的b减去t-1期的b

（2）删
drop variable_names  // 删除变量variable_names
drop if a == b  // 删除符合if条件的观测值
duplicates drop a b , force // 删除以a和b为键值的重复观测值
    force (强制删除)

（3）改
// 数据修改
replace a = b      // 用b替代a
replace a = b if a>1
ereplace：
ereplace a = total(b) // 用b的和（total）替代a
    replace升级版，具体函数对标egen
collapse (sum) a (mean) b , by(year)  // 根据firm和year分组，对每组内变量进行压缩。a等于组内数据之和；b等于组内数据的均值
    // collapse会将未列明的其他变量删除，因此一般在数据清洗的最后使用。
    // 在前面使用时，可以用“by/bysort 分类变量: gen/egen”的组合


// 变量重命名
rename a b // 将变量a重命名为b
// 修改标签
label var a "A" // 将变量a的标签命名为A


（4）补
mvencode a b c , mv(0) // 用0填充变量a、b、c的空缺值



/****   6、数据分析   ****/


reg  // 最普通的回归命令
    reg y x1 x2 x3  


// 面板回归
xtset firm year // 声明是面板数据，个体变量为firm，时间变量为year

xtreg // 官方面板回归
    xtreg y x1 x2 x3 , fe
    // fe：模型包含Firm Fixed Effect和Year Fixed Effect，不可变换，灵活性差

reghdfe // 高维固定效应回归
    reghdfe y x1 x2 x3 , absord(firm year) vce(cluster firm)
    // absorb：模型包含Firm Fixed Effect和Year Fixed Effect，可调整
    // vce(cluster )：t值显著性根据firm进行聚类







