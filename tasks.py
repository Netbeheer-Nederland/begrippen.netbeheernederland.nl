import os, shutil
from invoke import task

# Configuratie
DOCS_DIR = "docs"
STAGING_DIR = "_staging"
SITE_DIR = "_site"

# Windows compatibiliteit
PYTHON = "python"
JEKYLL = "bundle exec jekyll"

@task
def clean(c):
    """Ruim de gegenereerde mappen op (_site en _staging)."""
    print("🧹 Cleaning...")
    for folder in [STAGING_DIR, SITE_DIR]:
        if os.path.exists(folder):
            print(f"   - Verwijderen: {folder}")
            shutil.rmtree(folder)

@task
def setup(c):
    """Installeer dependencies (Python & Ruby) en download SpaCy model."""
    print("📦 Setup dependencies...")
    c.run(f"{PYTHON} -m pip install -r requirements.txt")
    
    print("🧠 Checking SpaCy model...")
    try:
        import spacy
        spacy.load("nl_core_news_sm")
        print("   - Model aanwezig.")
    except (ImportError, OSError):
        c.run(f"{PYTHON} -m spacy download nl_core_news_sm")

    print("💎 Checking Ruby dependencies...")
    c.run("gem list -i bundler || gem install bundler")
    c.run("bundle install")

@task
def prepare_build(c):
    """
    Kopieert docs -> _staging en draait generate.py.
    Deze stap is essentieel voor build en serve.
    """
    print(f"🏗  Preparing staging directory: {DOCS_DIR} -> {STAGING_DIR}")
    
    # 1. Schoonmaken en kopiëren
    if os.path.exists(STAGING_DIR):
        shutil.rmtree(STAGING_DIR)
    shutil.copytree(DOCS_DIR, STAGING_DIR)
    
    # 2. Generatie script draaien (DIT IS DE STAP DIE JIJ MISTE)
    print("🔮 Running Python generator...")
    # We geven _staging mee als argument, zodat generate.py daarin schrijft
    c.run(f"{PYTHON} generate.py {STAGING_DIR}")

@task
def build(c):
    """Bouw de statische site voor productie (inclusief generatie)."""
    # Stap 1: Altijd eerst genereren
    prepare_build(c)
    
    # Stap 2: Jekyll bouwen
    print("🚀 Jekyll Build (Production)...")
    c.run(f"{JEKYLL} build -s {STAGING_DIR} -d {SITE_DIR}")

@task
def serve(c):
    """Draai lokaal met live-reload (inclusief generatie)."""
    # Stap 1: Altijd eerst genereren
    prepare_build(c)
    
    # Stap 2: Server starten
    print("🌍 Starting Local Server...")
    # --incremental zorgt dat hij niet bij elke wijziging alles opnieuw bouwt
    c.run(f"{JEKYLL} serve -s {STAGING_DIR} -d {SITE_DIR} --livereload --incremental --open-url")

@task
def menu(c):
    """Toon interactief menu."""
    while True:
        print("\n========================================================")
        print("                 BEGRIPPENKADER MENU")
        print("========================================================")
        print("  [1] SETUP   (Dependencies installeren)")
        print("  [2] CLEAN   (Oude bestanden opruimen)")
        print("  [3] BUILD   (Site genereren & bouwen)")
        print("  [4] SERVE   (Lokaal bekijken)")
        print("  [Q] STOPPEN")
        print("========================================================")
        
        choice = input("Maak een keuze: ").strip().lower()
        
        if choice == '1': setup(c)
        elif choice == '2': clean(c)
        elif choice == '3': build(c)
        elif choice == '4': serve(c)
        elif choice == 'q': break
        else: print("Ongeldige keuze.")
