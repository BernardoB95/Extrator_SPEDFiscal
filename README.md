# Extrator SPED Fiscal 
## Descrição
**Extrator de SPED Fiscal** é uma iniciativa de código aberto que nasceu perante a necessidade de quebra desta modalidade de arquivo e a dificuldade vivenciada pelas mais diversas áreas de negócios. O **objetivo principal** da ferramenta é trazer liberdade tecnológica e acessibilidade aos mais diversos públicos, focado nos não especializados em tecnologia, de forma simples e descomplicada. Assim, permitindo às áreas de tecnologia, focarem seus recursos para trabalhos de maior complexidade.

## Instalação
TO BE FILLED

## Opções
| Flag | Extended Flag | Description |
| :----: | :------: | ----------- |
| -h | --help | show this help message and exit |
| -i | --input_dir | Specify the directory where SPEDs are located between quotation marks (""). Default value is in "Extrator SPED Fiscal/data". |
| -o | --output_dir &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Specify the directory where the excel files will be saved between quotation marks (""). Default value is in "Extrator SPED Fiscal/data". |
| -v | --verbose | Specify verbosity of the process. Default value is False. |
| -r | --regs | Specify the Regs to be exported separated by spaces, as in the following example: 0001 0150 0200 C100 C190. Default value will consider all regs identified per file. |

```
 -h   --help          show this help message and exit 
 -i   --input_dir     Specify the directory where SPEDs are located between quotation marks (""). 
                      Default value is in "Extrator SPED Fiscal/data". 
 -o   --output_dir    Specify the directory where the excel files will be saved between quotation marks (""). 
                      Default value is in "Extrator SPED Fiscal/data". 
 -v   --verbose       Specify verbosity of the process. Default value is False. 
 -r   --regs          Specify the Regs to be exported separated by spaces, as in the following example: 
                      0001 0150 0200 C100 C190. Default value will consider all regs identified per file. 
```

## Uso
After installing show how to open command line and add flags

Depois de rodar a ferramenta, o procesamento dos arquivos estará na pasta indicada pelo usuario (**Obs**: Caso não seja especificado, o resultado do processamento será encontrado na pasta XXXX\YYYY\ZZZZ.xlsx). Um arquivo de log sera criado como parte do output, indicando a existencia de algum erro ou aviso.

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
 - Escolher **um único** item para trabalhar por vez.
 - Realizar o **Pull Request** para a branch **stable**
   - Para correções de *bugs* existentes, nomear "Issue - \<Nome do PR\>" e referenciar o id do *issue*.
   - Para melhorias no codigo, nomear "Feature - \<Nome do PR\>".
 - Mandar o PR para revisão.
