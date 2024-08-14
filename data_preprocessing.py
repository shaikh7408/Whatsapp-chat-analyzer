# import libraries
import pandas as pd
import re
def prerocess(chat):
    # finding date pattern
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{2}:\d{2}\s-\s'
    messages = re.split(pattern, chat)[1:]
    dates = re.findall(pattern, chat)
    df_chat = pd.DataFrame({'Date': dates, 'Messages': messages})
    # separate user and mesages
    user = []
    messages = []
    for message in df_chat['Messages']:
        data = re.split('([\w\W]+?):\s', message)
        if data[1:]:
            user.append(data[1])
            # print(user)
            messages.append(data[2])
        else:
            user.append("notification")
            messages.append(data[0])
    df_chat['User'] = user
    df_chat['message'] = messages
    df_chat.drop(['Messages'], inplace=True, axis=1)
    df_chat['Date'] = pd.to_datetime(df_chat['Date'], format='%d/%m/%Y, %H:%M - ')
    df_chat['Year'] = df_chat['Date'].dt.year
    df_chat['Month'] = df_chat['Date'].dt.month_name()
    df_chat['Day'] = df_chat['Date'].dt.day
    df_chat['Hour'] = df_chat['Date'].dt.hour
    df_chat['Minute'] = df_chat['Date'].dt.minute
    print(df_chat)
    return df_chat