# New Horizon

> A small Python playground for learning by typing, running, changing, and trying again.

This repository is a growing set of beginner-friendly exercises from New Horizon Computer Learning Center. Each script explores one idea at a time—from the first `if` statement to reading JSON and joining SQLite tables.

## Start Here

You only need Python 3.8 or later. There are no third-party packages to install.

```bash
git clone <your-repository-url>
cd "New Horizon"
python3 calculator.py
```

Most scripts ask for keyboard input, so run them in an interactive terminal. To try a different exercise, replace `calculator.py` with its filename:

```bash
python3 fibonacci.py
```

## Learning Trail

Pick a trail, run a script, then open it and make one small change. That is the whole idea.

| Trail | Try these files | You will practise |
| --- | --- | --- |
| **Python foundations** | `for.py`, `while.py`, `string.py`, `sample.py` | variables, strings, lists, loops, and output |
| **Decisions** | `voter.py`, `Election.py`, `miif.py`, `Multiple_elif.py` | comparisons, validation, `if` / `elif` / `else` |
| **Functions & calculations** | `calculator.py`, `function.py`, `functions.py`, `fibonacci.py` | parameters, return values, arithmetic, and simple algorithms |
| **Collections** | `assignment.py`, `dic.py`, `dic_example.py` | lists, dictionaries, sorting, and nested data |
| **Files & data** | `json_file_handling.py`, `employee1.json` | writing structured JSON data |
| **SQLite basics** | `table.sql`, `create.py`, `join.py`, `joins.py`, `left_join.py` | tables, inserts, and SQL joins |
| **Open practice** | `count1.py`, `DevOp.py`, `Excercise.py` | mixed challenges and experiments |

## A Good First Session

1. Run `python3 calculator.py` and test every operator.
2. Open `calculator.py`; add a new operator or improve an error message.
3. Run `python3 fibonacci.py`; change the number of values printed.
4. Move to `voter.py` or `Multiple_elif.py` and test edge cases.
5. Keep a copy of a script before experimenting—mistakes are useful here.

## Working With the Database Exercises

The SQLite examples use the local `database.db` file. `table.sql` shows the `students` and `courses` table structure, while `create.py` adds a student and the join scripts read related records.

```bash
python3 joins.py
```

`create.py` changes `database.db` each time it runs. If you are only exploring joins, start with `join.py` or `joins.py` instead.

## Notes From the Workshop

- The scripts are learning snapshots, so some intentionally keep rough edges, alternate approaches, and original filenames such as `Excercise.py`.
- A few files collect multiple snippets in one place. Read and run them section by section when needed.
- `json_file_handling.py` rewrites `employee1.json` with its sample employee record.
- No virtual environment is required, but you can create one if you want a clean Python workspace:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

## Make It Yours

This is a practice space, not a finished product. Fork an exercise, rename it, break it, rebuild it, and add your own examples. The best next lesson is usually the version you write yourself.

---

**Small scripts. Real progress. Keep going.**
