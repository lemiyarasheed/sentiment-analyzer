import streamlit as st
from transformers import pipeline
import pandas as pd
from datetime import datetime

#Page config
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🎭",
    layout="centered"
)

st.title("🎭Sentiment Analyzer")
st.markdown("Enter text below and I'll tell you if it's **anger**, **disgust**, **fear**, **joy**, **neutral**, **sadness** or **surprise**.")

#Load the model(Cached for performance)
@st.cache_resource
def load_model():
    return pipeline("text-classification",model="j-hartmann/emotion-english-distilroberta-base")

try:
    classifier=load_model()
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌Failed to load model: {e}")
    st.stop()

# Text input
user_input=st.text_area("📝Enter your text:", height=120)

#History storage in session state
if "history" not in st.session_state:
    st.session_state.history=[]

#Analyze button
col1,col2=st.columns([1,4])
with col1:
    analyze=st.button("🔍 Analyze", type="primary")

if analyze and user_input.strip():
    with st.spinner("Analyzing..."):
        result=classifier(user_input)     #returns list of dicts; [{'label':'anger','score':0.01},...]
         
        # Debug: print to terminal to see structure
        print("Result type:", type(result))
        print("Result content:", result)
        
        # Handle different return formats
        if isinstance(result, list) and len(result) > 0:
            # If it's a list, get first item
            prediction = result[0]
        elif isinstance(result, dict):
            # If it's a dict directly
            prediction = result
        else:
            st.error(f"Unexpected result format: {type(result)}")
            st.stop()
        
        # Extract label and score
        sentiment = prediction.get('label', 'unknown')
        confidence = prediction.get('score', 0)
    
    # Emoji mapping for emotions
    emoji_map = {
        'anger': '😤',
        'disgust': '🤢', 
        'fear': '😨',
        'joy': '😀',
        'neutral': '😐',
        'sadness': '😢',
        'surprise': '😲'
    }
    
    # Display result with appropriate color
    emoji = emoji_map.get(sentiment.lower(), '🎭')
    
    if sentiment.lower() == 'joy':
        st.success(f"### {emoji} Emotion: **{sentiment.upper()}**")
    elif sentiment.lower() in ['anger', 'fear', 'sadness', 'disgust']:
        st.error(f"### {emoji} Emotion: **{sentiment.upper()}**")
    else:
        st.info(f"### {emoji} Emotion: **{sentiment.upper()}**")
    
    st.metric("Confidence Score", f"{confidence:.2%}")
    
    # Save to history
    st.session_state.history.append({
        "text": user_input[:50] + "..." if len(user_input) > 50 else user_input,
        "emotion": sentiment,
        "confidence": confidence,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

# Display history
if st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Analysis History")
    
    # Convert to DataFrame for display
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df, use_container_width=True)
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

# Footer
st.markdown("---")
st.caption("Powered by Hugging Face's emotion-english-distilroberta-base model")