# Detecção e Análise de Padrões Comportamentais em Animais através de Visão Computacional

`PPC-CC: PUC Poços de Caldas - Ciência da Computação`
`Disciplina: Visão Computacional e Realidade Misturada`
`2024 - 2 Semestre `

## Integrantes

- Marcos Vinícius de Lima Silva
- Raphael Lanzoni Fracarolli

## Professor

- M. Sc. Will Machado

# Descrição Geral

Este projeto propõe o desenvolvimento e aplicação de técnicas de Visão Computacional para a análise automática de comportamentos e sentimentos de animais em diferentes ambientes, como clínicas veterinárias e dentro de casa. Utilizando algoritmos avançados de processamento de imagens e vídeos, o sistema será capaz de identificar e classificar padrões comportamentais de animais de forma autônoma e em tempo real. 

O projeto visa superar os desafios tradicionais de monitoramento manual, proporcionando aos proprietários dos animais uma ferramenta robusta e de fácil entendimento da etologia animal, incluindo a detecção de estados emocionais, análise comportamental e respostas a estímulos ambientais. Além disso, o sistema também poderá auxiliar na compreensão das preferências do pet, identificação de comportamentos atípicos, e na saúde e bem-estar animal. 

O uso da Visão Computacional para a análise comportamental de animais oferece uma abordagem inovadora e multidisciplinar, integrando áreas como inteligência artificial, etologia e veterinária. A plataforma resultante será uma contribuição importante para médicos veterinários, estudantes da área de biológicas e até mesmo donos e adestradores desses animais, permitindo um entendimento em tempo real e contínuo com impacto significativo na preservação da saúde dos animais. 

# Ferramentas Utilizadas

- Python
- Pandas
- Numpy
- Pillow
- OpenCV
- TensorFlow
- Keras
- Matplot
- Seaborn
- Sklearn

# Instalação

pip install Pillow numpy opencv-python tensorflow

# Execução

1. modelo.ipnyb : Treinamendo do modelo, rode o script e espere o final do treinamento, ao final irá gerar o arquivo pets_detection.keras
2. main.py : Inicialização da API 
3. gui.py : Rode o script para inicialização da interface gráfica integrada a API

# Funcionamento

- Faça o upload da imagem que deseja analisar
- O modelo irá retornar Happy, Sad ou Angry dependendo das caracteristicas do animal
- O modelo também irá informar a % de confiança da predição






