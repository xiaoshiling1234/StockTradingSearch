CREATE DATABASE crawler;
use crawler;
create table LonghuTHSItem(
code varchar(10) comment '股票代码',
name varchar(255) comment '股票名称',
href varchar(255) comment '股票链接',
price varchar(20) comment '现价',
price_change_rate varchar(20) comment '涨跌幅',
trading_volume varchar(20) comment '成交金额',
purchases varchar(20) comment '净买入额',
date varchar(20) comment '数据日期'
);

create table LonghuTop5THSItem(
code varchar(10) comment '股票代码',
title varchar(20) comment '标题',
fund_company varchar(255) comment '基金公司名称',
fund_company_href varchar(255) comment '基金公司链接',
purchases varchar(20) comment '买入额/万',
sell varchar(20) comment '卖出额/万',
net_amount varchar(20) comment '净额/万',
date varchar(20) comment '数据日期'
);

-- create table company_his(
-- code varchar(10) comment '股票代码',
-- `date` varchar(20) comment '日期',
-- `open` double comment '开盘价',
-- `high` double comment '最高价',
-- `close` double comment '收盘价',
-- `low` double comment '最低价',
-- `volume` double comment '成交量',
-- `price_change` double comment '价格变动',
-- `p_change` double comment '涨跌幅',
-- `ma5` double comment '5日均价',
-- `ma10` double comment '10日均价',
-- `ma20` double comment '20日均价',
-- `v_ma5` double comment '5日均量',
-- `v_ma10` double comment '10日均量',
-- `v_ma20` double comment '20日均量',
-- `turnover` double comment '换手率'
-- )comment '股票历史价格';