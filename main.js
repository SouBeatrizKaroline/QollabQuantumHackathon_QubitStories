import * as quantum from 'quantum';

const videoInfo = [["The Forest of Qubits", "English · 16 chapters / capítulos", "https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4"], ["A floresta dos qubits", "Português (Brasil) · 16 chapters / capítulos", "https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4"], ["El bosque de los cúbits", "Español · 16 chapters / capítulos", "https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4"], ["A floresta dos qubits — Portugal", "Português (Portugal) · 16 chapters / capítulos", "https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4"]];
const videoRoot = document.getElementById('videos');
videoInfo.forEach(([title, subtitle, url]) => {
  const card = document.createElement('article');
  const heading = document.createElement('h3'); heading.textContent = title;
  const description = document.createElement('p'); description.textContent = subtitle;
  const link = document.createElement('a'); link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer'; link.textContent = 'Watch / Assistir ↗';
  card.append(heading, description, link); videoRoot.append(card);
});
const status = document.getElementById('status');
const runButton = document.getElementById('run');
function element(tag, text, className) { const e = document.createElement(tag); e.textContent = text; if (className) e.className = className; return e; }
function render(report) {
  const root = document.getElementById('lessons'); root.replaceChildren();
  report.experiments.forEach((lesson, index) => {
    const card = element('article', '', 'lesson');
    card.append(element('p', `EXPERIMENT ${index + 1}`, 'eyebrow'), element('h3', lesson.title));
    const links = element('div', '', 'timestamps');
    lesson.links.forEach((url, i) => {
      const link = element('a', `${videoInfo[i][0]} · Chapter / Capítulo ${lesson.chapter} ↗`);
      link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer'; links.append(link);
    });
    card.append(links, element('p', 'What do you expect? / O que você espera?'));
    const prediction = element('textarea', ''); prediction.rows = 2; prediction.setAttribute('aria-label', `Your prediction for ${lesson.title}`); prediction.placeholder = 'Write your prediction / Escreva sua previsão'; card.append(prediction);
    const details = document.createElement('details'); details.append(element('summary', 'Reveal & compare / Revelar e comparar'));
    details.append(element('p', `Theory: ${lesson.prediction}`), element('p', lesson.explanation), element('pre', lesson.diagram));
    details.append(element('p', `Ideal probabilities: ${JSON.stringify(lesson.ideal)}`));
    const total = Object.values(lesson.counts).reduce((a,b) => a + b, 0);
    const table = document.createElement('table'); const caption = element('caption', `Observed counts · ${total} shots`); table.append(caption);
    const head = document.createElement('thead'); const hr = document.createElement('tr'); ['Outcome','Count','Frequency'].forEach(t=>hr.append(element('th',t))); head.append(hr); table.append(head);
    const body = document.createElement('tbody'); Object.entries(lesson.counts).sort().forEach(([outcome,count]) => {const row = document.createElement('tr'); row.append(element('td', outcome),element('td',String(count)),element('td',`${(100*count/total).toFixed(1)}%`)); body.append(row);}); table.append(body); details.append(table);
    if (lesson.key === 'corrected') {
      const recovered = Object.entries(lesson.counts).filter(([bits]) => bits.replaceAll(' ','').endsWith(report.logical_one ? '1' : '0')).reduce((n,[,count]) => n+count,0);
      details.append(element('p', `Recovered logical bit (rightmost): ${(100*recovered/total).toFixed(1)}% correct. Other bits are syndrome ancillas.`));
    }
    card.append(details); root.append(card);
  });
}
async function run() {
  runButton.disabled = true; status.textContent = 'Running eight circuits in one job… / Executando oito circuitos…';
  try {
    const shots = Number(document.getElementById('shots').value);
    const phase = Number(document.getElementById('phase').value) * Math.PI / 180;
    const report = JSON.parse(await quantum.run_suite.callPromising(backend, shots, phase, document.getElementById('logical').checked));
    render(report); status.textContent = `Ready · ${shots} shots per circuit. Results are from your selected backend.`;
  } catch (error) { status.textContent = `Could not run: ${error.message || error}. Select a free simulator in Qollab and try again.`; }
  finally { runButton.disabled = false; }
}
runButton.addEventListener('click', run);
await run();
