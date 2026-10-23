/*
 * Colour theme selection: "auto" (follow the system setting), "light" or "dark".
 * The choice is stored in the browser; without a stored choice "auto" is used.
 * This script has to be loaded in <head> so that the theme is applied before
 * the page is rendered.
 */
(function () {
    var KEY = "ooresults.theme";

    function getTheme() {
        try {
            var t = window.localStorage.getItem(KEY);
            return (t === "light" || t === "dark") ? t : "auto";
        } catch (e) {
            return "auto";
        }
    }

    function applyTheme(theme) {
        if (theme === "light" || theme === "dark") {
            document.documentElement.setAttribute("data-theme", theme);
        } else {
            document.documentElement.removeAttribute("data-theme");
        }
    }

    window.getTheme = getTheme;

    window.setTheme = function (theme) {
        try {
            if (theme === "light" || theme === "dark") {
                window.localStorage.setItem(KEY, theme);
            } else {
                window.localStorage.removeItem(KEY);
            }
        } catch (e) {
            // storage not available: theme only applies to this page view
        }
        applyTheme(theme);
    };

    applyTheme(getTheme());
})();
