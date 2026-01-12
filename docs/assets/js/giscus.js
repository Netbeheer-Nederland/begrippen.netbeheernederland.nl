function loadGiscusComments() {
    let script = document.createElement('script');
    script.src = "https://giscus.app/client.js";
    script.async = true;
    script.crossOrigin = "anonymous";

    script.setAttribute("data-repo", "netbeheer-nederland/begrippen.netbeheernederland.nl");
    script.setAttribute("data-repo-id", "R_kgDOQbdEvg");
    script.setAttribute("data-category", "Announcements");
    script.setAttribute("data-category-id", "DIC_kwDOQbdEvs4Cy4mX");
    script.setAttribute("data-mapping", "pathname");
    script.setAttribute("data-strict", "1");
    script.setAttribute("data-reactions-enabled", "0");
    script.setAttribute("data-emit-metadata", "0");
    script.setAttribute("data-input-position", "bottom");
    script.setAttribute("data-theme", "light");
    script.setAttribute("data-lang", "nl");
    script.setAttribute("data-loading", "lazy");

    document.getElementById("giscus-container").replaceChild(script, document.getElementById('load-giscus-comments'));
}
