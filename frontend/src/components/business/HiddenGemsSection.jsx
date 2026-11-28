import { useQuery } from "@tanstack/react-query";
import { Link } from "react-router-dom";
import { Coffee, Utensils, ArrowRight } from "lucide-react";

import api from "../../api/axios";

function getTimeAgo(dateString) {
  const date = new Date(dateString);
  const now = new Date();

  const seconds = Math.floor((now - date) / 1000);

  if (seconds < 60) return "just now";

  const minutes = Math.floor(seconds / 60);
  if (minutes < 60) return `${minutes} ${minutes === 1 ? "minute" : "minutes"} ago`;

  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours} ${hours === 1 ? "hour" : "hours"} ago`;

  const days = Math.floor(hours / 24);
  if (days < 7) return `${days} ${days === 1 ? "day" : "days"} ago`;

  const weeks = Math.floor(days / 7);
  if (weeks < 5) return `${weeks} ${weeks === 1 ? "week" : "weeks"} ago`;

  const months = Math.floor(days / 30);
  if (months < 12) return `${months} ${months === 1 ? "month" : "months"} ago`;

  const years = Math.floor(days / 365);
  return `${years} ${years === 1 ? "year" : "years"} ago`;
}

function HiddenGemsSection() {
  const {
    data: businesses = [],
    isPending,
    isError,
  } = useQuery({
    queryKey: ["hidden-gems"],

    queryFn: async () => {
      const response = await api.get("discovery/businesses/", {
        params: {
          hidden_gems: "true",
        },
      });

      const results = Array.isArray(response.data)
        ? response.data
        : response.data.results ?? [];

      return results.slice(0, 3);
    },
  });

  return (
    <div className="bg-surface px-5 py-10 sm:px-8 lg:px-10">
      <div className="mx-auto grid max-w-7xl gap-8 rounded-2xl bg-accent p-7 sm:p-10 lg:grid-cols-2 lg:items-center lg:gap-12 lg:px-16 lg:py-12">

        <div>
          <h2 className="font-serif text-3xl italic text-white sm:text-3xl">
            Hidden gems of Lucena
          </h2>

          <p className="mt-4 max-w-sm leading-relaxed text-white/65">
            Smaller places doing something well — not ranked by popularity,
            chosen because they deserve a look.
          </p>

          <Link
            to="/explore?category=hidden-gems"
            className="mt-5 inline-flex items-center gap-2 rounded-lg bg-white px-5 py-2.5 text-sm font-semibold text-accent transition hover:bg-background"
          >
            Explore all gems
            <ArrowRight size={16} />
          </Link>
        </div>

        <div className="space-y-3">

          {isPending && (
            [1, 2, 3].map((item) => (
              <div
                key={item}
                className="flex animate-pulse items-center gap-3 rounded-xl bg-white/15 p-3"
              >
                <div className="h-12 w-12 shrink-0 rounded-lg bg-white/20" />

                <div className="flex-1 space-y-2">
                  <div className="h-3 w-1/3 rounded bg-white/20" />
                  <div className="h-2 w-2/3 rounded bg-white/20" />
                </div>
              </div>
            ))
          )}

          {isError && (
            <div className="rounded-xl bg-white/10 p-5 text-sm text-white">
              Unable to load hidden gems. Please try again later.
            </div>
          )}

          {!isPending && !isError && businesses.length > 0 && (
            businesses.map((business) => {
              const Icon =
                business.business_type === "CAFE" ? Coffee : Utensils;

              return (
                <Link
                  key={business.id}
                  to={`/businesses/${business.id}`}
                  className="flex items-center gap-3 rounded-xl bg-white/15 p-3 transition hover:bg-white/25"
                >
                  <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-lg bg-primary text-white">
                    <Icon size={22} />
                  </div>

                  <div className="min-w-0">
                    <h3 className="truncate text-sm font-semibold text-white">
                      {business.name}
                    </h3>

                    <p className="mt-1 text-xs text-white/60">
                      {business.business_type === "CAFE"
                        ? "Café"
                        : "Restaurant"}
                      {" · "}
                      {business.review_count === 0
                        ? "No reviews yet"
                        : `${business.review_count} ${
                            business.review_count === 1 ? "review" : "reviews"
                          }`}
                      {" · Added "}
                      {getTimeAgo(business.created_at)}
                    </p>
                  </div>
                </Link>
              );
            })
          )}

          {!isPending && !isError && businesses.length === 0 && (
            <div className="rounded-xl bg-white/10 p-5 text-sm text-white/80">
              No hidden gems to discover just yet. Check back later!
            </div>
          )}

        </div>
      </div>
    </div>
  );
}

export default HiddenGemsSection;
