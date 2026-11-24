import { Coffee, MapPin, Utensils } from "lucide-react";

function BusinessCard({ business }) {
  const location = business.locations?.[0];

  const address = location
    ? [
        location.street_address,
        location.barangay,
        location.city,
      ]
        .filter(Boolean)
        .join(", ")
    : "Lucena City";

  const BusinessIcon =
    business.business_type === "CAFE" ? Coffee : Utensils;

  const businessType =
    business.business_type === "CAFE" ? "Cafe" : "Restaurant";

  return (
    <article className="group overflow-hidden rounded-3xl border border-border bg-surface shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg">
      <div className="relative flex h-52 items-center justify-center bg-gradient-to-br from-lucena-primary/40 to-[#E5DDD5]">
        <BusinessIcon
          size={55}
          strokeWidth={1.2}
          className="text-lucena-primary-dark transition duration-300 group-hover:scale-110"
        />

        <span className="absolute right-4 top-4 rounded-full bg-background/90 px-3 py-1 text-xs font-semibold text-text-dark">
          {business.price_range}
        </span>

        <span className="absolute bottom-4 left-4 rounded-full bg-surface/90 px-3 py-1 text-xs font-semibold text-text-dark">
          {businessType}
        </span>
      </div>

      <div className="p-5">
        <h3 className="text-lg font-bold text-text-dark">
          {business.name}
        </h3>

        <p className="mt-2 flex items-start gap-2 text-sm text-text-secondary">
          <MapPin size={16} className="mt-0.5 shrink-0" />
          <span>{address}</span>
        </p>

        <p className="mt-3 line-clamp-2 text-sm leading-relaxed text-text-secondary">
          {business.description || "Discover this local spot in Lucena City."}
        </p>

        {business.features?.length > 0 && (
          <div className="mt-4 flex flex-wrap gap-2">
            {business.features.slice(0, 3).map((feature) => (
              <span
                key={feature}
                className="rounded-full bg-background px-3 py-1 text-xs text-text-secondary"
              >
                {feature}
              </span>
            ))}
          </div>
        )}
      </div>
    </article>
  );
}

export default BusinessCard;
