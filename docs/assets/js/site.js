(function () {
  var cfg = window.HUB2U || {};
  var doc = document;

  // ---- menu on phones ----
  var header = doc.querySelector('.site-header');
  var toggle = doc.getElementById('navToggle');
  if (toggle && header) {
    toggle.addEventListener('click', function () {
      var open = header.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // ---- sub menu on desktop ----
  var subs = doc.querySelectorAll('.has-sub');
  Array.prototype.forEach.call(subs, function (item) {
    var btn = item.querySelector('.sub-toggle');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var open = item.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  doc.addEventListener('click', function (e) {
    Array.prototype.forEach.call(subs, function (item) {
      if (!item.contains(e.target)) {
        item.classList.remove('open');
        var b = item.querySelector('.sub-toggle');
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    });
  });
  doc.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      Array.prototype.forEach.call(subs, function (item) { item.classList.remove('open'); });
      if (header) header.classList.remove('nav-open');
    }
  });

  // ---- buttons that need real links ----
  var links = {
    line: cfg.lineUrl,
    shop: cfg.shopSignupUrl,
    rider: cfg.riderSignupUrl,
    app: cfg.appUrl
  };
  Array.prototype.forEach.call(doc.querySelectorAll('[data-link]'), function (el) {
    var key = el.getAttribute('data-link');
    var url = links[key];
    if (url) {
      el.setAttribute('href', url);
      if (/^https?:/i.test(url)) { el.setAttribute('rel', 'noopener'); }
    } else if (key === 'app') {
      el.classList.add('is-pending');
      el.setAttribute('aria-disabled', 'true');
      el.addEventListener('click', function (e) { e.preventDefault(); });
    }
  });

  // ---- fill in information from config.js ----
  Array.prototype.forEach.call(doc.querySelectorAll('[data-fill]'), function (el) {
    var val = cfg[el.getAttribute('data-fill')];
    if (val) {
      el.textContent = val;
      el.classList.remove('ph');
    }
  });
  if (cfg.phone) {
    Array.prototype.forEach.call(doc.querySelectorAll('[data-tel]'), function (el) {
      el.setAttribute('href', 'tel:' + String(cfg.phone).replace(/[^0-9+]/g, ''));
    });
  }
  Array.prototype.forEach.call(doc.querySelectorAll('[data-image]'), function (el) {
    var src = cfg[el.getAttribute('data-image')];
    if (src) {
      var img = doc.createElement('img');
      img.src = src;
      img.alt = el.getAttribute('data-alt') || '';
      el.textContent = '';
      el.classList.remove('photo-ph');
      el.appendChild(img);
    }
  });
})();
