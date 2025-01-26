from eth_account import Account


def generate_wallets(count=1, output_file="evm_wallets.txt"):
    """
    Generate EVM-compatible wallets and save them to a file in Address:Private Key format.

    Args:
        count (int): Number of wallets to generate.
        output_file (str): Path to the output file.
    """
    with open(output_file, "w") as file:
        for _ in range(count):
            account = Account.create()
            address = account.address
            private_key = account.key.hex()
            file.write(f"{address}:{private_key}\n")
    print(f"{count} wallet(s) generated and saved to {output_file}.")


if __name__ == "__main__":
    # Configure the number of wallets to generate
    num_wallets = int(input("Enter the number of wallets to generate: "))
    output_file_name = input("Enter the output file name (default: evm_wallets.txt): ").strip() or "evm_wallets.txt"

    generate_wallets(count=num_wallets, output_file=output_file_name)
