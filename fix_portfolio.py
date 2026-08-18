from pathlib import Path
import re

path = Path(r"f:\PORTFLIO\portfolio (2).html")
text = path.read_text(encoding="utf-8")

new_text, count_photo = re.subn(
    r'<div data-reveal class="photo-slot"><img src="data:image/jpeg;base64,.*?</div>',
    '<div data-reveal class="photo-slot"><img src="assets/profile-taj.png" alt="NCC photo" /><span class="photo-caption">NCC · Under Officer</span></div>',
    text,
    count=1,
    flags=re.S,
)

new_text, count_gallery = re.subn(
    r'\s*<div class="tier-label">NCC — moments</div>\s*<div class="photo-strip">.*?</div>\s*</div>\s*</section>',
    '\n  </section>',
    new_text,
    count=1,
    flags=re.S,
)

path.write_text(new_text, encoding="utf-8")
print(f"photo block updated: {count_photo}; NCC gallery removed: {count_gallery}")
