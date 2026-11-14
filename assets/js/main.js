/* Nithin Singh — site script. No dependencies, no tracking. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");

  // ---- Mobile navigation ----
  var toggle = document.querySelector(".nav-toggle");
  var header = document.querySelector(".site-header");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && header.classList.contains("nav-open")) {
        header.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.setAttribute("aria-label", "Open menu");
        toggle.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 1020 && header.classList.contains("nav-open")) {
        header.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // ---- Header shadow on scroll ----
  var onScroll = function () {
    if (header) header.classList.toggle("scrolled", window.scrollY > 8);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---- Reveal on scroll ----
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // ---- Apply the shared visual system on every route ----
  document.body.classList.add("studio-page");
  var pageRevealTargets = document.querySelectorAll(
    "body:not(.home-page) .page-hero .container > h1, body:not(.home-page) .section-head, body:not(.home-page) .card, body:not(.home-page) .pv-card, body:not(.home-page) .prose > h2, body:not(.home-page) .form-card, body:not(.home-page) .side-card"
  );
  pageRevealTargets.forEach(function (el) { el.classList.add("reveal"); });
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var pageRevealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          pageRevealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -28px 0px" });
    pageRevealTargets.forEach(function (el) { pageRevealObserver.observe(el); });
  } else {
    pageRevealTargets.forEach(function (el) { el.classList.add("in"); });
  }

  // ---- Homepage motion: staggered reveals, with reduced-motion support ----
  if (document.body.classList.contains("home-page")) {
    var revealTargets = document.querySelectorAll(
      ".premium-section-head, .premium-service-card, .review-card, .process-mini > div, .premium-cta-inner"
    );
    revealTargets.forEach(function (el) { el.classList.add("reveal"); });
    if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -35px 0px" });
      revealTargets.forEach(function (el) { revealObserver.observe(el); });
    } else {
      revealTargets.forEach(function (el) { el.classList.add("in"); });
    }
  }

  // ---- Footer year ----
  var y = document.querySelectorAll("[data-year]");
  y.forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // ---- Contact form ----
  // Two honest modes, configured with data attributes on the <form>:
  //  1) data-google-form="https://docs.google.com/forms/d/e/FORM_ID/formResponse"
  //     plus data-entry-* attributes mapping each field to its Google Forms entry id.
  //     The form then submits to Google Forms in a new tab, where Google shows its own confirmation.
  //  2) Default: mailto fallback that opens the visitor's email app with the enquiry prefilled.
  var form = document.getElementById("enquiry-form");
  if (!form) return;
  var status = document.getElementById("form-status");
  var email = form.getAttribute("data-email") || "";
  var gForm = (form.getAttribute("data-google-form") || "").trim();

  function show(msg, ok) {
    status.textContent = msg;
    status.className = "form-status show " + (ok ? "ok" : "err");
  }

  function valid() {
    var okAll = true;
    form.querySelectorAll("[required]").forEach(function (f) {
      var ok = f.value.trim() !== "" && (!f.checkValidity || f.checkValidity());
      f.setAttribute("aria-invalid", ok ? "false" : "true");
      if (!ok) okAll = false;
    });
    return okAll;
  }

  form.addEventListener("submit", function (e) {
    if (!valid()) {
      e.preventDefault();
      show("Please complete the required fields (marked *) with valid values.", false);
      var first = form.querySelector('[aria-invalid="true"]');
      if (first) first.focus();
      return;
    }

    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = String(v).trim(); });

    if (gForm) {
      // Rebuild a native form with Google's entry names and submit to a new tab.
      e.preventDefault();
      var g = document.createElement("form");
      g.action = gForm; g.method = "POST"; g.target = "_blank"; g.style.display = "none";
      Object.keys(data).forEach(function (k) {
        var entry = form.getAttribute("data-entry-" + k);
        if (!entry) return;
        var i = document.createElement("input");
        i.type = "hidden"; i.name = entry; i.value = data[k];
        g.appendChild(i);
      });
      document.body.appendChild(g);
      g.submit();
      g.remove();
      show("Your enquiry was sent to Google Forms in a new tab. Google's confirmation page appears there.", true);
      return;
    }

    e.preventDefault();
    if (!email || /example\.com$/i.test(email)) {
      show("The site owner has not set a contact email yet. Please use the Fiverr button below to get in touch.", false);
      return;
    }
    var lines = [
      "Name: " + (data.name || ""),
      "Business email: " + (data.email || ""),
      "Company website: " + (data.company || "-"),
      "Data source URL: " + (data.source || "-"),
      "Estimated records: " + (data.records || "-"),
      "Required output format: " + (data.format || "-"),
      "Deadline: " + (data.deadline || "-"),
      "",
      "Project description:",
      data.description || ""
    ];
    var subject = "Project enquiry: " + (data.name || "Web scraping project");
    var href = "mailto:" + email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
    window.location.href = href;
    show("Your email app should now open with the enquiry prefilled. Press send there to deliver it. If nothing opened, email " + email + " directly.", true);
  });
})();
