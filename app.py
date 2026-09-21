import streamlit as st
import asyncio
import pandas as pd
from agents.orchestrator import PipelineOrchestrator

st.set_page_config(page_title="AI Creative Finder", layout="wide")

st.title("🚀 Automated Dropshipping Creative Finder")
st.markdown("Search for high-converting creatives across TikTok and Meta Ads using AI agents.")

# Sidebar for inputs
with st.sidebar:
    st.header("Search Parameters")
    product_input = st.text_input("Product Keyword or URL", placeholder="e.g., posture corrector")
    
    platforms = st.multiselect(
        "Select Platforms to Scrape",
        ["TikTok", "Meta"],
        default=["TikTok", "Meta"]
    )
    
    max_results = st.slider("Max Results per Platform", min_value=1, max_value=20, value=5)
    
    start_search = st.button("🔍 Find Creatives", type="primary", use_container_width=True)

if start_search:
    if not product_input:
        st.warning("Please enter a product keyword or URL.")
    elif not platforms:
        st.warning("Please select at least one platform.")
    else:
        with st.spinner("Agents are analyzing the product and scraping platforms... This may take a minute."):
            orchestrator = PipelineOrchestrator()
            
            # Run the async pipeline in a synchronous Streamlit context
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(orchestrator.run_pipeline(product_input, platforms, max_results))
            except Exception as e:
                st.error(f"Pipeline error: {e}")
                result = {"keywords_used": [], "creatives": []}
                
        # Display Results
        st.success("Search Complete!")
        
        st.subheader("🤖 Strategist Agent Analysis")
        st.write(f"**Optimized Search Keywords:** {', '.join(result['keywords_used'])}")
        
        creatives = result['creatives']
        
        if not creatives:
            st.info("No creatives found or scraping blocked. Try another keyword.")
        else:
            st.subheader(f"🏆 Top Curated Creatives ({len(creatives)} found)")
            
            # Display as a grid of cards
            st.divider()
            cols = st.columns(3)
            
            for i, row in enumerate(creatives):
                col = cols[i % 3]
                with col:
                    with st.container(border=True):
                        st.markdown(f"### {row['platform']}")
                        
                        # Preview Media
                        if row.get('media_url'):
                            if row['media_type'] == 'video':
                                try:
                                    st.video(row['media_url'])
                                    st.caption("*(Click the 3 dots in the bottom right of the video to download)*")
                                except:
                                    st.write(f"[Direct Video Link]({row['media_url']})")
                            elif row['media_type'] == 'image':
                                st.image(row['media_url'], use_container_width=True)
                                if row['platform'] == 'TikTok':
                                    st.caption("*(Live video preview blocked by ISP. Use the download button below)*")
                            elif row['media_type'] == 'link':
                                st.info("Use the download button below to view/download.")
                        else:
                            st.info("No Preview Available")
                            
                        # Metrics & Description
                        source_name = row.get('source_name', 'Unknown Source')
                        st.markdown(f"**Source:** {source_name}")
                        st.markdown(f"**Score:** {row['engagement_score']} | **Views:** {row['views']}")
                        st.caption(str(row['description'])[:150] + "...")
                        
                        if row['platform'] == 'TikTok':
                            st.code(row['url'], language="text")
                            st.caption("*(Click the icon inside the box above to copy the video URL)*")
                            
                        # Buttons
                        col1, col2 = st.columns(2)
                        with col1:
                            st.link_button("🌐 Source", row['url'], use_container_width=True)
                        with col2:
                            dl_url = row.get('download_url') or row.get('media_url')
                            if dl_url:
                                btn_label = "⬇️ Download Media"
                                if "snaptik.app" in dl_url:
                                    btn_label = "⬇️ Get MP4 via SnapTik"
                                st.link_button(btn_label, dl_url, use_container_width=True)
                        st.divider()
