# Qollab submission — lightweight Python package

Upload `qollab-runtime.zip` using **Upload your own files**. The archive has
`main.py` at its root and uses the Python/Qiskit project shape.
You can also upload `main.py` alone: all eight experiments and video links
are included in that single file. Do not add `index.html` or `main.js` to
this Python upload.

Qollab supplies `backend` and calls `main()` automatically. Select a free
simulator and press **Run**. There are no credentials or network downloads
in the program. It submits all eight circuits as one backend job per run.

The output lists full videos in EN, ES, pt-BR and pt-PT, plus relevant
chapter links. `VIDEOS.md` is a clickable index of all 64 chapters.
Videos open externally; no MP4 is included in this archive.

To change the experiment, edit the defaults in `main()`:
- `phase_degrees`: 0, 90 or 180
- `shots`: 32 to 4096
- `logical_one`: False or True
- `language`: "en", "es", "pt-BR" or "pt-PT" (chapter links)

Local run: install `requirements.txt` and run `python main.py`.
Code and documentation are MIT licensed; see LICENSE.
The error-recovery activity corrects one injected X error, not arbitrary
noise. No hardware result or measured educational benefit is claimed.
Qollab and IonQ execution must still be verified before submission.

Repository:
https://github.com/SouBeatrizKaroline/QollabQuantumHackathon_QubitStories

This effort is supported by Qollab & IonQ
