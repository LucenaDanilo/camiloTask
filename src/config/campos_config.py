"""
Configuração centralizada dos campos do dashboard
"""
from typing import Dict, Any
from zoneinfo import ZoneInfo
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Timezone padrão
TIMEZONE = ZoneInfo(os.getenv('TZ', "America/Sao_Paulo"))

# Configuração do Google Sheets
GOOGLE_SHEETS_CONFIG = {
    "credentials_path": os.getenv('GOOGLE_CREDENTIALS_PATH', 'credentials.json'),
    "sheet_url": os.getenv('SHEET_URL'),
    "scopes": [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
    "default_range": os.getenv('GOOGLE_SHEETS_RANGE', "Sheet1!A1:Z1000"),
    "update_interval": int(os.getenv('UPDATE_INTERVAL', '300')),  # 5 minutos
    "timezone": TIMEZONE,
    "date_format": os.getenv('DATE_FORMAT', "%d/%m/%Y %H:%M:%S"),
    "default_start_time": os.getenv('DEFAULT_START_TIME', "00:00:00"),
    "default_end_time": os.getenv('DEFAULT_END_TIME', "23:59:59.999999")
}

# Mapeamento de nomes das colunas da planilha (dadoX) para nomes internos
MAPEAMENTO_COLUNAS = {
    'dado1': 'identificador',        
    'dado2': 'funcionario',          
    'dado3': 'cliente',              
    'dado4': 'solicitante',          
    'dado5': 'data_hora',            
    'dado6': 'relato_detalhado_1',   
    'dado7': 'relato_detalhado_2',   
    'dado8': 'descricao_atendimento',
    'dado9': 'status_atendimento'    
}

# Valores default para campos vazios
VALORES_DEFAULT = {
    'identificador': os.getenv('DEFAULT_IDENTIFICADOR', '0'),
    'funcionario': os.getenv('DEFAULT_FUNCIONARIO', 'Não informado'),
    'cliente': os.getenv('DEFAULT_CLIENTE', 'Não informado'),
    'solicitante': os.getenv('DEFAULT_SOLICITANTE', 'Não informado'),
    'data_hora': os.getenv('DEFAULT_DATETIME', '1899-12-30 00:00:00'),
    'relato_detalhado_1': '',
    'relato_detalhado_2': '',
    'descricao_atendimento': os.getenv('DEFAULT_DESCRICAO', 'Sem descrição'),
    'status_atendimento': os.getenv('DEFAULT_STATUS', 'Pendente')
}

# Configuração detalhada de cada campo
CAMPOS_CONFIGURACAO = {
    "dado1": {
        "nome_interno": "identificador",
        "tipo": "int",
        "obrigatorio": True,
        "valor_default": VALORES_DEFAULT['identificador'],
        "permite_filtro": True,
        "tipo_filtro": "number",
        "label": "ID",
        "visivel": True
    },
    "dado2": {
        "nome_interno": "funcionario",
        "tipo": "string",
        "obrigatorio": True,
        "valor_default": VALORES_DEFAULT['funcionario'],
        "permite_filtro": True,
        "tipo_filtro": "select",
        "label": "Funcionário",
        "visivel": True
    },
    "dado3": {
        "nome_interno": "cliente",
        "tipo": "string",
        "obrigatorio": True,
        "valor_default": VALORES_DEFAULT['cliente'],
        "permite_filtro": True,
        "tipo_filtro": "select",
        "label": "Cliente",
        "visivel": True
    },
    "dado4": {
        "nome_interno": "solicitante",
        "tipo": "string",
        "obrigatorio": False,
        "valor_default": VALORES_DEFAULT['solicitante'],
        "permite_filtro": True,
        "tipo_filtro": "select",
        "label": "Solicitante",
        "visivel": True
    },
    "dado5": {
        "nome_interno": "data_hora",
        "tipo": "datetime",
        "obrigatorio": True,
        "formato": GOOGLE_SHEETS_CONFIG['date_format'],
        "valor_default": VALORES_DEFAULT['data_hora'],
        "permite_filtro": True,
        "tipo_filtro": "date",
        "label": "Data/Hora",
        "visivel": True
    },
    "dado6": {
        "nome_interno": "relato_detalhado_1",
        "tipo": "string",
        "obrigatorio": False,
        "valor_default": VALORES_DEFAULT['relato_detalhado_1'],
        "permite_filtro": False,
        "visivel": False
    },
    "dado7": {
        "nome_interno": "relato_detalhado_2",
        "tipo": "string",
        "obrigatorio": False,
        "valor_default": VALORES_DEFAULT['relato_detalhado_2'],
        "permite_filtro": False,
        "visivel": False
    },
    "dado8": {
        "nome_interno": "descricao_atendimento",
        "tipo": "string",
        "obrigatorio": False,
        "valor_default": VALORES_DEFAULT['descricao_atendimento'],
        "permite_filtro": False,
        "label": "Descrição",
        "visivel": True
    },
    "dado9": {
        "nome_interno": "status_atendimento",
        "tipo": "string",
        "obrigatorio": True,
        "valor_default": VALORES_DEFAULT['status_atendimento'],
        "valores_permitidos": os.getenv('STATUS_PERMITIDOS', "OPEN,CLOSED").split(','),
        "permite_filtro": True,
        "tipo_filtro": "select",
        "label": "Status",
        "visivel": True
    }
}

def get_mapeamento_colunas() -> Dict[str, str]:
    """Retorna o mapeamento de colunas da planilha para nomes internos."""
    return MAPEAMENTO_COLUNAS

def get_valores_default() -> Dict[str, Any]:
    """Retorna os valores default para cada campo."""
    return VALORES_DEFAULT

def get_campos_visiveis() -> Dict[str, Dict[str, Any]]:
    """Retorna apenas os campos configurados como visíveis."""
    return {
        nome: config for nome, config in CAMPOS_CONFIGURACAO.items()
        if config.get('visivel', False)
    }

def get_campos_filtraveis() -> Dict[str, Dict[str, Any]]:
    """Retorna apenas os campos que permitem filtro."""
    return {
        nome: config for nome, config in CAMPOS_CONFIGURACAO.items()
        if config.get('permite_filtro', False)
    }

def validar_cabecalho(cabecalho: list) -> bool:
    """Valida se o cabeçalho da planilha corresponde à configuração."""
    campos_obrigatorios = {
        nome for nome, config in CAMPOS_CONFIGURACAO.items()
        if config.get('obrigatorio', False)
    }
    campos_planilha = set(cabecalho)
    return campos_obrigatorios.issubset(campos_planilha)
