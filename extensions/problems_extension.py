"""
MkDocs extension for generating problem cards from problems.yaml

This extension reads problem metadata from problems.yaml and generates
a filterable problem grid with tags and difficulty levels.

Usage in markdown:
    !problemlist
"""

import re
try:
    import yaml
except ImportError:  # pragma: no cover - runtime fallback when PyYAML is not installed
    yaml = None
from pathlib import Path
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class ProblemsExtension(Extension):
    """MkDocs extension for problem list generation."""

    def __init__(self, **kwargs):
        self.config = {
            "problems_file": ["problems.yaml", "Path to the problems YAML file"]
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        problems_file = self.getConfig("problems_file")
        md.preprocessors.register(
            ProblemsPreprocessor(md, problems_file), "problemlist", 175
        )


class ProblemsPreprocessor(Preprocessor):
    """Preprocessor that replaces !problemlist with generated HTML."""

    tag = re.compile(r"^!problemlist\s*$", re.MULTILINE)

    def __init__(self, md, problems_file):
        super().__init__(md)
        self.problems_file = Path(problems_file)

    def run(self, lines):
        """Process lines and replace !problemlist tag."""
        text = "\n".join(lines)

        if self.tag.search(text):
            # Load problems from YAML
            problems = self._load_problems()

            # Generate HTML
            html = self._generate_html(problems)

            # Replace tag with HTML
            text = self.tag.sub(html, text)

        return text.split("\n")

    def _load_problems(self):
        """Load problems from YAML file."""
        # If PyYAML is not available, don't fail the whole MkDocs build.
        if yaml is None:
            print(
                "Warning: PyYAML is not installed; problems.yaml will not be loaded. Install PyYAML to enable problem list generation."
            )
            return []

        if not self.problems_file.exists():
            return []

        try:
            with open(self.problems_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
                return data.get("problems", [])
        except Exception as e:
            print(f"Error loading problems.yaml: {e}")
            return []

    def _generate_html(self, problems):
        """Generate the complete HTML for the problems page."""

        # Collect all unique values for filters
        all_difficulties = set()
        all_sources = set()
        all_topics = set()

        for problem in problems:
            all_difficulties.add(problem.get("difficulty", "Unknown"))
            all_sources.add(problem.get("source", "Unknown"))
            for topic in problem.get("topics", []):
                all_topics.add(topic)

        # Sort for consistent ordering
        all_difficulties = sorted(
            all_difficulties,
            key=lambda x: ["Very Easy", "Easy", "Medium", "Hard"].index(x)
            if x in ["Very Easy", "Easy", "Medium", "Hard"]
            else 999,
        )
        all_sources = sorted(all_sources)
        all_topics = sorted(all_topics)

        # Generate HTML sections
        html_parts = []

        # Tags toggle button
        html_parts.append("""
<!-- Tags menu at the top -->
<div style="margin-bottom: 20px;">
  <button class="tag-toggle" id="toggle-tags-btn" onclick="toggleTagPicker()" style="padding:5px 15px; cursor:pointer;">Tags ⬇️</button>
</div>
""")

        # Tag picker
        html_parts.append("""
<!-- Tag picker -->
<div class="tagbox" id="tag-picker" style="border:1px solid #868686; padding:10px; margin-bottom:20px; border-radius:5px; max-width:600px; display:none;">
""")

        # Difficulty filter
        html_parts.append("""
  <!-- Difficulty filter -->
  <strong>Difficulty: (วัดจากความยากในการแก้เมื่อคุณเข้าใจเนื้อหาที่ต้องใช้ในโจทย์ข้อนั้นแล้ว)</strong><br>
""")
        for difficulty in all_difficulties:
            html_parts.append(
                f'  <label><input type="checkbox" value="{difficulty}" class="filter-difficulty"> {difficulty}</label>\n'
            )

        html_parts.append("  <br><br>\n")

        # Source filter
        html_parts.append("  <!-- Source filter -->\n  <strong>Source:</strong><br>\n")
        for source in all_sources:
            html_parts.append(
                f'  <label><input type="checkbox" value="{source}" class="filter-source"> {source}</label>\n'
            )

        html_parts.append("  <br><br>\n")

        # Topics filter
        html_parts.append("  <!-- Topics filter -->\n  <strong>Topics:</strong><br>\n")
        for topic in all_topics:
            html_parts.append(
                f'  <label><input type="checkbox" value="{topic}" class="tag"> {topic}</label>\n'
            )

        html_parts.append("</div>\n\n")

        # Problems grid
        html_parts.append(
            '<!-- Problems grid -->\n<div class="grid cards" markdown="1">\n\n'
        )

        # Generate problem cards
        for problem in problems:
            card = self._generate_card(problem)
            html_parts.append(card)

        html_parts.append("\n</div>\n\n")

        # Add JavaScript
        html_parts.append(self._generate_javascript())

        # Add CSS
        html_parts.append(self._generate_css())

        return "".join(html_parts)

    def _generate_card(self, problem):
        """Generate HTML for a single problem card."""
        pid = problem.get("id", "")
        title = problem.get("title", "Untitled")
        link = problem.get("link", "#")
        difficulty = problem.get("difficulty", "Unknown")
        source = problem.get("source", "Unknown")
        topics = problem.get("topics", [])
        solution = problem.get("solution", f"/problems/{pid}")

        # Difficulty styling
        difficulty_class_map = {
            "Very Easy": "tip",
            "Easy": "success",
            "Medium": "warning",
            "Hard": "danger",
        }
        difficulty_class = difficulty_class_map.get(difficulty, "note")

        # Join topics for data attribute and display
        topics_str = ",".join(topics)
        topics_display = (
            "\n    - `{}`".format("`\n    - `".join(topics)) if topics else ""
        )

        card = f'''<div class="problem-card" data-difficulty="{difficulty}" data-source="{source}" data-topics="{topics_str}" markdown="1">
### [{title}]({link})

!!! {difficulty_class} "**Difficulty**: `{difficulty}`"
!!! quote "**Source**: `{source}`"
'''

        if topics:
            card += f"""??? Topics
{topics_display}

"""

        card += f"""[View Solution]({solution})
</div>

"""
        return card

    def _generate_javascript(self):
        """Generate JavaScript for filtering."""
        return """<!-- Scripts -->
<script>
// Toggle tag picker visibility and arrow direction
function toggleTagPicker() {
    const picker = document.getElementById('tag-picker');
    const btn = document.getElementById('toggle-tags-btn');

    const isHidden = picker.style.display === 'none';
    picker.style.display = isHidden ? 'block' : 'none';

    // Change arrow
    btn.textContent = isHidden ? 'Tags ⬆️' : 'Tags ⬇️';

    // Save visibility in localStorage
    localStorage.setItem('tagPickerVisible', picker.style.display);
}

// On page load, set arrow according to saved visibility
document.addEventListener("DOMContentLoaded", function() {
    const picker = document.getElementById('tag-picker');
    const btn = document.getElementById('toggle-tags-btn');
    const visible = localStorage.getItem('tagPickerVisible') || 'none';
    picker.style.display = visible;
    btn.textContent = visible === 'none' ? 'Tags ⬇️' : 'Tags ⬆️';

    // Add instant filtering when checkboxes are toggled
    document.querySelectorAll('.filter-difficulty, .filter-source, .tag').forEach(cb => {
        cb.addEventListener('change', applyFilter);
    });

    // Initial filter
    applyFilter();
});

// Apply filter
function applyFilter() {
    const selectedD = Array.from(document.querySelectorAll('.filter-difficulty:checked')).map(cb => cb.value);
    const selectedS = Array.from(document.querySelectorAll('.filter-source:checked')).map(cb => cb.value);
    const selectedT = Array.from(document.querySelectorAll('.tag:checked')).map(cb => cb.value);

    const cards = document.querySelectorAll('.problem-card');
    cards.forEach(card => {
        const cardD = card.getAttribute('data-difficulty').split(',').map(s => s.trim());
        const cardS = card.getAttribute('data-source').split(',').map(s => s.trim());
        const cardT = card.getAttribute('data-topics').split(',').map(s => s.trim());

        const visible = (selectedD.length === 0 || selectedD.some(d => cardD.includes(d))) &&
                        (selectedS.length === 0 || selectedS.some(s => cardS.includes(s))) &&
                        (selectedT.length === 0 || selectedT.every(t => cardT.includes(t)));

        card.style.display = visible ? '' : 'none';
    });
}
</script>

"""

    def _generate_css(self):
        """Generate CSS for problem cards."""
        return """<!-- CSS -->
<style>
.grid.cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 10px;
}
.problem-card {
    border: 1px solid #ccc;
    border-radius: 7px;
    padding: 15px;
    background: #fff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    color: grey;
}
.tagbox {
    color: black;
    border-color: #868686;
}
</style>
"""


def makeExtension(**kwargs):
    """Required function for MkDocs to load the extension."""
    return ProblemsExtension(**kwargs)
