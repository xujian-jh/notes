# 发布前后涉及的数据表

分解：
1.ud_erp_order_interface中is_split(是否分解)写是（1）；
2.uda_order表中status 写0；
排程：
1.uda_order表中status 写1；
发布：
1.uda_order表中status 写4；
2.初始化holdcode  ud_mes_qm_holdCodeCar表中插入新数据。
3.向VIN打刻发布车辆信息： vehicle_model_parameter表中插入新数据；
总计：
1.ud_erp_order_interface中is_split 订单接口表；
2.uda_order 单车计划表
3.ud_mes_qm_holdCodeCar holdcode验证表
4.vehicle_model_parameter vin打刻记录表

就查这4个表，涉及到的这些vin码信息都删掉就行
