import os

icons = {
    "dashboard.html": '<path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>',
    "products.html": '<path d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>',
    "app_vendors.html": '<path d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>',
    "app_customers.html": '<path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>',
    "app_orders.html": '<path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>',
    "renewals.html": '<path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>',
    "wallet.html": '<path d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>',
    "invoices.html": '<path d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2zM10 8.5a.5.5 0 11-1 0 .5.5 0 011 0zm5 5a.5.5 0 11-1 0 .5.5 0 011 0z"></path>',
    "reports.html": '<path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>',
    "app_erp.html": '<path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>',
    "profile.html": '<path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>',
    "settings.html": '<path d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"></path>',
    "notifications.html": '<path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path>',
    "support.html": '<path d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"></path>'
}

PAGES = [
    ("dashboard.html", "Dashboard", "Dashboard"),
    ("products.html", "Products", "Products"),
    ("app_vendors.html", "Vendors", "Vendors"),
    ("app_customers.html", "Customers", "Customers"),
    ("app_orders.html", "Orders", "Orders"),
    ("renewals.html", "Renewals", "Renewals"),
    ("wallet.html", "Wallet", "Finance & Operations"),
    ("invoices.html", "Invoices", "Finance & Operations"),
    ("reports.html", "Reports", "Finance & Operations"),
    ("app_erp.html", "ERP Options", "Finance & Operations"),
    ("profile.html", "Profile", "Settings"),
    ("settings.html", "Settings", "Settings"),
    ("notifications.html", "Notifications", "Settings"),
    ("support.html", "Support", "Settings")
]

def generate_layout(active_page, content, is_dark_hero=False):
    sidebar = '''        <aside class="app-sidebar" id="appSidebar">
            <div class="app-sidebar__header">
                <a href="index.html" class="header__logo">
                    <svg class="header__logo-icon" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10,40 A30,30 0 0,1 70,40" stroke="#FF1160" stroke-width="10" stroke-linecap="round" fill="none"/>
                        <path d="M18,40 A22,22 0 0,1 62,40" stroke="#8B44B8" stroke-width="10" stroke-linecap="round" fill="none"/>
                        <path d="M26,48 A14,14 0 0,0 54,48" stroke="#29ABE2" stroke-width="10" stroke-linecap="round" fill="none"/>
                    </svg>
                    <span class="header__logo-name">SAAS<span>ORDER</span></span>
                </a>
            </div>
            <nav class="app-sidebar__nav">'''
    
    sidebar += '''\n                <div class="app-nav-label">Core</div>'''
    for p in PAGES[:6]:
        act = " active" if p[0] == active_page else ""
        sidebar += f'''\n                <a href="{p[0]}" class="app-nav-link{act}"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">{icons[p[0]]}</svg>{p[1]}</a>'''
    
    sidebar += '''\n                <div class="app-nav-label">Finance & Operations</div>'''
    for p in PAGES[6:10]:
        act = " active" if p[0] == active_page else ""
        sidebar += f'''\n                <a href="{p[0]}" class="app-nav-link{act}"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">{icons[p[0]]}</svg>{p[1]}</a>'''
        
    sidebar += '''\n                <div class="app-nav-label">Settings</div>'''
    for p in PAGES[10:]:
        act = " active" if p[0] == active_page else ""
        sidebar += f'''\n                <a href="{p[0]}" class="app-nav-link{act}"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">{icons[p[0]]}</svg>{p[1]}</a>'''

    sidebar += '''\n            </nav>
            <div class="app-sidebar__footer">
                <a href="login.html" class="app-nav-link"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>Logout</a>
            </div>
        </aside>'''

    title = next((p[1] for p in PAGES if p[0] == active_page), "App")
    topbar_class = "app-topbar dark-topbar" if is_dark_hero else "app-topbar"
    
    # Hide the standard wallet indicator in the dark topbar since we have a dedicated wallet card
    wallet_indicator = ""
    if not is_dark_hero:
        wallet_indicator = '''
                        <div style="display: flex; align-items: center; gap: 12px; background: var(--neutral-50); padding: 4px 12px 4px 4px; border-radius: var(--radius-full); border: 1px solid var(--neutral-200); margin: 0 8px;">
                            <div style="width: 28px; height: 28px; background: var(--primary-100); color: var(--primary-600); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px;">W</div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 10px; font-weight: 600; color: var(--neutral-500); text-transform: uppercase;">Wallet</span>
                                <span style="font-size: 13px; font-weight: 700; color: var(--neutral-900);">$42,500</span>
                            </div>
                        </div>'''

    topbar = f'''            <header class="{topbar_class}">
                <div style="display: flex; align-items: center; gap: 16px;">
                    <button class="mobile-menu-toggle" onclick="document.getElementById('appSidebar').classList.toggle('active')">
                        <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"></path></svg>
                    </button>
                    <h1 class="app-topbar__title">{title}</h1>
                </div>
                
                <div class="app-topbar__actions">
                    <div class="app-topbar__search">
                        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                        <input type="text" placeholder="Search...">
                    </div>
                    
                    <div style="display: flex; align-items: center; gap: 8px; padding-left: 16px; border-left: 1px solid var(--neutral-200);">
                        <button class="btn btn--ghost btn--sm" style="padding: 8px; border-radius: 50%;">
                            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
                        </button>
                        {wallet_indicator}
                        <div class="app-user-profile" onclick="window.location.href='profile.html'">
                            <div class="app-user-avatar">SM</div>
                        </div>
                    </div>
                </div>
            </header>'''
            
    content_padding = "0" if is_dark_hero else "24px"

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SaaSOrder — {title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="app-layout">
{sidebar}
        <main class="app-main" style="position: relative;">
{topbar}
            <div class="app-content" style="padding: {content_padding};">
{content}
            </div>
        </main>
    </div>
    <script src="script.js"></script>
</body>
</html>'''

# Dashboard Content (FinTech)
dashboard_content = '''
                <div class="fintech-hero" style="padding-top: 100px; margin: 0; border-radius: 0;">
                    <div class="fintech-grid">
                        <div style="display: flex; flex-direction: column; justify-content: center;">
                            <h2 style="font-family: var(--font-display); font-size: 32px; font-weight: 800; margin-bottom: 24px;">Financial Overview</h2>
                            
                            <div class="fintech-stats-row">
                                <div class="fintech-stat">
                                    <span class="fintech-stat-label">Total Spend</span>
                                    <span class="fintech-stat-value">$4.2M</span>
                                    <span style="color: #4ade80; font-size: 12px; margin-top: 4px; display: flex; align-items: center; gap: 4px;">
                                        <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                                        12.5% vs last month
                                    </span>
                                </div>
                                <div class="fintech-stat">
                                    <span class="fintech-stat-label">Active Vendors</span>
                                    <span class="fintech-stat-value">34</span>
                                    <span style="color: #4ade80; font-size: 12px; margin-top: 4px; display: flex; align-items: center; gap: 4px;">
                                        <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                                        +2 new vendors
                                    </span>
                                </div>
                                <div class="fintech-stat">
                                    <span class="fintech-stat-label">Renewals (30d)</span>
                                    <span class="fintech-stat-value">3</span>
                                    <span style="color: #f87171; font-size: 12px; margin-top: 4px; display: flex; align-items: center; gap: 4px;">
                                        <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                        Action required
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Wallet Card Widget -->
                        <div>
                            <div class="premium-card">
                                <div>
                                    <div class="premium-card__chip"></div>
                                    <span style="font-size: 12px; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; font-weight: 600;">SaaSOrder Wallet</span>
                                    <div class="premium-card__balance">$42,500.00</div>
                                    <span style="font-size: 13px; color: #cbd5e1;">Available Credit: $150,000.00</span>
                                </div>
                                <div style="display: flex; gap: 12px; margin-top: 24px;">
                                    <button class="btn" style="background: white; color: black; border: none; flex-grow: 1; font-weight: 700; padding: 10px;">Top-Up</button>
                                    <button class="btn" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2); padding: 10px;">History</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div style="padding: 24px;">
                    <div class="fintech-grid" style="grid-template-columns: 2fr 1fr;">
                        <!-- Spend Chart -->
                        <div class="app-card" style="display: flex; flex-direction: column; margin-bottom: 0;">
                            <div class="app-card__header">
                                <h2 class="app-card__title">Monthly Procurement Spend</h2>
                                <select style="padding: 6px 12px; border-radius: 6px; border: 1px solid var(--neutral-200); outline: none; background: var(--neutral-50); color: var(--neutral-600); font-weight: 500; font-size: 13px;">
                                    <option>Last 6 Months</option>
                                    <option>This Year</option>
                                </select>
                            </div>
                            <div class="app-card__body" style="flex-grow: 1; min-height: 250px; position: relative;">
                                <canvas id="spendChart"></canvas>
                            </div>
                        </div>

                        <!-- Floating Activity Cards -->
                        <div>
                            <h2 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 16px;">Recent Activity</h2>
                            
                            <div class="floating-activity">
                                <div class="floating-activity__icon" style="background: var(--success-100); color: var(--success-700);">
                                    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"></path></svg>
                                </div>
                                <div class="floating-activity__details">
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <strong style="font-size: 14px;">Datadog, Inc.</strong>
                                        <span style="font-size: 12px; color: var(--neutral-500);">10:45 AM</span>
                                    </div>
                                    <div style="font-size: 13px; color: var(--neutral-600);">Renewal completed</div>
                                </div>
                            </div>

                            <div class="floating-activity">
                                <div class="floating-activity__icon" style="background: var(--primary-100); color: var(--primary-600);">
                                    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                                </div>
                                <div class="floating-activity__details">
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <strong style="font-size: 14px;">Wallet Recharged</strong>
                                        <span style="font-size: 12px; color: var(--neutral-500);">Yesterday</span>
                                    </div>
                                    <div style="font-size: 13px; color: var(--success); font-weight: 600;">+$10,000.00</div>
                                </div>
                            </div>
                            
                            <div class="floating-activity">
                                <div class="floating-activity__icon" style="background: var(--neutral-100); color: var(--neutral-600);">
                                    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                                </div>
                                <div class="floating-activity__details">
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <strong style="font-size: 14px;">Acme Corp</strong>
                                        <span style="font-size: 12px; color: var(--neutral-500);">Yesterday</span>
                                    </div>
                                    <div style="font-size: 13px; color: var(--neutral-600);">Purchased Microsoft 365</div>
                                </div>
                            </div>
                            
                            <button class="btn btn--ghost btn--sm" style="width: 100%; justify-content: center;">View All Activity</button>
                        </div>
                    </div>
                </div>
                
                <script>
                    document.addEventListener('DOMContentLoaded', function() {
                        const ctx = document.getElementById('spendChart');
                        if (ctx) {
                            new Chart(ctx, {
                                type: 'bar',
                                data: {
                                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                                    datasets: [{
                                        label: 'Spend ($)',
                                        data: [125000, 195000, 140000, 225000, 180000, 290000],
                                        backgroundColor: '#0f172a', /* Slate 900 for modern look */
                                        borderRadius: 6,
                                        barPercentage: 0.6
                                    }]
                                },
                                options: {
                                    responsive: true,
                                    maintainAspectRatio: false,
                                    plugins: { legend: { display: false } },
                                    scales: {
                                        y: { beginAtZero: true, grid: { color: '#F1F5F9', drawBorder: false }, border: { display: false } },
                                        x: { grid: { display: false, drawBorder: false }, border: { display: false } }
                                    }
                                }
                            });
                        }
                    });
                </script>
'''

# Wallet Content (FinTech)
wallet_content = '''
                <div class="fintech-hero" style="padding-top: 100px; margin: 0; border-radius: 0; padding-bottom: 64px;">
                    <div style="max-width: 600px; margin: 0 auto; text-align: center;">
                        <span style="font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; font-weight: 600;">Wallet Balance</span>
                        <div class="premium-card__balance" style="font-size: 64px; margin: 16px 0;">$42,500.00</div>
                        <span style="font-size: 14px; color: #cbd5e1; display: block; margin-bottom: 32px;">Available Credit Limit: $150,000.00</span>
                        
                        <div style="display: flex; gap: 16px; justify-content: center;">
                            <button class="btn" style="background: white; color: black; border: none; font-weight: 700; padding: 12px 32px; border-radius: 8px;">Top-Up Funds</button>
                            <button class="btn" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2); padding: 12px 32px; border-radius: 8px;">Withdraw</button>
                        </div>
                    </div>
                </div>

                <div style="padding: 24px; margin-top: -32px; position: relative; z-index: 5;">
                    <div class="fintech-grid" style="grid-template-columns: 2fr 1fr;">
                        
                        <!-- Transactions List -->
                        <div class="app-card" style="margin-bottom: 0;">
                            <div class="app-card__header">
                                <h2 class="app-card__title">Recent Transactions</h2>
                                <button class="btn btn--ghost btn--sm">Download Statement</button>
                            </div>
                            <div style="padding: 0 24px 24px 24px;">
                                <!-- Transaction Item -->
                                <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px 0; border-bottom: 1px solid var(--neutral-100);">
                                    <div style="display: flex; align-items: center; gap: 16px;">
                                        <div style="width: 40px; height: 40px; border-radius: 50%; background: var(--success-50); color: var(--success-600); display: flex; align-items: center; justify-content: center;">
                                            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                                        </div>
                                        <div>
                                            <div style="font-weight: 700; font-size: 15px;">Wallet Top-Up</div>
                                            <div style="font-size: 13px; color: var(--neutral-500);">Jun 28, 2026 • Bank Transfer ACH</div>
                                        </div>
                                    </div>
                                    <div style="text-align: right;">
                                        <div style="font-weight: 800; color: var(--success); font-size: 16px;">+$25,000.00</div>
                                        <div style="font-size: 12px; color: var(--neutral-500);">Cleared</div>
                                    </div>
                                </div>
                                
                                <!-- Transaction Item -->
                                <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px 0; border-bottom: 1px solid var(--neutral-100);">
                                    <div style="display: flex; align-items: center; gap: 16px;">
                                        <div style="width: 40px; height: 40px; border-radius: 50%; background: var(--neutral-100); color: var(--neutral-600); display: flex; align-items: center; justify-content: center;">
                                            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
                                        </div>
                                        <div>
                                            <div style="font-weight: 700; font-size: 15px;">Datadog Renewal</div>
                                            <div style="font-size: 13px; color: var(--neutral-500);">Jun 25, 2026 • Auto-deduction</div>
                                        </div>
                                    </div>
                                    <div style="text-align: right;">
                                        <div style="font-weight: 800; color: var(--neutral-900); font-size: 16px;">-$4,200.00</div>
                                        <div style="font-size: 12px; color: var(--neutral-500);">Processed</div>
                                    </div>
                                </div>

                                <!-- Transaction Item -->
                                <div style="display: flex; align-items: center; justify-content: space-between; padding: 16px 0; border-bottom: 1px solid var(--neutral-100);">
                                    <div style="display: flex; align-items: center; gap: 16px;">
                                        <div style="width: 40px; height: 40px; border-radius: 50%; background: var(--success-50); color: var(--success-600); display: flex; align-items: center; justify-content: center;">
                                            <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                                        </div>
                                        <div>
                                            <div style="font-weight: 700; font-size: 15px;">Wallet Top-Up</div>
                                            <div style="font-size: 13px; color: var(--neutral-500);">Jun 12, 2026 • Credit Card ending in 4242</div>
                                        </div>
                                    </div>
                                    <div style="text-align: right;">
                                        <div style="font-weight: 800; color: var(--success); font-size: 16px;">+$5,000.00</div>
                                        <div style="font-size: 12px; color: var(--neutral-500);">Cleared</div>
                                    </div>
                                </div>
                            </div>
                            <div style="padding: 16px; border-top: 1px solid var(--neutral-100); text-align: center;">
                                <button class="btn btn--ghost" style="width: 100%; justify-content: center; font-weight: 600;">View Full History</button>
                            </div>
                        </div>

                        <!-- Payment Methods -->
                        <div>
                            <h2 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 16px;">Payment Methods</h2>
                            
                            <div class="payment-card" style="margin-bottom: 16px;">
                                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                    <div class="payment-card-logo">VISA</div>
                                    <span style="font-size: 11px; background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 12px; font-weight: 600;">DEFAULT</span>
                                </div>
                                <div>
                                    <div class="payment-card-number">**** **** **** 4242</div>
                                    <div style="display: flex; justify-content: space-between; margin-top: 8px; font-size: 12px; color: rgba(255,255,255,0.7);">
                                        <span>Expires 12/28</span>
                                        <span>Sarah Miller</span>
                                    </div>
                                </div>
                            </div>

                            <div class="payment-card" style="background: linear-gradient(135deg, #334155 0%, #0f172a 100%); margin-bottom: 16px;">
                                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                    <div class="payment-card-logo" style="font-style: normal;">ACH</div>
                                </div>
                                <div>
                                    <div class="payment-card-number" style="font-family: var(--font-body); font-weight: 600; letter-spacing: normal;">Chase Corporate</div>
                                    <div style="display: flex; justify-content: space-between; margin-top: 8px; font-size: 12px; color: rgba(255,255,255,0.7);">
                                        <span>Account **** 9901</span>
                                    </div>
                                </div>
                            </div>
                            
                            <button class="btn btn--outline" style="width: 100%; justify-content: center; border-style: dashed; padding: 16px; font-weight: 600;">+ Add Payment Method</button>
                        </div>

                    </div>
                </div>
'''

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("dashboard.html", dashboard_content, is_dark_hero=True))
    
with open("wallet.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("wallet.html", wallet_content, is_dark_hero=True))

print("Dashboard and Wallet pages updated with FinTech aesthetic.")
