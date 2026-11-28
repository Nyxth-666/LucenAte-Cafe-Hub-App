import { Coffee } from "lucide-react";

function SurpriseSection() {
  return (
    <div className="mx-auto flex w-full flex-col items-center px-5 py-12 text-center sm:px-8 sm:py-16 lg:px-10">

      <div className="flex h-20 w-20 items-center justify-center rounded-full bg-primary shadow-xl shadow-primary-dark/30 sm:h-23 sm:w-23">
        <Coffee
          size={40}
          className="shrink-0 text-text-secondary"
        />
      </div>

      <div className="flex flex-col items-center">
        <h2 className="mt-6 text-2xl font-bold font-serif text-text-dark sm:text-3xl lg:text-4xl">
          Find your next favorite spot.
        </h2>

        <p className="mt-3 max-w-md text-sm leading-relaxed text-text-secondary sm:text-base">
          Browse local cafés and restaurants around the city.
        </p>
      </div>

      <button
        type="button"
        className="mt-8 inline-flex items-center justify-center rounded-xl bg-accent px-8 py-3 text-sm font-semibold text-white transition hover:bg-primary-dark focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-accent"
      >
        Surprise me
      </button>

    </div>
  );
}

export default SurpriseSection;
