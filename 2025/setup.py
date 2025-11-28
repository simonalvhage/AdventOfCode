import os
import shutil
from datetime import date
from pathlib import Path

import requests


def get_session_cookie() -> str:
	"""Get session cookie from environment variable or return default."""
	return os.environ.get(
		"AOC_SESSION",
		"53616c7465645f5fe233abb71092fb5980da9509390027d557c95f28612dfca79dd54ea801bd035daab1b825dbe0c3d702afa3c05528b7eb071c6f10182e6314"
	)


def create_folder(day: int, year: int = 2025) -> Path:
	"""Create folder structure for the given day."""
	day_path = Path(f"day{day}")
	day_path.mkdir(exist_ok=True)

	template_path = Path(__file__).parent / "template.py"
	main_path = day_path / "main.py"

	if not main_path.exists():
		if template_path.exists():
			shutil.copy(template_path, main_path)
			print(f"✓ Created {main_path} from template")
		else:
			print(f"✗ Warning: template.py not found at {template_path}")
			main_path.write_text("""from pathlib import Path

def read_input(file_path: str = "input.txt") -> list[str]:
	return Path(file_path).read_text().strip().splitlines()

def part1(data):
	return None

def part2(data):
	return None

if __name__ == "__main__":
	data = read_input("input.txt")
	print(f"Part 1: {part1(data)}")
	print(f"Part 2: {part2(data)}")
""")
			print(f"✓ Created {main_path} with basic template")

	return day_path


def download_input(day: int, year: int = 2025) -> None:
	"""Download input file for the given day."""
	day_path = Path(f"day{day}")
	input_path = day_path / "input.txt"

	if input_path.exists():
		print(f"✓ Input already exists at {input_path}")
		return

	url = f"https://adventofcode.com/{year}/day/{day}/input"
	session_cookie = get_session_cookie()

	try:
		response = requests.get(url, cookies={"session": session_cookie}, timeout=10)
		response.raise_for_status()

		input_path.write_text(response.text)
		print(f"✓ Downloaded input to {input_path}")

	except requests.exceptions.HTTPError as e:
		if e.response.status_code == 404:
			print(f"✗ Day {day} not yet available or invalid")
		elif e.response.status_code == 400:
			print(f"✗ Invalid session cookie. Set AOC_SESSION environment variable")
		else:
			print(f"✗ HTTP error: {e}")
	except requests.exceptions.RequestException as e:
		print(f"✗ Failed to download input: {e}")


def main(day: int | None = None, year: int = 2025) -> None:
	"""Setup folder and download input for Advent of Code."""
	if day is None:
		today = date.today()
		if today.month == 12 and 1 <= today.day <= 25:
			day = today.day
		else:
			print("Not December 1-25, please specify a day: python setup.py <day>")
			return

	print(f"\n🎄 Setting up Advent of Code {year} - Day {day}")
	create_folder(day, year)
	download_input(day, year)
	print(f"\n✅ Setup complete! Run: cd day{day} && python main.py\n")


if __name__ == "__main__":
	import sys

	day_arg = int(sys.argv[1]) if len(sys.argv) > 1 else None
	main(day=day_arg)
