import streamlit as st
import pandas as pd
import preprocessor
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df1= preprocessor.fun(df_microsoft)
df2= preprocessor.fun(df_oracle)

df_microsoft= pd.read_csv('Microsoft.csv')
df_oracle= pd.read_csv('Oracle.csv')


st.sidebar.title("Placement Analysis")
st.sidebar.image('CareerSync.png')

user_menu= st.sidebar.radio(
    'Select an Option: ',
    ('Overall Analysis','Branch-wise Analysis','Company-wise Analysis','Placed Student Analysis')
)

selected_year= st.sidebar.selectbox('Select Year', list(range(2019, 2025)))
selected_branch = st.sidebar.selectbox('Select Branch', ['IT', 'CSE', 'ECE', 'EEE', 'ICE'])


if user_menu == 'Overall Analysis':
    st.title("Overall Placement Analysis")
    
    # CGPA distribution
    st.subheader("CGPA Distribution")
    fig_cgpa= px.histogram(df_microsoft, x='CGPA', nbins=20, title='CGPA Distribution', labels={'CGPA': 'CGPA Score', 'count': 'Frequency'})
    fig_cgpa.update_traces(marker_color='royalblue', marker_line_color='black', marker_line_width=1.5)
    fig_cgpa.update_layout(showlegend=False)
    st.plotly_chart(fig_cgpa)

    # Branches Focus
    st.subheader("Branches Focus")
    branch_counts= df_microsoft['Branch'].value_counts()
    fig_branch= px.bar(branch_counts, x=branch_counts.index, y=branch_counts.values, labels={'x':'Branch', 'y':'Count'}, title='Branches Focus', color=branch_counts.values)
    fig_branch.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig_branch.update_layout(showlegend=False)
    st.plotly_chart(fig_branch)

    # Placed distribution
    st.subheader("Placed Distribution")
    placed_counts= df_microsoft['Placed'].value_counts()
    fig_placed= px.pie(placed_counts, values=placed_counts.values, names=placed_counts.index, title='Placed Distribution')
    fig_placed.update_traces(marker=dict(colors=['green','red'], line=dict(color='#000000', width=2)))
    st.plotly_chart(fig_placed)

    # Branch vs CGPA
    st.subheader("Branch vs CGPA")
    fig_branch_cgpa= px.box(df_microsoft, x='Branch', y='CGPA', title='Branch vs CGPA', color='Branch')
    fig_branch_cgpa.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig_branch_cgpa.update_layout(showlegend=False)
    st.plotly_chart(fig_branch_cgpa)

    # 10th and 12th Marks
    st.subheader("10th and 12th Marks")
    fig_marks= px.scatter(df_microsoft, x='10th Percentage',y='12th Percentage',title='10th vs 12th Marks',color='Branch')
    fig_marks.update_traces(marker_line_color='black',marker_line_width=1.5)
    fig_marks.update_layout(showlegend=True)
    st.plotly_chart(fig_marks)

elif user_menu=='Placed Student Analysis':
    st.title("Specially Placed Analysis")
    
    # Filtering dataframe for specially placed students
    df_placed= df_microsoft[df_microsoft['Placed'] == 'YES']
    selected_gender= st.radio("Select Gender", ('All', 'Male', 'Female'))

    if selected_gender=='Male':
        df_placed= df_placed[df_placed['Gender']=='Male']
    elif selected_gender=='Female':
        df_placed= df_placed[df_placed['Gender']=='Female']

    # CGPA trends for specially placed students
    st.subheader("CGPA Trends for Placed Students")
    fig_cgpa_placed= px.line(df_placed, x=df_placed.index, y='CGPA', title='CGPA Trends for Placed Students')
    fig_cgpa_placed.update_traces(marker_color='green', marker_line_color='black', marker_line_width=1.5)
    st.plotly_chart(fig_cgpa_placed)

    # Branch distribution for specially placed students
    st.subheader("Branch Distribution for Placed Students")
    branch_counts_placed= df_placed['Branch'].value_counts()
    fig_branch_placed= px.bar(branch_counts_placed, x=branch_counts_placed.index, y=branch_counts_placed.values, labels={'x':'Branch', 'y':'Count'}, title='Branch Distribution for Specially Placed Students')
    fig_branch_placed.update_traces(marker_line_color='black', marker_line_width=1.5)
    st.plotly_chart(fig_branch_placed)

    # 10th and 12th Marks for specially placed students
    st.subheader("10th and 12th Marks for Placed Students")
    fig_marks_placed = px.scatter(df_placed, x='10th Percentage', y='12th Percentage', title='10th vs 12th Marks for Specially Placed Students', color='Branch')
    fig_marks_placed.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig_marks_placed.update_layout(showlegend=True)
    st.plotly_chart(fig_marks_placed)


# Branch-wise Analysis
elif user_menu =='Branch-wise Analysis':
    st.title("Branch-wise Placement Analysis")
    
    # Select Branch
    selected_branch=st.selectbox('Select Branch', df_microsoft['Branch'].unique())

    # CGPA distribution for selected branch
    st.subheader(f"CGPA Distribution for {selected_branch}")
    fig_cgpa_branch= px.histogram(df_microsoft[df_microsoft['Branch'] == selected_branch], x='CGPA', nbins=20, title=f'CGPA Distribution for {selected_branch}', labels={'CGPA': 'CGPA Score', 'count': 'Frequency'})
    fig_cgpa_branch.update_traces(marker_color='green', marker_line_color='black', marker_line_width=1.5)
    fig_cgpa_branch.update_layout(showlegend=False)
    st.plotly_chart(fig_cgpa_branch)

    # 10th and 12th Marks for selected branch
    st.subheader(f"10th and 12th Marks for {selected_branch}")
    fig_marks_branch= px.scatter(df_microsoft[df_microsoft['Branch'] == selected_branch], x='10th Percentage', y='12th Percentage', title=f'10th vs 12th Marks for {selected_branch}', color='CGPA')
    fig_marks_branch.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig_marks_branch.update_layout(showlegend=True)
    st.plotly_chart(fig_marks_branch)


elif user_menu=='Company-wise Analysis':
    st.title("Company-wise Placement Analysis")
    
    # Select Company
    selected_company= st.selectbox('Select Company', ['Microsoft','Oracle'])

    if selected_company=='Microsoft':
        df_company= df_microsoft
    else:
        df_company= df_oracle

    # CGPA distribution for selected company
    st.subheader(f"CGPA Distribution for {selected_company}")
    fig_cgpa_company= px.histogram(df_company, x='CGPA', nbins=20, title=f'CGPA Distribution for {selected_company}', labels={'CGPA': 'CGPA Score', 'count': 'Frequency'})
    fig_cgpa_company.update_traces(marker_color='red', marker_line_color='black', marker_line_width=1.5)
    fig_cgpa_company.update_layout(showlegend=False)
    st.plotly_chart(fig_cgpa_company)

    # Branches focus for selected company
    st.subheader(f"Branches Focus for {selected_company}")
    branch_counts_company= df_company['Branch'].value_counts()
    fig_branch_company= px.bar(branch_counts_company, x=branch_counts_company.index, y=branch_counts_company.values, labels={'x':'Branch', 'y':'Count'}, title=f'Branches Focus for {selected_company}', color=branch_counts_company.index, color_continuous_scale='RdYlBu')
    fig_branch_company.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig_branch_company.update_layout(showlegend=False)
    st.plotly_chart(fig_branch_company)

    # 10th and 12th Marks for selected company
    st.subheader(f"10th and 12th Marks for {selected_company}")
    fig_marks_company= px.scatter(df_company, x='10th Percentage', y='12th Percentage', title=f'10th vs 12th Marks for {selected_company}', color='Branch')
    fig_marks_company.update_traces(marker_line_color='black', marker_line_width=1.5)
    fig_marks_company.update_layout(showlegend=True)
    st.plotly_chart(fig_marks_company)