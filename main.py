import os

TEXT = "I just told your mum about the 3am scrolling. All of it. I'm at 1% and I regret nothing."

def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"
    out = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
