/* Showcase front-end: fetches index.json and renders filterable project cards.
   Framework-free, no build step. */
(function () {
  "use strict";

  var state = {
    projects: [],
    category: "All",
    query: "",
  };

  var els = {
    grid: document.getElementById("grid"),
    count: document.getElementById("result-count"),
    loading: document.getElementById("loading"),
    error: document.getElementById("error"),
    empty: document.getElementById("empty"),
    search: document.getElementById("search"),
    categoryFilters: document.getElementById("category-filters"),
    clearFilters: document.getElementById("clear-filters"),
    heroStats: document.getElementById("hero-stats"),
    template: document.getElementById("card-template"),
  };

  var LINK_LABELS = { demo: "Demo", repo: "Source repo", video: "Video" };

  function show(el) { if (el) el.hidden = false; }
  function hide(el) { if (el) el.hidden = true; }

  function init() {
    fetch("index.json", { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        state.projects = (data && data.projects) || [];
        hide(els.loading);
        renderStats();
        buildCategoryFilters(data && data.categories);
        bindControls();
        render();
      })
      .catch(function () {
        hide(els.loading);
        show(els.error);
      });
  }

  // Live hero counts: total projects and distinct contributors (by github handle).
  function renderStats() {
    if (!els.heroStats) return;
    var projects = state.projects;
    var n = projects.length;
    if (n === 0) {
      els.heroStats.textContent = "No projects yet — be the first.";
      return;
    }
    var contributors = {};
    projects.forEach(function (p) {
      var gh = (p.github || "").trim().toLowerCase();
      if (gh) contributors[gh] = true;
    });
    var c = Object.keys(contributors).length;
    els.heroStats.textContent =
      n + " project" + (n === 1 ? "" : "s") + " · " +
      c + " contributor" + (c === 1 ? "" : "s");
  }

  function buildCategoryFilters(categories) {
    var all = ["All"].concat(categories || []);
    all.forEach(function (cat) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "chip";
      btn.textContent = cat;
      btn.setAttribute("aria-pressed", cat === state.category ? "true" : "false");
      btn.addEventListener("click", function () {
        state.category = cat;
        updatePressed();
        render();
      });
      els.categoryFilters.appendChild(btn);
    });
  }

  function updatePressed() {
    var chips = els.categoryFilters.querySelectorAll(".chip");
    chips.forEach(function (chip) {
      chip.setAttribute(
        "aria-pressed",
        chip.textContent === state.category ? "true" : "false"
      );
    });
  }

  function bindControls() {
    els.search.addEventListener("input", function () {
      state.query = this.value.trim().toLowerCase();
      render();
    });
    if (els.clearFilters) {
      els.clearFilters.addEventListener("click", function () {
        state.query = "";
        state.category = "All";
        els.search.value = "";
        updatePressed();
        render();
      });
    }
  }

  function matches(project) {
    if (state.category !== "All" && project.category !== state.category) {
      return false;
    }
    if (!state.query) return true;
    var haystack = [
      project.title,
      project.author,
      project.summary,
      (project.tags || []).join(" "),
    ].join(" ").toLowerCase();
    return haystack.indexOf(state.query) !== -1;
  }

  function render() {
    var visible = state.projects.filter(matches);
    els.grid.textContent = "";

    if (visible.length === 0) {
      hide(els.grid);
      show(els.empty);
    } else {
      hide(els.empty);
      visible.forEach(function (p) { els.grid.appendChild(card(p)); });
      show(els.grid);
    }

    var total = state.projects.length;
    els.count.textContent =
      visible.length === total
        ? total + " project" + (total === 1 ? "" : "s")
        : visible.length + " of " + total + " project" + (total === 1 ? "" : "s");
  }

  function card(p) {
    var node = els.template.content.cloneNode(true);

    var handle = node.querySelector("[data-handle]");
    handle.textContent = p.path || "";
    if (p.source) handle.href = p.source;

    node.querySelector("[data-title]").textContent = p.title || "Untitled";
    node.querySelector("[data-author]").textContent = p.author || "Unknown";
    node.querySelector("[data-year]").textContent = p.year || "";
    node.querySelector("[data-category]").textContent = p.category || "";
    node.querySelector("[data-summary]").textContent = p.summary || "";

    var tagList = node.querySelector("[data-tags]");
    (p.tags || []).forEach(function (tag) {
      var li = document.createElement("li");
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "tag";
      btn.textContent = tag;
      btn.setAttribute("aria-label", "Filter by tag " + tag);
      btn.addEventListener("click", function () {
        state.query = tag.toLowerCase();
        els.search.value = tag;
        render();
      });
      li.appendChild(btn);
      tagList.appendChild(li);
    });

    var linksWrap = node.querySelector("[data-links]");
    var links = p.links || {};
    var anyLink = false;
    ["demo", "repo", "video"].forEach(function (key) {
      var url = links[key];
      if (url) {
        anyLink = true;
        var a = document.createElement("a");
        a.href = url;
        a.textContent = LINK_LABELS[key];
        a.rel = "noopener";
        a.target = "_blank";
        linksWrap.appendChild(a);
      }
    });
    if (p.source) {
      var src = document.createElement("a");
      src.href = p.source;
      src.textContent = "View files";
      src.rel = "noopener";
      src.target = "_blank";
      linksWrap.appendChild(src);
      anyLink = true;
    }
    if (!anyLink) linksWrap.remove();

    return node;
  }

  init();
})();
