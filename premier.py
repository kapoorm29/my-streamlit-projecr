import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',
                   page_title='premier league dashboard',
                   page_icon=":soccer:")
@st.cache_data
def load():
    return pd.read_csv('premierleague.csv')

#main code starts here
df = load()

st.title("premier league dashboard")
with st.expander("view raw premier league data"):
    st.dataframe(df.sample(1000))  #random record

rows, cols = df.shape
c1, c2 = st.columns(2)
c1.markdown(f'### total records : {rows}')  
c2.markdown(f'### total columns : {cols}')  

numeric_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(exclude='number')
with st.expander("column names"):
    st.markdown(f'columns with numbers: {",".join(numeric_df)}')
    st.markdown(f'columns without numbers: {",".join(cat_df)}')

#visualization 

c1, c2 = st.columns([1,2])
xcol = c1.selectbox("choose a column for x-axis", numeric_df.columns)        
ycol = c1.selectbox("choose a column for y-axis", numeric_df.columns)        
zcol = c1.selectbox("choose a column for z-axis", numeric_df.columns)        
color = c1.selectbox('choose column for color', cat_df.columns)
fig= px.scatter_3d(df, x=xcol, y=ycol, z=zcol, color=color)
c2.plotly_chart(fig, use_container_width=True)        

st.title("what is premier league")
c1, c2 = st.columns(2)
c1.video("https://youtu.be/2PtHZMRfdVE")
c2.markdown('''The Premier League, England's top professional football league, continues to captivate audiences worldwide with its thrilling matches and talented players. Established in 1992, the league has evolved into one of the most prestigious and competitive football competitions globally. With its fast-paced style of play and fiercely contested matches, the Premier League consistently delivers excitement and drama throughout the season. Clubs like Manchester United, Liverpool, Manchester City, Chelsea, and Arsenal boast rich histories and passionate fan bases, adding to the league's allure. The league's global appeal is further enhanced by its diverse array of international stars, drawing fans from all corners of the globe. From the intensity of the title race to the drama of relegation battles, the Premier League remains a cornerstone of world football, captivating fans with its unparalleled excitement and quality of play.''')

st.title("premier league clubs")
clubs = df['HomeTeam'].unique() + df['AwayTeam'].unique()
clubs = sorted(set(clubs))
st.info(",".join(clubs))