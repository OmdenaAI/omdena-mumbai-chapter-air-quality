import streamlit as st

# ---- HIDE STREAMLIT STYLE ----

def streamlit_style():

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.set_page_config(initial_sidebar_state = "collapsed", layout = 'centered', page_icon = 'icon.png', page_title = 'AeroHue')

    st.markdown('<style> div.block-container{padding-top:0rem;} </style>', unsafe_allow_html=True)

    st.markdown("""
                    <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                    </style>
                """, unsafe_allow_html=True)

    st.markdown("""
                    <style>
                        [data-testid=stSidebar] {
                            background-color: #ff000050;
                        }
                    </style>
                """, unsafe_allow_html=True)

    hvar = """
                <script>
                
                    var elements = window.parents.document.querySelectorAll('.streamlit-expanderHeader')
                    elements[0].style.color = 'rgba(83, 36, 118, 1)';
                    elements[0].style.fontFamily = 'Didot';
                    elements[0].style.fontStyle = 'x-large';
                    elements[0].style.fontWeight = 'bold';

                </script>    
            """