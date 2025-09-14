---
hide: navigation, toc
---

# Algorithms

<!-- Tags menu at the top -->
<div style="margin-bottom: 20px;">
  <button class="tag-toggle" id="toggle-tags-btn" onclick="toggleTagPicker()" style="padding:5px 15px; cursor:pointer;">Tags ⬇️</button>
</div>

<!-- Tag picker -->
<div class="tagbox" id="tag-picker" style="border:1px solid #868686; padding:10px; margin-bottom:20px; border-radius:5px; background:#f9f9f9; max-width:600px; display:none;">

  <!-- Difficulty filter -->
  <strong>Difficulty:</strong><br>
  <label><input type="checkbox" value="Easy" class="filter-difficulty"> Easy</label>
  <label><input type="checkbox" value="Medium" class="filter-difficulty"> Medium</label>
  <label><input type="checkbox" value="Hard" class="filter-difficulty"> Hard</label>
  <br><br>

  <!-- Topics filter -->
  <strong>Topics:</strong><br>
  <label><input type="checkbox" value="Graph" class="tag"> Graph Algorithms</label>
  <label><input type="checkbox" value="Dynamic Programming" class="tag"> Dynamic Programming</label>
  <label><input type="checkbox" value="Data Structures" class="tag"> Data Structures</label>
</div>

<!-- Problems grid -->
<div class="grid cards" markdown="1">

<div class="problem-card" data-difficulty="Hard" data-topics="Dynamic Programming" markdown="1">
### Bitmask DP

!!! danger "**Difficulty**: `Hard`"
??? Topics
    - `Dynamic Programming`

[View Solution](/problems/toi20_bit_string)
</div>


</div>

<!-- Scripts -->
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

    // Add instant filtering on checkbox change
    document.querySelectorAll('.filter-difficulty, .tag').forEach(cb => {
        cb.addEventListener('change', applyFilter);
    });

    // Initial filter
    applyFilter();
});

// Apply filter
function applyFilter() {
    const selectedD = Array.from(document.querySelectorAll('.filter-difficulty:checked')).map(cb => cb.value);
    const selectedT = Array.from(document.querySelectorAll('.tag:checked')).map(cb => cb.value);

    const cards = document.querySelectorAll('.problem-card');
    cards.forEach(card => {
        const cardD = card.getAttribute('data-difficulty').split(',').map(s => s.trim());
        const cardT = card.getAttribute('data-topics').split(',').map(s => s.trim());

        const visible = (selectedD.length === 0 || selectedD.some(d => cardD.includes(d))) &&
                        (selectedT.length === 0 || selectedT.some(t => cardT.includes(t)));

        card.style.display = visible ? '' : 'none';
    });
}
</script>

<!-- CSS -->
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
