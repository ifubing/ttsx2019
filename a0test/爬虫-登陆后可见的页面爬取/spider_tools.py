def parse_header(header):
    """
    把请求头字符串转换为字典
    :param header: 复制过来的请求头字符串
    :return:
    """
    # 按照：分割，左边是键，右边是值
    header_key, header_val = header.split(':')
    return {header_key.strip(): header_val.strip()}

if __name__ == '__main__':
    str_cookie = """cookie: uuid_tt_dd=10_28743412270-1569723942844-420746; dc_session_id=10_1569723942844.879679; UserName=ifubing; UserInfo=e72ddbe6095f4d70b8d33a74c9083818; UserToken=e72ddbe6095f4d70b8d33a74c9083818; UserNick=ifubing; AU=94D; UN=ifubing; BT=1569723985205; p_uid=U000000; notice=1; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=5744*1*ifubing!6525*1*10_28743412270-1569723942844-420746!1788*1*PC_VC; smidV2=20191005134300f5230bb3cc5b208784317f4b583725d400ed78b71e2634350; aliyun_webUmidToken=T0E516205D4129D3EC233C6038E6A436F9D6858BCC3C1A47F51F930CCB6; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1570254184,1570254379,1570262953,1570263365; TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2Fmdeditor%22%2C%22tid%22%3A%22fd405a8b6c0f54%22%2C%22q%22%3A0%2C%22a%22%3A79%7D; dc_tos=pywf5w; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1570273988"""
    r = parse_header(str_cookie)
    print(r)
