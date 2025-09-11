import csv
import os
from pathlib import Path

# These are the brands that have product data sheets.
BRANDS = [
    "Eacochem",
    "Envirobiocleaner",
    "Front9restoration",
    "Tridentprotects",
]

# These are the headers for our CSV files.
SDS_HEADERS = ["brand", "product_name", "sds_link"]
TDS_HEADERS = ["brand", "product_name", "tds_link"]


def main():
    """
    This is the main function of our script. It finds all the product data sheets,
    processes them, and then writes them to two separate CSV files.
    """
    sds_rows = []
    tds_rows = []

    for brand in BRANDS:
        for root, _, files in os.walk(brand):
            product_name = os.path.basename(root)
            if product_name == brand:
                continue

            for file in files:
                if not file.lower().endswith(".pdf"):
                    continue

                # Create a markdown link to the file.
                link = f"[{file}](../{Path(root, file)})"

                if "sds" in file.lower():
                    sds_rows.append(
                        {
                            "brand": brand,
                            "product_name": product_name,
                            "sds_link": link,
                        }
                    )
                else:
                    tds_rows.append(
                        {
                            "brand": brand,
                            "product_name": product_name,
                            "tds_link": link,
                        }
                    )

    # Write the data to the SDS CSV file.
    with open("docs/assets/tables/sds.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SDS_HEADERS)
        writer.writeheader()
        writer.writerows(sds_rows)

    # Write the data to the TDS CSV file.
    with open("docs/assets/tables/tds.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TDS_HEADERS)
        writer.writeheader()
        writer.writerows(tds_rows)


if __name__ == "__main__":
    main()
