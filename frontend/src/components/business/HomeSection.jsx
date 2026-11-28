import heroImage from "../../assets/hero.png";

import {
  Search,
  Coffee,
} from "lucide-react";

function HomeSection() {
  return (
    <section className="mx-auto grid max-w-7xl items-center gap-10 px-5 py-14 sm:px-8 md:py-20 lg:grid-cols-2 lg:px-10">
      <div>
        <h1 className="mt-6 max-w-xl text-5xl font-extrabold leading-tight tracking-tight text-text-dark sm:text-6xl">
          Discover Lucena,
          One <span className="text-accent">Café</span> at a Time.
        </h1>

        <p className="mt-6 max-w-lg text-base leading-relaxed text-text-secondary">
          A local guide to the coffee shops and
          restaurants around the city - the popular
          ones, and the ones worth finding.
        </p>

        <div className="flex gap-2">
          <a
            href="#discover"
            className="mt-8 inline-flex items-center gap-2 rounded-xl bg-accent px-4 py-2 font-semibold text-white transition hover:bg-primary-dark"
          >
            Explore Places
            <Search size={18} />
          </a>

          <a
            href="#surprise-me"
            className="mt-8 inline-flex items-center gap-2 rounded-xl bg-transparent px-4 py-2 font-semibold text-accent border-3 border-accent transition hover:bg-accent hover:text-white"
          >
            Surprise Me
            <Coffee size={18} />
          </a>
        </div>

        <div className="mt-10 flex items-center gap-3 text-sm text-text-secondary">
          <div className="rounded-full bg-success w-2 h-2"></div><p>Showing places near your current location</p>
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
  );
}

export default HomeSection;
