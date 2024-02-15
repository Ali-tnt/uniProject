from django.contrib import messages
from item.models import Category, Item
def js_messages(request):
    js_messages = [str(message) for message in messages.get_messages(request)]
    return {'js_messages': js_messages}
#TODO اینجا یه مقدار بفرستم با جی اس چکش کنم، اگر یوزر خارج شد مقدارشو عوض کنم جی اس بفهمه بعد باز با جی اس مقدارشو برگردونم


def categories(request):
    nav_categories = Category.objects.all()  # Retrieve all categories
    styles = """<style>
        .dropdown {
            position: relative; /* Ensure the dropdown is positioned relative to the parent */
        }
        .dropdown .dropbtn {
            border: none;
            outline: none;
            color: white;
            padding: 14px 16px;
            background-color: inherit;
            font-family: inherit;
            margin: 0;
            cursor: pointer; /* To indicate this can be clicked */
        }
        .dropdown-content {
            display: none;
            position: absolute;
            right: 0;
            top: 100%;
            background-color: #f9f9f9;
            min-width: 100%;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
            border-radius: 0.5em; /* Whole dropdown has rounded corners */
        }
        .dropdown-content a,
        .dropdown-content form {
            float: none;
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            text-align: right;
        }
        .dropdown-content a:hover,
        .dropdown-content form:hover {
            background-color: #ddd;
        }
        /* First and last child rounded corners */
        .dropdown-content form:first-child {
            border-top-left-radius: 0.5em;
            border-top-right-radius: 0.5em;
        }
        .dropdown-content form:last-child {
            border-bottom-left-radius: 0.5em;
            border-bottom-right-radius: 0.5em;
        } 
        .dropdown:hover .dropdown-content {
            display: block;
        }"""
    return {
        'nav_categories': nav_categories,
        'styles': styles,
        } 