/* ================================================================
   AI Digest – Modern JS
   • Dark/Light theme toggle (persists to localStorage)
   • Sidebar live date
   • Reading progress bar
   • Back-to-top button
   • Mobile navigation drawer
   • Sort buttons (no-op hook for future server-side sort)
   • Legacy paper card upgrader (old markdown → two-column HTML)
   ================================================================ */
(function () {
  'use strict';

  /* ── 0. Category → CSS class map ─────────────────────────── */
  var CAT_MAP = {
    'cs.ai':      'cat-ai',
    'cs.cl':      'cat-nlp',
    'cs.cv':      'cat-cv',
    'cs.lg':      'cat-ml',
    'stat.ml':    'cat-ml',
    'cs.ro':      'cat-ro',
    'cs.hc':      'cat-hci',
    'cs.se':      'cat-se',
    'cs.ir':      'cat-ir',
    'cs.dc':      'cat-dc',
    'cs.ne':      'cat-ne',
    'cs.cr':      'cat-security',
    'cs.it':      'cat-eess',
    'eess.':      'cat-eess',
    'math.':      'cat-math',
    'q-bio.':     'cat-bio',
    'physics.':   'cat-physics',
  };

  function catClass(raw) {
    var key = (raw || '').toLowerCase().split(/\s+/)[0];
    for (var prefix in CAT_MAP) {
      if (Object.prototype.hasOwnProperty.call(CAT_MAP, prefix) && key.startsWith(prefix)) {
        return CAT_MAP[prefix];
      }
    }
    return 'cat-default';
  }

  /* ── 0b. PDF SVG icon (inline, no external request) ─────── */
  var PDF_SVG = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3.75 1.5a.25.25 0 0 0-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25V6H9.75A1.75 1.75 0 0 1 8 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237V13.25A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25V1.75z"/><path d="M4.5 8.75a.75.75 0 0 1 .75-.75h1a2.25 2.25 0 0 1 0 4.5h-.25V13.5a.75.75 0 0 1-1.5 0v-4.75zm1.5.75v1.5h.25a.75.75 0 0 0 0-1.5H6z"/></svg>';
  var GH_SVG  = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>';

  /* ── 0c. Upgrade legacy paper cards ─────────────────────── */
  /*
   * Old format inside .paper-item:
   *   <p><strong>[R: ●●●●○]</strong> <code>cs.AI</code> · Date</p>
   *   <h4><a href="…arxiv…">Title</a></h4>
   *   <p>Authors: … · <a href="…arxiv…">arxiv…</a></p>
   *   <details><summary>Abstract</summary>…</details>
   *
   * New format: .paper-item > .paper-body + .paper-actions
   */
  function upgradePaperCards() {
    document.querySelectorAll('.paper-item').forEach(function (card) {
      // Already upgraded by render_paper() — has .paper-body child
      if (card.querySelector('.paper-body')) return;

      /*
       * Jekyll (kramdown) does NOT process markdown inside raw HTML block elements,
       * so the card's inner content is raw markdown text, not rendered HTML.
       * We therefore regex-parse card.innerHTML directly instead of using querySelector.
       */
      var raw = card.innerHTML;

      /* 1. Relevance dots — match **[R: ●●●●○]** */
      var dotsMatch = raw.match(/\*\*\[R:\s*([●○]+)\]\*\*/);
      var dotsStr   = dotsMatch ? dotsMatch[1] : '';
      var filled    = (dotsStr.match(/●/g) || []).length;
      var relDots   = '';
      for (var i = 0; i < 5; i++) {
        relDots += '<span class="rel-dot' + (i < filled ? ' filled' : '') + '"></span>';
      }

      /* 2. Category — match `cs.XX` backtick span */
      var catMatch = raw.match(/`([A-Za-z0-9.\-]+)`/);
      var catRaw   = catMatch ? catMatch[1].trim() : '';
      var cls      = catClass(catRaw);

      /* 3. Title and href — match #### [Title](url) or ## [Title](url) */
      var titleMatch = raw.match(/#{1,4}\s+\[([^\]]+)\]\(([^)]+)\)/);
      var title      = titleMatch ? titleMatch[1].trim() : '';
      var href       = titleMatch ? titleMatch[2].trim() : '#';

      /* 4. arXiv PDF link */
      var arxivId = (href.match(/arxiv\.org\/abs\/([^\s/?#]+)/) || [])[1] || '';
      var pdfHref = arxivId ? 'https://arxiv.org/pdf/' + arxivId : href;

      /* 5. Date — text between category backtick and newline/tag */
      var dateMatch = raw.match(/`[A-Za-z0-9.\-]+`[^·\n]*·[^·\n]*?([\w,\s]+(?:\d{4})?)\s*(?:\n|$|<)/);
      var dateStr   = dateMatch ? dateMatch[1].replace(/&nbsp;/g, ' ').trim() : '';

      /* 6. Authors — match "Authors: ..." line, strip the trailing arxiv mirror link */
      var authorsMatch = raw.match(/Authors:\s*([^\n<]+)/);
      var authorsText  = authorsMatch
        ? authorsMatch[1]
            .replace(/&amp;nbsp;·&amp;nbsp;.*$/, '')
            .replace(/&nbsp;·&nbsp;.*$/, '')
            .replace(/\s*·\s*\[.*$/, '')
            .trim()
        : '';

      /* 7. Details elements (these ARE real HTML even in un-parsed divs) */
      var detailsEls = Array.from(card.querySelectorAll('details'));

      /* 8. GitHub link */
      var ghHref = '';
      card.querySelectorAll('a[href]').forEach(function (a) {
        if (a.href && a.href.includes('github.com') && !a.href.includes('arxiv')) {
          ghHref = a.href;
        }
      });

      /* 9. Build new two-column structure */
      var actionsHtml =
        '<a class="paper-action-btn pdf-btn"' +
        '   href="' + pdfHref + '"' +
        '   target="_blank" rel="noopener noreferrer"' +
        '   title="Download PDF" aria-label="Download PDF">' +
        PDF_SVG + '<span>PDF</span></a>';

      if (ghHref) {
        actionsHtml +=
          '<a class="paper-action-btn gh-btn"' +
          '   href="' + ghHref + '"' +
          '   target="_blank" rel="noopener noreferrer"' +
          '   title="View code on GitHub" aria-label="View code on GitHub">' +
          GH_SVG + '<span>Code</span></a>';
      }

      var detailsHtml = detailsEls.map(function (d) {
        var sumEl = d.querySelector('summary');
        var cls2  = sumEl && sumEl.textContent.toLowerCase().includes('abstract')
          ? 'abstract' : 'insights';
        d.className = cls2;

        if (cls2 === 'abstract') {
          /* Collect text content from all non-<summary> child nodes */
          var bodyText = '';
          d.childNodes.forEach(function (node) {
            if (node.nodeName !== 'SUMMARY') {
              bodyText += (node.textContent || node.nodeValue || '');
            }
          });
          /* Strip arXiv scraper prefix: "arXiv:XXXX Announce Type: new  Abstract: " */
          bodyText = bodyText.trim()
            .replace(/^arXiv:\S+\s+Announce Type:\s*\S+\s+Abstract:\s*/i, '')
            .trim();

          return '<details class="abstract">' +
            '<summary>Abstract</summary>' +
            (arxivId
              ? '<p class="paper-detail"><strong>ArXiv ID:</strong>' +
                ' <a href="https://arxiv.org/abs/' + arxivId + '"' +
                ' target="_blank" rel="noopener noreferrer">' + arxivId + '</a></p>'
              : '') +
            (authorsText
              ? '<p class="paper-detail"><strong>Authors:</strong> ' + authorsText + '</p>'
              : '') +
            '<p class="paper-detail abstract-body"><strong>Abstract:</strong></p>' +
            '<p class="abstract-text">' + bodyText + '</p>' +
            '</details>';
        }
        return d.outerHTML;
      }).join('\n');

      var authorIcon =
        '<svg class="author-icon" viewBox="0 0 16 16" fill="currentColor"' +
        '     aria-hidden="true" width="12" height="12">' +
        '<path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07' +
        ' 4.5 4.5 0 0 0-2.97-3.93l-.04-.012a.75.75 0 0 1 .076-1.27zm-4.5-.31a4.5' +
        ' 4.5 0 0 0-2.97 3.93.75.75 0 0 1-1.498-.07A6.005 6.005 0 0 1 5.025 6.44' +
        'l-.004.001a.75.75 0 0 1 .04 1.322zM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0' +
        ' 1.5a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7z"/></svg>';

      card.innerHTML =
        '<div class="paper-body">' +
          '<div class="paper-meta">' +
            '<span class="relevance-pill">' +
              '<span class="rel-dots" aria-label="Relevance: ' + filled + ' out of 5">' +
                relDots +
              '</span>' +
            '</span>' +
            (catRaw ? '<span class="cat-tag ' + cls + '">' + catRaw + '</span>' : '') +
            (dateStr ? '<span class="paper-date">' + dateStr + '</span>' : '') +
          '</div>' +
          '<a class="paper-title" href="' + href + '">' + title + '</a>' +
          '<p class="paper-authors">' + authorIcon + ' ' + authorsText + '</p>' +
          detailsHtml +
        '</div>' +
        '<div class="paper-actions">' +
          actionsHtml +
        '</div>';
    });
  }

  /* Run upgrader after DOM is ready, then apply initial sort, then observe */
  function initPage() {
    upgradePaperCards();
    applyInitialSort();
    // Set up fade-in after cards are in their final positions
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'none';
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -40px 0px', threshold: 0.08 });

      document.querySelectorAll('.paper-item, .news-item, .gh-trending-item').forEach(function (el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(10px)';
        el.style.transition = 'opacity .3s ease, transform .3s ease';
        io.observe(el);
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPage);
  } else {
    initPage();
  }

  /* ── 1. Theme ─────────────────────────────────────────────── */
  var THEME_KEY = 'ai-digest-theme';
  var html      = document.documentElement;
  var themeBtn  = document.getElementById('theme-toggle');
  var themeIcon = document.getElementById('theme-icon');

  function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    if (themeIcon) themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
    if (themeBtn)  themeBtn.setAttribute('aria-label',
      theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    try { localStorage.setItem(THEME_KEY, theme); } catch (_) {}
  }

  function getSavedTheme() {
    try { return localStorage.getItem(THEME_KEY); } catch (_) { return null; }
  }

  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  // Initialise on page load
  applyTheme(getSavedTheme() || getSystemTheme());

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
    });
  }

  // Respect OS-level changes if user hasn't overridden
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
    if (!getSavedTheme()) applyTheme(e.matches ? 'dark' : 'light');
  });

  /* ── 2. Sidebar – Live Date ───────────────────────────────── */
  function renderSidebarDate() {
    var now  = new Date();
    var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    var months = ['January','February','March','April','May','June',
                  'July','August','September','October','November','December'];

    var dayEl  = document.getElementById('sidebar-day');
    var myEl   = document.getElementById('sidebar-month-year');
    var wdEl   = document.getElementById('sidebar-weekday');

    if (dayEl) dayEl.textContent = now.getDate();
    if (myEl)  myEl.textContent  = months[now.getMonth()] + ' ' + now.getFullYear();
    if (wdEl)  wdEl.textContent  = days[now.getDay()];
  }
  renderSidebarDate();

  /* Update header date text dynamically (falls back to Jekyll-rendered value) */
  (function () {
    var el = document.getElementById('header-date-text');
    if (!el) return;
    var now = new Date();
    var opts = { month: 'short', day: 'numeric', year: 'numeric' };
    el.textContent = now.toLocaleDateString('en-US', opts);
  })();

  /* ── 3. Reading Progress Bar ──────────────────────────────── */
  var bar = document.getElementById('progress');
  if (bar) {
    var raf;
    function updateProgress() {
      var doc     = document.documentElement;
      var scrolled = doc.scrollTop || document.body.scrollTop;
      var total    = doc.scrollHeight - doc.clientHeight;
      bar.style.width = total > 0 ? (scrolled / total * 100).toFixed(1) + '%' : '0%';
    }
    window.addEventListener('scroll', function () {
      if (!raf) raf = requestAnimationFrame(function () { updateProgress(); raf = null; });
    }, { passive: true });
  }

  /* ── 4. Back-to-Top ──────────────────────────────────────── */
  var bttBtn = document.getElementById('back-to-top');
  if (bttBtn) {
    window.addEventListener('scroll', function () {
      var shown = (document.documentElement.scrollTop || document.body.scrollTop) > 400;
      bttBtn.classList.toggle('visible', shown);
    }, { passive: true });
    bttBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── 5. Mobile Nav Drawer ────────────────────────────────── */
  var menuBtn   = document.getElementById('mobile-menu-btn');
  var menuIcon  = document.getElementById('menu-icon');
  var mobileNav = document.getElementById('mobile-nav');

  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', function () {
      var open = mobileNav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
      mobileNav.setAttribute('aria-hidden', String(!open));
      if (menuIcon) menuIcon.textContent = open ? '✕' : '☰';
      document.body.style.overflow = open ? 'hidden' : '';
    });

    // Close on nav link click
    mobileNav.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileNav.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
        mobileNav.setAttribute('aria-hidden', 'true');
        if (menuIcon) menuIcon.textContent = '☰';
        document.body.style.overflow = '';
      });
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (!mobileNav.contains(e.target) && !menuBtn.contains(e.target)) {
        if (mobileNav.classList.contains('open')) {
          mobileNav.classList.remove('open');
          menuBtn.setAttribute('aria-expanded', 'false');
          mobileNav.setAttribute('aria-hidden', 'true');
          if (menuIcon) menuIcon.textContent = '☰';
          document.body.style.overflow = '';
        }
      }
    });
  }

  /* ── 6. Sort Buttons ─────────────────────────────────────── */

  /** Populate missing data-date / data-relevance on a card, then return the card. */
  function ensureCardData(card, index) {
    if (!card.hasAttribute('data-original-index')) {
      card.setAttribute('data-original-index', String(index));
    }
    // data-relevance: fall back to counting filled dots in the DOM
    if (!card.getAttribute('data-relevance')) {
      card.setAttribute('data-relevance',
        String(card.querySelectorAll('.rel-dot.filled').length));
    }
    // data-date: fall back to YYMM prefix from the arxiv link
    if (!card.getAttribute('data-date')) {
      var link = card.querySelector('.paper-title, a[href*="arxiv.org/abs/"]');
      var href  = link ? (link.getAttribute('href') || '') : '';
      var m     = href.match(/arxiv\.org\/abs\/(\d{4})/);
      if (m) {
        card.setAttribute('data-date',
          '20' + m[1].slice(0, 2) + '-' + m[1].slice(2, 4) + '-00');
      }
    }
  }

  function sortPapers(sortKey) {
    var cards = Array.from(document.querySelectorAll('.paper-item'));
    if (!cards.length) return;

    cards.forEach(ensureCardData);

    cards.sort(function (a, b) {
      if (sortKey === 'relevance') {
        var ra = parseInt(a.getAttribute('data-relevance') || '0', 10);
        var rb = parseInt(b.getAttribute('data-relevance') || '0', 10);
        if (rb !== ra) return rb - ra;
      } else {
        // recent: newest submission date first
        var da = a.getAttribute('data-date') || '0000-00-00';
        var db = b.getAttribute('data-date') || '0000-00-00';
        if (da !== db) return db < da ? -1 : 1;
      }
      // Secondary: preserve original order
      return parseInt(a.getAttribute('data-original-index') || '0', 10) -
             parseInt(b.getAttribute('data-original-index') || '0', 10);
    });

    // All paper-items share the same parent in Jekyll-rendered posts
    var parent = cards[0].parentNode;

    // Hide topic sub-headings and descriptions — not meaningful when papers are reordered
    // (h4 = topic categories like LLM/Multimodal, h3 = section intros, p.section-desc = descriptions)
    parent.querySelectorAll('h3, h4, p.section-desc').forEach(function (h) { h.style.display = 'none'; });

    // Find insertion anchor: right after the FIRST papers section h2 (global-trends or
    // personal-topics), so sorted cards never bleed into the Tech News section.
    var paperH2 = parent.querySelector('h2[id="global-trends"], h2[id="personal-topics"]');
    var anchor = paperH2 ? paperH2.nextSibling : parent.firstChild;

    cards.forEach(function (card) {
      parent.insertBefore(card, anchor);
    });
  }

  function setSort(btn, sortKey) {
    document.querySelectorAll('.sort-btn').forEach(function (b) {
      b.classList.remove('active');
    });
    btn.classList.add('active');

    // Update URL hash for deep-linking (no page reload)
    if (history.replaceState) {
      history.replaceState(null, '', '#' + sortKey);
    }

    sortPapers(sortKey);

    document.dispatchEvent(new CustomEvent('digest:sort', { detail: { sort: sortKey } }));
  }
  // Expose globally for inline onclick handlers in Jekyll content
  window.setSort = setSort;

  // Apply initial sort (default = recent) after cards are upgraded
  function applyInitialSort() {
    var hash = location.hash.replace('#', '');
    var initialKey = (hash === 'recent' || hash === 'relevance') ? hash : 'recent';
    var activeBtn  = document.querySelector('[data-sort="' + initialKey + '"]');
    if (activeBtn) {
      document.querySelectorAll('.sort-btn').forEach(function (b) { b.classList.remove('active'); });
      activeBtn.classList.add('active');
    }
    if (document.querySelector('.paper-item')) {
      sortPapers(initialKey);
    }
  }

  /* ── 7. Active Nav Link (client-side highlight) ──────────── */
  (function () {
    var path = location.pathname;
    document.querySelectorAll('.nav-link').forEach(function (link) {
      var href = link.getAttribute('href') || '';
      // Strip baseurl prefix if present
      var norm = href.replace(/^\/ai-digest-daily/, '');
      if (norm === '/' ? path === '/' || path.endsWith('/index.html') : path.indexOf(norm) !== -1) {
        link.classList.add('active');
      }
    });
  })();

  /* ── 8. Keyboard Accessibility – Close mobile nav on Escape ─ */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && mobileNav && mobileNav.classList.contains('open')) {
      mobileNav.classList.remove('open');
      if (menuBtn) { menuBtn.setAttribute('aria-expanded', 'false'); menuBtn.focus(); }
      mobileNav.setAttribute('aria-hidden', 'true');
      if (menuIcon) menuIcon.textContent = '☰';
      document.body.style.overflow = '';
    }
  });

})();
