const navToggle=document.querySelector('.nav-toggle');const siteNav=document.querySelector('.site-nav');const year=document.querySelector('#year');if(year){year.textContent=new Date().getFullYear();}if(navToggle&&siteNav){navToggle.addEventListener('click',()=>{const isOpen=siteNav.classList.toggle('open');navToggle.setAttribute('aria-expanded',String(isOpen));});siteNav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{siteNav.classList.remove('open');navToggle.setAttribute('aria-expanded','false');}));}
/* SUS analytics: opt-in only. No Google tag request is made before consent. */
(function () {
  "use strict";
  var MEASUREMENT_ID = "G-C8R92WS0QH";
  var STORAGE_KEY = "sus-analytics-choice-v1";
  var trackingLoaded = false;
  var consent = null;
  try { consent = window.localStorage.getItem(STORAGE_KEY); } catch (_) { /* storage blocked */ }
  function storeChoice(choice) {
    consent = choice;
    try { window.localStorage.setItem(STORAGE_KEY, choice); } catch (_) { /* session only */ }
  }
  function loadAnalytics() {
    if (trackingLoaded || consent !== "accepted") return;
    trackingLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", MEASUREMENT_ID);
    var script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(MEASUREMENT_ID);
    document.head.appendChild(script);
  }
  function closeBanner() {
    var element = document.getElementById("sus-consent-banner");
    if (element) element.remove();
  }
  function choose(value) {
    var wasAccepted = consent === "accepted";
    storeChoice(value);
    closeBanner();
    if (value === "accepted") {
      loadAnalytics();
    } else if (wasAccepted) {
      // Reload stops analytics already loaded in this page.
      window.location.reload();
    }
  }
  function showBanner() {
    closeBanner();
    var notice = document.createElement("section");
    notice.id = "sus-consent-banner";
    notice.className = "sus-consent";
    notice.setAttribute("role", "region");
    notice.setAttribute("aria-label", "Website analytics preference");
    notice.innerHTML =
      '<div class="sus-consent-copy"><strong>Optional website analytics</strong>' +
      '<p>Help us understand visits and app-link clicks. Google Analytics stays off unless you agree. ' +
      '<a href="/privacy/">Privacy details</a>.</p></div>' +
      '<div class="sus-consent-actions"><button type="button" data-consent="declined">Decline</button>' +
      '<button type="button" class="sus-consent-accept" data-consent="accepted">Allow analytics</button></div>';
    notice.querySelector('[data-consent="declined"]').addEventListener("click", function () { choose("declined"); });
    notice.querySelector('[data-consent="accepted"]').addEventListener("click", function () { choose("accepted"); });
    document.body.appendChild(notice);
  }
  function attachPreferencesButton() {
    var button = document.getElementById("sus-analytics-preferences");
    if (button) button.addEventListener("click", showBanner);
  }
  document.addEventListener("click", function (event) {
    if (consent !== "accepted" || typeof window.gtag !== "function") return;
    var element = event.target instanceof Element ? event.target.closest("a[href]") : null;
    if (!element) return;
    var target;
    try { target = new URL(element.href, window.location.href); } catch (_) { return; }
    var isPlayApp = target.hostname === "play.google.com" && target.pathname === "/store/apps/details";
    var isGitHubRelease = target.hostname === "github.com" && target.pathname.includes("/releases");
    if (!isPlayApp && !isGitHubRelease) return;
    window.gtag("event", "app_download_click", {
      link_destination: target.origin + target.pathname,
      source_page: window.location.pathname,
      product_label: (document.title || "Sanat Utility Studio").slice(0, 90),
      transport_type: "beacon"
    });
  }, true);
  attachPreferencesButton();
  if (consent === "accepted") loadAnalytics();
  else if (consent !== "declined") showBanner();
}());
