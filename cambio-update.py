import yfinance as yf


def get_exchange_rate(base_currency, target_currency):
    ticker = f"{base_currency}{target_currency}=X"
    data = yf.download(tickers=ticker, period='1d')
    rate = data["Close"].iloc[-1]
    return rate


def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount


def main():
    print("Bem-vindo ao conversor de moedas!")
    print("Selecione as moedas de origem e destino para a conversão.")

    base_currency = input("Digite a moeda de origem (ex: BRL): ")
    target_currency = input("Digite a moeda de destino (ex: USD): ")

    try:
        exchange_rate = get_exchange_rate(base_currency, target_currency)

        print(
            f"\nTaxa de câmbio atual: 1 {base_currency} = {exchange_rate} {target_currency}\n")

        option = input(
            "Selecione a opção:\n1. Converter de moeda de origem para moeda de destino.\n2. Converter de moeda de destino para moeda de origem.\nOpção: ")

        if option == "1":
            amount = float(input(f"Digite o valor em {base_currency}: "))
            converted_amount = convert_currency(amount, exchange_rate)
            print(
                f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        elif option == "2":
            amount = float(input(f"Digite o valor em {target_currency}: "))
            converted_amount = convert_currency(amount, 1/exchange_rate)
            print(
                f"{amount} {target_currency} = {converted_amount:.2f} {base_currency}")
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

    except Exception as e:
        print(f"Ocorreu um erro ao obter a taxa de câmbio: {str(e)}")


if __name__ == "__main__":
    main()
