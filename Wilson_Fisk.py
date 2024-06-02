import os
import subprocess
import time
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_chkdsk():
    subprocess.run(["chkdsk", "/r", "/f"], shell=True)
def run_dism():
    print("Verificando e reparando a imagem do Windows...")
    subprocess.run(["dism","/Online", "/Cleanup-image", "/RestoreHealth"], shell=True)
def run_sfc():
    print("verificando a integridade dos arquivos de sistema...")
    subprocess.run(["sfc/scannow"], shell=True)
    
def restart_computer():
    print("O computador será reiniciado para localizar setores defeituosos e corrigir erros do disco...")
    time.sleep(10)
    os.system("shutdown /r /t 0")

if __name__ == "__main__":
    
    if is_admin():
        run_chkdsk()
        run_dism()
        run_sfc()
        restart_computer()
    else:
        
        print("Solicitando privilégios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
