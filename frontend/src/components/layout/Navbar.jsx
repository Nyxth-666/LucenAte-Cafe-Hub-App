import { useState } from "react";
import { Link } from "react-router-dom";
import { Search } from "lucide-react";
import logoImage from "../../assets/logo.png";

function Navbar({ onSearch }) {
  const [searchInput, setSearchInput] = useState("");

  function handleSearch(event) {
    event.preventDefault();

    onSearch?.(searchInput.trim());

    document.getElementById("discover")?.scrollIntoView({
      behavior: "smooth",
    });
  }

  return (
    <header className="sticky top-0 z-50 border-b border-border bg-surface shadow-lg shadow-border">
      <div className="mx-auto max-w-7xl px-5 py-3.5 sm:px-8 lg:px-10">
        <div className="flex h-14 items-center justify-between">
          <Link
            to="/"
            className="flex items-center gap-3 font-serif text-2xl font-bold tracking-tight text-text-dark"
          >
            <img src={logoImage} alt="logo" className="h-16 w-16 object-contain" />
            LucenAte
          </Link>

          <div className="flex items-center gap-3">
            <Link
              to="/login"
              className="rounded-lg border border-primary-dark px-5 py-2 text-sm font-medium text-primary-dark transition hover:bg-primary-dark hover:text-white"
            >
              Login
            </Link>

            <Link
              to="/register/business"
              className="rounded-lg bg-accent px-4 py-2 text-sm font-medium text-white transition hover:bg-primary-dark"
            >
              Register a Business
            </Link>
          </div>
        </div>

        <div className="flex min-h-12 items-center justify-between gap-4 pb-3 sm:pb-0">
          <nav className="flex items-center gap-5 overflow-x-auto sm:gap-8">
            <Link
              to="/"
              className="shrink-0 text-sm font-medium text-text-secondary transition hover:text-accent"
            >
              Home
            </Link>

            <a
              href="#discover"
              className="shrink-0 text-sm font-medium text-text-secondary transition hover:text-accent"
            >
              Explore
            </a>

            <a
              href="#map"
              className="shrink-0 text-sm font-medium text-text-secondary transition hover:text-accent"
            >
              Map
            </a>

            <a
              href="#surprise-me"
              className="shrink-0 text-sm font-medium text-text-secondary transition hover:text-accent"
            >
              Surprise Me
            </a>
          </nav>

          <form
            onSubmit={handleSearch}
            className="hidden w-full max-w-[430px] shrink-0 items-center gap-2 rounded-lg border border-border bg-surface p-3 sm:flex"
          >
            <Search size={17} className="shrink-0 text-text-secondary" />

            <input
              type="search"
              value={searchInput}
              onChange={(event) => setSearchInput(event.target.value)}
              placeholder="Search cafés, dishes, places..."
              className="w-full min-w-0 bg-transparent text-xs text-text-dark outline-none placeholder:text-text-secondary"
            />
          </form>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
