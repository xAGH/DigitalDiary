/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      gridColumn: {
        pro: "1",
      },
      fontFamily: {
        itim: ["Itim", "cursive"],
        openSans: ["Open Sans", "sans-serif"],
      },
      height: {
        "90%": "90%",
        "95%": "95%",
        "85vh": "85vh",
      },
      textColor: {
        primary: "#EBEBEB",
      },
      fontSize: {
        profile: ["11rem", "150px"],
        contact: ["7rem", "110px"],
      },
      fontFamily: {
        openSans: ["OpenSans", ""],
        itim: ["Itim", "cursive"],
      },
      backgroundColor: {
        primary: "#EBEBEB",
        edit: "#5aceea",
        delete: "#ff5757",
      },
    },
  },
  plugins: [],
};
