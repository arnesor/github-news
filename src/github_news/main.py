import asyncio
from check_releases import check_updates


def main() -> None:
    """Entry point for the nightly monitor."""
    print("Starting Arneso News GitHub Monitor...")
    try:
        asyncio.run(check_updates())
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print(f"Fatal error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
