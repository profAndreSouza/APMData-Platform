import streamlit as st
import os

def testar_funcao(func, *args, **kwargs):
    """
    Retorna True se a função executa sem NotImplementedError, 
    'NotImplemented' caso contrário, ou 'RuntimeError' para outros erros.
    """
    if func is None:
        return "NotImplemented"
    try:
        func(*args, **kwargs)
        return True
    except NotImplementedError:
        return "NotImplemented"
    except Exception:
        return "RuntimeError"

def obter_readme_markdown() -> str:
    """Carrega dinamicamente o arquivo README.md da raiz do projeto."""
    caminho_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_readme = os.path.join(caminho_dir, "../../README.md")
    
    if not os.path.exists(caminho_readme):
        caminho_readme = "README.md"
        
    if os.path.exists(caminho_readme):
        try:
            with open(caminho_readme, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Não foi possível ler o arquivo README.md: {e}"
    return ""
