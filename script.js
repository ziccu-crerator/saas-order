/* ============================================================
   SaaSOrder Enterprise Website — JavaScript
   ============================================================
   - Sticky header with scroll detection
   - Mobile menu toggle
   - Scroll-triggered animations (IntersectionObserver)
   - Stats counter animation
   - FAQ accordion
   - Smooth scrolling for anchor links
   - Journey timeline animation
   - Active nav state tracking
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ── CURRENCY MANAGEMENT SYSTEM ──
    const currencyRates = {
        'USD': { symbol: '$', rate: 1 },
        'AED': { symbol: 'AED ', rate: 3.67 },
        'INR': { symbol: '₹', rate: 83.2 }
    };

    let currentCurrency = localStorage.getItem('current_currency') || 'USD';
    if (!currencyRates[currentCurrency]) {
        currentCurrency = 'USD';
        localStorage.setItem('current_currency', 'USD');
    }

    function formatMoney(value, currency, compact = false) {
        const c = currencyRates[currency];
        const converted = value * c.rate;
        
        if (compact) {
            if (currency === 'INR') {
                if (converted >= 10000000) return c.symbol + (converted / 10000000).toFixed(1) + 'Cr';
                if (converted >= 100000) return c.symbol + (converted / 100000).toFixed(1) + 'L';
                if (converted >= 1000) return c.symbol + (converted / 1000).toFixed(1) + 'k';
            } else {
                if (converted >= 1000000) return c.symbol + (converted / 1000000).toFixed(1) + 'M';
                if (converted >= 1000) return c.symbol + (converted / 1000).toFixed(1) + 'k';
            }
        }
        
        const locale = (currency === 'INR') ? 'en-IN' : 'en-US';
        return c.symbol + converted.toLocaleString(locale, {minimumFractionDigits: 0, maximumFractionDigits: 2});
    }

    window.formatMoney = formatMoney; // Make formatMoney globally accessible

    function updateAllPrices(currency) {
        const moneyElements = document.querySelectorAll('.money');
        moneyElements.forEach(el => {
            let value = parseFloat(el.getAttribute('data-value'));
            if (isNaN(value)) {
                value = parseFloat(el.dataset.value);
            }
            if (!isNaN(value)) {
                const compact = el.classList.contains('money-compact') || el.hasAttribute('data-compact');
                el.textContent = formatMoney(value, currency, compact);
            }
        });
        
        // Also update ROI calculator displays if they exist on the page
        const spendValue = document.getElementById('calc-spend-value');
        const spendSlider = document.getElementById('calc-spend');
        if (spendValue && spendSlider) {
            const spend = parseFloat(spendSlider.value);
            spendValue.textContent = formatMoney(spend, currency);
        }
        const savingsAmount = document.getElementById('savings-amount');
        const vendorsSelect = document.getElementById('calc-vendors');
        if (savingsAmount && spendSlider && vendorsSelect) {
            const spend = parseFloat(spendSlider.value);
            const calculatedSavings = spend * 0.18;
            savingsAmount.textContent = formatMoney(calculatedSavings, currency);
        }
    }

    // Inject currency selector into public headers
    const headerActions = document.querySelector('.header__actions');
    if (headerActions && !document.getElementById('global-currency-selector')) {
        const selector = document.createElement('select');
        selector.id = 'global-currency-selector';
        selector.className = 'currency-selector';
        selector.style.cssText = "padding: 6px 10px; border-radius: var(--radius-md); border: 1px solid var(--neutral-200); outline: none; background: white; color: var(--neutral-700); font-weight: 500; font-size: 13px; font-family: 'Inter', sans-serif; cursor: pointer; margin-right: 8px;";
        selector.innerHTML = `
            <option value="USD">USD ($)</option>
            <option value="AED">AED (AED)</option>
            <option value="INR">INR (₹)</option>
        `;
        headerActions.insertBefore(selector, headerActions.firstChild);
    }

    // Sync all selectors on the page
    const allSelectors = document.querySelectorAll('#global-currency-selector, #currency-selector');
    allSelectors.forEach(sel => {
        sel.value = currentCurrency;
        sel.addEventListener('change', (e) => {
            currentCurrency = e.target.value;
            localStorage.setItem('current_currency', currentCurrency);
            allSelectors.forEach(s => s.value = currentCurrency);
            updateAllPrices(currentCurrency);
        });
    });

    // Run initial price update
    updateAllPrices(currentCurrency);

    // ── SCROLL TO TOP BUTTON ──
    const scrollTopBtn = document.createElement('div');
    scrollTopBtn.className = 'scroll-to-top';
    scrollTopBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width: 20px; height: 20px;"><polyline points="18 15 12 9 6 15"></polyline></svg>';
    document.body.appendChild(scrollTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ── 1. STICKY HEADER ──
    const header = document.getElementById('header');

    function toggleHeaderSolid() {
        if (!header) return;
        if (window.scrollY > 30) {
            header.classList.add('header--solid');
        } else {
            header.classList.remove('header--solid');
        }
    }

    window.addEventListener('scroll', toggleHeaderSolid, { passive: true });
    toggleHeaderSolid();

    // ── 2. MOBILE MENU ──
    const menuToggle = document.getElementById('menuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const mobileOverlay = document.getElementById('mobileOverlay');
    const mobileLinks = document.querySelectorAll('.mobile-menu__link');

    function openMobileMenu() {
        if (!menuToggle || !mobileMenu || !mobileOverlay) return;
        menuToggle.classList.add('active');
        mobileMenu.classList.add('active');
        mobileOverlay.classList.add('active');
        menuToggle.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
    }

    function closeMobileMenu() {
        if (!menuToggle || !mobileMenu || !mobileOverlay) return;
        menuToggle.classList.remove('active');
        mobileMenu.classList.remove('active');
        mobileOverlay.classList.remove('active');
        menuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    }

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            const isOpen = mobileMenu.classList.contains('active');
            isOpen ? closeMobileMenu() : openMobileMenu();
        });
    }

    if (mobileOverlay) {
        mobileOverlay.addEventListener('click', closeMobileMenu);
    }

    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('active')) {
            closeMobileMenu();
        }
    });

    // ── 3. SCROLL ANIMATIONS ──
    const animateElements = document.querySelectorAll('.animate-on-scroll');

    if (animateElements.length > 0) {
        const scrollObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        scrollObserver.unobserve(entry.target);
                    }
                });
            },
            {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            }
        );

        animateElements.forEach(el => scrollObserver.observe(el));
    }

    // ── 4. JOURNEY TIMELINE ANIMATION ──
    const timeline = document.getElementById('journeyTimeline');

    if (timeline) {
        const timelineObserver = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting) {
                    timeline.classList.add('animated');
                    timelineObserver.unobserve(timeline);
                }
            },
            { threshold: 0.2 }
        );
        timelineObserver.observe(timeline);
    }

    // ── 5. STATS COUNTER ANIMATION ──
    const statsNumbers = document.querySelectorAll('.stats__number[data-target]');
    let statsCounted = false;

    function animateCounter(element) {
        const target = parseFloat(element.dataset.target);
        const suffix = element.dataset.suffix || '';
        const isDecimal = element.dataset.decimal === 'true';
        const duration = 2200;
        const startTime = performance.now();

        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Ease-out cubic
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const currentValue = target * easeOut;

            if (isDecimal) {
                element.textContent = currentValue.toFixed(1) + suffix;
            } else {
                element.textContent = Math.floor(currentValue).toLocaleString() + suffix;
            }

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                if (isDecimal) {
                    element.textContent = target.toFixed(1) + suffix;
                } else {
                    element.textContent = target.toLocaleString() + suffix;
                }
            }
        }

        requestAnimationFrame(updateCounter);
    }

    const statsSection = document.getElementById('stats') || document.getElementById('statsGrid');
    if (statsSection && statsNumbers.length > 0) {
        const statsObserver = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting && !statsCounted) {
                    statsCounted = true;
                    statsNumbers.forEach(el => animateCounter(el));
                    statsObserver.unobserve(statsSection);
                }
            },
            { threshold: 0.2 }
        );
        statsObserver.observe(statsSection);
    }

    // ── 6. FAQ ACCORDION ──
    const faqItems = document.querySelectorAll('.faq__item');

    faqItems.forEach(item => {
        const btn = item.querySelector('.faq__question');
        const answer = item.querySelector('.faq__answer');

        if (!btn) return;

        btn.addEventListener('click', () => {
            const isOpen = item.classList.contains('active');

            // Close all others
            faqItems.forEach(other => {
                if (other !== item) {
                    other.classList.remove('active');
                    const otherBtn = other.querySelector('.faq__question');
                    if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
                }
            });

            // Toggle current
            item.classList.toggle('active', !isOpen);
            btn.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
        });

        btn.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                btn.click();
            }
        });
    });

    // ── 7. SMOOTH SCROLLING FOR ANCHOR LINKS ──
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ── 8. HEADER NAV ACTIVE STATE ──
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.header__nav-link');

    if (sections.length > 0 && navLinks.length > 0) {
        const activeObserver = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.getAttribute('id');
                        navLinks.forEach(link => {
                            link.classList.toggle('active',
                                link.getAttribute('href') === '#' + id
                            );
                        });
                    }
                });
            },
            {
                threshold: 0.15,
                rootMargin: '-80px 0px -50% 0px'
            }
        );

        sections.forEach(section => activeObserver.observe(section));
    }

    // ── 9. SCROLL TO TOP ──
    const scrollToTopBtn = document.getElementById('scrollToTop');

    if (scrollToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                scrollToTopBtn.classList.add('visible');
            } else {
                scrollToTopBtn.classList.remove('visible');
            }
        }, { passive: true });

        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // ── 10. B2B SPEND & ROI CALCULATOR ──
    const spendSlider = document.getElementById('calc-spend');
    const spendValue = document.getElementById('calc-spend-value');
    const vendorsSelect = document.getElementById('calc-vendors');
    
    const savingsAmount = document.getElementById('savings-amount');
    const consolidationRatio = document.getElementById('consolidation-ratio');
    const hoursSavedVal = document.getElementById('hours-saved');

    function updateCalculator() {
        if (!spendSlider || !spendValue || !vendorsSelect) return;

        const spend = parseFloat(spendSlider.value);
        const vendors = parseInt(vendorsSelect.value);

        // Update Slider Track Fill Gradient dynamically matching the brand color
        const fillPercent = (spend - spendSlider.min) / (spendSlider.max - spendSlider.min) * 100;
        spendSlider.style.background = `linear-gradient(to right, var(--primary-500) 0%, var(--primary-500) ${fillPercent}%, var(--neutral-200) ${fillPercent}%, var(--neutral-200) 100%)`;

        // Update display text for Spend using global currency
        spendValue.textContent = formatMoney(spend, currentCurrency);

        // ROI Math
        const calculatedSavings = spend * 0.18;
        const calculatedHours = vendors * 15;

        // Display Savings using global currency
        if (savingsAmount) {
            savingsAmount.textContent = formatMoney(calculatedSavings, currentCurrency);
        }
        
        // Update other metrics
        if (consolidationRatio) {
            consolidationRatio.textContent = `From ${vendors} contracts to 1 MSA`;
        }
        if (hoursSavedVal) {
            hoursSavedVal.textContent = `${calculatedHours} hrs / year`;
        }
    }

    function animateNumericValue(element, target, prefix = '') {
        if (!element) return;
        const currentText = element.textContent.replace(/[^0-9.]/g, '');
        const start = parseFloat(currentText) || 0;
        const duration = 400; // shorter animation for quick slider slide
        const startTime = performance.now();

        function updateAnim(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease-out
            const ease = 1 - Math.pow(1 - progress, 3);
            const val = start + (target - start) * ease;
            
            element.textContent = prefix + Math.floor(val).toLocaleString();

            if (progress < 1) {
                requestAnimationFrame(updateAnim);
            } else {
                element.textContent = prefix + Math.floor(target).toLocaleString();
            }
        }
        requestAnimationFrame(updateAnim);
    }

    if (spendSlider && vendorsSelect) {
        spendSlider.addEventListener('input', updateCalculator);
        vendorsSelect.addEventListener('change', updateCalculator);
        // Initialize values
        updateCalculator();
    }

    // ── 11. VENDOR MARKETPLACE FILTERING ──
    const filterBtns = document.querySelectorAll('.vendor-cat');
    const logoCards = document.querySelectorAll('.trust__logo-card');
    
    if (filterBtns.length > 0 && logoCards.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const filter = btn.dataset.filter;
                
                // Toggle active class
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                // Filter cards
                logoCards.forEach(card => {
                    const cat = card.dataset.cat;
                    if (filter === 'all' || cat === filter) {
                        card.style.display = '';
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95) translateY(5px)';
                        setTimeout(() => {
                            card.style.transition = 'all var(--duration-normal) var(--ease-default)';
                            card.style.opacity = '1';
                            card.style.transform = '';
                        }, 20);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // ── 11.5 VENDOR MSA STACK BUILDER WIDGET ──
    const msaDefaultState = document.getElementById('msaDefaultState');
    const msaSelectedState = document.getElementById('msaSelectedState');
    const selectedVendorsPills = document.getElementById('selectedVendorsPills');
    const msaContractsVal = document.getElementById('msa-contracts-val');
    const msaReviewsVal = document.getElementById('msa-reviews-val');
    const msaHoursVal = document.getElementById('msa-hours-val');
    const msaRequestQuoteBtn = document.getElementById('msaRequestQuoteBtn');

    let selectedVendors = [];

    if (logoCards.length > 0 && msaDefaultState && msaSelectedState) {
        logoCards.forEach(card => {
            card.addEventListener('click', () => {
                card.classList.toggle('selected');
                
                const name = card.dataset.name;
                const color = card.style.getPropertyValue('--vendor-glow') || 'var(--primary-500)';
                
                if (card.classList.contains('selected')) {
                    if (!selectedVendors.some(v => v.name === name)) {
                        selectedVendors.push({ name, color });
                    }
                } else {
                    selectedVendors = selectedVendors.filter(v => v.name !== name);
                }
                
                updateMsaWidget();
            });
        });
    }

    function updateMsaWidget() {
        if (!msaDefaultState || !msaSelectedState) return;

        const count = selectedVendors.length;

        if (count === 0) {
            msaSelectedState.style.display = 'none';
            msaDefaultState.style.display = 'block';
        } else {
            msaDefaultState.style.display = 'none';
            msaSelectedState.style.display = 'block';

            // Generate pills
            if (selectedVendorsPills) {
                selectedVendorsPills.innerHTML = '';
                selectedVendors.forEach(vendor => {
                    const pill = document.createElement('div');
                    pill.className = 'selected-vendor-pill';
                    const solidColor = vendor.color.replace('0.22', '1').replace('0.25', '1');
                    pill.style.setProperty('--dot-color', solidColor);
                    pill.innerHTML = `<span class="selected-vendor-pill__dot"></span>${vendor.name}`;
                    selectedVendorsPills.appendChild(pill);
                });
            }

            // Update stats
            if (msaContractsVal) {
                msaContractsVal.innerHTML = `${count} Contracts → <span class="text-gradient">1 MSA</span>`;
            }
            if (msaReviewsVal) {
                msaReviewsVal.innerHTML = `${count} Reviews → <span class="text-gradient">1 Audit</span>`;
            }
            if (msaHoursVal) {
                msaHoursVal.textContent = `${count * 15} Hours Saved / Yr`;
            }
        }
    }

    if (msaRequestQuoteBtn) {
        msaRequestQuoteBtn.addEventListener('click', () => {
            const vendorList = selectedVendors.map(v => v.name).join(', ');
            const message = encodeURIComponent(`Hi, I am building a technology stack and am interested in procuring a unified Master Service Agreement (MSA) quote through SaaSOrder for the following vendors: ${vendorList}. Please reach out with next steps.`);
            window.location.href = `contact.html?subject=demo&message=${message}`;
        });
    }

    // ── 12. DYNAMIC QUERY PARAMETER POPULATION FOR CONTACT FORM ──
    const urlParams = new URLSearchParams(window.location.search);
    const subjectParam = urlParams.get('subject');
    const messageParam = urlParams.get('message');

    if (subjectParam) {
        const subjectSelect = document.getElementById('contact-subject');
        if (subjectSelect) {
            subjectSelect.value = subjectParam;
        }
    }
    if (messageParam) {
        const messageTextarea = document.getElementById('contact-message');
        if (messageTextarea) {
            messageTextarea.value = decodeURIComponent(messageParam);
        }
    }

    // ── GENERIC BUTTON & PLACEHOLDER LINK HANDLER ──
    document.addEventListener('click', (e) => {
        // Handle buttons without default behavior
        const button = e.target.closest('button');
        if (button) {
            if (button.type === 'submit') return;
            if (!button.onclick && button.id !== 'menuToggle' && !button.id.startsWith('faq-btn')) {
                e.preventDefault();
                alert('This button is currently a mockup and will be fully functional in the final application.');
            }
        }

        // Handle placeholder links
        const link = e.target.closest('a');
        if (link && link.getAttribute('href') === '#') {
            e.preventDefault();
            alert('This link is currently a placeholder.');
        }
    });

    // ── 13. SIDEBAR TOGGLE ──
    const sidebar = document.getElementById('appSidebar');
    const main = document.querySelector('.app-main');
    if (sidebar && main) {
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'sidebar-toggle-btn';
        toggleBtn.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>';
        
        sidebar.appendChild(toggleBtn);
        
        toggleBtn.addEventListener('click', () => {
            document.body.classList.toggle('sidebar-collapsed');
        });

        // Add mobile close button dynamically inside header
        const sidebarHeader = sidebar.querySelector('.app-sidebar__header');
        if (sidebarHeader) {
            const closeBtn = document.createElement('button');
            closeBtn.className = 'mobile-sidebar-close';
            closeBtn.innerHTML = '<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round"></path></svg>';
            sidebarHeader.appendChild(closeBtn);

            closeBtn.addEventListener('click', () => {
                sidebar.classList.remove('active');
            });
        }

        // Close sidebar drawer if clicking main content area on mobile
        main.addEventListener('click', (e) => {
            // Ignore if clicking the toggle button itself
            if (e.target.closest('.mobile-menu-toggle')) return;
            // Only trigger close if sidebar is active (drawer mode) and we aren't clicking a link inside main that does something else
            if (sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
            }
        });
    }

});
