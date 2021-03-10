


/*********  基本设置  *********/

clear all  // 清除Stata所有设置
set more off
set matsize 10000
mata: mata mlib index
global home "D:program_name\"              // 设置宏，为项目所在目录。引用时加$
global data "D:\OneDrive\DataCenter\CSMAR" // 设置宏，为数据库目录
cd  "$home\result"                         // 设置文件导出的目录（实际为默认的操作目录），为home下的result文件夹


/*********  数据导入  *********/

// 因子数据：
// 日期（trddy→date），因子（需要rf，mkt_rf，smb， hml三个变量）
import delimited "$data\fama-french\three_four_five_factor_daily\fivefactor_daily.csv", encoding(utf8) clear
gen date = date(trddy,"YMD")  // 日期
tempfile fivefactor_daily
save "`fivefactor_daily'",replace

// 日度股票收益率文件：
// 公司（stkcd→firm），日期（trddt→date），股票收益率（dretwd→return），公司市值（dsmvosd→mktcap）
use "$data\股票市场系列\股票市场交易2019\TRD_Dalyr.dta",clear
rename trddt    date    // 日期
rename stkcd    firm    // 公司
rename dretwd   return  // 日度收益率
rename dsmvosd  mktcap  // 公司市值
tempfile TRD_Dalyr
save "`TRD_Dalyr'", replace

// 资产负债表数据：公司（stkcd→firm），日期（trddt→date），总资产（a001000000→ta），总负债（a002000000→tl）
use "$data\财务报表\FS_Combas.dta", clear
keep if typrep=="A"        // 保留合并报表
gen date    = date(Accper,"YMD") // 日期变量
gen year    = year(date)         // 年份
gen quarter = quarter(date)      // 季度
rename stkcd      firm // 公司变量
rename a001000000 ta   // 资产总计
rename a002000000 tl   // 负债总计
tempfile FS_Combas
save "`FS_Combas'",replace

// 公司详情文件：
// 企业（stkcd→firm），所在行业（nnindcd→industry），上市年份（listdt→listyear）
use "$data\股票市场系列\股票市场交易2019\TRD_Co.dta",clear
gen listdate = date(listdt,"YMD") // 上市日期
gen listyear = year(listdate)     // 上市年份
rename indcd  industry            // 重命名行业变量
rename stkcd  firm                // 重命名公司变量
tempfile TRD_Co
save "`TRD_Co'",replace



/*********  合并数据  ********/

use "`TRD_Dalyr'", clear
// 用"`fivefactor_daily'"去匹配内存中的"`TRD_Dalyr'"文件
// 根据date两个变量进行多对一m:1匹配。
// "`fivefactor_daily'"可根据date确定唯一值；但内存中的master数据"`TRD_Dalyr'"每个日期有多个公司，因此可确定多个值
merge m:1 date       using "`fivefactor_daily'"  
drop if _merge==2   // 删除using文件中未匹配上的（即_merge==2的观测值，_merge会自动生成）
drop _merge         // 删除匹配中生成的_merge变量
// 合并公司详情
merge m:1 firm       using "`TRD_Co'"       
drop if _merge==2
drop _merge
// 合并资产负债表
gen year    = year(date)    // 生成年份变量
gen quarter = quarter(date) // 生成季度变量
merge m:1 firm year quarter using "`FS_Combas'"  
drop if _merge==2
drop _merge



/*********  数据生成  ********/

xtset stkcd date                 // 声明面板数据
keep if inrange(fyear,2005,2020) // 保留2005-2020年的数据
drop if industry=="1"            // 删除金融行业

// 星期变量
gen week   = dow(date) // 生成0-6变量
gen monday = (week==1) // 是否为星期一，是为1，否为0
gen friday = (week==5) // 是否为星期五，是为1，否为0

// 超额收益率
gen ret = return - rf       // 超过无风险收益率的收益率
// Fama-Frenc三因子回归：根据firm分组，在时间序列区间[364,0]共365天内估计系数
asreg ret  mkt_rf  smb  hml   , w(date 365) by(firm) fitted
// 超额收益率：实际收益率-模型拟合生成的收益率
gen ar_ff3 = ret - _fitted  // _fitted是命令生成的拟合值

// 控制变量
gen size = ln(mktcap)        // 对数化公司市值
gen age  = year - listyear   // 企业年龄
gen lev  = tl/ta             // 杠杆率

// 标签命名
label var monday "Monday"
label var friday "Friday"
label var size   "Size"  
label var age    "Age"
label var lev    "Lev"


/*********  回归分析  ********/
/*
    ar_ff3 = constant + beta_1*monday + beta_2*size + beta_3*age + beta_4*lev + epsilon 
    ar_ff3 = constant + beta_1*friday + beta_2*size + beta_3*age + beta_4*lev + epsilon 
*/

preserve  // preserve-restore中的为暂时的命令，只在区域内执行
reghdfe ar_ff3 monday size age lev , absorb(firm year) vce(cluster firm)
eststo table_1 , t(AR) // 回归数据保存，该列标题为AR

reghdfe ar_ff3 friday size age lev , absorb(firm year) vce(cluster firm)
eststo table_2 , t(AR)

local table "table_1 table_2"  // 生成暂元table，合并两列结果
// 结果导出
esttab `table' using "baseline.rtf", replace   								///
    star(* 0.1 ** 0.05 *** 0.01) b(%6.4f) t(%6.2f)							///
    stats(N r2_a, labels("Observations" "Adjusted R^2") fmt(%9.0fc %9.2fc)) ///					
    keep(  monday friday size age lev )    									///
    order( monday friday size age lev )    									///		
    coeflabels(_cons "Constant")  eqlabels("") 								///			
    label nonotes compress mtitles nodepvars nogaps
/*
    using "baseline.rtf" 导出回归文件，会输出到D:program_name\result\baseline.rtf
    keep(), order()      要输出的自变量
    ///                  三杠表示换行
*/
restore




