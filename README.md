# Script de Manutenção do Sistema
>Este script automatiza tarefas de manutenção do sistema em um computador Windows, garantindo a integridade e a saúde dos arquivos e do disco do sistema.
Ele utiliza três utilitários poderosos do Windows: sfc, dism e chkdsk.

## Funcionalidades
+ Check Disk (chkdsk): Escaneia e repara erros no disco.
+ Deployment Imaging Service and Management Tool (DISM): Verifica e repara a imagem do Windows.
+ System File Checker (sfc): Escaneia e restaura arquivos de sistema corrompidos.

## Uso
### Pré-requisitos
+ Certifique-se de que você tenha o Python instalado em seu sistema.
+ O script deve ser executado com privilégios de administrador para realizar as tarefas de manutenção.

## Executando o Script

+ Clone o repositório:
  
````
 https://github.com/gregorygustavo80/Wilson_Fisk.git
````
+ Navegue até o diretório do script:

````
cd Wilson_Fisk.py
````
+ Execute o script:

````
python Wilson_Fisk.py
````
Se você não tiver privilégios de administrador, o script solicitará que você o execute como administrador.

# Visão Geral dos Comandos

## 1. Verificador de Arquivos de Sistema (sfc)

#### O comando sfc verifica a integridade de todos os arquivos de sistema protegidos e substitui versões incorretas por versões corretas da Microsoft.

+ Comando Usado: sfc /scannow
+ Função no Script:

````
def run_sfc():
  print("Verificando a integridade dos arquivos de sistema...")
  subprocess.run(["sfc", "/scannow"], shell=True)
````
+ Propósito: Garante que quaisquer arquivos de sistema corrompidos ou modificados sejam restaurados ao seu estado original.

## 2. Ferramenta de Gerenciamento e Manutenção de Imagens de Implantação (DISM)

#### O comando dism é usado para gerenciar e preparar imagens do Windows, incluindo aquelas usadas para Windows PE, Ambiente de Recuperação do Windows (WinRE) e Configuração do Windows. A opção /RestoreHealth escaneia a imagem do Windows em busca de corrupção e a repara automaticamente.

+ Comando Usado: dism /Online /Cleanup-image /RestoreHealth
+ Função no Script:

````
def run_dism():
  print("Verificando e reparando a imagem do Windows...")
  subprocess.run(["dism", "/Online", "/Cleanup-image", "/RestoreHealth"], shell=True)
````

+ Propósito: Repara a imagem do Windows para garantir a estabilidade e o desempenho do sistema.

## 3. Verificação de Disco (chkdsk)

#### O comando chkdsk verifica a integridade do sistema de arquivos de um volume e corrige erros lógicos do sistema de arquivos. A opção /r localiza setores defeituosos e recupera informações legíveis, e a opção /f corrige erros no disco.

+ Comando Usado: chkdsk /r /f
+ Função no Script:

````
  def run_chkdsk():
    subprocess.run(["chkdsk", "/r", "/f"], shell=True)
````

+ Propósito: Garante que erros no disco sejam identificados e corrigidos, prevenindo possíveis problemas futuros.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.











