from dataclasses import dataclass


@dataclass
class Tool:
    name: str
    integration: int
    quality: int
    price: int
    reliability: int
    seo: int

    def score(self) -> float:
        return (
            self.integration * 0.30
            + self.quality * 0.25
            + self.price * 0.20
            + self.reliability * 0.15
            + self.seo * 0.10
        )


TOOLS = [
    Tool("Sora API", 90, 92, 88, 90, 95),
    Tool("Veo API", 88, 93, 90, 89, 93),
    Tool("Kling API", 84, 87, 86, 85, 88),
    Tool("Runway API", 82, 88, 78, 83, 84),
]


def main() -> None:
    ranked = sorted(TOOLS, key=lambda x: x.score(), reverse=True)
    print("Awesome AI API Plus - Scoring Preview")
    print("-" * 48)
    for i, tool in enumerate(ranked, start=1):
        print(f"{i}. {tool.name:<12} score={tool.score():.2f}")


if __name__ == "__main__":
    main()

