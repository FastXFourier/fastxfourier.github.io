function toggleTagPicker() {
  const picker = document.getElementById('tag-picker');
  const btn = document.getElementById('toggle-tags-btn');

  const isHidden = picker.style.display === 'none';
  picker.style.display = isHidden ? 'block' : 'none';
  btn.textContent = isHidden ? 'Tags ⬇️' : 'Tags ⬆️';

  localStorage.setItem('tagPickerVisible', picker.style.display);
}

document.addEventListener("DOMContentLoaded", () => {
  const picker = document.getElementById('tag-picker');
  const btn = document.getElementById('toggle-tags-btn');
  if (!picker || !btn) return;

  const visible = localStorage.getItem('tagPickerVisible') || 'none';
  picker.style.display = visible;
  btn.textContent = visible === 'none' ? 'Tags ⬆️' : 'Tags ⬇️';

  document.querySelectorAll('.filter-difficulty, .tag')
    .forEach(cb => cb.addEventListener('change', applyFilter));

  applyFilter();
});

function applyFilter() {
  const selectedD = [...document.querySelectorAll('.filter-difficulty:checked')].map(cb => cb.value);
  const selectedT = [...document.querySelectorAll('.tag:checked')].map(cb => cb.value);

  document.querySelectorAll('.problem-card').forEach(card => {
    const cardD = card.dataset.difficulty.split(',').map(s => s.trim());
    const cardT = card.dataset.topics.split(',').map(s => s.trim());

    const visible =
      (selectedD.length === 0 || selectedD.some(d => cardD.includes(d))) &&
      (selectedT.length === 0 || selectedT.some(t => cardT.includes(t)));

    card.style.display = visible ? '' : 'none';
  });
}
