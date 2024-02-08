from django.contrib import messages

def js_messages(request):
    js_messages = [str(message) for message in messages.get_messages(request)]
    return {'js_messages': js_messages}
#TODO اینجا یه مقدار بفرستم با جی اس چکش کنم، اگر یوزر خارج شد مقدارشو عوض کنم جی اس بفهمه بعد باز با جی اس مقدارشو برگردونم