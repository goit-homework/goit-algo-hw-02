"""
Імітація сервісного центру.

Заявки летять у чергу, оператор Степан їх по черзі розгрібає.
"""

from queue import Queue
from random import choice, randint, uniform
from time import sleep


ISSUES = [
    "інтернет лагає",
    "забув пароль",
    "принтер з'їв папір",
    "не вмикається ноут",
    "екран синій, шрифт білий",
    "кіт сів на клавіатуру",
    "Wi-Fi бачить, але не любить",
    "монітор показує сни",
]

PRIORITIES = ["low", "normal", "high", "high", "normal"]  # high зустрічається частіше

OPERATOR = "Степан"


class Ticket:
    __slots__ = ("id", "issue", "priority")

    def __init__(self, ticket_id: int) -> None:
        self.id = ticket_id
        self.issue = choice(ISSUES)
        self.priority = choice(PRIORITIES)

    def __str__(self) -> str:
        return f"#{self.id:03d} [{self.priority:>6}] {self.issue}"


queue: Queue[Ticket] = Queue()
counters = {"created": 0, "processed": 0}
_next_id = 1


def generate_request() -> None:
    global _next_id
    ticket = Ticket(_next_id)
    queue.put(ticket)
    counters["created"] += 1
    _next_id += 1
    print(f"  [new ] {ticket}")


def process_request() -> None:
    if queue.empty():
        print("  [idle] черга порожня, Степан п'є каву")
        return
    ticket = queue.get()
    work_time = round(uniform(0.1, 0.5), 2)
    print(f"  [work] {OPERATOR} взяв {ticket} (займе ~{work_time}s)")
    sleep(work_time)
    counters["processed"] += 1
    print(f"  [done] {ticket}")


def print_summary() -> None:
    left = queue.qsize()
    print()
    print("=" * 50)
    print(f"  створено:  {counters['created']}")
    print(f"  оброблено: {counters['processed']}")
    print(f"  залишок:   {left}")
    print("=" * 50)


def main() -> None:
    print("Сервісний центр відкрито. Команди: [g]enerate, [p]rocess, [q]uit, Enter = авто")
    print("-" * 50)

    try:
        while True:
            cmd = input("> ").strip().lower()

            if cmd == "q":
                break
            if cmd == "g":
                generate_request()
                continue
            if cmd == "p":
                process_request()
                continue

            # авто-режим: трохи заявок, одна обробка
            for _ in range(randint(1, 3)):
                generate_request()
            process_request()
    except (KeyboardInterrupt, EOFError):
        print()  # чистий перенос рядка після Ctrl+C

    print_summary()
    print("Зачиняємось. До побачення.")


if __name__ == "__main__":
    main()
