async function fillUoms(selectId, selectedId){
  const sel = document.getElementById(selectId);
  if(!sel) return;
  sel.innerHTML = '';
  const uoms = await (await fetch('/api/uoms')).json();
  for(const u of uoms){
    const opt = document.createElement('option');
    opt.value = u.id; opt.textContent = u.name;
    if(selectedId && Number(selectedId) === Number(u.id)) opt.selected = true;
    sel.appendChild(opt);
  }
}
