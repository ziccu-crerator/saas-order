import os
import re

CSS_APPEND = """
/* =========================================
   AUTH SPLIT SCREEN STYLES
========================================= */
.auth-split {
  display: flex;
  min-height: 100vh;
  width: 100%;
}

.auth-video-container {
  display: none; /* hidden on mobile */
  position: relative;
  width: 50%;
  background: var(--neutral-900);
  overflow: hidden;
}

@media (min-width: 992px) {
  .auth-video-container {
    display: block;
  }
}

.auth-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.auth-video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255, 17, 96, 0.2) 0%, rgba(139, 68, 184, 0.4) 100%);
  z-index: 2;
}

.auth-form-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-8);
  background: var(--neutral-50);
}

@media (min-width: 992px) {
  .auth-form-container {
    width: 50%;
  }
}

.auth-split .auth-card {
  box-shadow: none;
  background: transparent;
  width: 100%;
  max-width: 440px;
}
"""

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the auth-card
    match = re.search(r'(<div class="auth-card".*?</div>\s*</div>)', content, re.DOTALL)
    if not match:
        match = re.search(r'(<div class="auth-card".*?</div>)', content, re.DOTALL)
        
    if not match:
        print(f"Could not find auth-card in {filename}")
        return

    # Extract the auth-card content, excluding the wrapper auth-page if it's there
    card_match = re.search(r'(<div class="auth-card".*?)(<script.*|</body>)', content, re.DOTALL)
    if not card_match:
        return
        
    card_html = card_match.group(1).strip()
    # sometimes there is an extra </div> closing auth-page
    if card_html.endswith('</div>\n    </div>'):
        card_html = card_html[:-6].strip()
    elif card_html.endswith('</div>\n</div>'):
        card_html = card_html[:-6].strip()

    new_body = f"""
    <div class="auth-split">
        <div class="auth-video-container">
            <video class="auth-video" autoplay loop muted playsinline>
                <source src="login-video.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <div class="auth-video-overlay"></div>
        </div>
        <div class="auth-form-container">
            {card_html}
        </div>
    </div>
"""
    
    # Replace the body content
    new_content = re.sub(r'<div class="auth-page">.*?</div>\s*<script', new_body + '\n<script', content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")

update_file('login.html')
update_file('register.html')

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(CSS_APPEND)
print("Updated styles.css")
