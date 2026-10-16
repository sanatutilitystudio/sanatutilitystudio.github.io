(function () {
  "use strict";
  const query = document.getElementById("article-query");
  const results = document.getElementById("search-results");
  const status = document.getElementById("search-count");
  if (!query || !results || !status) return;
  let articles = [];
  let loaded = false;
  fetch("/search.json", { credentials: "same-origin" }).then(function (response) {
    if (!response.ok) throw new Error("Unable to load article index");
    return response.json();
  }).then(function (data) {
    articles = Array.isArray(data) ? data : [];
    loaded = true;
    render();
  }).catch(function () { status.textContent = "Search index is currently unavailable. Please browse the journal."; });
  query.addEventListener("input", render);
  function render() {
    if (!loaded) return;
    const term = query.value.trim().toLocaleLowerCase();
    results.replaceChildren();
    if (!term) { status.textContent = "Enter a keyword to search published articles."; return; }
    const found = articles.filter(function (post) {
      return [post.title, post.description, post.categories].join(" ").toLocaleLowerCase().includes(term);
    }).slice(0, 50);
    status.textContent = found.length + (found.length === 1 ? " result" : " results");
    found.forEach(function (post) {
      const article = document.createElement("article"); article.className = "journal-card";
      const date = document.createElement("p"); date.className = "journal-kicker"; date.textContent = post.date + " · " + post.categories;
      const title = document.createElement("h3"); const link = document.createElement("a");
      if (typeof post.url !== "string" || !post.url.startsWith("/") || post.url.startsWith("//")) return;
      link.href = post.url; link.textContent = post.title; title.append(link);
      const description = document.createElement("p"); description.textContent = post.description;
      article.append(date, title, description); results.append(article);
    });
  }
})();
