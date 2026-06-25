"""Dynamic blocklist management."""

from pathlib import Path


class BlocklistManager:
    def __init__(self, path: str = "data/blocklist.txt"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("")

    def list_domains(self) -> list[str]:
        return [
            line.strip()
            for line in self.path.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]

    def add_domain(self, domain: str) -> bool:
        domains = self.list_domains()
        if domain in domains:
            return False
        with self.path.open("a") as f:
            f.write(f"{domain}\n")
        return True

    def remove_domain(self, domain: str) -> bool:
        domains = self.list_domains()
        if domain not in domains:
            return False
        remaining = [d for d in domains if d != domain]
        self.path.write_text("\n".join(remaining) + "\n")
        return True

    def count(self) -> int:
        return len(self.list_domains())
