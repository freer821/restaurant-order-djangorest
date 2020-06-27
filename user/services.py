from logging import getLogger

import jwt
from django.contrib.auth.models import User

from common.constants import sys_template
from common.utils import sendEmail


def sendActiveEmail(username):
    encoded = jwt.encode({'username': username}, 'secret', algorithm='HS256')
    html_content = sys_template['regist_email_content']+encoded.decode("utf-8")
    sendEmail('邮箱验证', html_content, username)
    getLogger().info(username+":"+html_content)


def sendNewPassw(email, newpassw):
    html_content = '用户名：'+ email + ',  新密码：'+newpassw
    sendEmail('密码重置', html_content, email)
    getLogger().info((email+":"+html_content).encode("utf-8"))


def activate_user_handle(activate_code):
    decode = jwt.decode(activate_code, 'secret', algorithms=['HS256'])
    user = User.objects.filter(username=decode['username']).first()
    if user is not None:
        user.is_active = True
        user.save()
