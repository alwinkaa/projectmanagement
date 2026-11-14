# Project Documentation

## Project Structure

```text
project/
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── ...
└── README.md
```

---

## Tech Stack

* **Backend:** Django (Function-based views)
* **Database:** SQLite
* **Frontend:** Django templates + minimal inline CSS

---

## Installation & Running

### 1. Get the Project
Unzip the project folder, or clone it if hosted on Git.

### 2. Open a Terminal in the Project Folder
Navigate to the folder that contains `manage.py`:

* **Windows (CMD/PowerShell):**
  ```bash
  cd path\to\project
  ```
* **macOS/Linux:**
  ```bash
  cd path/to/project
  ```

### 3. Create and Activate a Virtual Environment (Recommended)

* **Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
* **macOS/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

> You should see `(.venv)` at the start of your terminal prompt.

* **PowerShell users:** If activation fails with `"running scripts is disabled"`, run this once, then activate again:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### 4. Install Django
```bash
pip install django
```

### 5. Apply Database Migrations
This creates the SQLite database (`db.sqlite3`) and sets up the tables:
```bash
python manage.py makemigration
python manage.py migrate
```

### 6. Create an Admin Account (Optional)
Optional step to gain access to the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts (username, email, password). Password validation is strict — pick something reasonably strong.

### 7. Run the Development Server
```bash
python manage.py runserver
```
You should see output similar to:
```text
Starting development server at http://127.0.0.1:8000/
```

### 8. Open the App in Your Browser
* **App:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin Panel (optional):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

To stop the server, press `Ctrl + C` in the terminal.

---

## How to Use

* **Create a project:** Click **`+ New Project`** on the home page.
* **Add tasks:** Open a project and click **`+ Add Task`**.
* **Update status:** Use the dropdown on any task row (auto-saves).
* **Delete a task:** Click **`Delete`** and confirm.
* **Search / Filter:** Use the search box and status dropdown on the project page. Click **`Clear`** to reset filters.

---

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `'python' is not recognized` | Install Python from [python.org](https://www.python.org/) and ensure **"Add Python to PATH"** is checked during installation. On macOS/Linux, use `python3`. |
| `No module named django` | Activate the virtual environment first (step 3), then run `pip install django`. |
| `Port 8000 already in use` | Run on a different port: `python manage.py runserver 8080` |
| `TemplateDoesNotExist` | Ensure the `app/templates/app/` folder exists and files are named correctly. |
| `no such table error` | Run `python manage.py migrate`. |
| **PowerShell:** `"running scripts is disabled"` | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, then activate again. |

---

## Project Notes

* **Database:** SQLite (file: `db.sqlite3`). Auto-created on first migration. No setup required.
* **Dependencies:** No external dependencies beyond Django — no frontend framework or Node.js required.
* **Styling:** Inline in `app/templates/app/base.html` (kept simple and dependency-free).
* **Validation:** Handled via Django `ModelForms` plus custom `clean_` methods that reject whitespace-only input.