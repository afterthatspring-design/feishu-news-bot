import requests
import datetime

APP_ID = "cli_a945f08b2c611cd2"
APP_SECRET = "XSHiz00HzeiN4xqFtjwVMbJ8EkNExlpp"
CHAT_ID = "oc_bf1cf0b695aa6eccaac36b45538b6c99"

def handler(request):
    # 获取 token
    res = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": APP_ID, "app_secret": APP_SECRET}
    )
    token = res.json()["tenant_access_token"]

    # 构造消息
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    text = f"📰 测试消息 {today}"

    # 发送到飞书群
    requests.post(
        "https://open.feishu.cn/open-apis/im/v1/messages",
        headers={"Authorization": f"Bearer {token}"},
        params={"receive_id_type": "chat_id"},
        json={"receive_id": CHAT_ID, "msg_type": "text", "content": f'{{"text":"{text}"}}'}
    )

    return {"statusCode": 200, "body": "ok"}
