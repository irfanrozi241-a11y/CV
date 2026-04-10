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

# Fix paths in header
header = header.replace('href="#', 'href="index.html#')
header = header.replace('href="index.html#hero"', 'href="index.html"')

reflection_day_content = """
    <section>
        <div class="container" style="padding-top: 4rem; padding-bottom: 6rem;">
            <div class="fade-up">
                <a href="index.html#leadership" class="text-link" style="margin-bottom: 2rem; display: inline-block;">&larr; Back to Leadership</a>
                <br><br>
                <span class="section-label">EVENT ORGANISER · STUDENT COUNCIL</span>
                <h1 style="font-size: 3.5rem; margin-bottom: 1.5rem; letter-spacing: -0.03em;">Reflection Day Lead Organiser</h1>
                <p style="font-size: 1.25rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 4rem; max-width: 800px;">
                    Reflection Day is a cornerstone event in the school calendar. As the Lead Organiser, I was responsible for transforming a high-level concept into a fully operational day-long event for hundreds of students.
                </p>
                
                <!-- Section 1: Alternating Layout (Image Left, Text Right) -->
                <div class="lead-row fade-up" style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 4rem; align-items: center; margin-bottom: 8rem;">
                    <div class="lead-image" style="aspect-ratio: 16/10; overflow: hidden; border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                        <img src="Building Communities From Scratch/reflection_planning.webp" alt="Planning and Logistics" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div class="lead-text">
                        <span class="lead-tag">PHASE 1</span>
                        <h2 style="font-size: 2.25rem; margin-bottom: 1.5rem;">Strategic Planning & Logistics</h2>
                        <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">
                            The success of Reflection Day was rooted in meticulous planning. I coordinated with various departments to manage logistics, from catering and venue booking to finance and procurement. Every detail, from the minute-by-minute schedule to the dietary requirements of participants, was cross-referenced and validated.
                        </p>
                    </div>
                </div>

                <!-- Section 2: Alternating Layout (Text Left, Image Right) -->
                <div class="lead-row fade-up" style="display: grid; grid-template-columns: 0.8fr 1.2fr; gap: 4rem; align-items: center; margin-bottom: 4rem;">
                    <div class="lead-text" style="order: 1;">
                        <span class="lead-tag">PHASE 2</span>
                        <h2 style="font-size: 2.25rem; margin-bottom: 1.5rem;">Media Production & Execution</h2>
                        <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">
                            Beyond logistics, I led the media team in capturing the essence of the day. This involved managing photographers, videographers, and graphic designers to create a cohesive visual narrative. On the day of the event, I acted as the primary point of contact, ensuring that every session ran smoothly and that any unforeseen issues were resolved instantly.
                        </p>
                    </div>
                    <div class="lead-image" style="order: 2; aspect-ratio: 16/10; overflow: hidden; border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                        <img src="Building Communities From Scratch/Reflection Day.webp" alt="Event Execution" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <style>
        @media (max-width: 992px) {
            .lead-row {
                grid-template-columns: 1fr !important;
                gap: 2rem !important;
                margin-bottom: 4rem !important;
            }
            .lead-text {
                order: 2 !important;
            }
            .lead-image {
                order: 1 !important;
            }
        }
    </style>
"""

with open("reflection-day.html", "w") as f:
    f.write(header + reflection_day_content + footer)
    print("Generated reflection-day.html")
