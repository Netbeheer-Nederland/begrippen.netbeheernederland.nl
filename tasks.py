import os, shutil, sys
from invoke import task

# ==============================================================================
# CONFIGURATIE
# ==============================================================================

DOCS_DIR = "docs"
STAGING_DIR = "_staging"
SITE_DIR = "_site"

PYTHON = sys.executable
JEKYLL = "bundle exec jekyll"

# ==============================================================================
# TAKEN
# ==============================================================================

@task
def setup(c):
    """1. Installeren: Zet alle dependencies klaar."""
    print("📦 Dependencies installeren...")
    c.run(f"{PYTHON} -m pip install -r requirements.txt")
    print("💎 Ruby dependencies...")
    c.run("bundle install")
    
    print("🧠 SpaCy model controleren...")
    try:
        import spacy; spacy.load("nl_core_news_sm")
    except:
        c.run(f"{PYTHON} -m spacy download nl_core_news_sm")
    print("✅ Klaar.")

@task
def update(c):
    """2. Verversen: Draai dit om wijzigingen in data door te voeren."""
    print(f"📂 Content kopiëren: {DOCS_DIR} -> {STAGING_DIR}")
    
    # dirs_exist_ok=True zorgt dat we kunnen overschrijven terwijl Jekyll draait
    shutil.copytree(DOCS_DIR, STAGING_DIR, dirs_exist_ok=True)
    
    print("🔮 Genereren start...")
    res = c.run(f"{PYTHON} generate.py {STAGING_DIR}", warn=True)
    
    if res.failed:
        print("❌ FOUT: Generatie mislukt."); 
    else:
        print("✅ Data bijgewerkt.")

@task
def serve(c):
    """3. Starten: Start de website lokaal (begint met schone lei)."""
    # Verwijder oude staging rommel (ignore_errors voorkomt crash bij eerste run)
    print("🧹 Opruimen...")
    shutil.rmtree(STAGING_DIR, ignore_errors=True)
    
    # Bouw alles vers op
    update(c)
    
    print("\n🌍 Server start... (Ctrl+C om te stoppen)")
    c.run(f"{JEKYLL} serve -s {STAGING_DIR} -d {SITE_DIR} --livereload --incremental --open-url")

@task
def build(c):
    """Productie build (voor CI/CD)."""
    update(c)
    c.run(f"{JEKYLL} build -s {STAGING_DIR} -d {SITE_DIR}")

# ==============================================================================
# INTERACTIEF MENU
# ==============================================================================

@task(default=True)
def menu(c):
    while True:
        print("\n=== BEGRIPPENKADER TOOL ===")
        print(" [1] Setup  (Installeren)")
        print(" [2] Start  (Website bekijken)")
        print(" [3] Update (Verversen tijdens draaien)")
        print(" [Q] Stop")
        
        try:
            choice = input("\nKies een optie: ").strip().lower()
        except KeyboardInterrupt:
            break # Netjes afsluiten bij Ctrl+C in menu
            
        if choice == '1': setup(c)
        elif choice == '2': serve(c)
        elif choice == '3': update(c)
        elif choice == 'q': break
