import re

with open("index.html", "r") as f:
    content = f.read()

# Split out the header (up to </header>) and footer (from <footer>)
header_match = re.search(r'(.*?</header>)', content, re.DOTALL)
footer_match = re.search(r'(<footer>.*)', content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer.")
    exit(1)

header = header_match.group(1)
footer = footer_match.group(1)

# In the header, let's make sure the logo points back to index.html#hero and the nav links point back to index.html
header = header.replace('href="#', 'href="index.html#')
# Fix logo specific
header = header.replace('href="index.html#hero"', 'href="index.html"')

award_template = """
    <section>
        <div class="container" style="padding-top: 4rem; padding-bottom: 6rem; max-width: 800px;">
            <div class="fade-up">
                <a href="index.html#recognition" class="text-link" style="margin-bottom: 2rem; display: inline-block;">&larr; Back to Portfolio</a>
                <br><br>
                <span class="section-label">{tag}</span>
                <h1 style="font-size: 3rem; margin-bottom: 1.5rem; letter-spacing: -0.03em;">{title}</h1>
                <p style="font-size: 1.2rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 3rem;">{description}</p>
                
                <div style="background: var(--surface); padding: 2.5rem; border-radius: 8px; border-top: 4px solid var(--accent); display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                    {details}
                </div>
            </div>
        </div>
    </section>
"""

pages = {
    "award-director.html": {
        "tag": "AWARD · SHORT FILM FESTIVAL",
        "title": "Best Director",
        "description": "Awarded Best Director for my short film in 2024. The film was recognized for its compelling storytelling and strong visual direction.",
        "details": "<div><div class='stat-label'>Year</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>2024</div></div><div><div class='stat-label'>Organisation</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>Short Film Festival</div></div>"
    },
    "award-editor.html": {
        "tag": "AWARD · SHORT FILM FESTIVAL",
        "title": "Best Editor",
        "description": "Awarded Best Editor for meticulous pacing and seamless cuts that enhanced the emotional arc of my short film in 2024.",
        "details": "<div><div class='stat-label'>Year</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>2024</div></div><div><div class='stat-label'>Organisation</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>Short Film Festival</div></div>"
    },
    "award-speaker.html": {
        "tag": "AWARD · UNODC MUN",
        "title": "Best Speaker",
        "description": "Recognized as Best Speaker at the UNODC Model United Nations 2024. This award was achieved by articulating nuanced perspectives on vigilante justice during complex debates.",
        "details": "<div><div class='stat-label'>Year</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>2024</div></div><div><div class='stat-label'>Organisation</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>UNODC Model United Nations</div></div>"
    }
}

for filename, data in pages.items():
    page_content = header + "\n" + award_template.format(**data) + "\n" + footer
    with open(filename, "w") as f:
        f.write(page_content)
    print(f"Generated {filename}")
