import re

a = ["核心网设备",
     "电路域",
     "MSC数量",
     "eMSC数量",
     "CSFBMSC数量",
     "MSC话务承载能力",
     "VLR数据库容量",
     "三融合HSS/HLR数量",
     "三融合HSS/HLR基础容量",
     "三融合HSS/HLR4G容量",
     "三融合HSS/HLRVoLTE容量",
     "分组域",
     "MME/SGSN数量",
     "MME/SGSN基础容量",
     "MME/SGSN4G容量",
     "SAE-GW/GGSN数量",
     "SAE-GW/GGSN基础容量",
     "SAE-GW/GGSN4G容量",
     "PCRF/SPR数量",
     "PCRF/SPR容量",
     "IMS域",
     "CM-IMS会话控制功能实体I/S/E-CSCF/BGCF数量",
     "CM-IMS会话控制功能实体I/S/E-CSCF/BGCF容量",
     "固网IMSHSS数量",
     "固网IMSHSS容量",
     "统一Centrex业务平台数量",
     "统一Centrex业务平台容量",
     "CM-IMS多媒体电话业务平台数量",
     "CM-IMS多媒体电话业务平台容量",
     "IMS/TD多媒体彩铃业务平台数量",
     "IMS/TD多媒体彩铃业务平台容量",
     "VoLTEAS数量",
     "VoLTEAS容量",
     "VoLTESBC数量",
     "VoLTESBC用户容量",
     "VoLTESBC话务承载能力",
     "GMSC和GMSC/MGCF/IM-MGW数量",
     "GMSC和GMSC/MGCF/IM-MGW基础容量",
     "GMSC和GMSC/MGCF/IM-MGWIP化容量",
     "GMSC/MGCF/IM-MGWMGCF容量",
     "纯MGCF/IM-MGW数量",
     "纯MGCF/IM-MGW容量",
     "固网SBC数量",
     "固网SBC用户容量",
     "VoLTE网络日均忙时话务量",
     "5G核心网",
     "AMF数量",
     "AMF5G容量",
     "SMF数量",
     "SMF5G容量",
     "两融合PCF/UDR数量",
     "两融合PCF/UDR容量",
     "四融合UDM/UDR数量",
     "四融合UDM/UDR基础容量",
     "四融合UDM/UDRVoLTE容量",
     "四融合UDM/UDR5G容量",
     "NSSF数量",
     "NSSF容量",
     "NRF数量",
     "NRF容量",
     "UPF数量",
     "UPF5G容量",
     "接入网设备",
     "GSM无线接入网",
     "GSM网BSC数",
     "GSM逻辑基站数",
     "GSM900逻辑基站数",
     "GSM1800逻辑基站数",
     "GSM逻辑室外宏基站数",
     "GSM逻辑室内分布基站数",
     "GSM物理基站数",
     "GSM物理宏基站数",
     "GSM900物理宏基站数",
     "GSM1800物理宏基站数",
     "GSM900与GSM1800共站址物理宏基站数",
     "GSM物理室内分布基站数",
     "GSM900室内分布基站数",
     "GSM1800室内分布基站数",
     "GSM900与GSM1800共站址室内分布基站数",
     "GSM小区数",
     "GSM1800小区数",
     "GSM载频数",
     "GSM1800载频数",
     "GSM话音信道数",
     "GSM1800话音信道数",
     "TD无线接入网",
     "TD-SCDMARNC数",
     "TD-SCDMA基站数",
     "宏基站数",
     "室内分布基站数",
     "TD-SCDMA小区数",
     "TD-SCDMA载频数",
     "WLAN",
     "WLANAC数",
     "WLANAP数",
     "完成覆盖的WLAN热点数",
     "TD-LTE",
     "TD-LTE基站数",
     "室外基站数",
     "室内基站数",
     "室外宏基站数",
     "室外微基站",
     "传统室分基站数",
     "分布式皮飞基站数",
     "TD-LTE一体化皮飞基站数",
     "TD-LTE载频数",
     "F频段载频数",
     "D频段载频数",
     "E频段载频数",
     "A频段载频数",
     "TD-LTE3D-MIMO载扇数",
     "TD-LTE物理小区数",
     "TD-LTE室外宏基站物理小区数",
     "TD-LTE室外微基站物理小区数",
     "TD-LTE室内分布基站物理小区数",
     "GSM无线接入网",
     "TD无线接入网",
     "TD-LTE",
     "WLAN",
     "LTEFDD",
     "LTEFDD逻辑基站数",
     "室外基站数",
     "室内基站数",
     "单LTEFDD900基站数",
     "室外基站数",
     "单LTEFDD900室外宏基站数",
     "单LTEFDD900室外微基站数",
     "室内分布基站数",
     "单LTEFDD900传统室分基站数",
     "单LTEFDD900分布式皮飞基站数",
     "单LTEFDD1800基站数",
     "室外基站数",
     "单LTEFDD1800室外宏基站数",
     "单LTEFDD1800室外微基站数",
     "室内分布基站数",
     "单LTEFDD1800传统室分基站数",
     "单LTEFDD1800分布式皮飞基站数",
     "LTEFDD900与LTEFDD1800共站址的基站数",
     "室外基站数",
     "LTEFDD900与LTEFDD1800共站址室外宏基站数",
     "LTEFDD900与LTEFDD1800共站址室外微基站数",
     "室内基站数",
     "LTEFDD900与LTEFDD1800共站址传统室分基站数",
     "LTEFDD900与LTEFDD1800共站址分布式皮飞基站数",
     "LTEFDD载频数",
     "LTEFDD1800载频数",
     "LTEFDD3D-MIMO载扇数",
     "LTEFDD小区数",
     "LTEFDD900室外宏基站小区数",
     "LTEFDD900室外微基站小区数",
     "LTEFDD900室内分布基站小区数",
     "LTEFDD1800室外宏基站小区数",
     "LTEFDD1800室外微基站小区数",
     "LTEFDD1800室内分布基站小区数",
     "开通eMTC小区数",
     "开通eMTC的900M室外小区数",
     "开通eMTC的900M室内小区数",
     "开通eMTC的1800M室外小区数",
     "开通eMTC的1800M室内小区数",
     "NB-IoT",
     "开通NB-IoT基站数",
     "室外基站数",
     "室内基站数",
     "NB-IoT载频数",
     "NB-IoT小区数",
     "5G",
     "5G逻辑基站数",
     "室外基站数",
     "室外宏基站数",
     "2.6GHz室外宏基站数",
     "4.9GHz室外宏基站数",
     "室外微基站数",
     "2.6GHz室外微基站数",
     "4.9GHz室外微基站数",
     "室内逻辑基站数",
     "传统室内基站数",
     "分布式皮飞基站数",
     "扩展型皮基站数",
     "5G载频数",
     "室外宏基站载频数",
     "2.6GHz室外宏基站载频数",
     "4.9GHz室外宏基站载频数",
     "室外微基站载频数",
     "2.6GHz室外微基站载频数",
     "4.9GHz室外微基站载频数",
     "室内覆盖载频数",
     "物理站址资源",
     "总物理站址数",
     "室外覆盖物理站址数",
     "室内覆盖物理站址数",
     "自有物理站址数",
     "宽带能力指标",
     "PON端口",
     "PON端口数量",
     "EPON端口数量",
     "GPON端口数量",
     "XG(S)-PON端口数量",
     "用于家庭宽带业务接入的PON端口数量",
     "采用FTTH模式开通的PON端口数量",
     "采用1:64/2:64总分光的PON端口数量",
     "采用1:32/2:32总分光的PON端口数量",
     "采用FTTB模式开通的PON端口数量",
     "ONU设备",
     "ONU设备数量",
     "GPON/EPONONU设备数量",
     "FTTB场景ONU设备数量",
     "用于家宽接入的FTTB场景ONU设备数量",
     "SFU设备数量",
     "用于家宽接入的SFU设备数量",
     "HGU设备数量",
     "用于家宽接入的HGU设备数量",
     "智能家庭网关设备数量",
     "用于家宽接入的智能家庭网关设备数量",
     "XG(S)-PONONU设备数量",
     "FTTB场景ONU设备数量",
     "用于家宽接入的FTTB场景ONU设备数量",
     "智能家庭网关设备数量",
     "用于家宽接入的智能家庭网关设备数量",
     "OLT设备数量",
     "宽带接入端口",
     "有线宽带接入端口",
     "xDSL端口",
     "FTTB端口",
     "FTTH/O端口",
     "WBS端口",
     "城市地区接入端口",
     "xDSL端口",
     "FTTB端口",
     "FTTH/O端口",
     "WBS端口",
     "50M以上城市宽带接入端口",
     "100M以上城市宽带接入端口",
     "农村地区接入端口",
     "xDSL端口",
     "FTTB端口",
     "FTTH/O端口",
     "WBS端口",
     "20M以上农村宽带接入端口",
     "100M以上农村宽带接入端口",
     "家庭宽带接入端口数",
     "xDSL端口",
     "FTTB端口",
     "已开通家庭宽带业务的FTTBONU端口数量",
     "使用XG(S)-PON技术的FTTB端口数",
     "已开通家庭宽带业务的XG(S)-PON技术的FTTB端口数",
     "FTTH/O端口",
     "已开通家庭宽带业务的FTTH光分路器端口数量",
     "使用XG(S)-PON技术的FTTH光分路器端口数",
     "已开通家庭宽带业务的XG(S)-PON技术的FTTH光分路器端口数",
     "WBS端口",
     "分纤点",
     "光纤分纤点数量",
     "其他：城区一级分纤点数量",
     "城区二级分纤点数量",
     "非城区一级分纤点数量",
     "非城区二级分纤点数量",
     "宽带接入速率",
     "全省有线宽带用户总接入带宽",
     "全省家庭宽带用户总接入带宽",
     "计划单列市和省会城市总接入带宽",
     "计划单列市和省会城市家庭宽带总接入带宽",
     "核心网设备",
     "CMN数量",
     "CMN处理能力",
     "长途Diameter信令网HDRA数量",
     "长途Diameter信令网DRA处理能力",
     "省内Diameter信令网LDRA数量",
     "省内Diameter信令网LDRA处理能力",
     "省内Diameter信令网LDRA会话绑定消息处理能力",
     "长途七号信令网HSTP数量",
     "长途七号信令网HSTP等效2M链路数",
     "省内七号信令网LSTP数量",
     "省内七号信令网LSTP等效2M链路数",
     "业务网设备",
     "业务平台",
     "短消息中心数量",
     "短消息中心处理能力",
     "短消息中心平时实际峰值处理业务量",
     "短消息中心节假日实际峰值处理业务量",
     "彩信中心处理能力",
     "彩信中心实际峰值处理业务量",
     "智能网",
     "智能业务控制节点SCP数量",
     "智能业务控制节点SCP硬件能力",
     "智能业务控制节点SCP用户容量",
     "智能业务控制节点SCPAS数量",
     "智能业务控制节点SCPAS硬件能力",
     "智能业务控制节点SCPAS用户容量",
     "智能业务管理点SMP数量",
     "智能网充值中心VC数量",
     "智能网充值中心VC容量",
     "IT基础设施",
     "企业私有云资源池服务器台数",
     "企业私有云资源池存储容量",
     "公众服务云资源池服务器台数",
     "公众服务云资源池存储容量",
     "内容分发网络",
     "边缘服务节点数量",
     "边缘服务节点总容量",
     "统一DPI设备",
     "互联网统一DPI覆盖规模",
     "4G/5G上网日志留存系统容量",
     "数据承载网",
     "CMNET城域网出口带宽",
     "CMNET城域网业务接入控制层设备配置等效GE端口数",
     "IP专网AR上连BR带宽",
     "IP专网AR设备配置等效GE端口数",
     "IP专网CE设备台数",
     "互联网省际出口带宽",
     "CMNET省网出口带宽",
     "CMNET省网第三方出口带宽",
     "核心网设备",
     "业务网设备",
     "数据承载网",
     "传送网",
     "杆路线路长度",
     "自有",
     "租用",
     "租用电信杆路线路长度",
     "租用联通杆路线路长度",
     "租用杆路费用",
     "租用电信杆路费用",
     "租用联通杆路费用",
     "直埋光缆线路长度",
     "自有",
     "租用",
     "租用电信直埋光缆线路长度",
     "租用联通直埋光缆线路长度",
     "租用直埋光缆费用",
     "租用电信直埋光缆费用",
     "租用联通直埋光缆费用",
     "管道线路长度",
     "自有",
     "租用",
     "租用电信管道线路长度",
     "租用联通管道线路长度",
     "租用管道线路费用",
     "租用电信管道线路费用",
     "租用联通管道线路费用",
     "敷设自有管道的市政道路长度",
     "传送网合计",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "省际骨干传送网",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆线路长度",
     "光缆长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "省内骨干传送网",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆线路长度",
     "光缆长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "传送网",
     "光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "波分复用系统长度",
     "10Gb/s同步数字系列设备套数",
     "2.5Gb/s同步数字系列设备套数",
     "622Mb/s及以下同步数字系列设备套数",
     "10GEPTN设备套数",
     "40GEPTN设备套数",
     "100GEPTN设备套数",
     "2.5G线路侧端口数量",
     "10G线路侧端口数量",
     "40G线路侧端口数量",
     "100G线路侧端口数量",
     "2.5G支路侧端口数量",
     "10G支路侧端口数量",
     "40G支路侧端口数量",
     "100G支路侧端口数量",
     "城域网",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "引入光缆线路长度",
     "租用光缆线路长度",
     "光缆长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "引入光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "光缆纤芯长度",
     "引入光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "已占用引入光缆纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "10Gb/s同步数字系列设备套数",
     "2.5Gb/s同步数字系列设备套数",
     "622Mb/s以下同步数字系列设备套数",
     "PTN设备总数量",
     "GEPTN设备数量",
     "10GEPTN设备数量",
     "40GEPTN设备套数",
     "100GEPTN设备套数",
     "2.5G线路侧端口数量",
     "10G线路侧端口数量",
     "40G线路侧端口数量",
     "100G线路侧端口数量",
     "传送网",
     "SDH：2Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "155Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "2.5Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "10Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "1Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "2.5Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "10Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "100Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "2Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "155Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "2.5Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "10Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "传输电路",
     "分布系统情况",
     "室内分布系统物业点数",
     "分布式皮飞物业点数",
     "室分系统覆盖面积",
     "分布式皮飞基站覆盖面积",
     "高铁覆盖情况",
     "4G覆盖高铁线路数",
     "4G覆盖高铁线路里程",
     "4G高铁基站数",
     "TD-LTE高铁基站数",
     "LTEFDD高铁基站数",
     "4G高铁载频数",
     "TD-LTE高铁载频数",
     "LTEFDD高铁载频数",
     "4G高铁物理基站数",
     "2G高铁基站数",
     "GSM900M高铁基站数",
     "GSM1800M高铁基站数",
     "5G覆盖高铁线路数",
     "5G覆盖高铁线路里程",
     "5G高铁逻辑基站数",
     "5G高铁载频数",
     "5G高铁物理基站数",
     "汇聚机房",
     "汇聚机房数量",
     "城区汇聚机房数量",
     "自有城区汇聚机房数量",
     "非城区汇聚机房数量",
     "自有非城区汇聚机房数量",
     "重要汇聚机房数量",
     "城区重要汇聚机房数量",
     "城区自有重要汇聚机房数量",
     "非城区重要汇聚机房数量",
     "非城区自有重要汇聚机房数量",
     "普通汇聚机房数量",
     "城区普通汇聚机房数量",
     "城区自有普通汇聚机房数量",
     "非城区普通汇聚机房数量",
     "非城区自有普通汇聚机房数量",
     "业务汇聚机房数量",
     "城区业务汇聚机房数量",
     "城区自有业务汇聚机房数量",
     "非城区业务汇聚机房数量",
     "非城区自有业务汇聚机房数量",
     "开通移动电话的地市",
     "开通4G的地市",
     "开通5G的地市",
     "开通移动电话的县市",
     "开通4G的县市",
     "开通5G的县市",
     "开通移动电话的乡镇",
     "开通4G的乡镇",
     "开通5G的乡镇",
     "开通移动电话的行政村",
     "开通4G的行政村",
     "开通5G的行政村",
     "开通2G的行政村",
     "宽带网络覆盖",
     "宽带通达的地市",
     "有线宽带通达的地市",
     "宽带通达的县市",
     "有线宽带通达的县市",
     "宽带通达的乡镇",
     "有线宽带通达的乡镇",
     "市区区域通信能力",
     "市区基站数合计",
     "室外基站数量",
     "室内基站数量",
     "GSM基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-LTE基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "LTEFDD基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "5G基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "NB-IoT基站数量",
     "室外基站数量",
     "室内基站数量",
     "市区载频数合计",
     "GSM载频数",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "LTEFDD载频数",
     "5G载频数",
     "NB-IoT载频数",
     "市区GSM话音信道数",
     "县城城区区域通信能力",
     "县城城区基站数合计",
     "室外基站数量",
     "室内基站数量",
     "GSM基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-LTE基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "LTEFDD基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "5G基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "NB-IoT基站数量",
     "室外基站数量",
     "室内基站数量",
     "县城城区载频数合计",
     "GSM载频数",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "LTEFDD载频数",
     "5G载频数",
     "NB-IoT载频数",
     "县城城区GSM话音信道数",
     "农村区域通信能力",
     "农村基站数合计",
     "室外基站数量",
     "室内基站数量",
     "GSM基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-LTE基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "LTEFDD基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "5G基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "NB-IoT基站数量",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "农村GSM话音信道数",
     "农村载频数",
     "GSM载频数",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "LTEFDD载频数",
     "5G载频数",
     "NB-IoT载频数",
     "农村GSM话音信道数",
     "2G无线接入网承载的语音话务量（全速率）",
     "2G无线接入网承载的语音话务量（半速率）",
     "无线接入网承载的短信条数（包括上下行，2G与3G）",
     "2G无线接入网承载的GPRS折算话务量",
     "TD无线承载的语音话务量",
     "TD无线承载的移动数据流量业务流量",
     "CMNET承载总业务流量",
     "CMNET承载GPRS业务流量",
     "CMNET承载WLAN业务流量",
     "CMNET承载家庭宽带业务流量",
     "城域网下行流量",
     "完成建设的有线接入小区数量",
     "铁塔租赁",
     "自有铁塔数量",
     "租用铁塔数量",
     "租用地面塔数量",
     "租用普通地面塔数量",
     "租用景观塔数量",
     "租用简易塔数量",
     "租用楼面塔数量",
     "租用普通楼面塔数量",
     "租用楼面抱杆数量",
     "租用共享塔数量",
     "租用两家共享塔数量",
     "租用三家共享塔数量",
     "租用独享塔数量",
     "租赁铁塔公司铁塔数量情况",
     "租用铁塔公司铁塔数量",
     "租用铁塔公司地面塔数量",
     "租用铁塔公司普通地面塔数量",
     "租用铁塔公司景观塔数量",
     "租用铁塔公司简易塔数量",
     "租用铁塔公司楼面塔数量",
     "租用铁塔公司普通楼面塔数量",
     "租用铁塔公司楼面抱杆数量",
     "租用铁塔公司共享塔数量",
     "租用铁塔公司两家共享塔数量",
     "租用铁塔公司三家共享塔数量",
     "租用铁塔公司独享塔数量""核心网设备",
     "电路域",
     "MSC数量",
     "eMSC数量",
     "CSFBMSC数量",
     "MSC话务承载能力",
     "VLR数据库容量",
     "三融合HSS/HLR数量",
     "三融合HSS/HLR基础容量",
     "三融合HSS/HLR4G容量",
     "三融合HSS/HLRVoLTE容量",
     "分组域",
     "MME/SGSN数量",
     "MME/SGSN基础容量",
     "MME/SGSN4G容量",
     "SAE-GW/GGSN数量",
     "SAE-GW/GGSN基础容量",
     "SAE-GW/GGSN4G容量",
     "PCRF/SPR数量",
     "PCRF/SPR容量",
     "IMS域",
     "CM-IMS会话控制功能实体I/S/E-CSCF/BGCF数量",
     "CM-IMS会话控制功能实体I/S/E-CSCF/BGCF容量",
     "固网IMSHSS数量",
     "固网IMSHSS容量",
     "统一Centrex业务平台数量",
     "统一Centrex业务平台容量",
     "CM-IMS多媒体电话业务平台数量",
     "CM-IMS多媒体电话业务平台容量",
     "IMS/TD多媒体彩铃业务平台数量",
     "IMS/TD多媒体彩铃业务平台容量",
     "VoLTEAS数量",
     "VoLTEAS容量",
     "VoLTESBC数量",
     "VoLTESBC用户容量",
     "VoLTESBC话务承载能力",
     "GMSC和GMSC/MGCF/IM-MGW数量",
     "GMSC和GMSC/MGCF/IM-MGW基础容量",
     "GMSC和GMSC/MGCF/IM-MGWIP化容量",
     "GMSC/MGCF/IM-MGWMGCF容量",
     "纯MGCF/IM-MGW数量",
     "纯MGCF/IM-MGW容量",
     "固网SBC数量",
     "固网SBC用户容量",
     "VoLTE网络日均忙时话务量",
     "5G核心网",
     "AMF数量",
     "AMF5G容量",
     "SMF数量",
     "SMF5G容量",
     "两融合PCF/UDR数量",
     "两融合PCF/UDR容量",
     "四融合UDM/UDR数量",
     "四融合UDM/UDR基础容量",
     "四融合UDM/UDRVoLTE容量",
     "四融合UDM/UDR5G容量",
     "NSSF数量",
     "NSSF容量",
     "NRF数量",
     "NRF容量",
     "UPF数量",
     "UPF5G容量",
     "接入网设备",
     "GSM无线接入网",
     "GSM网BSC数",
     "GSM逻辑基站数",
     "GSM900逻辑基站数",
     "GSM1800逻辑基站数",
     "GSM逻辑室外宏基站数",
     "GSM逻辑室内分布基站数",
     "GSM物理基站数",
     "GSM物理宏基站数",
     "GSM900物理宏基站数",
     "GSM1800物理宏基站数",
     "GSM900与GSM1800共站址物理宏基站数",
     "GSM物理室内分布基站数",
     "GSM900室内分布基站数",
     "GSM1800室内分布基站数",
     "GSM900与GSM1800共站址室内分布基站数",
     "GSM小区数",
     "GSM1800小区数",
     "GSM载频数",
     "GSM1800载频数",
     "GSM话音信道数",
     "GSM1800话音信道数",
     "TD无线接入网",
     "TD-SCDMARNC数",
     "TD-SCDMA基站数",
     "宏基站数",
     "室内分布基站数",
     "TD-SCDMA小区数",
     "TD-SCDMA载频数",
     "WLAN",
     "WLANAC数",
     "WLANAP数",
     "完成覆盖的WLAN热点数",
     "TD-LTE",
     "TD-LTE基站数",
     "室外基站数",
     "室内基站数",
     "室外宏基站数",
     "室外微基站",
     "传统室分基站数",
     "分布式皮飞基站数",
     "TD-LTE一体化皮飞基站数",
     "TD-LTE载频数",
     "F频段载频数",
     "D频段载频数",
     "E频段载频数",
     "A频段载频数",
     "TD-LTE3D-MIMO载扇数",
     "TD-LTE物理小区数",
     "TD-LTE室外宏基站物理小区数",
     "TD-LTE室外微基站物理小区数",
     "TD-LTE室内分布基站物理小区数",
     "GSM无线接入网",
     "TD无线接入网",
     "TD-LTE",
     "WLAN",
     "LTEFDD",
     "LTEFDD逻辑基站数",
     "室外基站数",
     "室内基站数",
     "单LTEFDD900基站数",
     "室外基站数",
     "单LTEFDD900室外宏基站数",
     "单LTEFDD900室外微基站数",
     "室内分布基站数",
     "单LTEFDD900传统室分基站数",
     "单LTEFDD900分布式皮飞基站数",
     "单LTEFDD1800基站数",
     "室外基站数",
     "单LTEFDD1800室外宏基站数",
     "单LTEFDD1800室外微基站数",
     "室内分布基站数",
     "单LTEFDD1800传统室分基站数",
     "单LTEFDD1800分布式皮飞基站数",
     "LTEFDD900与LTEFDD1800共站址的基站数",
     "室外基站数",
     "LTEFDD900与LTEFDD1800共站址室外宏基站数",
     "LTEFDD900与LTEFDD1800共站址室外微基站数",
     "室内基站数",
     "LTEFDD900与LTEFDD1800共站址传统室分基站数",
     "LTEFDD900与LTEFDD1800共站址分布式皮飞基站数",
     "LTEFDD载频数",
     "LTEFDD1800载频数",
     "LTEFDD3D-MIMO载扇数",
     "LTEFDD小区数",
     "LTEFDD900室外宏基站小区数",
     "LTEFDD900室外微基站小区数",
     "LTEFDD900室内分布基站小区数",
     "LTEFDD1800室外宏基站小区数",
     "LTEFDD1800室外微基站小区数",
     "LTEFDD1800室内分布基站小区数",
     "开通eMTC小区数",
     "开通eMTC的900M室外小区数",
     "开通eMTC的900M室内小区数",
     "开通eMTC的1800M室外小区数",
     "开通eMTC的1800M室内小区数",
     "NB-IoT",
     "开通NB-IoT基站数",
     "室外基站数",
     "室内基站数",
     "NB-IoT载频数",
     "NB-IoT小区数",
     "5G",
     "5G逻辑基站数",
     "室外基站数",
     "室外宏基站数",
     "2.6GHz室外宏基站数",
     "4.9GHz室外宏基站数",
     "室外微基站数",
     "2.6GHz室外微基站数",
     "4.9GHz室外微基站数",
     "室内逻辑基站数",
     "传统室内基站数",
     "分布式皮飞基站数",
     "扩展型皮基站数",
     "5G载频数",
     "室外宏基站载频数",
     "2.6GHz室外宏基站载频数",
     "4.9GHz室外宏基站载频数",
     "室外微基站载频数",
     "2.6GHz室外微基站载频数",
     "4.9GHz室外微基站载频数",
     "室内覆盖载频数",
     "物理站址资源",
     "总物理站址数",
     "室外覆盖物理站址数",
     "室内覆盖物理站址数",
     "自有物理站址数",
     "宽带能力指标",
     "PON端口",
     "PON端口数量",
     "EPON端口数量",
     "GPON端口数量",
     "XG(S)-PON端口数量",
     "用于家庭宽带业务接入的PON端口数量",
     "采用FTTH模式开通的PON端口数量",
     "采用1:64/2:64总分光的PON端口数量",
     "采用1:32/2:32总分光的PON端口数量",
     "采用FTTB模式开通的PON端口数量",
     "ONU设备",
     "ONU设备数量",
     "GPON/EPONONU设备数量",
     "FTTB场景ONU设备数量",
     "用于家宽接入的FTTB场景ONU设备数量",
     "SFU设备数量",
     "用于家宽接入的SFU设备数量",
     "HGU设备数量",
     "用于家宽接入的HGU设备数量",
     "智能家庭网关设备数量",
     "用于家宽接入的智能家庭网关设备数量",
     "XG(S)-PONONU设备数量",
     "FTTB场景ONU设备数量",
     "用于家宽接入的FTTB场景ONU设备数量",
     "智能家庭网关设备数量",
     "用于家宽接入的智能家庭网关设备数量",
     "OLT设备数量",
     "宽带接入端口",
     "有线宽带接入端口",
     "xDSL端口",
     "FTTB端口",
     "FTTH/O端口",
     "WBS端口",
     "城市地区接入端口",
     "xDSL端口",
     "FTTB端口",
     "FTTH/O端口",
     "WBS端口",
     "50M以上城市宽带接入端口",
     "100M以上城市宽带接入端口",
     "农村地区接入端口",
     "xDSL端口",
     "FTTB端口",
     "FTTH/O端口",
     "WBS端口",
     "20M以上农村宽带接入端口",
     "100M以上农村宽带接入端口",
     "家庭宽带接入端口数",
     "xDSL端口",
     "FTTB端口",
     "已开通家庭宽带业务的FTTBONU端口数量",
     "使用XG(S)-PON技术的FTTB端口数",
     "已开通家庭宽带业务的XG(S)-PON技术的FTTB端口数",
     "FTTH/O端口",
     "已开通家庭宽带业务的FTTH光分路器端口数量",
     "使用XG(S)-PON技术的FTTH光分路器端口数",
     "已开通家庭宽带业务的XG(S)-PON技术的FTTH光分路器端口数",
     "WBS端口",
     "分纤点",
     "光纤分纤点数量",
     "其他：城区一级分纤点数量",
     "城区二级分纤点数量",
     "非城区一级分纤点数量",
     "非城区二级分纤点数量",
     "宽带接入速率",
     "全省有线宽带用户总接入带宽",
     "全省家庭宽带用户总接入带宽",
     "计划单列市和省会城市总接入带宽",
     "计划单列市和省会城市家庭宽带总接入带宽",
     "核心网设备",
     "CMN数量",
     "CMN处理能力",
     "长途Diameter信令网HDRA数量",
     "长途Diameter信令网DRA处理能力",
     "省内Diameter信令网LDRA数量",
     "省内Diameter信令网LDRA处理能力",
     "省内Diameter信令网LDRA会话绑定消息处理能力",
     "长途七号信令网HSTP数量",
     "长途七号信令网HSTP等效2M链路数",
     "省内七号信令网LSTP数量",
     "省内七号信令网LSTP等效2M链路数",
     "业务网设备",
     "业务平台",
     "短消息中心数量",
     "短消息中心处理能力",
     "短消息中心平时实际峰值处理业务量",
     "短消息中心节假日实际峰值处理业务量",
     "彩信中心处理能力",
     "彩信中心实际峰值处理业务量",
     "智能网",
     "智能业务控制节点SCP数量",
     "智能业务控制节点SCP硬件能力",
     "智能业务控制节点SCP用户容量",
     "智能业务控制节点SCPAS数量",
     "智能业务控制节点SCPAS硬件能力",
     "智能业务控制节点SCPAS用户容量",
     "智能业务管理点SMP数量",
     "智能网充值中心VC数量",
     "智能网充值中心VC容量",
     "IT基础设施",
     "企业私有云资源池服务器台数",
     "企业私有云资源池存储容量",
     "公众服务云资源池服务器台数",
     "公众服务云资源池存储容量",
     "内容分发网络",
     "边缘服务节点数量",
     "边缘服务节点总容量",
     "统一DPI设备",
     "互联网统一DPI覆盖规模",
     "4G/5G上网日志留存系统容量",
     "数据承载网",
     "CMNET城域网出口带宽",
     "CMNET城域网业务接入控制层设备配置等效GE端口数",
     "IP专网AR上连BR带宽",
     "IP专网AR设备配置等效GE端口数",
     "IP专网CE设备台数",
     "互联网省际出口带宽",
     "CMNET省网出口带宽",
     "CMNET省网第三方出口带宽",
     "核心网设备",
     "业务网设备",
     "数据承载网",
     "传送网",
     "杆路线路长度",
     "自有",
     "租用",
     "租用电信杆路线路长度",
     "租用联通杆路线路长度",
     "租用杆路费用",
     "租用电信杆路费用",
     "租用联通杆路费用",
     "直埋光缆线路长度",
     "自有",
     "租用",
     "租用电信直埋光缆线路长度",
     "租用联通直埋光缆线路长度",
     "租用直埋光缆费用",
     "租用电信直埋光缆费用",
     "租用联通直埋光缆费用",
     "管道线路长度",
     "自有",
     "租用",
     "租用电信管道线路长度",
     "租用联通管道线路长度",
     "租用管道线路费用",
     "租用电信管道线路费用",
     "租用联通管道线路费用",
     "敷设自有管道的市政道路长度",
     "传送网合计",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "省际骨干传送网",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆线路长度",
     "光缆长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "省内骨干传送网",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆线路长度",
     "光缆长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "传送网",
     "光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "波分复用系统长度",
     "10Gb/s同步数字系列设备套数",
     "2.5Gb/s同步数字系列设备套数",
     "622Mb/s及以下同步数字系列设备套数",
     "10GEPTN设备套数",
     "40GEPTN设备套数",
     "100GEPTN设备套数",
     "2.5G线路侧端口数量",
     "10G线路侧端口数量",
     "40G线路侧端口数量",
     "100G线路侧端口数量",
     "2.5G支路侧端口数量",
     "10G支路侧端口数量",
     "40G支路侧端口数量",
     "100G支路侧端口数量",
     "城域网",
     "管道长度",
     "租用管道长度",
     "租用电信管道长度",
     "租用联通管道长度",
     "光缆线路长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "引入光缆线路长度",
     "租用光缆线路长度",
     "光缆长度",
     "管道光缆长度",
     "直埋光缆长度",
     "架空光缆长度",
     "引入光缆长度",
     "租用光缆长度",
     "租用电信光缆长度",
     "租用联通光缆长度",
     "光缆纤芯长度",
     "引入光缆纤芯长度",
     "租用光缆纤芯长度",
     "租用电信光缆纤芯长度",
     "租用联通光缆纤芯长度",
     "已占用纤芯长度",
     "已占用引入光缆纤芯长度",
     "租用管道费用",
     "租用电信管道费用",
     "租用联通管道费用",
     "租用光缆费用",
     "租用电信光缆费用",
     "租用联通光缆费用",
     "租用光缆纤芯费用",
     "租用电信光缆纤芯费用",
     "租用联通光缆纤芯费用",
     "10Gb/s同步数字系列设备套数",
     "2.5Gb/s同步数字系列设备套数",
     "622Mb/s以下同步数字系列设备套数",
     "PTN设备总数量",
     "GEPTN设备数量",
     "10GEPTN设备数量",
     "40GEPTN设备套数",
     "100GEPTN设备套数",
     "2.5G线路侧端口数量",
     "10G线路侧端口数量",
     "40G线路侧端口数量",
     "100G线路侧端口数量",
     "传送网",
     "SDH：2Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "155Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "2.5Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "10Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "租用电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "租用电信",
     "租用联通",
     "城域网内电路",
     "租用电信",
     "租用联通",
     "电路租费",
     "租用省内长途电路费用",
     "租用电信费用",
     "租用联通费用",
     "租用城域网内电路费用",
     "租用电信费用",
     "租用联通费用",
     "1Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "2.5Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "10Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "100Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "2Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "155Mbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "2.5Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "10Gbps",
     "自建传输系统已开放电路",
     "国际及港澳台电路",
     "省际电路",
     "省内长途电路",
     "省内本地/城域网内电路",
     "合建电路",
     "混合电路",
     "传输电路",
     "分布系统情况",
     "室内分布系统物业点数",
     "分布式皮飞物业点数",
     "室分系统覆盖面积",
     "分布式皮飞基站覆盖面积",
     "高铁覆盖情况",
     "4G覆盖高铁线路数",
     "4G覆盖高铁线路里程",
     "4G高铁基站数",
     "TD-LTE高铁基站数",
     "LTEFDD高铁基站数",
     "4G高铁载频数",
     "TD-LTE高铁载频数",
     "LTEFDD高铁载频数",
     "4G高铁物理基站数",
     "2G高铁基站数",
     "GSM900M高铁基站数",
     "GSM1800M高铁基站数",
     "5G覆盖高铁线路数",
     "5G覆盖高铁线路里程",
     "5G高铁逻辑基站数",
     "5G高铁载频数",
     "5G高铁物理基站数",
     "汇聚机房",
     "汇聚机房数量",
     "城区汇聚机房数量",
     "自有城区汇聚机房数量",
     "非城区汇聚机房数量",
     "自有非城区汇聚机房数量",
     "重要汇聚机房数量",
     "城区重要汇聚机房数量",
     "城区自有重要汇聚机房数量",
     "非城区重要汇聚机房数量",
     "非城区自有重要汇聚机房数量",
     "普通汇聚机房数量",
     "城区普通汇聚机房数量",
     "城区自有普通汇聚机房数量",
     "非城区普通汇聚机房数量",
     "非城区自有普通汇聚机房数量",
     "业务汇聚机房数量",
     "城区业务汇聚机房数量",
     "城区自有业务汇聚机房数量",
     "非城区业务汇聚机房数量",
     "非城区自有业务汇聚机房数量",
     "开通移动电话的地市",
     "开通4G的地市",
     "开通5G的地市",
     "开通移动电话的县市",
     "开通4G的县市",
     "开通5G的县市",
     "开通移动电话的乡镇",
     "开通4G的乡镇",
     "开通5G的乡镇",
     "开通移动电话的行政村",
     "开通4G的行政村",
     "开通5G的行政村",
     "开通2G的行政村",
     "宽带网络覆盖",
     "宽带通达的地市",
     "有线宽带通达的地市",
     "宽带通达的县市",
     "有线宽带通达的县市",
     "宽带通达的乡镇",
     "有线宽带通达的乡镇",
     "市区区域通信能力",
     "市区基站数合计",
     "室外基站数量",
     "室内基站数量",
     "GSM基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-LTE基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "LTEFDD基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "5G基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "NB-IoT基站数量",
     "室外基站数量",
     "室内基站数量",
     "市区载频数合计",
     "GSM载频数",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "LTEFDD载频数",
     "5G载频数",
     "NB-IoT载频数",
     "市区GSM话音信道数",
     "县城城区区域通信能力",
     "县城城区基站数合计",
     "室外基站数量",
     "室内基站数量",
     "GSM基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-LTE基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "LTEFDD基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "5G基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "NB-IoT基站数量",
     "室外基站数量",
     "室内基站数量",
     "县城城区载频数合计",
     "GSM载频数",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "LTEFDD载频数",
     "5G载频数",
     "NB-IoT载频数",
     "县城城区GSM话音信道数",
     "农村区域通信能力",
     "农村基站数合计",
     "室外基站数量",
     "室内基站数量",
     "GSM基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA基站数",
     "室外基站数量",
     "室内基站数量",
     "TD-LTE基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "LTEFDD基站数",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "5G基站数量",
     "室外基站数量",
     "室外宏基站数量",
     "室外微基站数量",
     "室内基站数量",
     "NB-IoT基站数量",
     "室外基站数量",
     "室内基站数量",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "农村GSM话音信道数",
     "农村载频数",
     "GSM载频数",
     "TD-SCDMA载频数",
     "TD-LTE载频数",
     "LTEFDD载频数",
     "5G载频数",
     "NB-IoT载频数",
     "农村GSM话音信道数",
     "2G无线接入网承载的语音话务量（全速率）",
     "2G无线接入网承载的语音话务量（半速率）",
     "无线接入网承载的短信条数（包括上下行，2G与3G）",
     "2G无线接入网承载的GPRS折算话务量",
     "TD无线承载的语音话务量",
     "TD无线承载的移动数据流量业务流量",
     "CMNET承载总业务流量",
     "CMNET承载GPRS业务流量",
     "CMNET承载WLAN业务流量",
     "CMNET承载家庭宽带业务流量",
     "城域网下行流量",
     "完成建设的有线接入小区数量",
     "铁塔租赁",
     "自有铁塔数量",
     "租用铁塔数量",
     "租用地面塔数量",
     "租用普通地面塔数量",
     "租用景观塔数量",
     "租用简易塔数量",
     "租用楼面塔数量",
     "租用普通楼面塔数量",
     "租用楼面抱杆数量",
     "租用共享塔数量",
     "租用两家共享塔数量",
     "租用三家共享塔数量",
     "租用独享塔数量",
     "租赁铁塔公司铁塔数量情况",
     "租用铁塔公司铁塔数量",
     "租用铁塔公司地面塔数量",
     "租用铁塔公司普通地面塔数量",
     "租用铁塔公司景观塔数量",
     "租用铁塔公司简易塔数量",
     "租用铁塔公司楼面塔数量",
     "租用铁塔公司普通楼面塔数量",
     "租用铁塔公司楼面抱杆数量",
     "租用铁塔公司共享塔数量",
     "租用铁塔公司两家共享塔数量",
     "租用铁塔公司三家共享塔数量",
     "租用铁塔公司独享塔数量"]
beaut_word = []


def get_word(s):
    resu = re.search(r"(([a-zA-Z0-9|\(*|\)*｜\.*]+)(/|-)*)+", s)
    if resu != None and resu.group() != None and resu.group().strip() != "":
        beaut_word.append(resu.group())
        return get_word(s.replace(resu.group(), ""))
    else:
        return s

for k,v in enumerate(a):
     a[k]=get_word(v)
print(beaut_word)
print("---")
print(a)
