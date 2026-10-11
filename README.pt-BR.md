# Qubit Stories — Laboratório multilíngue de aprendizagem quântica

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

Uma série educativa ilustrada conecta histórias a oito experiências executáveis em Qiskit. São quatro vídeos completos de aproximadamente 9min30s e 64 capítulos independentes com narração: 16 por variante de idioma. As imagens e as transições dos capítulos são alinhadas. Português do Brasil e de Portugal têm roteiros e vozes próprios. Os três vídeos originais do YouTube continuam disponíveis como referências.

| | Vídeos completos | Capítulos |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](media/chapters/pt-PT/README.md) |

Assista ao capítulo, escreva uma previsão, execute o circuito e explique o resultado. Compare probabilidades ideais com contagens amostradas. Mude a fase relativa para 0°, 90° ou 180° e compare medições antes e depois de uma Hadamard final. Compare correlações de Bell nas bases Z e X e explore a recuperação de um erro X controlado. As previsões são temporárias e não coletamos dados dos estudantes. Os benefícios educativos ainda não foram medidos em um estudo com participantes.

## Executar no Qollab

1. Crie um projeto com **Upload your own files** e envie `qollab-runtime.zip`. Mantenha os arquivos de execução na raiz; não envie os vídeos MP4 para o Qollab.
2. Pressione **Run** e escolha um simulador gratuito. O Qollab fornece `backend`; o projeto não inclui credenciais de conta.
3. Escolha o idioma, abra um capítulo correspondente e escreva uma previsão antes de revelar o resultado.
4. Ajuste a fase, o número de medições ou a entrada lógica e execute novamente. Os oito circuitos são compilados e enviados em um único trabalho por execução, seguindo a restrição do IonQ no Qollab.

`index.html` e `main.js` selecionam a interface JS/Qiskit; o JavaScript chama Python pela ponte documentada `callPromising`. Essa interface precisa do ambiente Qollab. Para a alternativa apenas em Python, use `main.py`, `quantum.py` e `requirements.txt`, sem `index.html` ou `main.js`; o Qollab chama `main()` automaticamente.

[Baixar o pacote Qollab](qollab-runtime.zip)

## Executar localmente e verificar

É necessário Python 3.10+ e Qiskit 2.x. A execução local usa o `BasicSimulator` gratuito do Qiskit. Os três testes verificam fase/interferência, recuperação coerente de um erro X em cada posição e envio de um único trabalho com os totais de contagens. A execução no Qollab e no IonQ ainda não foi verificada.

```sh
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```

## Escopo científico

- Personagens e floresta são metáforas visuais; um qubit é um estado quântico, não uma esfera luminosa.
- Amplitudes e fase relativa distinguem superposição de desconhecimento clássico. Cada medição entrega um resultado; distribuições exigem novas preparações.
- Correlações em uma única base não provam emaranhamento. A preparação de Bell e a comparação X/Z destacam coerência; não é um teste de Bell sem brechas. Emaranhamento não permite mensagens mais rápidas que a luz.
- O código de repetição de três qubits recupera um erro X injetado. Não corrige ruído arbitrário, erros de fase ou dois erros de bit, e não demonstra tolerância a falhas. O qubit lógico recuperado é q0, o bit à direita nas strings do Qiskit; os demais guardam informação da síndrome.
- Probabilidades ideais exatas diferem das contagens do simulador. Não alegamos execução em hardware real, vantagem quântica ou melhoria de aprendizagem medida.
- Os circuitos não modelam resfriamento de supercondutores, lasers de íons aprisionados, simulação molecular ou sensores mencionados nas histórias.

## Acessibilidade

Os vídeos incluem narração sintética, legendas incorporadas e arquivos ASS/SRT editáveis. Roteiros acompanham os materiais. O laboratório tem controles por teclado, foco visível, campos identificados, tabelas textuais de resultados e avisos de estado. Assistir aos vídeos é opcional; não há flashes ou reprodução automática forçada. A interface tem rótulos em inglês e português; os vídeos e documentos abrangem as quatro variantes. Não alegamos uma auditoria WCAG concluída.

## Fontes, autoria e licença

A licença MIT abrange o software e a documentação. Os vídeos originais do YouTube pertencem aos respectivos titulares; links públicos não dão direito à redistribuição. Autoria, datas e ferramentas desses originais ainda não foram confirmadas. Novos roteiros, traduções, diagramas e produção foram preparados com assistência do Codex em 11 de outubro de 2026. As notas de produção informam a geração da imagem e o uso de vozes sintéticas. O texto original da licença MIT em inglês permanece o texto oficial; estas explicações não o substituem.

- [The World of Qubits — English](https://youtu.be/EAcDVqTb0lk)
- [O Mundo dos Qubits — pt-BR](https://youtu.be/nkQpc2YPSCA)
- [The Fellowship Of The Qubit — English](https://youtu.be/uPTSfysNvgw)

## Situação da entrega

A publicação dos materiais educativos no GitHub está concluída. Ainda faltam a importação no Qollab, os testes nos simuladores gratuitos e IonQ, a publicação sob MIT e a submissão ao hackathon. Uma demonstração pública separada de 2–3 minutos deve mostrar o laboratório executável; os vídeos educativos longos não a substituem.

## Documentação

- [README](docs/pt-BR/README.md)
- [Project Card](docs/pt-BR/QOLLAB_PROJECT_CARD.md)
- [Guia de preenchimento](docs/pt-BR/QOLLAB_SETUP.md)
- [Lista de preparação](docs/pt-BR/SUBMISSION_CHECKLIST.md)
- [Origem e autoria](docs/pt-BR/PROVENANCE.md)
- [Notas de produção](docs/pt-BR/PRODUCTION_NOTES.md)
- [Entregáveis](docs/pt-BR/DELIVERABLES.md)

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

This effort is supported by Qollab & IonQ
