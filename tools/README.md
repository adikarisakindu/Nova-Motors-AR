# Optional developer scripts

`build_concept_car.py` rebuilds the original local GLB car model. It uses Python packages `numpy` and `trimesh`.

`validate_project.py` performs static assignment checks. It uses Python packages `beautifulsoup4` and `trimesh`.

Neither script is necessary for the WebAR site to run on Live Server, GitHub Pages, or Netlify Drop. The complete GLB file is already in `models/`.

Real phone-camera testing and successful HTTPS deployment cannot be established by a static script.
