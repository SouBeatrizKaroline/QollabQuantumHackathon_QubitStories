# A floresta dos qubits — produção e versões

Vídeo educativo ilustrado em 16 capítulos. As versões em português brasileiro, inglês americano e espanhol latino-americano preservam a sequência, os conceitos, os personagens e a duração de aproximadamente 9min30s. Cada capítulo também é entregue como um MP4 independente, com narração e legendas incorporadas.

## Conteúdo e forma

A referência fornecida foi um vídeo local de 30 segundos com uma menina, um mascote luminoso e uma floresta noturna. A nova ilustração foi criada para este projeto. A montagem utiliza essa ilustração com movimentos de câmera, cartões explicativos, diagramas e legendas. A voz é sintética. Não há diálogos com sincronização labial.

A explicação diferencia superposição de desconhecimento clássico, distingue probabilidades de amplitudes e fase, explica repetição da preparação antes das medições e evita associar emaranhamento a comunicação mais rápida que a luz. A correção de erros é apresentada como um exemplo limitado para um único erro X; não há alegação de tolerância a falhas, vantagem computacional ou execução em hardware real.

## Ferramentas e autoria assistida

- Roteiro, tradução, diagramas e montagem preparados com assistência do Codex em 11 de outubro de 2026.
- Ilustração gerada com a ferramenta integrada `image_gen`, usando a habilidade imagegen. O prompt completo está abaixo.
- Narração sintética: pt-BR-FranciscaNeural, en-US-AriaNeural e es-MX-DaliaNeural.
- Renderização: 1280 × 720, 24 quadros por segundo, H.264 e AAC.
- Legendas derivadas dos tempos de palavra retornados pelo serviço de voz, além de arquivos separados para edição.
- Os tempos dos capítulos são alinhados entre idiomas; a velocidade de cada narração foi ajustada para manter as mesmas transições.

## Prompt da ilustração — ferramenta integrada

Use case: illustration-story. Asset type: cinematic illustrated educational video background. Create a polished wide 16:9 landscape illustration, highest practical resolution. A whimsical bioluminescent forest at night, glowing violet mushrooms, teal trees, fireflies, an old stone path that leads to a tiny observatory under stars. On the far RIGHT third stand a curious young girl with medium brown skin, curly dark hair in two puffs, yellow T-shirt, denim overalls, pink shoes and a small green backpack; beside her floats a friendly round pale cyan luminous mascot with expressive eyes and tiny arms. Original stylized 3D children's animation aesthetic, coherent anatomy, soft cinematic lighting, expressive but calm, charming, detailed. Left half should have dark calm uncluttered space and atmosphere for explanatory diagrams placed later in editing. No typography, no logos, no symbols, no visible writing, no mathematical graphics. Do not depict magic as literal science. One continuous environment, no collage or panels. Keep girl and mascot entirely inside frame with space above and below.

## Relação com o repositório

[Qubit Stories no GitHub](https://github.com/SouBeatrizKaroline/qubit-stories) contém o laboratório Qiskit e os três vídeos originais fornecidos. Esta nova série longa está publicada no GitHub, com três vídeos completos e 48 capítulos individuais. Os vídeos novos não foram publicados no YouTube e o projeto ainda não foi submetido ao Qollab.

## Referências e verificação

- [Regras do Qollab](https://qollab.xyz/programs/hackathon/terms#submissions).
- [Ambiente de execução Qollab](https://qollab.xyz/learn/docs/runtime-environment).
- [IBM Quantum — códigos de repetição](https://quantum.cloud.ibm.com/learning/en/courses/foundations-of-quantum-error-correction/correcting-quantum-errors/repetition-codes).
- Circuitos testados localmente com Qiskit, incluindo recuperação coerente para diferentes estados e cada posição de um erro X.

O vídeo longo não substitui a demonstração pública de 2 a 3 minutos exigida para apresentar o projeto executável no hackathon.
