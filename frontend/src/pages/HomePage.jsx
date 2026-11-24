import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import {
  Search,
  MapPin,
  Coffee,
  Utensils,
  RefreshCw,
} from "lucide-react";

import api from "../api/axios";
import Navbar from "../components/layout/Navbar";
import BusinessCard from "../components/business/BusinessCard";
import heroImage from "../assets/hero.png";

function HomePage() {
  const [searchInput, setSearchInput] = useState("");
  const [search, setSearch] = useState("");
  const [businessType, setBusinessType] = useState("ALL");
  const [priceRange, setPriceRange] = useState("ALL");

  // Fetch businesses from Django.
  const {
    data: businesses = [],
    isPending,
    isError,
    error,
    refetch,
  } = useQuery({
    queryKey: ["businesses", search, businessType, priceRange],

    queryFn: async () => {
      const params = {};

      if (search) {
        params.search = search;
      }

      if (businessType !== "ALL") {
        params.business_type = businessType;
      }

      if (priceRange !== "ALL") {
        params.price_range = priceRange;
      }

      const response = await api.get("discovery/businesses/", {
        params,
      });

      return Array.isArray(response.data)
        ? response.data
        : response.data.results ?? [];
    },
  });

  function handleSearch(event) {
    event.preventDefault();
    setSearch(searchInput.trim());
  }

  function resetFilters() {
    setSearchInput("");
    setSearch("");
    setBusinessType("ALL");
    setPriceRange("ALL");
  }

  return (
    <div className="min-h-screen bg-background">
      <Navbar
        onSearch={(value) => {
          setSearchInput(value);
          setSearch(value);
        }}
      />

      <main>
        {/* Hero Section */}
        <section className="mx-auto grid max-w-7xl items-center gap-10 px-5 py-14 sm:px-8 md:py-20 lg:grid-cols-2 lg:px-10">
          <div>
            <span className="inline-flex items-center gap-2 rounded-full border border-border bg-surface px-4 py-2 text-sm font-medium text-primary-dark">
              <MapPin size={15} />
              Your local guide to Lucena City
            </span>

            <h1 className="mt-6 max-w-xl text-5xl font-extrabold leading-tight tracking-tight text-text-dark sm:text-6xl">
              Discover Lucena.
              <span className="block text-primary-dark">
                One Café at a Time.
              </span>
            </h1>

            <p className="mt-6 max-w-lg text-base leading-relaxed text-text-secondary">
              Find cozy cafés, hidden restaurants, and local
              favorites around Lucena City. Your next favorite
              place might be closer than you think.
            </p>

            <a
              href="#discover"
              className="mt-8 inline-flex items-center gap-2 rounded-xl bg-primary-dark px-6 py-3 font-semibold text-white transition hover:bg-accent"
            >
              Start Exploring
              <Search size={18} />
            </a>

            <div className="mt-10 flex flex-wrap gap-6 text-sm text-text-secondary">
              <div className="flex items-center gap-2">
                <Coffee size={18} className="text-primary-dark" />
                Local Cafés
              </div>

              <div className="flex items-center gap-2">
                <Utensils size={18} className="text-primary-dark" />
                Restaurants
              </div>
            </div>
          </div>

          <div className="relative">
            <img
              src={heroImage}
              alt="Explore cafés and restaurants in Lucena City"
              className="h-[320px] w-full rounded-[2rem] object-cover shadow-lg sm:h-[420px]"
            />

            <div className="absolute -bottom-5 left-5 rounded-2xl bg-surface p-4 shadow-lg sm:left-8">
              <p className="text-sm font-bold text-text-dark">
                Discover something new.
              </p>
              <p className="mt-1 text-xs text-text-secondary">
                Support local businesses.
              </p>
            </div>
          </div>
        </section>

        {/* Discovery Section */}
        <section
          id="discover"
          className="scroll-mt-24 bg-surface py-16"
        >
          <div className="mx-auto max-w-7xl px-5 sm:px-8 lg:px-10">
            <div className="mb-8">
              <p className="text-sm font-semibold uppercase tracking-widest text-primary-dark">
                Explore Lucena
              </p>

              <h2 className="mt-2 text-3xl font-bold text-text-dark sm:text-4xl">
                Find your next favorite spot.
              </h2>

              <p className="mt-3 text-text-secondary">
                Browse local cafés and restaurants around the city.
              </p>
            </div>

            {/* Search and filters */}
            <form
              onSubmit={handleSearch}
              className="grid gap-3 rounded-2xl border border-border bg-background p-4 md:grid-cols-[1fr_180px_180px_auto]"
            >
              <div className="flex items-center gap-3 rounded-xl border border-border bg-surface px-4">
                <Search size={19} className="shrink-0 text-text-secondary" />

                <input
                  type="text"
                  value={searchInput}
                  onChange={(event) => setSearchInput(event.target.value)}
                  placeholder="Search businesses..."
                  className="w-full bg-transparent py-3 text-sm text-text-dark outline-none placeholder:text-text-secondary"
                />
              </div>

              <select
                value={businessType}
                onChange={(event) => setBusinessType(event.target.value)}
                className="rounded-xl border border-border bg-surface px-4 py-3 text-sm text-text-dark outline-none"
              >
                <option value="ALL">All places</option>
                <option value="CAFE">Cafés</option>
                <option value="RESTAURANT">Restaurants</option>
              </select>

              <select
                value={priceRange}
                onChange={(event) => setPriceRange(event.target.value)}
                className="rounded-xl border border-border bg-surface px-4 py-3 text-sm text-text-dark outline-none"
              >
                <option value="ALL">All prices</option>
                <option value="₱">₱</option>
                <option value="₱₱">₱₱</option>
                <option value="₱₱₱">₱₱₱</option>
              </select>

              <button
                type="submit"
                className="rounded-xl bg-primary-dark px-6 py-3 text-sm font-semibold text-white transition hover:bg-accent"
              >
                Search
              </button>
            </form>

            {/* Results heading */}
            <div className="mt-10 flex flex-wrap items-center justify-between gap-3">
              <div>
                <h3 className="text-xl font-bold text-text-dark">
                  Local Businesses
                </h3>

                {!isPending && !isError && (
                  <p className="mt-1 text-sm text-text-secondary">
                    {businesses.length}{" "}
                    {businesses.length === 1 ? "place" : "places"} found
                  </p>
                )}
              </div>

              <button
                type="button"
                onClick={resetFilters}
                className="flex items-center gap-2 text-sm font-medium text-primary-dark hover:text-accent"
              >
                <RefreshCw size={15} />
                Reset filters
              </button>
            </div>

            {/* Loading */}
            {isPending && (
              <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {[1, 2, 3].map((item) => (
                  <div
                    key={item}
                    className="animate-pulse overflow-hidden rounded-3xl border border-border bg-background"
                  >
                    <div className="h-52 bg-border" />
                    <div className="space-y-3 p-5">
                      <div className="h-5 w-2/3 rounded bg-border" />
                      <div className="h-4 w-full rounded bg-border" />
                      <div className="h-4 w-1/2 rounded bg-border" />
                    </div>
                  </div>
                ))}
              </div>
            )}

            {/* Error */}
            {isError && (
              <div className="mt-8 rounded-2xl border border-error/30 bg-error/5 p-6 text-center">
                <p className="font-semibold text-error">
                  Unable to load businesses.
                </p>

                <p className="mt-2 text-sm text-text-secondary">
                  {error?.response?.data?.detail ||
                    error.message ||
                    "Please check your Django server and try again."}
                </p>

                <button
                  type="button"
                  onClick={() => refetch()}
                  className="mt-4 rounded-xl bg-primary-dark px-5 py-2 text-sm font-semibold text-white"
                >
                  Try again
                </button>
              </div>
            )}

            {/* Business cards */}
            {!isPending && !isError && businesses.length > 0 && (
              <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                {businesses.map((business) => (
                  <BusinessCard
                    key={business.id}
                    business={business}
                  />
                ))}
              </div>
            )}

            {/* Empty state */}
            {!isPending && !isError && businesses.length === 0 && (
              <div className="mt-8 rounded-2xl border border-dashed border-border p-12 text-center">
                <Coffee
                  size={36}
                  className="mx-auto text-primary-dark"
                />

                <h3 className="mt-4 font-bold text-text-dark">
                  No businesses found.
                </h3>

                <p className="mt-2 text-sm text-text-secondary">
                  Try changing your search or filters.
                </p>

                <button
                  type="button"
                  onClick={resetFilters}
                  className="mt-4 text-sm font-semibold text-primary-dark hover:text-accent"
                >
                  Clear filters
                </button>
              </div>
            )}
          </div>
        </section>

        {/* About Section */}
        <section id="about" className="scroll-mt-24 py-16">
          <div className="mx-auto max-w-4xl px-5 text-center sm:px-8">
            <p className="text-sm font-semibold uppercase tracking-widest text-primary-dark">
              About LucenAte
            </p>

            <h2 className="mt-3 text-3xl font-bold text-text-dark">
              Discover local. Support local.
            </h2>

            <p className="mt-4 leading-relaxed text-text-secondary">
              LucenAte helps people discover cafés and restaurants
              throughout Lucena City, giving local businesses more
              visibility and helping customers find places worth visiting.
            </p>
          </div>
        </section>
      </main>

      <footer className="border-t border-border bg-surface py-6">
        <p className="text-center text-sm text-text-secondary">
          © {new Date().getFullYear()} LucenAte. Discover Lucena. One Café at a Time.
        </p>
      </footer>
    </div>
  );
}

export default HomePage;
