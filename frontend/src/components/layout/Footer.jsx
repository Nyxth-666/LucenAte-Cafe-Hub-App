
import { Link } from "react-router-dom";
import logoImage from "../../assets/logo.png";

function Footer() {
  const currentYear = new Date().getFullYear();

  const linkStyle =
    "text-sm text-text-secondary transition hover:text-accent";

  return (
    <footer className="border-t border-border bg-surface shadow-lg shadow-border">
      <div className="mx-auto max-w-7xl px-5 sm:px-8 lg:px-10">

        <div className="grid grid-cols-2 gap-8 py-8 sm:grid-cols-3 lg:grid-cols-[1.2fr_1fr_1fr_1.2fr] lg:gap-10">

          <div className="col-span-2 flex items-center sm:col-span-1">
            <Link to="/" aria-label="LucenAte homepage">
              <img
                src={logoImage}
                alt="LucenAte"
                className="h-12 w-auto object-contain"
              />
            </Link>
          </div>

          <div className="flex flex-col gap-3">
            <a
              href="mailto:lucenate@gmail.com"
              className={linkStyle}
            >
              lucenate@gmail.com
            </a>
          </div>

          <div className="flex flex-col gap-3">
            <Link to="/about" className={linkStyle}>
              About Us
            </Link>

            <Link to="/contact" className={linkStyle}>
              Contact
            </Link>

            <Link to="/cuisines" className={linkStyle}>
              All Cuisines
            </Link>
          </div>

          <div className="flex flex-col gap-3">
            <Link to="/terms-and-conditions" className={linkStyle}>
              Terms and Conditions
            </Link>

            <Link to="/policies" className={linkStyle}>
              Policies
            </Link>
          </div>

        </div>

        <div className="border-t border-border py-4">
          <p className="text-center text-xs text-text-secondary">
            © {currentYear} LucenAte. All rights reserved.
          </p>
        </div>

      </div>
    </footer>
  );
}

export default Footer;
