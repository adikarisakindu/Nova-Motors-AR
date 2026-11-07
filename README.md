# Nova Motors | Mini AR Showroom

A marker-based augmented reality car showroom for the **AR Activity** group assignment. It starts from the lecture's **Step 5** implementation and turns the scene into a miniature car exhibit with a rotating GLB car, an animated color-changing ball, a second tappable object, text labels, and marker detection feedback.

## Features and assessment mapping

| Assignment requirement | Implementation |
|---|---|
| Hiro marker with at least four objects | `a-marker preset="hiro"` contains a ground plane, cylinders, torus, bouncing sphere, tappable box and the glTF car; 3D text labels are also present. |
| At least two primitive types and text | `a-plane`, `a-cylinder`, `a-torus`, `a-sphere`, `a-box`, and four `a-text` labels. |
| Two animations using different properties | The GLB car rotates using `rotation`; the colored sphere bounces using `position`. |
| Non-duck glTF/GLB model with credits | `models/concept_car.glb`, an original procedural concept car, with model licence and source disclosed below. |
| Workshop ball color change | The sphere uses the `color-changer` custom component. |
| Different second tappable interaction | A yellow box uses the separately authored `grow-toggle` component to enlarge/reset with a scale animation. |
| Marker status banner | The `marker-status` component handles `markerFound` and `markerLost` and changes both message and banner color. |
| HTTPS and phone test | Deploy to GitHub Pages or Netlify Drop using the steps below, then follow the mobile test checklist. **Deployment and phone testing must be performed by your group.** |

## Project files

```text
AR_Showroom_Project/
  index.html                  # Complete WebAR application
  models/concept_car.glb      # 3D model; local and included in repo
  models/LICENSE.txt          # 3D asset credits and CC0 licence statement
  tools/build_concept_car.py  # Optional source script to rebuild the model
  markers/README.md          # Official Hiro marker instructions
  README.md                  # This document
```

## Run on a computer

1. Open this folder using **Visual Studio Code**.
2. Install the **Live Server** extension by Ritwick Dey if needed.
3. Right-click `index.html` and select **Open with Live Server**.
4. In Chrome/Edge, grant camera permission. The URL should start with `http://localhost:` or `http://127.0.0.1:`. **Do not double-click the HTML file.**
5. Show the [official AR.js Hiro marker](https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png) on a different screen, or print it on paper with an intact white margin.
6. Keep the marker flat, well lit and entirely in camera view, about 20–40 cm away.
7. The header should turn green, the car rotate, and the colored ball bounce. Click the ball to cycle through colors. Click the yellow cube to enlarge it; click again to restore its size.
8. Click **the 3D ball itself** to change its color and **the yellow 3D cube itself** to grow/reset it. There are no screen buttons.

A network connection is necessary on initial load because A-Frame and AR.js are loaded from the same CDN versions used in the workshop. The **3D car model itself loads locally**.

## Publish the app over HTTPS

### GitHub Pages (preferred because the assignment also requires a public GitHub repository)

1. Sign in to GitHub and create a **new PUBLIC repository** for this group assignment.
2. Add all project files and folders, preserving their relative paths. The root of the repository must contain `index.html`.
3. Open the repository's **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, choose `main`, folder `/(root)`, then Save.
5. Once GitHub reports the deployment, open the HTTPS site address it provides (typically `https://USERNAME.github.io/REPOSITORY/`). **Only use the address after verifying it actually loads.**
6. Separately copy the real GitHub **repository** URL (typically `https://github.com/USERNAME/REPOSITORY`) into the group submission Word document. The repository link is **not** the same as the live Pages link.

### Netlify Drop (alternative HTTPS host)

1. Open https://app.netlify.com/drop and upload the **whole folder**, keeping the `models` directory.
2. Visit the HTTPS URL issued by Netlify on a phone. You **still must upload the project to a public GitHub repository** for the required Word submission.

## Mobile test checklist

Use Chrome on Android or Safari on iPhone. Open your **real HTTPS deployment URL**, grant camera access and point the rear camera at the Hiro marker. Record the result of each check before submission:

- [ ] HTTPS page loads and browser requests camera permission.
- [ ] Entire scene appears when the Hiro marker is visible.
- [ ] Header changes from red (search/lost) to green (found).
- [ ] **Original GLB car** is visible and rotates slowly.
- [ ] Colored ball bounces and changes color when tapped.
- [ ] Yellow box grows on first tap and returns to normal on second tap.
- [ ] Hiding the marker removes the scene and changes the banner back to red.
- [ ] `index.html`, `models/concept_car.glb`, README and license are in the public GitHub repository.

**These are tests to perform, not claimed completed test results.** No phone-camera session can be run from the generated files alone.

## Model authorship and licence

- **Model:** `models/concept_car.glb`, *Nova Motors Concept 01* (not the Duck).
- **Credit:** Original project geometry, procedurally produced for this AR class project. Reproducible source: `tools/build_concept_car.py`. The model is not copied from Sketchfab or another 3D model download.
- **License:** **CC0 1.0 Universal** for the original geometry, to the extent the creators control the relevant rights. The model and `models/LICENSE.txt` are included with this project. Licence details: https://creativecommons.org/publicdomain/zero/1.0/ .
- **Third-party 3D models:** None. No third-party textures or sound assets are used.

The original geometry uses procedural mesh creation rather than modifying the lecture Duck. The project keeps the same A-Frame / AR.js stack as the guide. A-Frame and AR.js are third-party libraries and remain subject to their respective licences.

## Code explanation for presentation

- `AFRAME.registerComponent('color-changer', ...)` listens for clicks on the bouncing sphere and cycles its `color` property across five entries.
- `AFRAME.registerComponent('grow-toggle', ...)` is the new interaction. Its click handler alternates the cube between scale `1 1 1` and `1.55 1.55 1.55`, using a short animation.
- `AFRAME.registerComponent('marker-status', ...)` listens for `markerFound` / `markerLost` and updates the HTML banner's text and CSS color class.
- `<a-assets>` preloads the GLB file; `gltf-model="#concept-car"` places the model inside the Hiro marker.
- The camera has `cursor="fuse: false; rayOrigin: mouse"` and `raycaster="objects: .clickable"` as in the workshop. A document-level mouse/touch raycast also detects taps directly on the projected 3D ball and cube when AR.js camera/video layers interfere with ordinary canvas clicks. Each 3D object includes a slightly larger fully transparent hit area; there are **no separate UI buttons**.
- `listenForObjectActivation()` debounces duplicate click events so a single tap will not change a ball's color twice.
- All 3D content is nested inside the marker element, so it only shows when marker tracking succeeds.

## Known limitations and troubleshooting

- **Camera blank:** Allow camera permission and run from localhost or HTTPS, not a regular `file://` URL.
- **Marker missing:** Show the entire black and white marker, avoid glare, and move the camera farther back.
- **Model invisible:** Check `models/concept_car.glb` is present with that exact spelling and open the browser Console for 404 errors.
- **Tap not working:** Click directly on the colored 3D sphere or yellow cube while the marker status is green. There are no on-screen buttons. After replacing an old `index.html`, save and hard-refresh (`Ctrl+Shift+R`); if needed, stop and restart Live Server. Open the browser Console (F12) to check for errors.
- **Phone camera fails:** Confirm the page uses HTTPS and try a supported, up-to-date mobile browser.
- **External scripts fail:** Internet access is required to load A-Frame and AR.js from their CDNs.

## Submission reminder

Submit **one `.docx` named using the group number** containing the URL of the **PUBLIC GitHub repository**. This is a **group assignment**, and only **one group member** submits. Deploy and phone-test before marking the project complete. There is no provided word-count requirement, referencing format, or separate grading rubric.

## Reference materials

- *AR Activity* assignment sheet, page 1 (uploaded by the student)
- *Build Your First AR App*, especially **Step 5, pp. 16–18**, **Challenges and Hosting, pp. 20–21**, and **Troubleshooting, p. 22** (uploaded by the student)
- [A-Frame official site](https://aframe.io/)
- [AR.js official documentation](https://ar-js-org.github.io/AR.js-Docs/)
- [Official Hiro marker](https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png)
- [Creative Commons CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
