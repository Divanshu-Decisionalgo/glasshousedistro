/* Glass House Distro — Theme Manager */
(function () {
  var KEY = 'ghd-theme';

  function preferred() {
    var saved = localStorage.getItem(KEY);
    if (saved === 'light' || saved === 'dark') return saved;
    return 'light';
  }

  function applyBodyStyle(theme) {
    var b = document.body;
    if (!b) return;
    if (theme === 'dark') {
      b.style.backgroundColor = '#070b16';
      b.style.color = '#dde8f2';
    } else {
      b.style.backgroundColor = '#edf5ff';
      b.style.color = '#0b1928';
    }
  }

  function apply(theme) {
    var html = document.documentElement;
    if (theme === 'dark') {
      html.classList.add('dark');
    } else {
      html.classList.remove('dark');
    }
    localStorage.setItem(KEY, theme);

    // Update any toggle icons present in the DOM
    document.querySelectorAll('.theme-toggle-icon').forEach(function (el) {
      el.textContent = theme === 'dark' ? 'light_mode' : 'dark_mode';
    });

    // Update floating FAB icon if present
    var fab = document.querySelector('.theme-toggle-fab .material-symbols-outlined');
    if (fab) fab.textContent = theme === 'dark' ? 'light_mode' : 'dark_mode';
  }

  function toggle() {
    var current = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
    var next = current === 'dark' ? 'light' : 'dark';
    apply(next);
    applyBodyStyle(next);
  }

  // Apply immediately (before DOM paint) to avoid flash
  var initialTheme = preferred();
  apply(initialTheme);

  // Wire up on DOM ready
  document.addEventListener('DOMContentLoaded', function () {
    // Re-apply body style (body exists now)
    applyBodyStyle(initialTheme);

    // Wire existing toggle buttons
    document.querySelectorAll('.theme-toggle, .theme-toggle-btn').forEach(function (btn) {
      btn.addEventListener('click', toggle);
    });

    // Inject floating FAB if not already on page
    if (!document.querySelector('.theme-toggle-fab')) {
      var btn = document.createElement('button');
      btn.className = 'theme-toggle-fab';
      btn.title = 'Toggle light / dark mode';
      btn.setAttribute('aria-label', 'Toggle theme');
      var icon = document.createElement('span');
      icon.className = 'material-symbols-outlined';
      icon.textContent = document.documentElement.classList.contains('dark') ? 'light_mode' : 'dark_mode';
      btn.appendChild(icon);
      btn.addEventListener('click', toggle);
      document.body.appendChild(btn);
    }
  });

  // Expose globally
  window.GHD = { toggleTheme: toggle };
})();
