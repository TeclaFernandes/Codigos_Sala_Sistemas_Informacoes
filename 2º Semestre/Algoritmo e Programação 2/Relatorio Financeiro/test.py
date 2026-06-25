import sqlite3
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import Tk, Button, messagebox
import os

# Configuração do banco de dados
def criar_banco():
    conn = sqlite3.connect('financeiro.db')
    cursor = conn.cursor()
    
    # Criação da tabela de transações, se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            tipo TEXT,
            categoria TEXT,
            valor REAL
        )
    ''')
    
    # Criação da tabela de previsões de gasto, se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS previsoes (
            categoria TEXT PRIMARY KEY,
            valor_previsto REAL
        )
    ''')
    
    # Dados exemplo (remova se já tiver dados no banco)
    dados_exemplo = [
        ('2024-01-01', 'Receita', 'Salário', 5000),
        ('2024-01-05', 'Despesa', 'Alimentação', 150),
        ('2024-01-10', 'Despesa', 'Transporte', 75),
        ('2024-01-15', 'Despesa', 'Lazer', 200),
        ('2024-01-20', 'Receita', 'Freelance', 800),
        ('2024-01-25', 'Despesa', 'Educação', 300)
    ]
    cursor.executemany('''
        INSERT INTO transacoes (data, tipo, categoria, valor) VALUES (?, ?, ?, ?)
    ''', dados_exemplo)
    
    # Previsões de gastos para algumas categorias
    previsoes_exemplo = [
        ('Alimentação', 200),
        ('Transporte', 100),
        ('Lazer', 150),
        ('Educação', 250)
    ]
    cursor.executemany('''
        INSERT OR IGNORE INTO previsoes (categoria, valor_previsto) VALUES (?, ?)
    ''', previsoes_exemplo)
    
    conn.commit()
    conn.close()
    print("Banco de dados configurado com sucesso.")

# Função para gerar o gráfico de linha
def gerar_grafico():
    conn = sqlite3.connect('financeiro.db')
    cursor = conn.cursor()
    
    # Consultar gastos reais e previstos
    cursor.execute("SELECT categoria, SUM(valor) FROM transacoes WHERE tipo='Despesa' GROUP BY categoria")
    gastos_reais = cursor.fetchall()
    
    cursor.execute("SELECT categoria, valor_previsto FROM previsoes")
    previsoes = cursor.fetchall()
    
    categorias = [cat for cat, _ in gastos_reais]
    gastos = [gasto for _, gasto in gastos_reais]
    previsoes_gastos = [prev for cat, prev in previsoes if cat in categorias]
    
    conn.close()
    
    # Gerar gráfico de linha
    plt.figure(figsize=(10, 6))
    plt.plot(categorias, gastos, label="Gasto Real", marker='o', color='blue', linestyle='-', linewidth=2)
    plt.plot(categorias, previsoes_gastos, label="Previsão de Gasto", marker='x', color='red', linestyle='--', linewidth=2)
    
    plt.title("Comparação entre Gasto Real e Previsão de Gasto", fontsize=14)
    plt.xlabel("Categorias", fontsize=12)
    plt.ylabel("Valor (R$)", fontsize=12)
    plt.legend()
    
    # Salvar o gráfico em um arquivo temporário
    grafico_path = "grafico_temp.png"
    plt.savefig(grafico_path)
    plt.close()
    
    return grafico_path

# Função para gerar o relatório PDF com gráfico
def gerar_relatorio_pdf():
    conn = sqlite3.connect('financeiro.db')
    cursor = conn.cursor()
    
    # Consultar dados de transações e previsões
    cursor.execute("SELECT * FROM transacoes")
    transacoes = cursor.fetchall()
    
    cursor.execute("SELECT categoria, SUM(valor) FROM transacoes WHERE tipo='Despesa' GROUP BY categoria")
    gastos_reais = cursor.fetchall()
    
    cursor.execute("SELECT categoria, valor_previsto FROM previsoes")
    previsoes = cursor.fetchall()
    
    # Calcular receita e despesa total
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Receita'")
    receita_total = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Despesa'")
    despesa_total = cursor.fetchone()[0] or 0
    conn.close()
    
    # Gerar gráfico
    grafico_path = gerar_grafico()
    
    # Criar o arquivo PDF
    pdf = canvas.Canvas("relatorio_financeiro.pdf", pagesize=letter)
    pdf.drawString(100, 750, "Relatório Financeiro Pessoal")
    pdf.drawString(100, 730, "------------------------------")
    
    # Resumo financeiro
    pdf.drawString(100, 710, f"Receita Total: R${receita_total:.2f}")
    pdf.drawString(100, 690, f"Despesa Total: R${despesa_total:.2f}")
    pdf.drawString(100, 670, f"Saldo Final: R${receita_total - despesa_total:.2f}")
    
    # Tabela de análise de previsões de gastos
    y = 640
    pdf.drawString(100, y, "Análise de Gastos por Categoria")
    pdf.drawString(100, y-10, "Categoria      | Previsão | Gasto Real | Diferença")
    pdf.drawString(100, y-20, "----------------------------------------------")
    y -= 40
    
    # Processar e exibir as previsões e gastos reais
    for categoria, valor_previsto in previsoes:
        # Buscar o gasto real da categoria, se houver
        gasto_real = next((gasto for cat, gasto in gastos_reais if cat == categoria), 0)
        diferenca = valor_previsto - gasto_real
        pdf.drawString(100, y, f"{categoria:<12} | R${valor_previsto:.2f} | R${gasto_real:.2f} | R${diferenca:.2f}")
        y -= 20
        if y < 100:  # Evita ultrapassar o fim da página
            pdf.showPage()  # Cria uma nova página
            y = 750
    
    # Inserir gráfico no PDF
    pdf.drawImage(grafico_path, 100, 300, width=400, height=200)
    
    pdf.save()
    
    # Deletar o arquivo temporário do gráfico
    os.remove(grafico_path)
    
    messagebox.showinfo("Relatório", "Relatório PDF gerado com sucesso!")

# Função para o botão de download do relatório
def baixar_relatorio():
    gerar_relatorio_pdf()

# Interface gráfica com Tkinter
def criar_interface():
    janela = Tk()
    janela.title("Sistema Financeiro")

    # Botão para baixar o relatório
    botao = Button(janela, text="Baixar Relatório em PDF", command=baixar_relatorio)
    botao.pack(pady=20)

    janela.mainloop()

# Configura o banco de dados e abre a interface
if __name__ == "__main__":
    criar_banco()
    criar_interface()
