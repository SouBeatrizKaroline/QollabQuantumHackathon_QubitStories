# Qubit Stories — Laboratório multilíngue de aprendizagem quântica

## Descrição curta (213/240)

Quatro vídeos ilustrados e 64 capítulos em inglês, espanhol, português do Brasil e de Portugal, ligados a oito experiências Qiskit. Assista, preveja, execute e explique superposição, interferência e emaranhamento.

## Tema

Quantum Unlocked

## O que faz

Uma série educativa ilustrada conecta histórias a oito experiências executáveis em Qiskit. São quatro vídeos completos de aproximadamente 9min30s e 64 capítulos independentes com narração: 16 por variante de idioma. As imagens e as transições dos capítulos são alinhadas. Português do Brasil e de Portugal têm roteiros e vozes próprios. Os três vídeos originais do YouTube continuam disponíveis como referências.

Assista ao capítulo, escreva uma previsão, execute o circuito e explique o resultado. Compare probabilidades ideais com contagens amostradas. Mude a fase relativa para 0°, 90° ou 180° e compare medições antes e depois de uma Hadamard final. Compare correlações de Bell nas bases Z e X e explore a recuperação de um erro X controlado. As previsões são temporárias e não coletamos dados dos estudantes. Os benefícios educativos ainda não foram medidos em um estudo com participantes.

## Problema e contribuição

Conceitos quânticos podem ser difíceis de entender apenas com palavras. O projeto combina uma história ilustrada coerente, quatro variantes de idioma, links diretos de capítulos, previsões e experiências executáveis que permitem comparações. Torna a fase visível pela interferência, compara correlações entre bases e relaciona uma explicação de engenharia à recuperação de um erro de bit controlado. Não alegamos melhoria educativa medida.

## Vídeos educativos

| | Vídeos completos | Capítulos |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/media/chapters/pt-PT/README.md) |

## Como executar

1. Crie um projeto com **Upload your own files** e envie `qollab-runtime.zip`. Mantenha os arquivos de execução na raiz; não envie os vídeos MP4 para o Qollab.
2. Pressione **Run** e escolha um simulador gratuito. O Qollab fornece `backend`; o projeto não inclui credenciais de conta.
3. Escolha o idioma, abra um capítulo correspondente e escreva uma previsão antes de revelar o resultado.
4. Ajuste a fase, o número de medições ou a entrada lógica e execute novamente. Os oito circuitos são compilados e enviados em um único trabalho por execução, seguindo a restrição do IonQ no Qollab.

`index.html` e `main.js` selecionam a interface JS/Qiskit; o JavaScript chama Python pela ponte documentada `callPromising`. Essa interface precisa do ambiente Qollab. Para a alternativa apenas em Python, use `main.py`, `quantum.py` e `requirements.txt`, sem `index.html` ou `main.js`; o Qollab chama `main()` automaticamente.

## Limites científicos

O exemplo de repetição corrige um erro X injetado, não qualquer ruído. As ilustrações são metáforas. Probabilidades exatas são diferenciadas das contagens amostradas. Não alegamos vantagem quântica, tolerância a falhas ou resultados de hardware.

## Acessibilidade

Os vídeos incluem narração sintética, legendas incorporadas e arquivos ASS/SRT editáveis. Roteiros acompanham os materiais. O laboratório tem controles por teclado, foco visível, campos identificados, tabelas textuais de resultados e avisos de estado. Assistir aos vídeos é opcional; não há flashes ou reprodução automática forçada. A interface tem rótulos em inglês e português; os vídeos e documentos abrangem as quatro variantes. Não alegamos uma auditoria WCAG concluída.

## Código, licença e originalidade

A licença MIT abrange o software e a documentação. Os vídeos originais do YouTube pertencem aos respectivos titulares; links públicos não dão direito à redistribuição. Autoria, datas e ferramentas desses originais ainda não foram confirmadas. Novos roteiros, traduções, diagramas e produção foram preparados com assistência do Codex em 11 de outubro de 2026. As notas de produção informam a geração da imagem e o uso de vozes sintéticas. O texto original da licença MIT em inglês permanece o texto oficial; estas explicações não o substituem.

[Git repository](https://github.com/SouBeatrizKaroline/qubit-stories)

## Demonstração e publicação

A publicação dos materiais educativos no GitHub está concluída. Ainda faltam a importação no Qollab, os testes nos simuladores gratuitos e IonQ, a publicação sob MIT e a submissão ao hackathon. Uma demonstração pública separada de 2–3 minutos deve mostrar o laboratório executável; os vídeos educativos longos não a substituem.

---

[English](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/en/README.md) | [Português (Brasil)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-BR/README.md) | [Português (Portugal)](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/pt-PT/README.md) | [Español](https://github.com/SouBeatrizKaroline/qubit-stories/blob/main/docs/es/README.md)

This effort is supported by Qollab & IonQ
