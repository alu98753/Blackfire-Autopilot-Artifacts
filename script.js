(() => {
  const manifestUrl = "assets/montage/manifest.json";
  const layers = [
    document.querySelector(".montage__layer--a"),
    document.querySelector(".montage__layer--b"),
  ].filter(Boolean);

  if (layers.length !== 2) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  fetch(manifestUrl, { cache: "no-cache" })
    .then((response) => {
      if (!response.ok) throw new Error("montage manifest unavailable");
      return response.json();
    })
    .then((manifest) => {
      const files = Array.isArray(manifest.files) ? manifest.files : [];
      if (!files.length) return;

      let index = 0;
      let visibleLayer = 0;

      const show = (file, layerIndex) => {
        const layer = layers[layerIndex];
        layer.style.backgroundImage = `url("assets/montage/${file}")`;
        requestAnimationFrame(() => layer.classList.add("is-visible"));
      };

      show(files[0], 0);
      if (reducedMotion || files.length === 1) return;

      window.setInterval(() => {
        index = (index + 1) % files.length;
        const nextLayer = 1 - visibleLayer;
        layers[nextLayer].classList.remove("is-visible");
        layers[nextLayer].style.backgroundImage = `url("assets/montage/${files[index]}")`;
        requestAnimationFrame(() => {
          layers[nextLayer].classList.add("is-visible");
          layers[visibleLayer].classList.remove("is-visible");
          visibleLayer = nextLayer;
        });
      }, 9000);
    })
    .catch(() => {
      // V1 deliberately falls back to the CSS atmosphere until real montage
      // outputs are generated from the private template library.
    });
})();
