import os

# 1. Update styles.css
css_append = """
/* =========================================
   FINTECH / PREMIUM STYLES OVERRIDE
========================================= */

/* Dark Hero Section */
.fintech-hero {
    background: #0f172a; /* Slate 900 */
    color: #ffffff;
    border-radius: var(--radius-2xl);
    padding: 32px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.fintech-hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(255,17,96,0.1) 0%, rgba(41,171,226,0.1) 100%);
    z-index: 1;
}

.fintech-hero > * {
    position: relative;
    z-index: 2;
}

/* Premium Wallet Card Widget */
.premium-card {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border-radius: 16px;
    padding: 24px;
    color: white;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.premium-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(255,17,96,0.15) 0%, rgba(255,255,255,0) 50%);
    transform: rotate(30deg);
    pointer-events: none;
}

.premium-card__balance {
    font-size: 36px;
    font-weight: 900;
    letter-spacing: -1px;
    margin: 8px 0;
    font-family: var(--font-display);
    background: linear-gradient(to right, #ffffff, #cbd5e1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.premium-card__chip {
    width: 40px; height: 28px;
    background: linear-gradient(135deg, #e2e8f0 0%, #94a3b8 100%);
    border-radius: 4px;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
}

.premium-card__chip::after {
    content: '';
    position: absolute;
    top: 50%; left: 0; right: 0; height: 1px;
    background: rgba(0,0,0,0.2);
}

.fintech-stat {
    display: flex;
    flex-direction: column;
}
.fintech-stat-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #94a3b8;
    font-weight: 600;
    margin-bottom: 4px;
}
.fintech-stat-value {
    font-size: 24px;
    font-weight: 800;
    color: white;
}

/* Asymmetric Grid */
.fintech-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
    margin-bottom: 24px;
}
@media (max-width: 1024px) {
    .fintech-grid { grid-template-columns: 1fr; }
}

.fintech-stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
@media (max-width: 768px) {
    .fintech-stats-row { grid-template-columns: 1fr; }
}

/* Floating Activity Cards */
.floating-activity {
    background: white;
    border-radius: var(--radius-lg);
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 12px;
    border: 1px solid var(--neutral-200);
    transition: transform 0.2s, box-shadow 0.2s;
}
.floating-activity:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}
.floating-activity__icon {
    width: 40px; height: 40px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: bold;
}
.floating-activity__details {
    flex-grow: 1;
}

/* Payment Method Card */
.payment-card {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border-radius: 12px;
    padding: 20px;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 120px;
    position: relative;
    overflow: hidden;
}
.payment-card-logo {
    font-size: 18px;
    font-weight: 900;
    font-style: italic;
    color: rgba(255,255,255,0.9);
}
.payment-card-number {
    font-family: monospace;
    font-size: 16px;
    letter-spacing: 2px;
    margin-top: 16px;
}

/* Override existing topbar in dark hero mode */
.dark-topbar {
    background: transparent !important;
    border-bottom: none !important;
    color: white !important;
    position: absolute;
    top: 0; left: 0; right: 0;
    z-index: 10;
}
.dark-topbar .app-topbar__title {
    color: white !important;
}
.dark-topbar .app-topbar__search input {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: white;
}
.dark-topbar .app-topbar__search input::placeholder {
    color: rgba(255,255,255,0.5);
}
.dark-topbar .app-topbar__search svg {
    color: rgba(255,255,255,0.5);
}
.dark-topbar .btn--ghost {
    color: white;
}
.dark-topbar .btn--ghost:hover {
    background: rgba(255,255,255,0.1);
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("styles.css updated.")
