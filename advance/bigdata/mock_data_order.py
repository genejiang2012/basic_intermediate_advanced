#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8


from faker import Faker,Factory
from faker.providers import internet,profile,user_agent,phone_number,barcode
import sys
import random
import datetime
import urllib3
import hashlib
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
from multiprocessing import Pool
sys.setdefaultencoding('utf-8')
faker = Faker(locale='zh_CN')
browsers = ['Chrome','FireFox','Internet Explorer','BaiDu','Other','Opera','Safari','SouGou','UC',' Microsoft Edge','QQ']
genders = ['男','女','未知']
medias = ['display','video']
device_types = ['PC','Mobile','Other']
province_list = ['北京市', '天津市', '上海市', '重庆市', '河南省', '安徽省', '福建省', '甘肃省', '贵州省', '海南省', '河北省', '黑龙江省', '湖北省', '湖南省', '吉林省', '江苏省', '江西省', '辽宁省', '青海省', '山东省', '山西省', '陕西省', '四川省', '云南省', '浙江省', '台湾省', '广东省', '广西壮族自治区', '内蒙古自治区', '宁夏回族自治区', '西藏藏族自治区', '新疆维吾尔自治区', '香港', '澳门']
province_city = {
    '北京市': ['北京市'],
    '天津市': ['天津市'],
    '上海市': ['上海市'],
    '重庆市': ['重庆市'],
    '河南省': ['郑州市', '洛阳市', '焦作市', '商丘市', '信阳市', '周口市', '鹤壁市', '安阳市', '濮阳市', '驻马店市', '南阳市', '开封市', '漯河市', '许昌市', '新乡市', '济源市', '灵宝市', '偃师市', '邓州市', '登封市', '三门峡市', '新郑市', '禹州市', '巩义市', '永城市', '长葛市', '义马市', '林州市', '项城市', '汝州市', '荥阳市', '平顶山市', '卫辉市', '辉县市', '舞钢市', '新密市', '孟州市', '沁阳市', '郏县'],
    '安徽省': ['合肥市', '亳州市', '芜湖市', '马鞍山市', '池州市', '黄山市', '滁州市', '安庆市', '淮南市', '淮北市', '蚌埠市', '宿州市', '宣城市', '六安市', '阜阳市', '铜陵市', '明光市', '天长市', '宁国市', '界首市', '桐城市'],
    '福建省': ['福州市', '厦门市', '泉州市', '漳州市', '南平市', '三明市', '龙岩市', '莆田市', '宁德市', '建瓯市', '武夷山市', '长乐市', '福清市', '晋江市', '南安市', '福安市', '龙海市', '邵武市', '石狮市', '福鼎市', '建阳市', '漳平市', '永安市'],
    '甘肃省': ['兰州市', '白银市', '武威市', '金昌市', '平凉市', '张掖市', '嘉峪关市', '酒泉市', '庆阳市', '定西市', '陇南市', '天水市', '玉门市', '临夏市', '合作市', '敦煌市', '甘南州'],
    '贵州省': ['贵阳市', '安顺市', '遵义市', '六盘水市', '兴义市', '都匀市', '凯里市', '毕节市', '清镇市', '铜仁市', '赤水市', '仁怀市', '福泉市'],
    '海南省': ['海口市', '三亚市', '万宁市', '文昌市', '儋州市', '琼海市', '东方市', '五指山市'],
    '河北省': ['石家庄市', '保定市', '唐山市', '邯郸市', '邢台市', '沧州市', '衡水市', '廊坊市', '承德市', '迁安市', '鹿泉市', '秦皇岛市', '南宫市', '任丘市', '叶城市', '辛集市', '涿州市', '定州市', '晋州市', '霸州市', '黄骅市', '遵化市', '张家口市', '沙河市', '三河市', '冀州市', '武安市', '河间市', '深州市', '新乐市', '泊头市', '安国市', '双滦区', '高碑店市'],
    '黑龙江省': ['哈尔滨市', '伊春市', '牡丹江市', '大庆市', '鸡西市', '鹤岗市', '绥化市', '齐齐哈尔市', '黑河市', '富锦市', '虎林市', '密山市', '佳木斯市', '双鸭山市', '海林市', '铁力市', '北安市', '五大连池市', '阿城市', '尚志市', '五常市', '安达市', '七台河市', '绥芬河市', '双城市', '海伦市', '宁安市', '讷河市', '穆棱市', '同江市', '肇东市'],
    '湖北省': ['武汉市', '荆门市', '咸宁市', '襄阳市', '荆州市', '黄石市', '宜昌市', '随州市', '鄂州市', '孝感市', '黄冈市', '十堰市', '枣阳市', '老河口市', '恩施市', '仙桃市', '天门市', '钟祥市', '潜江市', '麻城市', '洪湖市', '汉川市', '赤壁市', '松滋市', '丹江口市', '武穴市', '广水市', '石首市', '大冶市', '枝江市', '应城市', '宜城市', '当阳市', '安陆市', '宜都市', '利川市'],
    '湖南省': ['长沙市', '郴州市', '益阳市', '娄底市', '株洲市', '衡阳市', '湘潭市', '岳阳市', '常德市', '邵阳市', '永州市', '张家界市', '怀化市', '浏阳市', '醴陵市', '湘乡市', '耒阳市', '沅江市', '涟源市', '常宁市', '吉首市', '津市市', '冷水江市', '临湘市', '汨罗市', '武冈市', '韶山市', '湘西州'],
    '吉林省': ['长春市', '吉林市', '通化市', '白城市', '四平市', '辽源市', '松原市', '白山市', '集安市', '梅河口市', '双辽市', '延吉市', '九台市', '桦甸市', '榆树市', '蛟河市', '磐石市', '大安市', '德惠市', '洮南市', '龙井市', '珲春市', '公主岭市', '图们市', '舒兰市', '和龙市', '临江市', '敦化市'],
    '江苏省': ['南京市', '无锡市', '常州市', '扬州市', '徐州市', '苏州市', '连云港市', '盐城市', '淮安市', '宿迁市', '镇江市', '南通市', '泰州市', '兴化市', '东台市', '常熟市', '江阴市', '张家港市', '通州市', '宜兴市', '邳州市', '海门市', '溧阳市', '泰兴市', '如皋市', '昆山市', '启东市', '江都市', '丹阳市', '吴江市', '靖江市', '扬中市', '新沂市', '仪征市', '太仓市', '姜堰市', '高邮市', '金坛市', '句容市', '灌南县'],
    '江西省': ['南昌市', '赣州市', '上饶市', '宜春市', '景德镇市', '新余市', '九江市', '萍乡市', '抚州市', '鹰潭市', '吉安市', '丰城市', '樟树市', '德兴市', '瑞金市', '井冈山市', '高安市', '乐平市', '南康市', '贵溪市', '瑞昌市', '东乡县', '广丰县', '信州区', '三清山'],
    '辽宁省': ['沈阳市', '葫芦岛市', '大连市', '盘锦市', '鞍山市', '铁岭市', '本溪市', '丹东市', '抚顺市', '锦州市', '辽阳市', '阜新市', '调兵山市', '朝阳市', '海城市', '北票市', '盖州市', '凤城市', '庄河市', '凌源市', '开原市', '兴城市', '新民市', '大石桥市', '东港市', '北宁市', '瓦房店市', '普兰店市', '凌海市', '灯塔市', '营口市'],
    '青海省': ['西宁市', '格尔木市', '德令哈市'],
    '山东省': ['济南市', '青岛市', '威海市', '潍坊市', '菏泽市', '济宁市', '莱芜市', '东营市', '烟台市', '淄博市', '枣庄市', '泰安市', '临沂市', '日照市', '德州市', '聊城市', '滨州市', '乐陵市', '兖州市', '诸城市', '邹城市', '滕州市', '肥城市', '新泰市', '胶州市', '胶南市', '即墨市', '龙口市', '平度市', '莱西市'],
    '山西省': ['太原市', '大同市', '阳泉市', '长治市', '临汾市', '晋中市', '运城市', '忻州市', '朔州市', '吕梁市', '古交市', '高平市', '永济市', '孝义市', '侯马市', '霍州市', '介休市', '河津市', '汾阳市', '原平市', '潞城市'],
    '陕西省': ['西安市', '咸阳市', '榆林市', '宝鸡市', '铜川市', '渭南市', '汉中市', '安康市', '商洛市', '延安市', '韩城市', '兴平市', '华阴市'],
    '四川省': ['成都市', '广安市', '德阳市', '乐山市', '巴中市', '内江市', '宜宾市', '南充市', '都江堰市', '自贡市', '泸州市', '广元市', '达州市', '资阳市', '绵阳市', '眉山市', '遂宁市', '雅安市', '阆中市', '攀枝花市', '广汉市', '绵竹市', '万源市', '华蓥市', '江油市', '西昌市', '彭州市', '简阳市', '崇州市', '什邡市', '峨眉山市', '邛崃市', '双流县'],
    '云南省': ['昆明市', '玉溪市', '大理市', '曲靖市', '昭通市', '保山市', '丽江市', '临沧市', '楚雄市', '开远市', '个旧市', '景洪市', '安宁市', '宣威市'],
    '浙江省': ['杭州市', '宁波市', '绍兴市', '温州市', '台州市', '湖州市', '嘉兴市', '金华市', '舟山市', '衢州市', '丽水市', '余姚市', '乐清市', '临海市', '温岭市', '永康市', '瑞安市', '慈溪市', '义乌市', '上虞市', '诸暨市', '海宁市', '桐乡市', '兰溪市', '龙泉市', '建德市', '富德市', '富阳市', '平湖市', '东阳市', '嵊州市', '奉化市', '临安市', '江山市'],
    '台湾省': ['台北市', '台南市', '台中市', '高雄市', '桃源市'],
    '广东省': ['广州市', '深圳市', '珠海市', '汕头市', '佛山市', '韶关市', '湛江市', '肇庆市', '江门市', '茂名市', '惠州市', '梅州市', '汕尾市', '河源市', '阳江市', '清远市', '东莞市', '中山市', '潮州市', '揭阳市', '云浮市'],
    '广西壮族自治区': ['南宁市', '贺州市', '玉林市', '桂林市', '柳州市', '梧州市', '北海市', '钦州市', '百色市', '防城港市', '贵港市', '河池市', '崇左市', '来宾市', '东兴市', '桂平市', '北流市', '岑溪市', '合山市', '凭祥市', '宜州市'],
    '内蒙古自治区': ['呼和浩特市', '呼伦贝尔市', '赤峰市', '扎兰屯市', '鄂尔多斯市', '乌兰察布市', '巴彦淖尔市', '二连浩特市', '霍林郭勒市', '包头市', '乌海市', '阿尔山市', '乌兰浩特市', '锡林浩特市', '根河市', '满洲里市', '额尔古纳市', '牙克石市', '临河市', '丰镇市', '通辽市'],
    '宁夏回族自治区': ['银川市', '固原市', '石嘴山市', '青铜峡市', '中卫市', '吴忠市', '灵武市'],
    '西藏藏族自治区': ['拉萨市', '日喀则市'],
    '新疆维吾尔自治区': ['乌鲁木齐市', '石河子市', '喀什市', '阿勒泰市', '阜康市', '库尔勒市', '阿克苏市', '阿拉尔市', '哈密市', '克拉玛依市', '昌吉市', '奎屯市', '米泉市', '和田市'],
    '香港': ['香港'],
    '澳门': ['澳门']
}
campaigns = ['CC80013','CC80012','CC80011','CC80014','CC80015','CC80016','CC80017','CC80018','CC80019','CC80020','CC80021','CC80022','CC80023','CC80024']
order_status_list = ['用户拒收','未付款的订单','用户取消','待发货','配送中','确认收货']
pay_level_list = ['低级','中级','高级','钻石']
pay_from_list = ['支付宝','微信','银联','其他']
is_appraise_list = ['未点评','已点评']
appraise_level_list = ['一星','两星','三星','四星','五星']
deliver_companies = ['中通','圆通','顺丰','EMS','韵达','申通','百世汇通','其他']
http = urllib3.PoolManager()
def mock_user(seq,dt):
    print('step into profile............')
    for cycle in range(0,100):
        user_profile = []
        for num in range(0,50):
            faker.add_provider(barcode)
            user_id = faker.ean13()
            user_name = faker.name()
            address = faker.address()
            sex = genders[random.randint(0,2)]
            email = faker.email()
            phone = faker.phone_number()
            profile = faker.profile(fields=None, sex=None)
            birthdate = str(profile['birthdate'])
            ssn = faker.ssn()
            job = faker.job()
            user_profile.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (seq,user_id,user_name,address,sex,email,phone,birthdate,ssn,job,dt))
            seq = seq + 1
        f = open('test_profile_%s.csv' % dt, 'a+')
        f.write('\n'+'\n'.join(user_profile))
        f.close()


def mock_tracking(seq,dt):
    for cycle in range(0,100):
        user_tracking = []
        for num in range(0, 10):
            mac = faker.mac_address().replace(':', '')
            mac_md5 = hashlib.md5(mac.encode()).hexdigest()
            ip = faker.ipv4_public()
            tracking_url = faker.url(schemes=None)
            uri_extension = faker.uri_extension()[1:]
            media_type  = medias[random.randint(0,1)]
            device_type = device_types[random.randint(0,2)]
            campaign = campaigns[random.randint(0,13)]
            province = province_list[random.randint(0,33)]
            length = len(province_city[province])
            city = province_city[province][random.randint(0,length-1)]
            user_tracking.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (seq,mac,mac_md5,ip,tracking_url,uri_extension,media_type,device_type,campaign,province,city,dt))
            seq = seq + 1
    f = open('test2.txt', 'a+')
    f.write('\n'+'\n'.join(user_tracking))

def mock_order(seq,dt,row_cnt):
    print('step into order.........')
    with open('/home/dataservice/workspace/mock/result/seq/order/2019/test_order_%s.csv' % dt, 'w') as f:
        for num in range(1, row_cnt + 1):
            order_id = faker.ean13()
            order_status = order_status_list[random.randint(0,5)]
            pay_level = pay_level_list[random.randint(0,3)]
            pay_from = pay_from_list[random.randint(0,3)]
            is_appraise = is_appraise_list[random.randint(0,1)]
            if is_appraise == '未点评':
                appraise_level = is_appraise
            else :
                appraise_level  = appraise_level_list[random.randint(0,4)]
            deliver_company = deliver_companies[random.randint(0,7)]
            province = province_list[random.randint(0,33)]
            length = len(province_city[province])
            city = province_city[province][random.randint(0,length-1)]
            order_time = faker.past_datetime(start_date="-60d", tzinfo=None)
            seq = random.randint(0,2000000)
            f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' %  (seq,order_id,order_status,pay_level,pay_from,is_appraise,appraise_level,deliver_company,province,city,order_time,dt))
            seq += 1
            if num % 10000 == 0:
                f.flush()

if __name__ == "__main__":
    start_dt = datetime.datetime(2019, 01, 01)
    total = int(sys.argv[1])
    page_size = int(sys.argv[2])
    p = Pool((int(total) // int(page_size)) + 1)
    print("start")
    for index, i in enumerate(range(0, total, page_size)):
        delta = datetime.timedelta(days=index)
        t_str = (delta + start_dt).strftime("%Y-%m-%d")
        p.apply_async(mock_order,(i + 1,t_str, page_size))
        print("mock_order, params:%s,%s,%s" % (t_str, i + 1, page_size))
    p.close()
    p.join()
    print("finish")






