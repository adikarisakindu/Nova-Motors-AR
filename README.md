# Nova Motors AR Showroom

**Group 65 | AR Activity**

## About the Project

Nova Motors is a simple Augmented Reality car showroom created using A-Frame and AR.js.

The application uses the Hiro marker to display a miniature car showroom through a camera. It includes a 3D car model, animated objects, and interactive features.

## Features

- A 3D car that rotates on the Hiro marker.
- A coloured ball that bounces and changes colour when clicked.
- A yellow cube that grows when clicked and returns to its original size when clicked again.
- Different 3D shapes and text labels.
- A status message that changes when the Hiro marker is detected or lost.

## How to Run

1. Download the project files.
2. Open the project folder in Visual Studio Code.
3. Open `index.html` using the Live Server extension.
4. Allow camera access in your browser.
5. Show the Hiro marker to your camera.
6. Click the ball and cube to try the interactions.

## Live AR Application

https://adikarisakindu.github.io/Nova-Motors-AR/

## Technologies Used

- HTML, CSS and JavaScript
- A-Frame
- AR.js
- GLB 3D model

## 3D Model Credit

The car model, `models/concept_car.glb`, was generated specifically for this project using procedural 3D geometry. The generation script is available at `tools/build_concept_car.py`.

Model licence information is included in `models/LICENSE.txt`.

## References

- Build Your First AR App — Lecture Guide
- https://aframe.io/
- https://ar-js-org.github.io/AR.js-Docs/
