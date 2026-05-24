"""
Перевірка паліндрому через двосторонню чергу.

Ідея проста: кладемо всі символи в deque, потім по парі (зліва і справа)
відщипуємо і порівнюємо. Якщо хоч раз не співпали — не паліндром.
"""

from collections import deque


def _normalize(text: str) -> str:
    """Прибираємо пробіли і пунктуацію, опускаємо в нижній регістр."""
    return "".join(ch.lower() for ch in text if ch.isalnum())


def is_palindrome(text: str) -> bool:
    chars: deque[str] = deque(_normalize(text))

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


if __name__ == "__main__":
    samples = [
        # український класика
        "А роза упала на лапу Азора",
        "Я несу гусеня",
        # англ
        "Madam, I'm Adam",
        "A man, a plan, a canal: Panama",
        "Race car",
        "Was it a car or a cat I saw?",
        # довге і підступне
        "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.",
        # не паліндроми
        "Hello, world",
        "python",
        # edge cases
        "",
        "a",
        "Ab",
    ]

    for s in samples:
        verdict = "yes" if is_palindrome(s) else "no "
        preview = s if len(s) <= 50 else s[:47] + "..."
        print(f"  [{verdict}]  {preview!r}")
