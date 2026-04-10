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
# Wait, for simplicity, I can just replace `href="#` with `href="index.html#` globally in the header.
header = header.replace('href="#', 'href="index.html#')
# Fix logo specific
header = header.replace('href="index.html#hero"', 'href="index.html"')

venture_template = """
    <section>
        <div class="container" style="padding-top: 4rem; padding-bottom: 6rem; max-width: 800px;">
            <div class="fade-up">
                <a href="index.html#entrepreneurship" class="text-link" style="margin-bottom: 2rem; display: inline-block;">&larr; Back to Portfolio</a>
                <br><br>
                <span class="section-label">{tag}</span>
                <h1 style="font-size: 3rem; margin-bottom: 1.5rem; letter-spacing: -0.03em;">{title}</h1>
                <p style="font-size: 1.2rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 3rem;">{description}</p>
                
                {details}
                {extra_content}
            </div>
        </div>
    </section>
"""

pages = {
    "venture-pins.html": {
        "tag": "VENTURE · UAE NATIONAL DAY",
        "title": "National Day Pin Sales",
        "description": "Identified a seasonal opportunity around UAE National Day and sourced pins to resell within the school. Handled pricing, stock management, and direct peer-to-peer sales from start to finish.",
        "details": "<div style='background: var(--surface); padding: 2.5rem; border-radius: 8px; border-top: 4px solid var(--accent); display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;'><div><div class='stat-label'>Role</div><div style='font-size: 1.2rem; font-weight: 500; margin-top: 0.5rem;'>Organiser and Reseller</div></div></div>",
        "extra_content": """
            <div style="margin-top: 3rem; background: var(--surface); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--border);">
                <p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 2rem;">
                    Around UAE National Day, I noticed people were looking for pins and there wasn't really anywhere to get them at school. Myself and my team handled everything such as buying, selling, and keeping track of stock. It taught me more about how sales actually work than any class did.
                </p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                    <img src="UAE_Pins_1.webp" alt="UAE National Day Pins 1" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); object-fit: cover;">
                    <img src="UAE_Pins_2.webp" alt="UAE National Day Pins 2" style="width: 100%; border-radius: 6px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); object-fit: cover;">
                </div>
            </div>
        """
    },
    "venture-dates.html": {
        "tag": "CROSS-BORDER TRADE · 2025",
        "title": "Date Export Venture",
        "description": "Identified a price gap between dates in Dubai and Malaysia. Sourced three varieties, packaged them with custom stickers, and sold them directly to customers at a local market in Malaysia. Selling was slow until offering testers, which converted browsers into buyers quickly. Margins were tighter than expected after underpricing early on, which required adjusting prices mid-sale. Broke even overall. Came away with a practical understanding of sourcing, packaging, pricing, and direct sales that no classroom had given me.",
        "details": "",
        "extra_content": """
            <div style="margin-top: 4rem;">
                <span style="display: block; margin-bottom: 1.5rem; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.12em; color: var(--text-secondary); text-transform: uppercase;">PHOTOS</span>
                <style>
                    .date-slide { display: none; margin: auto; text-align: center; }
                    .date-slide img { width: 100%; max-height: 500px; object-fit: contain; border-radius: 8px; }
                    .date-slide.active { display: block; animation: date-fade .5s ease-in-out; }
                    @keyframes date-fade { from { opacity: .4; } to { opacity: 1; } }
                    .date-controls { display: flex; justify-content: center; gap: 1.5rem; align-items: center; margin-top: 1.5rem; }
                    .date-btn { cursor: pointer; width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--border); background: var(--surface); color: var(--accent); font-size: 18px; display: flex; align-items: center; justify-content: center; transition: .3s; box-shadow: 0 4px 12px rgba(0,0,0,0.05); user-select: none; }
                    .date-btn:hover { background: var(--accent); color: white; border-color: var(--accent); }
                    .date-dots { display: flex; gap: 8px; }
                    .date-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--border); cursor: pointer; transition: .3s; }
                    .date-dot.active-dot, .date-dot:hover { background: var(--accent); transform: scale(1.2); }
                </style>
                
                <div style="position: relative; max-width: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <div class="date-slide active"><img src="Date Plan/IMG_3251.webp"></div>
                    <div class="date-slide"><img src="Date Plan/IMG_3259.webp"></div>
                    <div class="date-slide"><img src="Date Plan/IMG_3661.webp"></div>
                    <div class="date-slide"><img src="Date Plan/Screenshot 2026-04-09 at 3.59.12 PM.webp"></div>
                    <div class="date-slide"><img src="Date Plan/Screenshot 2026-04-09 at 3.59.42 PM.webp"></div>
                    <div class="date-slide"><img src="Date Plan/Screenshot 2026-04-09 at 4.00.23 PM.webp"></div>
                    <div class="date-slide"><img src="Date Plan/Generated Image April 09, 2026 - 4_02PM.webp"></div>
                    <div class="date-slide"><img src="Date Plan/Generated Image April 09, 2026 - 4_03PM.webp"></div>

                    <div class="date-controls">
                        <div class="date-btn" onclick="nextDateSlide(-1)">&#10094;</div>
                        <div class="date-dots">
                            <div class="date-dot active-dot" onclick="setDateSlide(1)"></div>
                            <div class="date-dot" onclick="setDateSlide(2)"></div>
                            <div class="date-dot" onclick="setDateSlide(3)"></div>
                            <div class="date-dot" onclick="setDateSlide(4)"></div>
                            <div class="date-dot" onclick="setDateSlide(5)"></div>
                            <div class="date-dot" onclick="setDateSlide(6)"></div>
                            <div class="date-dot" onclick="setDateSlide(7)"></div>
                            <div class="date-dot" onclick="setDateSlide(8)"></div>
                        </div>
                        <div class="date-btn" onclick="nextDateSlide(1)">&#10095;</div>
                    </div>
                </div>

                <script>
                    let currentDateIndex = 1;
                    function nextDateSlide(n) { showDateSlide(currentDateIndex += n); }
                    function setDateSlide(n) { showDateSlide(currentDateIndex = n); }
                    function showDateSlide(n) {
                        let slides = document.getElementsByClassName("date-slide");
                        let dots = document.getElementsByClassName("date-dot");
                        if (!slides.length) return;
                        if (n > slides.length) currentDateIndex = 1;
                        if (n < 1) currentDateIndex = slides.length;
                        for (let i = 0; i < slides.length; i++) slides[i].classList.remove("active");
                        for (let i = 0; i < dots.length; i++) dots[i].classList.remove("active-dot");
                        slides[currentDateIndex-1].classList.add("active");
                        dots[currentDateIndex-1].classList.add("active-dot");
                    }
                </script>
            </div>
        """
    },
    "venture-bakesale.html": {
        "tag": "EVENT · FUNDRAISING",
        "title": "Charity Bake Sale",
        "description": "Organized and executed a charity bake sale, independently handling all logistics, finance, and marketing. Successfully generated over 2,000 dirhams in revenue for a local cause.",
        "details": "",
        "extra_content": """
            <div style="margin-top: 4rem;">
                <span style="display: block; margin-bottom: 1.5rem; font-size: 0.85rem; font-weight: 600; letter-spacing: 0.12em; color: var(--text-secondary); text-transform: uppercase;">PHOTOS</span>
                <style>
                    .bake-slide { display: none; margin: auto; text-align: center; }
                    .bake-slide img { width: 100%; max-height: 500px; object-fit: contain; border-radius: 8px; }
                    .bake-slide.active { display: block; animation: bake-fade .5s ease-in-out; }
                    @keyframes bake-fade { from { opacity: .4; } to { opacity: 1; } }
                    .bake-controls { display: flex; justify-content: center; gap: 1.5rem; align-items: center; margin-top: 1.5rem; }
                    .bake-btn { cursor: pointer; width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--border); background: var(--surface); color: var(--accent); font-size: 18px; display: flex; align-items: center; justify-content: center; transition: .3s; box-shadow: 0 4px 12px rgba(0,0,0,0.05); user-select: none; }
                    .bake-btn:hover { background: var(--accent); color: white; border-color: var(--accent); }
                    .bake-dots { display: flex; gap: 8px; }
                    .bake-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--border); cursor: pointer; transition: .3s; }
                    .bake-dot.active-dot, .bake-dot:hover { background: var(--accent); transform: scale(1.2); }
                </style>
                
                <div style="position: relative; max-width: 100%; display: flex; flex-direction: column; justify-content: center;">
                    <div class="bake-slide active"><img src="Bake Sale/IMG_5667.webp"></div>
                    <div class="bake-slide"><img src="Bake Sale/IMG_6507 copy.webp"></div>
                    <div class="bake-slide"><img src="Bake Sale/IMG_6512 copy.webp"></div>
                    <div class="bake-slide"><img src="Bake Sale/IMG_6515.webp"></div>
                    <div class="bake-slide"><img src="Bake Sale/Screenshot 2026-04-09 at 5.05.29 PM.webp"></div>
                    <div class="bake-slide"><img src="Bake Sale/Screenshot 2026-04-09 at 5.09.02 PM.webp"></div>

                    <div class="bake-controls">
                        <div class="bake-btn" onclick="nextBakeSlide(-1)">&#10094;</div>
                        <div class="bake-dots">
                            <div class="date-dot active-dot" onclick="setBakeSlide(1)"></div>
                            <div class="date-dot" onclick="setBakeSlide(2)"></div>
                            <div class="date-dot" onclick="setBakeSlide(3)"></div>
                            <div class="date-dot" onclick="setBakeSlide(4)"></div>
                            <div class="date-dot" onclick="setBakeSlide(5)"></div>
                            <div class="date-dot" onclick="setBakeSlide(6)"></div>
                        </div>
                        <div class="bake-btn" onclick="nextBakeSlide(1)">&#10095;</div>
                    </div>
                </div>

                <script>
                    let currentBakeIndex = 1;
                    function nextBakeSlide(n) { showBakeSlide(currentBakeIndex += n); }
                    function setBakeSlide(n) { showBakeSlide(currentBakeIndex = n); }
                    function showBakeSlide(n) {
                        let slides = document.getElementsByClassName("bake-slide");
                        let dots = document.querySelectorAll(".bake-controls .date-dot");
                        if (!slides.length) return;
                        if (n > slides.length) currentBakeIndex = 1;
                        if (n < 1) currentBakeIndex = slides.length;
                        for (let i = 0; i < slides.length; i++) slides[i].classList.remove("active");
                        for (let i = 0; i < dots.length; i++) dots[i].classList.remove("active-dot");
                        slides[currentBakeIndex-1].classList.add("active");
                        dots[currentBakeIndex-1].classList.add("active-dot");
                    }
                </script>
            </div>
        """
    }
}

for filename, data in pages.items():
    page_content = header + "\n" + venture_template.format(**data) + "\n" + footer
    with open(filename, "w") as f:
        f.write(page_content)
    print(f"Generated {filename}")

