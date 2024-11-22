from solana.keypair import Keypair
from mnemonic import Mnemonic
from base58 import b58encode


def generate_solana_wallet():
    # Generate a 12-word seed phrase
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)

    # Generate Keypair from seed
    seed = mnemo.to_seed(seed_phrase)
    keypair = Keypair.from_seed(seed[:32])  # Use first 32 bytes as seed for keypair

    private_key = keypair.secret_key
    private_key = b58encode(private_key).decode('utf-8')
    public_key = keypair.public_key

    return seed_phrase, private_key, str(public_key)


def main():
    num_wallets = int(input("Enter the number of wallets to generate: "))
    output_file = "solana_wallets.txt"

    with open(output_file, "w") as f:
        for i in range(num_wallets):
            seed, private_key, address = generate_solana_wallet()
            # f.write(f"{seed}:{private_key}:{address}\n")
            f.write(f"{private_key}\n")
            print(f"Wallet {i + 1} - Seed: {seed}, Private Key: {private_key}, Address: {address}")

    print(f"\nGenerated {num_wallets} wallets and saved to {output_file}")


if __name__ == "__main__":
    main()
