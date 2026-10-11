# Qubit Stories — Laboratório multilingue de aprendizagem quântica

## Descrição curta (206/240)

Quatro vídeos ilustrados e 64 capítulos em inglês, espanhol, português do Brasil e de Portugal, ligados a oito experiências Qiskit. Vê, prevê, executa e explica sobreposição, interferência e entrelaçamento.

## Tema

Quantum Unlocked

## O que faz

Uma série educativa ilustrada liga histórias a oito experiências executáveis em Qiskit. Existem quatro vídeos completos de aproximadamente 9min30s e 64 capítulos independentes com narração: 16 por variante linguística. As imagens e as transições dos capítulos estão alinhadas. As versões em português do Brasil e de Portugal têm guiões e vozes próprios. Os três vídeos originais do YouTube continuam disponíveis como referências.

Vê o capítulo correspondente, escreve uma previsão, executa o circuito e explica o resultado. Compara probabilidades ideais com contagens amostradas. Altera a fase relativa para 0°, 90° ou 180° e compara medições antes e depois de uma Hadamard final. Compara correlações de Bell nas bases Z e X e explora a recuperação de um erro X controlado. As previsões são temporárias e não recolhemos dados dos estudantes. Os benefícios educativos ainda não foram medidos num estudo com participantes.

## Problema e contributo

Os conceitos quânticos podem ser difíceis de compreender apenas com palavras. O projeto combina uma história ilustrada coerente, quatro variantes linguísticas, ligações diretas aos capítulos, previsões e experiências executáveis que permitem comparações. Torna a fase visível através da interferência, compara correlações entre bases e relaciona uma explicação de engenharia com a recuperação de um erro de bit controlado. Não alegamos melhoria educativa medida.

## Vídeos educativos

| | Vídeos completos | Capítulos |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt-PT/README.md) |

## Como executar

1. Cria um projeto com **Upload your own files** e carrega `qollab-runtime.zip`. Mantém os ficheiros de execução na raiz; não carregues os vídeos MP4 para o Qollab.
2. Prime **Run** e escolhe um simulador gratuito. O Qollab fornece `backend`; o projeto não inclui credenciais de conta.
3. Escolhe a variante linguística, abre um capítulo correspondente e escreve uma previsão antes de revelar o resultado.
4. Ajusta a fase, o número de medições ou a entrada lógica e executa novamente. Os oito circuitos são compilados e enviados num único trabalho por execução, respeitando a restrição do IonQ no Qollab.

`index.html` e `main.js` selecionam a interface JS/Qiskit; o JavaScript chama Python através da ponte documentada `callPromising`. Esta interface precisa do ambiente Qollab. Para a alternativa apenas em Python, usa `main.py`, `quantum.py` e `requirements.txt`, sem `index.html` nem `main.js`; o Qollab chama `main()` automaticamente.

## Limites científicos

O exemplo de repetição corrige um erro X introduzido, não qualquer ruído. As ilustrações são metáforas. As probabilidades exatas distinguem-se das contagens amostradas. Não alegamos vantagem quântica, tolerância a falhas ou resultados de hardware.

## Acessibilidade

Os vídeos incluem narração sintética, legendas incorporadas e ficheiros ASS/SRT editáveis. Os guiões acompanham os materiais. O laboratório disponibiliza controlos por teclado, foco visível, campos identificados, tabelas textuais de resultados e avisos de estado. Ver os vídeos é opcional; não há efeitos intermitentes nem reprodução automática forçada. A interface tem rótulos em inglês e português; os vídeos e documentos abrangem as quatro variantes. Não alegamos uma auditoria WCAG concluída.

## Código, licença e originalidade

A licença MIT abrange o software e a documentação. Os vídeos originais do YouTube pertencem aos respetivos titulares; ligações públicas não dão direito à redistribuição. A autoria, as datas e as ferramentas desses originais ainda não foram confirmadas. Os novos guiões, traduções, diagramas e produção foram preparados com assistência do Codex em 11 de outubro de 2026. As notas de produção identificam a geração da imagem e as vozes sintéticas. O texto original da licença MIT em inglês mantém-se como texto oficial; estas explicações não o substituem.

[Git repository](https://github.com/SouBeatrizKaroline/qubit-stories)

## Demonstração e publicação

A publicação dos materiais educativos no GitHub está concluída. Ainda faltam a importação no Qollab, as verificações nos simuladores gratuitos e IonQ, a publicação sob MIT e a submissão ao hackathon. Uma demonstração pública separada de 2–3 minutos deve mostrar o laboratório executável; os vídeos educativos longos não a substituem.

---

[English](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/en/README.md) | [Português (Brasil)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-BR/README.md) | [Português (Portugal)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-PT/README.md) | [Español](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/es/README.md)

This effort is supported by Qollab & IonQ
