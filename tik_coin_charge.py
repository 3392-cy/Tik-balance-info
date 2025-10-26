import requests
import json

sess=input("Enter session id : ")

url = "https://webcast.tiktok.com/webcast/wallet_api/fs/diamond_buy/permission_v2"
params = {"aid": "1988"}
headers = {"Cookie": (f"sessionid={sess}"),
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"}
gqpgqpg = requests.get(url, headers=headers, params=params)  
if json.loads(gqpgqpg.text).get('status_code') == 0:
    geo = json.loads(gqpgqpg.text).get("data", {})
    mess = f'''
Coins:              {geo.get("coins")}
Frozen coins:       {geo.get("frozen_coins")}
Blocked:            {geo.get("block_coin_page")}
Allow status:       {geo.get("is_allow")}
Email confirmed:    {geo.get("is_email_confirmed")}
First web recharge: {geo.get("is_first_web_recharge")}
Periodic payout:    {geo.get("is_periodic_payout")}
Show page:          {geo.get("is_show")}
PC web status:      {geo.get("pc_web_recharge_status")}
PWA category:       {geo.get("pwa_user_category")}
Quick payment:      {geo.get("quick_payment_available")}
Google recharge:    {geo.get("has_google_recharge")}
Tooltip shown:      {geo.get("show_input_tooltip")}
Redeem info :       {geo.get("redeem_info", {})}
Web option:         {geo.get("web_recharge_input_option")}
@gqpgqpg | @rwrqi
'''
    print(mess)
    print("")
    if str(geo.get("quick_payment_available")) == 'True' or str(geo.get("has_google_recharge"))=='True':
        print("Payment method available ✔️")
    elif str(geo.get("quick_payment_available")) == 'False' or str(geo.get("has_google_recharge"))=='False': 
        print('No payment mathod found ✖️ ')
    else:
        print("Error")
else:
    print("Error. Check session or api patched")
