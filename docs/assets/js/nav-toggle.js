const baseUrl = document.currentScript.getAttribute('data-baseurl');

document.addEventListener("DOMContentLoaded", function() {
    const toggleContainer = document.createElement('span');
    toggleContainer.id = 'skos-toggle-container';
    toggleContainer.className = 'fw-500';
    toggleContainer.style.display = 'inline';
    toggleContainer.appendChild(document.createTextNode(' - '));

    const btnToggle = document.createElement('span');
    btnToggle.id = 'btn-toggle-nav';
    btnToggle.className = 'text-purple-000';
    btnToggle.style.cursor = 'pointer';
    btnToggle.textContent = 'alfabetisch';
    toggleContainer.appendChild(btnToggle);

    const azList = document.createElement('ul');
    azList.className = 'nav-list';
    azList.style.display = 'none';

    const loadingItem = document.createElement('li');
    loadingItem.id = 'skos-loading-container';
    loadingItem.className = 'nav-list-item';
    azList.appendChild(loadingItem);

    const loadingMsg = document.createElement('span');
    loadingMsg.id = 'skos-loading-msg';
    loadingMsg.className = 'nav-list-link';
    loadingMsg.textContent = 'Laden...';
    loadingItem.appendChild(loadingMsg);

    let dataLoaded = false;
    const jsonUrl = `${baseUrl}/assets/json/alphabetical-nav.json`;

    function loadAndRenderData() {
        if (dataLoaded) return;

        fetch(jsonUrl)
        .then(response => response.json())
        .then(data => {
            const currentPath = window.location.pathname.replace(/\/$/, "");

            azList.innerHTML = data.map(item => {
                const itemUrlClean = item.url.replace(/\/$/, "");
                const isActive = item.type !== 'alias' && currentPath.endsWith(itemUrlClean);
                const cssClass = isActive ? 'nav-list-link active' : 'nav-list-link';

                let itemHTML = item.title;
                if (item.type === 'alias') itemHTML = `<span class="text-grey-dk-000">${item.title} &rarr; </span>${item.target_label}`;

                return `<li class="nav-list-item"><a href="${baseUrl}${item.url}" class="${cssClass}">${itemHTML}</a></li>`;
            }).join('');

            dataLoaded = true;
            scrollToActive();
        })
        .catch(err => {
            loadingMsg.textContent = "Fout bij laden begrippenlijst";
            console.error(err);
        });
    }

    function setNavMode(mode) {
        if (mode === 'az') {
            treeList.style.display = 'none';
            azList.style.display = 'block';
            btnToggle.textContent = 'hiërarchisch';
            localStorage.setItem('skos-nav-pref', 'az');
            if (!dataLoaded) loadAndRenderData(); 
            else scrollToActive(azList);
        } else {
            treeList.style.display = 'block';
            azList.style.display = 'none';
            btnToggle.textContent = 'alfabetisch'; 
            localStorage.setItem('skos-nav-pref', 'tree');
            scrollToActive(treeList);
        }
    }

    function scrollToActive(list) {
        const activeLink = list.querySelector('.active');
        if (activeLink) activeLink.scrollIntoView({block: 'center'}); 
    }

    // Main
    const sidebar = document.querySelector('.site-nav');
    const navCategory = document.querySelector('.nav-category');
    const allLists = document.querySelectorAll('.site-nav > .nav-list');
    const treeList = allLists.length > 0 ? allLists[allLists.length - 1] : null;

    if (!sidebar || !navCategory || !treeList) return;

    navCategory.appendChild(toggleContainer);

    sidebar.insertBefore(azList, treeList);

    btnToggle.addEventListener('click', function() {
        setNavMode(azList.style.display === 'none' ? 'az' : 'tree');
    });

    if (localStorage.getItem('skos-nav-pref') === 'az') setNavMode('az');
});
