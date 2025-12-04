import tkinter as tk
from tkinter import messagebox

def calcular_orcamento():
    try:
        # Pega os valores digitados
        renda = float(entry_renda.get().replace(",", ".") or 0)
        aluguel = float(entry_aluguel.get().replace(",", ".") or 0)
        alimentacao = float(entry_alimentacao.get().replace(",", ".") or 0)
        transporte = float(entry_transporte.get().replace(",", ".") or 0)
        outros = float(entry_outros.get().replace(",", ".") or 0)

        # Soma despesas
        total_despesas = aluguel + alimentacao + transporte + outros

        # Verifica se a renda é válida
        if renda <= 0:
            messagebox.showwarning("Aviso", "Informe uma renda mensal maior que zero.")
            return

        # Calcula saldo e percentual de despesas
        saldo = renda - total_despesas
        percentual_despesas = (total_despesas / renda) * 100

        # Estrutura de decisão para classificação do orçamento
        if percentual_despesas <= 60:
            status = "Situação saudável ✅"
            cor = "green"
            dica = "Você está usando bem seu dinheiro. Continue assim!"
        elif percentual_despesas <= 80:
            status = "Situação de atenção ⚠️"
            cor = "orange"
            dica = "Tente reduzir alguns gastos para evitar aperto no final do mês."
        else:
            status = "Situação crítica ⛔️"
            cor = "red"
            dica = "Suas despesas estão muito altas. Reveja seu orçamento urgentemente."

        # Atualiza os rótulos de resultado
        label_result_total.config(text=f"Total de despesas: R$ {total_despesas:.2f}")
        label_result_saldo.config(text=f"Saldo no fim do mês: R$ {saldo:.2f}")
        label_result_status.config(text=status, fg=cor)
        label_result_dica.config(text=dica)

    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos apenas com números.")


# Janela principal
root = tk.Tk()
root.title("Calculadora de Orçamento Mensal")
root.geometry("420x420")
root.resizable(False, False)

# Frame principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Título
label_titulo = tk.Label(frame, text="Calculadora de Orçamento Mensal", font=("Arial", 14, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Campo de renda
label_renda = tk.Label(frame, text="Renda mensal (R$):")
label_renda.grid(row=1, column=0, sticky="w")
entry_renda = tk.Entry(frame)
entry_renda.grid(row=1, column=1, pady=2, sticky="we")

# Campos de despesas
label_aluguel = tk.Label(frame, text="Aluguel / Financiamento (R$):")
label_aluguel.grid(row=2, column=0, sticky="w")
entry_aluguel = tk.Entry(frame)
entry_aluguel.grid(row=2, column=1, pady=2, sticky="we")

label_alimentacao = tk.Label(frame, text="Alimentação (R$):")
label_alimentacao.grid(row=3, column=0, sticky="w")
entry_alimentacao = tk.Entry(frame)
entry_alimentacao.grid(row=3, column=1, pady=2, sticky="we")

label_transporte = tk.Label(frame, text="Transporte (R$):")
label_transporte.grid(row=4, column=0, sticky="w")
entry_transporte = tk.Entry(frame)
entry_transporte.grid(row=4, column=1, pady=2, sticky="we")

label_outros = tk.Label(frame, text="Outras despesas (R$):")
label_outros.grid(row=5, column=0, sticky="w")
entry_outros = tk.Entry(frame)
entry_outros.grid(row=5, column=1, pady=2, sticky="we")

# Botão calcular
btn_calcular = tk.Button(frame, text="Calcular orçamento", command=calcular_orcamento)
btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

# Separador
separator = tk.Label(frame, text="Resultados", font=("Arial", 12, "bold"))
separator.grid(row=7, column=0, columnspan=2, pady=(10, 5))
# Resultados
label_result_total = tk.Label(frame, text="Total de despesas: R$ 0.00", font=("Arial", 10))
label_result_total.grid(row=8, column=0, columnspan=2, sticky="w")

label_result_saldo = tk.Label(frame, text="Saldo no fim do mês: R$ 0.00", font=("Arial", 10))
label_result_saldo.grid(row=9, column=0, columnspan=2, sticky="w")


label_result_status = tk.Label(frame, text="", font=("Arial", 11, "bold"))
label_result_status.grid(row=10, column=0, columnspan=2, pady=(5, 0))

label_result_dica = tk.Label(frame, text="", font=("Arial", 9), wraplength=380, justify="left")
label_result_dica.grid(row=11, column=0, columnspan=2, pady=(5, 0))

# Ajuste de colunas
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Inicia a interface
root.mainloop()