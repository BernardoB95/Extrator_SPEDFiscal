# Extrator SPED Fiscal 
## Descrição
**Extrator de SPED Fiscal** é uma iniciativa de código aberto que nasceu perante a necessidade de quebra desta modalidade de arquivo e a dificuldade vivenciada pelas mais diversas áreas de negócios. O **objetivo principal** da ferramenta é trazer liberdade tecnológica e acessibilidade aos mais diversos públicos, focado nos não especializados em tecnologia, de forma simples e descomplicada. Assim, permitindo às áreas de tecnologia, focarem seus recursos para trabalhos de maior complexidade.


## Licença
Esse projeto conta com uma licença para codigo aberto do [MIT](https://choosealicense.com/licenses/mit/). Para maiores informações, ler o arquivo [LICENSE.md](https://github.com/BernardoB95/Extrator_SPEDFiscal/blob/main/README.md) ou acessar o link.

## Instalação
Para desenvolvedores, se tem git instalado no computador, inserir o seguinte comando no git bash ou shell da sua preferência:
```
cd diretorio/de/preferência
git clone https://github.com/BernardoB95/Extrator_SPEDFiscal.git
```

Se não tiver git instalado, é possivel baixar o programa em um arquivo zip. Clicar em "Code > Download as ZIP" no canto direito da página. Após isso, extrair no diretorio de preferência.

Dentro da pasta, tem um arquivo executável (main.exe), clicar com botão direito e criar um atalho. Finalmente, mover o atalho para a área de trabalho.


## Uso
A ferramenta ainda não conta com uma interface gráfica (GUI), motivo pelo qual devemos rodar ela por linha de comando. Para realizar isso, devemos seguir as seguintes instruções:
1. Abrir o File Explorer e ir na pasta do executável (main.exe) ou do atalho criado.
2. Na barra superior de busca, digitar "cmd" e clicar Enter.
3. Uma janela de linha de comando vai abrir no diretorio, alí deve digitar: `start main.exe <opções>`
4. Esperar o programa terminar de rodar.

#### Opções
| Flag | <div style="width:300px">Extended Flag</div> | Description |
| :----: | :------: | --------------------- |
| -h     | --help       | show this help message and exit |
| -i     | --input_dir  | Specify the directory where SPEDs are located between quotation marks (""). Default value is in "Extrator SPED Fiscal/data". |
| -o     | --output_dir | Specify the directory where the excel files will be saved between quotation marks (""). Default value is in "Extrator SPED Fiscal/data". |
| -v     | --verbose    | Specify verbosity of the process. Default value is False. |
| -r     | --regs       | Specify the Regs to be exported separated by spaces, as in the following example: 0001 0150 0200 C100 C190. Default value will consider all regs identified per file. |

#### Exemplos
Varias combinações de opções são possíveis.
Para mostrar informações do processamento:<br>
`start main.exe -v`

Para processar registros específicos:<br>
`start main.exe -r 0000 0150 0200 C100 C170 C190`

Para especificar o diretorio de leitura  dos arquivos:<br>
`start main.exe -i diretorio/dos/arquivos`

Para especificar o diretorio de escritura dos arquivos:<br>
`start main.exe -o diretorio/dos/arquivos`

Para especificar o diretorio de leitura e escritura dos arquivos:<br>
`start main.exe -i diretorio/de/leitura  -o diretorio/de/escritura`

Depois de rodar a ferramenta, o procesamento dos arquivos estará na pasta indicada pelo usuario (**Obs**: Caso não seja especificado, o resultado do processamento será encontrado na pasta diretorio/de/preferência/Extrator_SPEDFiscal/data). Um arquivo de log sera criado como parte do output, indicando a existencia de algum erro ou aviso.

## TO DO
- [ ] Desenvolver lógica de atrelhar os REGs.
- [ ] Desenvolvimento de Interface Gráfica (GUI).

## Problemas / Issues
Para reportar os erros a serem corrigidos em proximos *releases*, é necessario seguir os seguintes passos:
- Conferir os problemas reportados anteriormente, para evitar duplicação.
- Usar o log ou o erro para descrever detalhadamente.
- Se necesario, tirar print e anexar.
- Enviar o *report*.


## Colaborações & Pull Requests
Para realizar colaborações, por favor, seguir a seguinte convenção:
 - Clonar a branch **stable**.
 - Instalar as dependencias do arquivo ***requirements.txt*.
 - Escolher **um único** item para trabalhar por vez.
 - Realizar o **Pull Request** para a branch **stable**
   - Para correções de *bugs* existentes, nomear "Issue - \<Nome do PR\>" e referenciar o id do *issue*.
   - Para melhorias no codigo, nomear "Feature - \<Nome do PR\>".
 - Mandar o PR para revisão.

## Para Desenvolvedores

### Estrutura das pastas

