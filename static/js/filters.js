const filterButtons = document.querySelectorAll(".filter-btn");
const clearButton = document.getElementById("filter-clear");

const activeFilters = new Set();

function updateFilters() {
  const filterArray = Array.from(activeFilters);
  const query = filterArray.length ? `?filters=${filterArray.join(",")}` : "";
  window.location.href = "" + query;
}


// Filter On/Off/Add
filterButtons.forEach((button) => {
  const filter = button.dataset.filter;

  if (filter) {
    button.addEventListener("click", () => {
      button.classList.toggle("active");

      if (activeFilters.has(filter)) {
        activeFilters.delete(filter);
      } else {
        activeFilters.add(filter);
      }

      updateFilters();
    });
  }
});

// Clear Button
clearButton.addEventListener("click", () => {
  filterButtons.forEach((btn) => btn.classList.remove("active"));
  activeFilters.clear();
  window.location.href = "";
});

// Highlight Active Filters on Page Load
window.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const filters = urlParams.get("filters");
  if (filters) {
    filters.split(",").forEach((filter) => {
      activeFilters.add(filter);
      const btn = document.querySelector(
        `.filter-btn[data-filter="${filter}"]`
      );
      if (btn) btn.classList.add("active");
    });
  }
});
