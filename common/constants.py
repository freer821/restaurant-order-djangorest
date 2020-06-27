from config.settings import ALLOWED_HOSTS

HOST_URL = 'http://'+ALLOWED_HOSTS[0]

sys_template = {
    'regist_email_content': '恭喜您注册成功， 请复制链接到浏览器上来激活邮箱 ：'+ HOST_URL +'/regist?activate_code=',
}
