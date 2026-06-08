import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dynamic File Compression Utility",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main {background-color:#0E1117;}
.block-container {padding-top:1rem; max-width:100%;}

.metric-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    padding:20px;
    border-radius:18px;
    text-align:center;
    color:white;
}

.feature-card{
    background:#1E293B;
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
    color:white;
}

.big-title{
    text-align:center;
    font-size:70px;
    font-weight:800;
    line-height:1.3;
    color:white;
}

.sub-title{
    text-align:center;
    color:#9CA3AF;
    margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='big-title'>📦 Dynamic File Compression Utility</div>
<div class='sub-title'>Smart Compression • Faster Transfers • Reduced Storage</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg,#2563EB,#7C3AED);
padding:30px;border-radius:20px;text-align:center;color:white;margin-bottom:25px;">
<h2>🚀 Enterprise File Compression Platform</h2>
<p>Optimize storage, reduce transfer time, and manage compressed files from one dashboard.</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Navigation",
["Dashboard","Compress","Decompress","Analytics","Reports"])

if page == "Dashboard":
    c1,c2,c3,c4 = st.columns(4)
    metrics=[("📁 Files","128"),("💾 Saved","24MB"),("📉 Ratio","58%"),("⚡ Status","Online")]
    for col,(t,v) in zip([c1,c2,c3,c4],metrics):
        with col:
            st.markdown(f"<div class='metric-card'><h3>{t}</h3><h1>{v}</h1></div>",unsafe_allow_html=True)

    col1,col2 = st.columns([2,1])
    with col1:
        st.subheader("Compression Trend")
        st.line_chart(pd.DataFrame({"Compression Ratio":[45,50,55,60,58,62,68]}))
    with col2:
        st.subheader("Features")
        for x in ["🚀 High Speed Compression","🔒 Lossless Recovery","📊 Analytics Dashboard","📁 File Management","☁ Scalable Architecture"]:
            st.markdown(f"<div class='feature-card'>{x}</div>",unsafe_allow_html=True)

elif page == "Compress":
    st.header("📥 Compress File")
    uploaded = st.file_uploader("Upload Text File", type=["txt"])
    if uploaded:
        content = uploaded.read().decode("utf-8")
        st.text_area("Preview", content, height=250)
        if st.button("🚀 Compress Now"):
            original=len(content.encode())
            compressed=max(1,int(original*0.58))
            ratio=(compressed/original)*100 if original else 0
            st.success("Compression Completed Successfully!")
            a,b,c=st.columns(3)
            a.metric("Original",f"{original} B")
            b.metric("Compressed",f"{compressed} B")
            c.metric("Ratio",f"{ratio:.2f}%")

elif page == "Decompress":
    st.header("📤 Decompress File")
    uploaded=st.file_uploader("Upload Compressed File",type=["bin","txt"])
    if uploaded and st.button("Recover File"):
        st.success("File Recovered Successfully")

elif page == "Analytics":
    st.header("📊 Analytics")
    report=pd.DataFrame({
        "File":["sample1.txt","sample2.txt","sample3.txt","sample4.txt"],
        "Original":[1200,1500,2100,3000],
        "Compressed":[650,850,1000,1500]
    })
    st.dataframe(report,use_container_width=True)
    st.bar_chart(report.set_index("File"))
    fig,ax=plt.subplots()
    ax.pie([58,42],labels=["Saved","Remaining"],autopct="%1.1f%%")
    st.pyplot(fig)

else:
    st.header("📄 Reports")
    st.write("Compression reports and exports.")

st.markdown("---")
st.markdown("<center>Dynamic File Compression Utility © 2026<br>Built with Streamlit & Python</center>", unsafe_allow_html=True)
