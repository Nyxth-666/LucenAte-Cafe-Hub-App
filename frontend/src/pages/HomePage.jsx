import { useNavigate } from "react-router-dom";

import Navbar from "../components/layout/Navbar";

import HomeSection from "../components/business/HomeSection";
import ExploreLocalLucena from "../components/business/ExploreSection";
import BrowseByCategory from "../components/business/BrowseByCategorySection";
import HiddenGems from "../components/business/HiddenGemsSection";
import SurpriseSection from "../components/business/SurpriseSection";

function HomePage() {
  return (
    <main className="min-h-screen bg-background">

      <section
        id="home"
        className="scroll-mt-24 py-12"
      >
        <HomeSection />
      </section>

      <section
        id="discover"
        className="scroll-mt-24 bg-surface py-12"
      >
        <ExploreLocalLucena />
      </section>

      <section
        id="browse"
        className="scroll-mt-18 bg-surface py-12"
      >
        <BrowseByCategory />
      </section>

      <section
        id="hidden-gems"
        className="scroll-mt-18 bg-surface py-12"
      >
        <HiddenGems />
      </section>

      <section
        id="surprise-me"
        className="scroll-mt-18 py-12"
      >
        <SurpriseSection />
      </section>

    </main>
  );
}

export default HomePage;
