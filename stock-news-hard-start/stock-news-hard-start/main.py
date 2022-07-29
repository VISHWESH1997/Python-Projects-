import requests
import smtplib
import re

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "#YOUR NEWS API KEY"
STOCK_API_KEY = "#YOUR STOCK API KEY"
G_MAIL = "#YOUR MAIL ID"
PASSWORD = "#YOUR PWD"


# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive
# difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.

parameter_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=parameter_stock)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
# stock_data_list = list(stock_data)
stock_data_list = [value for (key, value) in stock_data.items()]
y_close = float(stock_data_list[0]['4. close'])
dby_close = float(stock_data_list[1]['4. close'])
stock_type = "inc"
diff = y_close - dby_close

parameter_news = {
    'q': 'tsla',
    'apikey': NEWS_API_KEY
}

news_response = requests.get(url=NEWS_ENDPOINT, params=parameter_news)
news_response.raise_for_status()
news_data = news_response.json()
articles_slice = news_data["articles"][:3]
# ["title"]
# ["description"]
# articles_desc = news_data["articles"][:3]

if y_close > dby_close:
    percent = round((diff / y_close) * 100)
    print(percent)
else:
    percent = round(((diff * -1) / y_close) * 100)
    print(percent)
    stock_type = "dec"

# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
article_title = []
article_desc = []
is_percent_gr = False
if percent >= 1:
    is_percent_gr = True
    for news_slice in articles_slice:
        article_title.append(news_slice["title"])
        article_desc.append(re.compile(r'<[^>]+>').sub('', news_slice["description"]))
    print(article_desc)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.

if is_percent_gr:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=G_MAIL, password=PASSWORD)
        for i in range(3):
            if stock_type == "dec":
                msg_dec = (f'Subject:{STOCK}: stock 🔻 by {percent}%\n\nHeadline: {article_title[i]} \nBrief: '
                           f'{article_desc[i]} ').encode('utf-8')
                connection.sendmail(from_addr="vishweshex@gmail.com",
                                    to_addrs=G_MAIL,
                                    msg=msg_dec)
                # msg=f"Subject:TSLA: stock decrease by {percent}%\n\nHeadline: {article_title[i]} \n"
                #    f"Brief: {article_desc[i]}")
            else:
                msg_inc = (f'Subject:{STOCK}: stock 🔺 by {percent}%\n\nHeadline: {article_title[i]} \nBrief: '
                           f'{article_desc[i]} ').encode('utf-8')
                connection.sendmail(from_addr="vishweshex@gmail.com",
                                    to_addrs=G_MAIL,
                                    msg=msg_inc)
                # msg=f"Subject:TSLA stock increase by{percent}%\n\nHeadline: {article_title[i]}
                # \n " f"Brief: {article_desc[i]}")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of 
the coronavirus market crash.
"""
