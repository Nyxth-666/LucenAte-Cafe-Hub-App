import { Link } from "react-router-dom";
import {
  Coffee,
  Utensils,
  CakeSlice,
  Croissant,
  Sandwich,
  CupSoda,
} from "lucide-react";

const categories = [
  {
    name: "Coffee Shops",
    value: "coffee-shops",
    icon: Coffee,
  },
  {
    name: "Restaurants",
    value: "restaurants",
    icon: Utensils,
  },
  {
    name: "Desserts",
    value: "desserts",
    icon: CakeSlice,
  },
  {
    name: "Bakeries",
    value: "bakeries",
    icon: Croissant,
  },
  {
    name: "Fast Foods",
    value: "fast-foods",
    icon: Sandwich,
  },
  {
    name: "Tea Shops",
    value: "tea-shops",
    icon: CupSoda,
  },
];

function BrowseByCategorySection() {
  return (
    <div className="bg-surface px-5 py-10 sm:px-8 lg:px-10">
      <div className="mx-auto max-w-7xl px-5 sm:px-8 lg:px-10">

        <div className="mb-8">
          <p className="text-sm font-semibold uppercase tracking-widest text-primary-dark">
            Look for cravings
          </p>

          <h2 className="mt-2 text-3xl font-bold text-text-dark sm:text-4xl">
            Browse by category.
          </h2>

          <p className="mt-3 text-text-secondary">
            Browse local cafés and restaurants around the city.
          </p>
        </div>

        <div className="flex flex-wrap justify-between gap-3 sm:gap-5">
          {categories.map((category) => {
            const Icon = category.icon;

            return (
              <Link
                key={category.value}
                to={`/explore?category=${category.value}`}
                className="flex items-center gap-3 rounded-lg border border-border bg-surface px-6 py-3.5 text-sm text-text-secondary transition hover:border-accent hover:bg-background hover:text-text-dark sm:px-4"
              >
                <span className="rounded-md bg-background p-1.5">
                  <Icon size={18} className="text-accent" />
                </span>

                <span className="whitespace-nowrap">
                  {category.name}
                </span>
              </Link>
            );
          })}
        </div>

      </div>
    </div>
  );
}

export default BrowseByCategorySection;
