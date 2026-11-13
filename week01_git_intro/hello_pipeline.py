"""Week 1 lab — minimal data pipeline stub for Git push demo."""


def main() -> None:
    rows = [{"store_id": 12, "sku": "SKU-4421", "qty": 3}]
    print(f"Loaded {len(rows)} bronze row(s) — ready for Glue later.")


if __name__ == "__main__":
    main()
