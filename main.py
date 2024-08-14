import streamlit as st
import data_preprocessing,stats
import matplotlib.pyplot as plt
#from wordcloud import  WordCloud

st.sidebar.title('Whatsapp Chat Analyzer')
file=st.sidebar.file_uploader("Choose a file name")
if file is not None:
    byte_data=file.getvalue()
    data=byte_data.decode('utf-8')
    #st.text(data)
    df=data_preprocessing.prerocess(data)
    user_list=df['User'].unique().tolist()
    user_list.remove('notification')
    user_list.insert(0,'All User')
    selected_user=st.sidebar.selectbox("Show Analysis",user_list)
    st.header('Whatsapp Chat Statistics')
    if st.sidebar.button('Display'):
        number_message,total_word,videos=stats.chat_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)
        with col1:

            st.header('Total Messages')
            st.title(number_message)
        with col2:
            st.header('Total Words')
            st.title(total_word)
        with col3:
            st.header('Total Video')
            st.title(videos)
        #\with col4:
            #st.header('Total Link')
            #st.title(urls)
        #fetch most bust person in group(only for grop chat )
        if selected_user=='All User':
            st.title('Most Busy Users')
            busy_user,dataframe=stats.busy_user(df)
            col1,col2=st.columns(2)
            with col1:
                st.title('Top 10 Busy Users in Group')
                plt.figure(figsize=(10,2))
                plt.subplot(1,2,1)
                plt.bar(busy_user.index,busy_user.values,color='g')
                plt.xticks(rotation=90)
                st.pyplot(plt.gcf())
            with col2:
                st.title('User chat Contribution in group')
                st.dataframe(dataframe)

        st.title('Analysis Most Whatsapp chat happend in which month')
        time=stats.timeline(selected_user,df)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            ax.plot(time['Time'], time['Total Message'],color='orange')
            plt.xticks(rotation=90)
            st.pyplot(fig)

        with col2:
            st.dataframe(time)
        dailytime = stats.Dailytimeline(selected_user, df)
        st.title('Analysis Most Whatsapp chat happend in Datewise')
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            ax.plot(dailytime['Day'], dailytime['message'],color='r')
            plt.xticks(rotation=60)
            st.pyplot(fig)
        with col2:
            st.dataframe(dailytime)
        st.title('Analysis Most Busy Day in Week on Whatsapp Chat')
        day_name=stats.Busy_day(selected_user,df)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            ax.bar(day_name.index,day_name.values)
            plt.xticks(rotation=60)
            st.pyplot(fig)
        with col2:
            st.text(day_name)
        st.title('Analysis Most Busy Month in year on Whatsapp Chat')
        month_name = stats.Busy_month(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            ax.bar(month_name.index, month_name.values,color='r')
            plt.xticks(rotation=60)
            st.pyplot(fig)
        with col2:
            st.text(month_name)
        st.title('Most Frequent word used in chat')
        top_25_word = stats.word_cloud(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            ax.bar(top_25_word['Word'], top_25_word['Count'],color='y')

            plt.xticks(rotation=90)
            # ax.imshow(top_25_word)
            st.pyplot(fig)

        with col2:
            st.dataframe(top_25_word)


        st.title('Top 20 Emojis Analysis used in Chat')
        emojis = stats.fetch_emoji(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots()
            ax.pie(emojis["Count"],labels=emojis['Emoji'],autopct="%0.2f")
            # ax.imshow(top_25_word)
            st.pyplot(fig)

        with col2:
            st.dataframe(emojis)





