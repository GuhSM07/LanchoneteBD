from Model.Funcionario import Funcionario
from Controller.FuncionarioController import inserir_funcionario, listar_funcionarios

# 🔥 Criando um funcionário de teste
funcionario_teste = Funcionario(
    nome="Maria Silva",
    celular="11988887777",
    rg="123456789",
    cargo="Atendente"
)

# ✅ Inserindo o funcionário no banco
inserir_funcionario(funcionario_teste)
print("Funcionário inserido com sucesso!")

# 🔍 Listando todos os funcionários cadastrados
funcionarios = listar_funcionarios()

print("\n--- Lista de Funcionários ---")
for func in funcionarios:
    print(f"ID: {func[0]}, Nome: {func[1]}, Celular: {func[2]}, RG: {func[3]}, Cargo: {func[4]}")

