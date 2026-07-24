from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Script(BaseModel):
    id: int
    name: str
    description: str
    type: str
    category: str
    rating: float
    code: str
    usage: str
    requirements: List[str]
    downloads: int
    updated: str

scripts_db = [
    Script(
        id=1,
        name="Get User Mailbox Size",
        type="PowerShell",
        category="Exchange",
        description="Script para obter o tamanho total da caixa de correio de um usuário no Exchange Online",
        rating=4.8,
        code="# Get Mailbox Size\nConnect-ExchangeOnline\n\n$mailbox = Get-Mailbox -Identity \"usuario@empresa.com\"\n$stats = Get-MailboxStatistics -Identity $mailbox.DistinguishedName\n\nWrite-Host \"Mailbox: $($mailbox.PrimarySmtpAddress)\"\nWrite-Host \"Size: $($stats.TotalItemSize)\"\nWrite-Host \"Item Count: $($stats.ItemCount)\"\nWrite-Host \"Last Logon: $($stats.LastLogonTime)\"",
        usage="1. Certifique-se de ter permissões de administrador do Exchange\n2. Conecte-se ao Exchange Online\n3. Substitua \"usuario@empresa.com\" pelo email do usuário\n4. Execute o script no PowerShell ISE ou Terminal\n5. O resultado será exibido no console",
        requirements=["PowerShell 5.1 ou superior", "Módulo ExchangeOnlineManagement", "Permissões de administrador do Exchange"],
        downloads=1250,
        updated="2024-07-24"
    ),
]

@router.get("/")
async def list_scripts(category: str = None, search: str = None):
    """Lista todos os scripts com filtros opcionais"""
    result = scripts_db
    
    if category:
        result = [s for s in result if s.category.lower() == category.lower()]
    
    if search:
        search_lower = search.lower()
        result = [s for s in result if search_lower in s.name.lower() or search_lower in s.description.lower()]
    
    return result

@router.get("/{script_id}")
async def get_script(script_id: int):
    """Obtém detalhes de um script específico"""
    for script in scripts_db:
        if script.id == script_id:
            return script
    return {"error": "Script não encontrado"}

@router.post("/")
async def create_script(script: Script):
    """Cria um novo script"""
    script.id = max([s.id for s in scripts_db]) + 1 if scripts_db else 1
    scripts_db.append(script)
    return script
