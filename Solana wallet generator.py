from solders.keypair import Keypair
from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from base58 import b58encode


def generate_solana_wallet():
    # Generate a 12-word seed phrase
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)

    # Derive Solana keypair using BIP44 (m/44'/501'/0'/0/0)
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
    bip44_ctx = (Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
                 .Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0))

    private_key_bytes = bip44_ctx.PrivateKey().Raw().ToBytes()
    keypair = Keypair.from_seed(private_key_bytes)

    # Encode private key as base58 (64 bytes secret key)
    private_key_b58 = b58encode(bytes(keypair)).decode("utf-8")
    address = str(keypair.pubkey())

    return seed_phrase, private_key_b58, address


def menu():
    print("\nChoose output format(s):")
    print("1 - Address only")
    print("2 - Private key (base58) only")
    print("3 - Seed phrase only")
    print("4 - Address + Private key (base58)")
    print("5 - Address + Seed phrase")
    print("6 - Private key (base58) + Seed phrase")
    print("7 - Address + Private key (base58) + Seed phrase")

    while True:
        choice = input("Enter choice (1-7): ").strip()
        if choice in [str(i) for i in range(1, 8)]:
            return int(choice)
        else:
            print("Invalid choice, try again.")


def format_output(choice, seed, private_key, address):
    if choice == 1:
        return f"{address}"
    elif choice == 2:
        return f"{private_key}"
    elif choice == 3:
        return f"{seed}"
    elif choice == 4:
        return f"{address}:{private_key}"
    elif choice == 5:
        return f"{address}:{seed}"
    elif choice == 6:
        return f"{private_key}:{seed}"
    elif choice == 7:
        return f"{address}:{private_key}:{seed}"


def main():
    num_wallets = int(input("Enter the number of wallets to generate: "))
    choice = menu()
    output_file = "solana_wallets.txt"

    with open(output_file, "w") as f:
        for _ in range(num_wallets):
            seed, private_key, address = generate_solana_wallet()
            entry = format_output(choice, seed, private_key, address)
            f.write(entry + "\n")

    print(f"\n{num_wallets} wallets saved to {output_file}")


if __name__ == "__main__":
    main()
