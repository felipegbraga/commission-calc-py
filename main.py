from datetime import datetime, timedelta

class SalesCommissionManager:
    """
    Sistema para gestão de comissões de vendas.
    Calcula a distribuição de lucros entre Felipe e Eduardo para o período de 09/03 a 27/03.
    """
    
    def __init__(self, start_date: str, end_date: str, rate: float = 0.02):
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y")
        self.end_date = datetime.strptime(end_date, "%d.%m.%Y")
        self.rate = rate
        self.total_revenue = 0.0

    def is_sunday(self, date_obj: datetime) -> bool:
        """Verifica se o dia é domingo (6 no Python)."""
        return date_obj.weekday() == 6

    def record_daily_sales(self):
        """Loop de entrada de dados ignorando os domingos."""
        current_date = self.start_date
        
        print(f"--- 📈 Commission Manager: {self.start_date.strftime('%d/%m')} to {self.end_date.strftime('%d/%m')} ---")
        print("Instrução: Digite os valores separados por espaço (ex: 150.50 200 30) e aperte Enter.\n")

        while current_date <= self.end_date:
            if self.is_sunday(current_date):
                current_date += timedelta(days=1)
                continue
            
            date_label = current_date.strftime('%d/%m (%A)')
            user_input = input(f"Vendas de {date_label}: ")
            
            try:
                # Converte strings em floats e soma
                daily_values = [float(val) for val in user_input.split()]
                daily_sum = sum(daily_values)
                self.total_revenue += daily_sum
                print(f"   ✅ Soma do dia: R$ {daily_sum:.2f}")
            except ValueError:
                print("   ⚠️ Erro: Use apenas números e ponto decimal. Tente novamente este dia.")
                continue
            
            current_date += timedelta(days=1)

    def display_final_report(self):
        """Calcula e exibe a divisão final das comissões."""
        total_commission = self.total_revenue * self.rate
        split_value = total_commission / 2

        print("\n" + "="*45)
        print("          FECHAMENTO DE COMISSÕES            ")
        print("="*45)
        print(f"Faturamento Total:     R$ {self.total_revenue:,.2f}")
        print(f"Comissão Total ({self.rate*100}%):  R$ {total_commission:,.2f}")
        print("-" * 45)
        print(f"Parte do EDUARDO:      R$ {split_value:,.2f}")
        print(f"Parte do FELIPE:       R$ {split_value:,.2f}")
        print("="*45)

if __name__ == "__main__":
    # Configuração do período conforme solicitado (09/03 a 27/03)
    # Nota: O ano foi definido como 2026 conforme o contexto atual.
    manager = SalesCommissionManager(start_date="09.03.2026", end_date="27.03.2026")
    manager.record_daily_sales()
    manager.display_final_report()