# Qubit Stories — Laboratório multilingue de aprendizagem quântica

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

Uma série educativa ilustrada liga histórias a oito experiências executáveis em Qiskit. Existem quatro vídeos completos de aproximadamente 9min30s e 64 capítulos independentes com narração: 16 por variante linguística. As imagens e as transições dos capítulos estão alinhadas. As versões em português do Brasil e de Portugal têm guiões e vozes próprios. Os três vídeos originais do YouTube continuam disponíveis como referências.

| | Vídeos completos | Capítulos |
|---|---|---|
| English | [The Forest of Qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/en/the-forest-of-qubits.mp4) | [16](media/chapters/en/README.md) |
| Português (Brasil) | [A floresta dos qubits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt/a-floresta-dos-qubits.mp4) | [16](media/chapters/pt/README.md) |
| Español | [El bosque de los cúbits](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/es/el-bosque-de-los-cubits.mp4) | [16](media/chapters/es/README.md) |
| Português (Portugal) | [A floresta dos qubits — Portugal](https://raw.githubusercontent.com/SouBeatrizKaroline/qubit-stories/main/media/full/pt-PT/a-floresta-dos-qubits-pt-PT.mp4) | [16](media/chapters/pt-PT/README.md) |

Vê o capítulo correspondente, escreve uma previsão, executa o circuito e explica o resultado. Compara probabilidades ideais com contagens amostradas. Altera a fase relativa para 0°, 90° ou 180° e compara medições antes e depois de uma Hadamard final. Compara correlações de Bell nas bases Z e X e explora a recuperação de um erro X controlado. As previsões são temporárias e não recolhemos dados dos estudantes. Os benefícios educativos ainda não foram medidos num estudo com participantes.

## Executar no Qollab

1. Cria um projeto com **Upload your own files** e carrega `qollab-runtime.zip`. Mantém os ficheiros de execução na raiz; não carregues os vídeos MP4 para o Qollab.
2. Prime **Run** e escolhe um simulador gratuito. O Qollab fornece `backend`; o projeto não inclui credenciais de conta.
3. Escolhe a variante linguística, abre um capítulo correspondente e escreve uma previsão antes de revelar o resultado.
4. Ajusta a fase, o número de medições ou a entrada lógica e executa novamente. Os oito circuitos são compilados e enviados num único trabalho por execução, respeitando a restrição do IonQ no Qollab.

`index.html` e `main.js` selecionam a interface JS/Qiskit; o JavaScript chama Python através da ponte documentada `callPromising`. Esta interface precisa do ambiente Qollab. Para a alternativa apenas em Python, usa `main.py`, `quantum.py` e `requirements.txt`, sem `index.html` nem `main.js`; o Qollab chama `main()` automaticamente.

[Descarregar o pacote Qollab](qollab-runtime.zip)

## Executar localmente e verificar

É necessário Python 3.10+ e Qiskit 2.x. A execução local utiliza o `BasicSimulator` gratuito do Qiskit. Os três testes verificam fase/interferência, recuperação coerente de um erro X em cada posição e envio de um único trabalho com os totais de contagens. A execução no Qollab e no IonQ ainda não foi verificada.

```sh
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```

## Âmbito científico

- As personagens e a floresta são metáforas visuais; um qubit é um estado quântico, não uma esfera luminosa.
- As amplitudes e a fase relativa distinguem sobreposição de desconhecimento clássico. Cada medição dá um resultado; as distribuições exigem novas preparações.
- Correlações numa única base não provam entrelaçamento. A preparação de Bell e a comparação X/Z evidenciam coerência; não se trata de um teste de Bell sem lacunas. O entrelaçamento não permite mensagens mais rápidas do que a luz.
- O código de repetição de três qubits recupera um erro X introduzido. Não corrige ruído arbitrário, erros de fase ou dois erros de bit, nem demonstra tolerância a falhas. O qubit lógico recuperado é q0, o bit à direita nas cadeias do Qiskit; os restantes guardam informação da síndrome.
- As probabilidades ideais exatas diferem das contagens do simulador. Não alegamos execução em hardware real, vantagem quântica ou melhoria de aprendizagem medida.
- Os circuitos não modelam arrefecimento de supercondutores, lasers de iões aprisionados, simulação molecular ou sensores mencionados nas histórias.

## Acessibilidade

Os vídeos incluem narração sintética, legendas incorporadas e ficheiros ASS/SRT editáveis. Os guiões acompanham os materiais. O laboratório disponibiliza controlos por teclado, foco visível, campos identificados, tabelas textuais de resultados e avisos de estado. Ver os vídeos é opcional; não há efeitos intermitentes nem reprodução automática forçada. A interface tem rótulos em inglês e português; os vídeos e documentos abrangem as quatro variantes. Não alegamos uma auditoria WCAG concluída.

## Fontes, autoria e licença

A licença MIT abrange o software e a documentação. Os vídeos originais do YouTube pertencem aos respetivos titulares; ligações públicas não dão direito à redistribuição. A autoria, as datas e as ferramentas desses originais ainda não foram confirmadas. Os novos guiões, traduções, diagramas e produção foram preparados com assistência do Codex em 11 de outubro de 2026. As notas de produção identificam a geração da imagem e as vozes sintéticas. O texto original da licença MIT em inglês mantém-se como texto oficial; estas explicações não o substituem.

- [The World of Qubits — English](https://youtu.be/EAcDVqTb0lk)
- [O Mundo dos Qubits — pt-BR](https://youtu.be/nkQpc2YPSCA)
- [The Fellowship Of The Qubit — English](https://youtu.be/uPTSfysNvgw)

## Estado da entrega

A publicação dos materiais educativos no GitHub está concluída. Ainda faltam a importação no Qollab, as verificações nos simuladores gratuitos e IonQ, a publicação sob MIT e a submissão ao hackathon. Uma demonstração pública separada de 2–3 minutos deve mostrar o laboratório executável; os vídeos educativos longos não a substituem.

## Documentação

- [README](docs/pt-PT/README.md)
- [Project Card](docs/pt-PT/QOLLAB_PROJECT_CARD.md)
- [Guia de preenchimento](docs/pt-PT/QOLLAB_SETUP.md)
- [Lista de preparação](docs/pt-PT/SUBMISSION_CHECKLIST.md)
- [Origem e autoria](docs/pt-PT/PROVENANCE.md)
- [Notas de produção](docs/pt-PT/PRODUCTION_NOTES.md)
- [Entregáveis](docs/pt-PT/DELIVERABLES.md)

- [Qollab — hackathon](https://qollab.xyz/programs/hackathon/terms#submissions)
- [Qollab — Python/Qiskit](https://qollab.xyz/learn/docs/python-qiskit-projects)
- [Qollab — runtime](https://qollab.xyz/learn/docs/runtime-environment)
- [Qollab — project page](https://qollab.xyz/learn/docs/write-your-project-page)
- [IBM Quantum — repetition codes](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes)


---

[English](docs/en/README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [Português (Portugal)](docs/pt-PT/README.md) | [Español](docs/es/README.md)

This effort is supported by Qollab & IonQ
