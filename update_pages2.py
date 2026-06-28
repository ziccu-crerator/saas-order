import os

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

def generate_layout(active_page, content):
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
    topbar = f'''            <header class="app-topbar">
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
                        
                        <div style="display: flex; align-items: center; gap: 12px; background: var(--neutral-50); padding: 4px 12px 4px 4px; border-radius: var(--radius-full); border: 1px solid var(--neutral-200); margin: 0 8px;">
                            <div style="width: 28px; height: 28px; background: var(--primary-100); color: var(--primary-600); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px;">W</div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 10px; font-weight: 600; color: var(--neutral-500); text-transform: uppercase;">Wallet</span>
                                <span style="font-size: 13px; font-weight: 700; color: var(--neutral-900);">$42,500</span>
                            </div>
                        </div>

                        <div class="app-user-profile" onclick="window.location.href='profile.html'">
                            <div class="app-user-avatar">SM</div>
                        </div>
                    </div>
                </div>
            </header>'''

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
        <main class="app-main">
{topbar}
            <div class="app-content">
{content}
            </div>
        </main>
    </div>
    <script src="script.js"></script>
</body>
</html>'''

# Write wallet.html
wallet_content = '''
                <div class="dashboard-grid">
                    <div class="stat-card">
                        <div class="stat-card__info">
                            <span class="stat-card__title">Current Balance</span>
                            <span class="stat-card__value" style="color: var(--primary-500);">$42,500.00</span>
                        </div>
                        <div class="stat-card__icon stat-card__icon--pink"><svg fill="none" stroke="currentColor" stroke-width="2" width="24" height="24" viewBox="0 0 24 24"><path d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg></div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-card__info">
                            <span class="stat-card__title">Available Credit Limit</span>
                            <span class="stat-card__value">$150,000.00</span>
                        </div>
                        <div class="stat-card__icon stat-card__icon--blue"><svg fill="none" stroke="currentColor" stroke-width="2" width="24" height="24" viewBox="0 0 24 24"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></div>
                    </div>
                    <div class="app-card" style="display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 0; padding: 24px; border: 2px dashed var(--primary-200); background: var(--primary-50); cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='var(--primary-100)'" onmouseout="this.style.background='var(--primary-50)'">
                        <svg width="24" height="24" fill="none" stroke="var(--primary-500)" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                        <span style="font-weight: 700; color: var(--primary-600); font-size: 16px;">Top-Up Wallet</span>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">
                    <div class="app-card">
                        <div class="app-card__header">
                            <h2 class="app-card__title">Recent Transactions</h2>
                        </div>
                        <div class="app-table-wrapper">
                            <table class="app-table">
                                <thead><tr><th>Date</th><th>Description</th><th>Reference</th><th>Amount</th><th>Status</th></tr></thead>
                                <tbody>
                                    <tr><td>Jun 28, 2026</td><td><strong>Wallet Top-Up</strong><br><span style="color:var(--neutral-500);font-size:12px;">Bank Transfer ACH</span></td><td>TXN-90210</td><td style="color:var(--success);font-weight:600;">+$25,000.00</td><td><span class="status-badge status-badge--success">Cleared</span></td></tr>
                                    <tr><td>Jun 25, 2026</td><td><strong>Datadog Renewal</strong><br><span style="color:var(--neutral-500);font-size:12px;">Auto-deduction</span></td><td>ORD-5541</td><td style="color:var(--neutral-800);font-weight:600;">-$4,200.00</td><td><span class="status-badge status-badge--neutral">Processed</span></td></tr>
                                    <tr><td>Jun 12, 2026</td><td><strong>Wallet Top-Up</strong><br><span style="color:var(--neutral-500);font-size:12px;">Credit Card ending in 4242</span></td><td>TXN-88122</td><td style="color:var(--success);font-weight:600;">+$5,000.00</td><td><span class="status-badge status-badge--success">Cleared</span></td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="app-card">
                        <div class="app-card__header"><h2 class="app-card__title">Payment Methods</h2></div>
                        <div class="app-card__body">
                            <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;border:1px solid var(--neutral-200);border-radius:var(--radius-md);margin-bottom:12px;background:var(--white);">
                                <div style="display:flex;align-items:center;gap:12px;">
                                    <div style="width:40px;height:24px;background:#1434CB;color:white;display:flex;align-items:center;justify-content:center;border-radius:4px;font-size:10px;font-style:italic;font-weight:bold;">VISA</div>
                                    <div style="display:flex;flex-direction:column;"><span style="font-weight:600;font-size:14px;">Visa ending in 4242</span><span style="font-size:12px;color:var(--neutral-500);">Expires 12/28</span></div>
                                </div>
                                <span class="status-badge status-badge--neutral">Default</span>
                            </div>
                            <div style="display:flex;align-items:center;justify-content:space-between;padding:12px;border:1px solid var(--neutral-200);border-radius:var(--radius-md);margin-bottom:12px;background:var(--white);">
                                <div style="display:flex;align-items:center;gap:12px;">
                                    <div style="width:40px;height:24px;background:var(--neutral-800);color:white;display:flex;align-items:center;justify-content:center;border-radius:4px;font-size:10px;font-weight:bold;">ACH</div>
                                    <div style="display:flex;flex-direction:column;"><span style="font-weight:600;font-size:14px;">Chase Corporate</span><span style="font-size:12px;color:var(--neutral-500);">Account ending in 9901</span></div>
                                </div>
                            </div>
                            <button class="btn btn--outline" style="width:100%;justify-content:center;">+ Add Payment Method</button>
                        </div>
                    </div>
                </div>
'''
with open("wallet.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("wallet.html", wallet_content))


# Write app_orders.html
orders_content = '''
                <div class="app-card">
                    <div class="app-card__header" style="flex-wrap: wrap; gap: 16px;">
                        <h2 class="app-card__title">All Orders</h2>
                        <div style="display: flex; gap: 8px;">
                            <input type="date" class="app-input" style="width: 150px; padding: 6px 12px;">
                            <select class="app-input" style="width: 150px; padding: 6px 12px;">
                                <option>All Statuses</option>
                                <option>Processing</option>
                                <option>Completed</option>
                            </select>
                            <button class="btn btn--secondary">Filter</button>
                            <button class="btn btn--primary">Export CSV</button>
                        </div>
                    </div>
                    <div class="app-table-wrapper">
                        <table class="app-table">
                            <thead>
                                <tr>
                                    <th>Order ID</th>
                                    <th>Date</th>
                                    <th>Vendor</th>
                                    <th>Customer</th>
                                    <th>Total</th>
                                    <th>Status</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td style="font-weight:600;color:var(--primary-500);">#ORD-8902</td>
                                    <td>Jun 28, 2026</td>
                                    <td>Microsoft</td>
                                    <td>Acme Corp</td>
                                    <td style="font-weight:600;">$14,500.00</td>
                                    <td><span class="status-badge status-badge--success">Completed</span></td>
                                    <td><button class="btn btn--ghost btn--sm">View</button></td>
                                </tr>
                                <tr>
                                    <td style="font-weight:600;color:var(--primary-500);">#ORD-8903</td>
                                    <td>Jun 28, 2026</td>
                                    <td>AWS</td>
                                    <td>Global Tech</td>
                                    <td style="font-weight:600;">$2,450.00</td>
                                    <td><span class="status-badge status-badge--warning">Processing</span></td>
                                    <td><button class="btn btn--ghost btn--sm">View</button></td>
                                </tr>
                                <tr>
                                    <td style="font-weight:600;color:var(--primary-500);">#ORD-8904</td>
                                    <td>Jun 27, 2026</td>
                                    <td>Slack</td>
                                    <td>Startup Inc</td>
                                    <td style="font-weight:600;">$840.00</td>
                                    <td><span class="status-badge status-badge--success">Completed</span></td>
                                    <td><button class="btn btn--ghost btn--sm">View</button></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div style="padding: 16px 24px; border-top: 1px solid var(--neutral-100); display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 13px; color: var(--neutral-500);">Showing 1-3 of 145 orders</span>
                        <div style="display: flex; gap: 4px;">
                            <button class="btn btn--secondary btn--sm" disabled>Previous</button>
                            <button class="btn btn--primary btn--sm">1</button>
                            <button class="btn btn--secondary btn--sm">2</button>
                            <button class="btn btn--secondary btn--sm">3</button>
                            <button class="btn btn--secondary btn--sm">Next</button>
                        </div>
                    </div>
                </div>
'''
with open("app_orders.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("app_orders.html", orders_content))

# Similar generation for products, customers, renewals, profile
# I will just write them quickly

products_content = '''
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                    <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 800; color: var(--neutral-900);">Product Catalog</h2>
                    <button class="btn btn--primary">Add Product Request</button>
                </div>
                
                <div style="display: grid; grid-template-columns: 260px 1fr; gap: 24px;">
                    <div class="app-card" style="align-self: start; position: sticky; top: 100px;">
                        <div class="app-card__header"><h3 style="font-size: 14px; font-weight: 700;">Filters</h3></div>
                        <div class="app-card__body" style="display: flex; flex-direction: column; gap: 16px;">
                            <div class="app-form-group">
                                <label class="app-label">Category</label>
                                <select class="app-input"><option>All Categories</option><option>Productivity</option><option>Cloud Infrastructure</option></select>
                            </div>
                            <div class="app-form-group">
                                <label class="app-label">Vendor</label>
                                <select class="app-input"><option>All Vendors</option><option>Microsoft</option><option>AWS</option></select>
                            </div>
                            <div class="app-form-group">
                                <label class="app-label">Billing Cycle</label>
                                <div>
                                    <label style="display:flex;align-items:center;gap:8px;font-size:13px;margin-bottom:8px;"><input type="checkbox"> Monthly</label>
                                    <label style="display:flex;align-items:center;gap:8px;font-size:13px;"><input type="checkbox"> Annual</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px;">
                        <div class="app-card" style="margin-bottom:0; display:flex; flex-direction:column; padding: 20px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:16px;">
                                <div style="width:48px;height:48px;background:var(--neutral-50);border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:bold;">M</div>
                                <span class="status-badge status-badge--success">Available</span>
                            </div>
                            <h3 style="font-weight:700;font-size:16px;margin-bottom:4px;">Microsoft 365 E3</h3>
                            <p style="font-size:13px;color:var(--neutral-500);margin-bottom:16px;flex-grow:1;">Enterprise productivity suite with advanced security.</p>
                            <div style="display:flex;align-items:end;justify-content:space-between;border-top:1px solid var(--neutral-100);padding-top:16px;">
                                <div><div style="font-size:12px;color:var(--neutral-500);">Price</div><div style="font-weight:800;font-size:18px;">$36.00<span style="font-size:12px;font-weight:normal;color:var(--neutral-500);">/user/mo</span></div></div>
                                <button class="btn btn--outline btn--sm">Order</button>
                            </div>
                        </div>
                        
                        <div class="app-card" style="margin-bottom:0; display:flex; flex-direction:column; padding: 20px;">
                            <div style="display:flex; justify-content:space-between; margin-bottom:16px;">
                                <div style="width:48px;height:48px;background:var(--neutral-50);border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:bold;color:#FF9900;">AWS</div>
                                <span class="status-badge status-badge--success">Available</span>
                            </div>
                            <h3 style="font-weight:700;font-size:16px;margin-bottom:4px;">AWS Reserved Instances</h3>
                            <p style="font-size:13px;color:var(--neutral-500);margin-bottom:16px;flex-grow:1;">Compute capacity with significant discount over On-Demand.</p>
                            <div style="display:flex;align-items:end;justify-content:space-between;border-top:1px solid var(--neutral-100);padding-top:16px;">
                                <div><div style="font-size:12px;color:var(--neutral-500);">Price</div><div style="font-weight:800;font-size:18px;">Custom</div></div>
                                <button class="btn btn--outline btn--sm">Quote</button>
                            </div>
                        </div>
                    </div>
                </div>
'''
with open("products.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("products.html", products_content))

customers_content = '''
                <div class="app-card">
                    <div class="app-card__header">
                        <h2 class="app-card__title">Customers Directory</h2>
                        <button class="btn btn--primary btn--sm">+ Add Customer</button>
                    </div>
                    <div class="app-table-wrapper">
                        <table class="app-table">
                            <thead>
                                <tr><th>Company</th><th>Contact</th><th>Active Subs</th><th>Lifetime Spend</th><th>Last Activity</th><th></th></tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><div style="display:flex;align-items:center;gap:12px;"><div style="width:32px;height:32px;background:var(--neutral-100);border-radius:4px;display:flex;align-items:center;justify-content:center;font-weight:bold;color:var(--neutral-600);">A</div><strong>Acme Corp</strong></div></td>
                                    <td>jane@acme.com</td>
                                    <td><span class="status-badge status-badge--info">12 Subs</span></td>
                                    <td style="font-weight:600;">$142,500</td>
                                    <td>Today</td>
                                    <td><button class="btn btn--ghost btn--sm">Manage</button></td>
                                </tr>
                                <tr>
                                    <td><div style="display:flex;align-items:center;gap:12px;"><div style="width:32px;height:32px;background:var(--neutral-100);border-radius:4px;display:flex;align-items:center;justify-content:center;font-weight:bold;color:var(--neutral-600);">G</div><strong>Global Tech</strong></div></td>
                                    <td>admin@global.tech</td>
                                    <td><span class="status-badge status-badge--info">4 Subs</span></td>
                                    <td style="font-weight:600;">$24,000</td>
                                    <td>2 days ago</td>
                                    <td><button class="btn btn--ghost btn--sm">Manage</button></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
'''
with open("app_customers.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("app_customers.html", customers_content))

renewals_content = '''
                <div class="dashboard-grid">
                    <div class="stat-card">
                        <div class="stat-card__info"><span class="stat-card__title">Renewing Next 30 Days</span><span class="stat-card__value" style="color:var(--error);">3</span></div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-card__info"><span class="stat-card__title">Upcoming Value</span><span class="stat-card__value">$18,400</span></div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-card__info"><span class="stat-card__title">Successfully Renewed</span><span class="stat-card__value" style="color:var(--success);">45</span></div>
                    </div>
                </div>
                
                <div class="app-card">
                    <div class="app-card__header">
                        <h2 class="app-card__title">Renewal Action Center</h2>
                        <div style="display:flex;gap:8px;"><button class="btn btn--secondary btn--sm">Export</button></div>
                    </div>
                    <div class="app-table-wrapper">
                        <table class="app-table">
                            <thead><tr><th>Subscription</th><th>Customer</th><th>Renewal Date</th><th>Value</th><th>Status</th><th>Actions</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td><strong>Microsoft 365 E3</strong><br><span style="font-size:12px;color:var(--neutral-500);">100 Seats</span></td>
                                    <td>Acme Corp</td>
                                    <td><span style="color:var(--error);font-weight:700;">Jul 1, 2026 (3 days)</span></td>
                                    <td style="font-weight:600;">$3,600.00</td>
                                    <td><span class="status-badge status-badge--error">Action Required</span></td>
                                    <td><button class="btn btn--primary btn--sm">Renew Now</button> <button class="btn btn--ghost btn--sm">Notify</button></td>
                                </tr>
                                <tr>
                                    <td><strong>AWS Support Enterprise</strong><br><span style="font-size:12px;color:var(--neutral-500);">Annual</span></td>
                                    <td>Global Tech</td>
                                    <td><span style="color:var(--warning);font-weight:700;">Jul 15, 2026</span></td>
                                    <td style="font-weight:600;">$15,000.00</td>
                                    <td><span class="status-badge status-badge--warning">Upcoming</span></td>
                                    <td><button class="btn btn--secondary btn--sm">Renew Now</button></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
'''
with open("renewals.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("renewals.html", renewals_content))

profile_content = '''
                <div style="display: grid; grid-template-columns: 250px 1fr; gap: 32px;">
                    <div>
                        <div class="app-card" style="margin-bottom:16px;">
                            <div class="app-card__body" style="display:flex;flex-direction:column;align-items:center;text-align:center;">
                                <div style="width:80px;height:80px;background:var(--primary-100);color:var(--primary-600);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:32px;margin-bottom:16px;">SM</div>
                                <h3 style="font-weight:700;font-size:18px;">Sarah Miller</h3>
                                <p style="font-size:13px;color:var(--neutral-500);">Procurement Manager<br>SaaSOrder Inc.</p>
                            </div>
                        </div>
                        <nav style="display:flex;flex-direction:column;gap:4px;">
                            <a href="#" style="padding:10px 16px;background:var(--primary-50);color:var(--primary-600);font-weight:600;border-radius:var(--radius-md);">Personal Info</a>
                            <a href="#" style="padding:10px 16px;color:var(--neutral-600);font-weight:500;border-radius:var(--radius-md);">Security & 2FA</a>
                            <a href="#" style="padding:10px 16px;color:var(--neutral-600);font-weight:500;border-radius:var(--radius-md);">API Keys</a>
                        </nav>
                    </div>
                    
                    <div>
                        <div class="app-card">
                            <div class="app-card__header"><h2 class="app-card__title">Personal Information</h2></div>
                            <div class="app-card__body">
                                <div class="app-form-grid">
                                    <div class="app-form-group"><label class="app-label">First Name</label><input type="text" class="app-input" value="Sarah"></div>
                                    <div class="app-form-group"><label class="app-label">Last Name</label><input type="text" class="app-input" value="Miller"></div>
                                    <div class="app-form-group"><label class="app-label">Email</label><input type="email" class="app-input" value="sarah@saasorder.com"></div>
                                    <div class="app-form-group"><label class="app-label">Phone</label><input type="tel" class="app-input" value="+1 (555) 123-4567"></div>
                                </div>
                                <button class="btn btn--primary" style="margin-top:24px;">Save Changes</button>
                            </div>
                        </div>
                    </div>
                </div>
'''
with open("profile.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("profile.html", profile_content))
    
vendors_content = '''
                <div class="app-card">
                    <div class="app-card__header">
                        <h2 class="app-card__title">Vendor Ecosystem</h2>
                        <button class="btn btn--primary btn--sm">+ Onboard Vendor</button>
                    </div>
                    <div class="app-table-wrapper">
                        <table class="app-table">
                            <thead><tr><th>Vendor Name</th><th>Category</th><th>Active Contracts</th><th>Spend YTD</th><th>Status</th></tr></thead>
                            <tbody>
                                <tr>
                                    <td><strong>Microsoft</strong></td>
                                    <td>Productivity</td>
                                    <td>14</td>
                                    <td style="font-weight:600;">$124,000</td>
                                    <td><span class="status-badge status-badge--success">Active</span></td>
                                </tr>
                                <tr>
                                    <td><strong>Amazon Web Services</strong></td>
                                    <td>Infrastructure</td>
                                    <td>8</td>
                                    <td style="font-weight:600;">$350,000</td>
                                    <td><span class="status-badge status-badge--success">Active</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
'''
with open("app_vendors.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("app_vendors.html", vendors_content))
    
erp_content = '''
                <div class="app-card">
                    <div class="app-card__header">
                        <h2 class="app-card__title">ERP Integrations</h2>
                    </div>
                    <div class="app-card__body">
                        <p style="color:var(--neutral-600);margin-bottom:24px;">Connect SaaSOrder to your accounting and ERP systems for automated invoice synchronization.</p>
                        
                        <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">
                            <div style="border:1px solid var(--neutral-200);border-radius:var(--radius-lg);padding:24px;display:flex;flex-direction:column;align-items:center;text-align:center;">
                                <div style="width:64px;height:64px;background:#F9FAFB;border-radius:12px;margin-bottom:16px;display:flex;align-items:center;justify-content:center;font-weight:800;color:#0078D4;">NetSuite</div>
                                <h3 style="font-weight:700;margin-bottom:8px;">Oracle NetSuite</h3>
                                <p style="font-size:13px;color:var(--neutral-500);margin-bottom:16px;">Sync invoices and purchase orders directly to NetSuite.</p>
                                <span class="status-badge status-badge--success" style="margin-bottom:16px;">Connected</span>
                                <button class="btn btn--outline btn--sm">Configure</button>
                            </div>
                            
                            <div style="border:1px solid var(--neutral-200);border-radius:var(--radius-lg);padding:24px;display:flex;flex-direction:column;align-items:center;text-align:center;">
                                <div style="width:64px;height:64px;background:#F9FAFB;border-radius:12px;margin-bottom:16px;display:flex;align-items:center;justify-content:center;font-weight:800;color:#2CA01C;">QB</div>
                                <h3 style="font-weight:700;margin-bottom:8px;">QuickBooks Online</h3>
                                <p style="font-size:13px;color:var(--neutral-500);margin-bottom:16px;">Automate billing and ledger entries with QuickBooks.</p>
                                <button class="btn btn--secondary btn--sm" style="margin-top:auto;">Connect</button>
                            </div>
                        </div>
                    </div>
                </div>
'''
with open("app_erp.html", "w", encoding="utf-8") as f:
    f.write(generate_layout("app_erp.html", erp_content))
