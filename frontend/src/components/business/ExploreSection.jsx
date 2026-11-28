import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { useSearchParams } from "react-router-dom";

import api from "../../api/axios";

import {
  Search,
  Coffee,
  RefreshCw,
} from "lucide-react";

import BusinessCard from "./BusinessCard";


function ExploreSection() {
  const [searchParams, setSearchParams] = useSearchParams();

  const [searchInput, setSearchInput] = useState(
    searchParams.get("search") || ""
  );

  const [businessType, setBusinessType] = useState("ALL");
  const [priceRange, setPriceRange] = useState("ALL");

  const search = searchParams.get("search") || "";
  const selectedCategory = searchParams.get("category") || "";

  const {
    data: businesses = [],
    isPending,
    isError,
    error,
    refetch,
  } = useQuery({
    queryKey: [
      "businesses",
      search,
      businessType,
      priceRange,
      selectedCategory,
    ],

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

      if (selectedCategory === "coffee-shops") {
        params.business_type = "CAFE";
      }

      if (selectedCategory === "restaurants") {
        params.business_type = "RESTAURANT";
      }

      const response = await api.get("discovery/businesses/", {
        params: {
          ...params,
          page_size: 3,
        },
      });

      return Array.isArray(response.data)
        ? response.data
        : response.data.results ?? [];
    },
  });

  function handleSearch(event) {
    event.preventDefault();

    const nextParams = new URLSearchParams(searchParams);

    if (searchInput.trim()) {
      nextParams.set("search", searchInput.trim());
    } else {
      nextParams.delete("search");
    }

    setSearchParams(nextParams);
  }

  function resetFilters() {
    setSearchInput("");
    setBusinessType("ALL");
    setPriceRange("ALL");
    setSearchParams({});
  }

  return (
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
  )
}

export default ExploreSection;
