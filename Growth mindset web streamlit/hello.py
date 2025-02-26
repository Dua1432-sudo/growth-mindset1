import streamlit as st
import pandas as pd
import os
from io import BytesIo

st.set_page_config(page_title= "Data Sweeper", layout='wide')

#custom css
st.markdown(
    ===
    <sytle>
    .stApp{
    backgroud-color: black;
    color: white;
    }
    </sytle>
    ===,
    unsafe_allow_html=True
)    

#tittle and description
st.title("Datasweeper sterling integrator by Dua iqbal")
st.write("Transform your files between CSV and Excel fromats with built-in data cleaning and  visualization the creating project for quater 3")

#file uploader
uploader_files = st.files_uploader("uploader your files (accept CSV or excel):" type=["CSV","xlsx"], accepte_multiple_file=(true))
if uploaded_file:
    for file in uploaded_file
    file_ext= os.path.splitext(file.name)[-1].lower()

    if file_ext == ".csv"
    df = pd.read_csv(file)
    elif file_ext == "xlsx":
        df =pd.read_excel(file)
        else:
            st.error(f"unsupported file type: {file.ext}")
            continue
            #file detail
            st.write("preview the head of the Dataframe")
            st.dataframe(df.head())

            #data cleaning option
            st.subheader("Data Cleaning Option")
            if st.checkbox(f"clean data for {file.name}"):
                col1, col2 = st.colume(2)

                with col1:
                    if st.button(f"Remove duplicate from the file :{file.name}"):
                        df.drop_duplicataes(inplace=True)
                        st.write("Duplicates removed!")

                        with col2:
                            if st.button(f"Fill missing values for {file.name}"):
                                numeric_col1 = df.select_dtypes(includes=['number']).columns
                                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_col1].mean())
                                st.write("Missing values have been filled!")

                st.subheader("select Columns to keep")
                columns = st.multiselect(f"Choose columns for {file.name}",df.columns, default=df.columns)
                df = df[columns]

                #data visualization
                st.subheader("Data visualization")
                if st.checkbox(f"show visualization for{file.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])   
                    #conversion Option

                    st.subheader("conversion Option") 
                    conversion_type =st.radio(f"convert {file.name} to:",["CVS" , "Excel"], key=file.name)
                    if st.button(f"Convert{file.name}"):
                        buffer = BytesIo() 
                        if conversion_type == "CSV":
                          df.to,csv(buffer,index=False)
                          file_name = file.replace(file_ext, ".csv")
                          mime_type = "text/csv"  

                          elif conversion_type =="Excel":
                            df.to.to_excel(butter, index=False) 
                            file_name = file.name.replace(file_ext, ".xlsx") 
                            mime_type = "allication/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  
                            buffer.seek(0)   

                            st.download_button(
                                label=f"Doenload{file.name} as {conversion_type}",
                                data=buffer,
                                file_name=file_name,
                                mime=mime_type
                            )

                st.success("All file processed successfully!")            
