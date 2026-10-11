# Notas de produção

Uma série educativa ilustrada liga histórias a oito experiências executáveis em Qiskit. Existem quatro vídeos completos de aproximadamente 9min30s e 64 capítulos independentes com narração: 16 por variante linguística. As imagens e as transições dos capítulos estão alinhadas. As versões em português do Brasil e de Portugal têm guiões e vozes próprios. Os três vídeos originais do YouTube continuam disponíveis como referências.

## Conteúdo e formato

A referência mostra uma menina e uma mascote luminosa numa floresta noturna. Foi gerada uma nova ilustração para este projeto. A montagem combina essa imagem, movimento de câmara, cartões explicativos, diagramas e legendas. A narração é sintética e não há sincronização labial. As versões mantêm a sequência dos capítulos e aproximadamente 9min30s; a adaptação de Portugal utiliza vocabulário, construções e voz europeus.

## Ferramentas e formato

Guiões, traduções, diagramas e edição: assistência do Codex. Ilustração: geração de imagem integrada. Voz: edge-tts com as vozes abaixo. Montagem: Pillow e FFmpeg. Saída: 1280 × 720, 24 fotogramas por segundo, vídeo H.264 e áudio AAC. Os tempos das palavras do serviço de voz orientam as legendas; os ficheiros ASS/SRT permitem edição. A velocidade da narração é ajustada por capítulo para alinhar as transições. Os novos vídeos estão no GitHub e não foram carregados para o YouTube. O capítulo 15 das três versões anteriores cita as histórias originais; a adaptação portuguesa mais recente apresenta as quatro variantes linguísticas.

| Locale | Voice |
|---|---|
| en-US | en-US-AriaNeural |
| es-MX | es-MX-DaliaNeural |
| pt-BR | pt-BR-FranciscaNeural |
| pt-PT | pt-PT-RaquelNeural |

## Prompt original da ilustração

```text
Use case: illustration-story. Asset type: cinematic illustrated educational video background. Create a polished wide 16:9 landscape illustration, highest practical resolution. A whimsical bioluminescent forest at night, glowing violet mushrooms, teal trees, fireflies, an old stone path that leads to a tiny observatory under stars. On the far RIGHT third stand a curious young girl with medium brown skin, curly dark hair in two puffs, yellow T-shirt, denim overalls, pink shoes and a small green backpack; beside her floats a friendly round pale cyan luminous mascot with expressive eyes and tiny arms. Original stylized 3D children's animation aesthetic, coherent anatomy, soft cinematic lighting, expressive but calm, charming, detailed. Left half should have dark calm uncluttered space and atmosphere for explanatory diagrams placed later in editing. No typography, no logos, no symbols, no visible writing, no mathematical graphics. Do not depict magic as literal science. One continuous environment, no collage or panels. Keep girl and mascot entirely inside frame with space above and below.
```

## Verificação e limites

As verificações locais abrangem número de capítulos, duração, áudio descodificável e comportamento do Qiskit. As prévias visuais são inspecionadas. A série distingue sobreposição de desconhecimento clássico, fase de probabilidades e correlação de comunicação. A recuperação de erro está limitada ao modelo de um erro X declarado. Não alegamos tradução perfeita, certificação completa de acessibilidade, execução em hardware real ou tolerância a falhas.

A publicação dos materiais educativos no GitHub está concluída. Ainda faltam a importação no Qollab, as verificações nos simuladores gratuitos e IonQ, a publicação sob MIT e a submissão ao hackathon. Uma demonstração pública separada de 2–3 minutos deve mostrar o laboratório executável; os vídeos educativos longos não a substituem.

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](../../docs/en/README.md) | [Português (Brasil)](../../docs/pt-BR/README.md) | [Português (Portugal)](../../docs/pt-PT/README.md) | [Español](../../docs/es/README.md)

This effort is supported by Qollab & IonQ
