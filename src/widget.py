# src/widget.py

from masks import get_mask_card_number, get_mask_account
from typing import Any


def mask_account_card(info: str) -> str:
    """
    Masks account or card information.

    Args:
        info (str): Account or card information.

    Returns:
        str: Masked account or card information.
    """
    if info.startswith("Счет"):
        return f"Счет {get_mask_account(info.split()[1])}"
    else:
        card_type, card_number = info.rsplit(' ', 1)
        return f"{card_type} {get_mask_card_number(card_number)}"


# src/widget.py

from datetime import datetime


def get_date(date_str: str) -> str:
    """
    Converts an ISO 8601 date string to a formatted date string.

    Args:
        date_str (str): ISO 8601 date string.

    Returns:
        str: Formatted date string in the format 'dd.mm.yyyy'.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


# Пример для карты
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361

# Пример для счета
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

# Пример для даты
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
