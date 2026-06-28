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

def exibir_codigo_funcao(func, titulo="Código-Fonte da Função"):
    """Exibe o código-fonte de uma função no Streamlit usando st.code."""
    import inspect
    if func is None:
        st.warning(f"⚠️ {titulo}: Função não importada ou indisponível.")
        return
    try:
        source_code = inspect.getsource(func)
        with st.expander(f"💻 Visualizar Código: `{titulo}`", expanded=False):
            st.code(source_code, language='python')
    except Exception as e:
        st.warning(f"Não foi possível ler o código-fonte de `{titulo}`: {e}")
