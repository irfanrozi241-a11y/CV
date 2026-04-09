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
header = header.replace('href="index.html#hero"', 'href="index.html"')

volunteer_page_content = """
    <style>
        .gallery-container {
            position: relative;
            max-width: 800px;
            margin: auto;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
            border-top: 4px solid var(--accent);
        }
        .slide {
            display: none;
            background: var(--surface);
            padding: 4rem 3rem;
            text-align: left;
            min-height: 400px;
            align-items: center;
            gap: 3rem;
            animation: fade 0.5s ease-in-out;
        }
        .slide-content {
            flex: 1;
        }
        .slide-image {
            flex: 1;
            height: 300px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .slide-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .slide.active {
            display: flex;
        }
        @keyframes fade {
            from {opacity: .4} 
            to {opacity: 1}
        }
        .prev, .next {
            cursor: pointer;
            position: absolute;
            top: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: -20px;
            color: var(--accent);
            font-weight: bold;
            font-size: 18px;
            transition: 0.3s ease;
            border-radius: 50%;
            user-select: none;
            background-color: var(--surface);
            border: 1px solid var(--border);
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .prev {
            left: 1rem;
        }
        .next {
            right: 1rem;
        }
        .prev:hover, .next:hover {
            background-color: var(--accent);
            color: white;
            border-color: var(--accent);
        }
        .dot-container {
            text-align: center;
            padding: 1.5rem;
        }
        .dot {
            cursor: pointer;
            height: 10px;
            width: 10px;
            margin: 0 5px;
            background-color: #d8d8d8;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .active-dot, .dot:hover {
            background-color: var(--accent);
            transform: scale(1.2);
        }
        .gallery-tag {
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.12em;
            color: var(--text-secondary);
            margin-bottom: 1rem;
            text-transform: uppercase;
        }
        .gallery-title {
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
        }
        .gallery-desc {
            font-size: 1.15rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.7;
        }
    </style>

    <section>
        <div class="container" style="padding-top: 4rem; padding-bottom: 6rem; max-width: 900px;">
            <div class="fade-up">
                <a href="index.html#volunteer" class="text-link" style="margin-bottom: 2rem; display: inline-block;">&larr; Back to Portfolio</a>
                <br><br>
                <div style="text-align: center; margin-bottom: 4rem;">
                    <span class="section-label">COMMUNITY SERVICE</span>
                    <h1 style="font-size: clamp(3rem, 6vw, 4rem); margin-bottom: 1.5rem; letter-spacing: -0.03em; color: var(--accent);">300+ Hours</h1>
                    <p style="font-size: 1.2rem; line-height: 1.8; color: var(--text-secondary); max-width: 700px; margin: 0 auto;">A look into the specific initiatives, organizations, and impact I've contributed to over the years, demonstrating a consistent commitment to community service.</p>
                </div>

                <div class="gallery-container">
                    <!-- Slide 1 -->
                    <div class="slide active">
                        <div class="slide-content">
                            <div class="gallery-tag">LEADERSHIP</div>
                            <h2 class="gallery-title">National Honor Society</h2>
                            <p class="gallery-desc" style="margin: 0;">Serving through the National Honor Society, I organized peer tutoring, managed community clean-ups, and coordinated school-wide charity drives. Consistency and reliable commitment were key to my role.</p>
                        </div>
                        <div class="slide-image">
                            <img src="nhs_volunteering.png" alt="National Honor Society Volunteering">
                        </div>
                    </div>
                    <!-- Slide 2 -->
                    <div class="slide">
                        <div class="slide-content">
                            <div class="gallery-tag">COMMUNITY EVENT</div>
                            <h2 class="gallery-title">Charity Bake Sale</h2>
                            <p class="gallery-desc" style="margin: 0;">Beyond the logistics and planning, the bake sale involved extensive volunteer hours coordinating teams, managing booths on the day, and ensuring total transparency for the AED 2,000+ raised.</p>
                        </div>
                        <div class="slide-image">
                            <img src="bake_sale.png" alt="Charity Bake Sale">
                        </div>
                    </div>
                    <!-- Slide 3 -->
                    <div class="slide">
                        <div class="slide-content">
                            <div class="gallery-tag">ENVIRONMENT</div>
                            <h2 class="gallery-title">Sustainability Ambassador</h2>
                            <p class="gallery-desc" style="margin: 0;">Dedicated extensive hours to promoting sustainability on campus and in the local community. This included organizing recycling initiatives and raising awareness about ecological footprints among the student body.</p>
                        </div>
                        <div class="slide-image">
                            <img src="sustainability.png" alt="Sustainability Ambassador">
                        </div>
                    </div>
                    <!-- Slide 4 -->
                    <div class="slide">
                        <div class="slide-content">
                            <div class="gallery-tag">MENTORSHIP</div>
                            <h2 class="gallery-title">Debate Club Mentoring</h2>
                            <p class="gallery-desc" style="margin: 0;">Volunteered significant time as a mentor for younger students in the Debate Club, guiding them step-by-step through argument structuring, public speaking techniques, and building intellectual confidence.</p>
                        </div>
                        <div class="slide-image">
                            <img src="debate_club.png" alt="Debate Club Mentoring">
                        </div>
                    </div>

                    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                    <a class="next" onclick="plusSlides(1)">&#10095;</a>
                </div>
                
                <div class="dot-container">
                    <span class="dot active-dot" onclick="currentSlide(1)"></span> 
                    <span class="dot" onclick="currentSlide(2)"></span> 
                    <span class="dot" onclick="currentSlide(3)"></span> 
                    <span class="dot" onclick="currentSlide(4)"></span> 
                </div>

            </div>
        </div>
    </section>

    <script>
        let slideIndex = 1;

        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function currentSlide(n) {
            showSlides(slideIndex = n);
        }

        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("slide");
            let dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}    
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
                slides[i].className = slides[i].className.replace(" active", "");
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active-dot", "");
            }
            slides[slideIndex-1].className += " active";
            dots[slideIndex-1].className += " active-dot";
        }
    </script>
"""

page_content = header + "\n" + volunteer_page_content + "\n" + footer
with open("volunteer-details.html", "w") as f:
    f.write(page_content)
    
print("Generated volunteer-details.html")
