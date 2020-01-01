from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.sms.v20190711 import sms_client, models
import random
import json


def send_sms(telephone, captcha):
        cred = credential.Credential("AKIDb0A8qIqRkpfFYczD7lCNuC8pGRL0bnIX", "81hBOK0TDixNZVDgIgxxjGWUC9rISMhm")
        http_profile = HttpProfile()
        http_profile.endpoint = "sms.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client = sms_client.SmsClient(cred, "", client_profile)

        req = models.SendSmsRequest()

        params = '{"PhoneNumberSet":["+86%s"],"TemplateID":"511960","Sign":"chaobbstop网站","TemplateParamSet":["%s"],"SmsSdkAppid":"1400302167"}' % (telephone,captcha)
        req.from_json_string(params)
        resp = client.SendSms(req)
        result = json.loads(resp.to_json_string())["SendStatusSet"][0]["Code"]
        if result == "Ok":
            return True
        else:
            return False


def generate_captcha(number = 6):
    captcha = ''
    for i in range(number):
        now_number = str(random.randint(0, 9))
        captcha += now_number
    return captcha


if __name__ == '__main__':
    send_sms(15201403874, generate_captcha())