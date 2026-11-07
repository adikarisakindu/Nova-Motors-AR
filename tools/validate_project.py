"""Static checks for the AR Activity assessment requirements.

These checks do not replace live marker tracking or a phone test.
"""
from pathlib import Path
import re
from bs4 import BeautifulSoup
import trimesh

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text(encoding='utf-8')
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
marker = soup.find('a-marker')
assert marker is not None and marker.get('preset') == 'hiro'
primitives = ('a-box', 'a-sphere', 'a-cylinder', 'a-plane', 'a-cone', 'a-torus')
primitive_nodes = [node for tag in primitives for node in marker.find_all(tag)]
assert len(primitive_nodes) >= 4, 'At least four objects required'
assert len({node.name for node in primitive_nodes}) >= 2, 'Two primitive types required'
assert marker.find('a-text') is not None, 'A-Frame text is missing'
assert marker.find('a-entity', attrs={'gltf-model': '#concept-car'}) is not None
assert 'property: rotation' in html and 'property: position' in html
assert "registerComponent('color-changer'" in html
assert "registerComponent('grow-toggle'" in html
assert 'markerFound' in html and 'markerLost' in html
assert 'class="clickable"' in html and 'raycaster="objects: .clickable' in html
assert 'src="models/concept_car.glb"' in html
assert 'CC0' in readme and 'concept_car.glb' in readme
assert (ROOT/'models/concept_car.glb').is_file()
assert (ROOT/'models/LICENSE.txt').is_file()
model = trimesh.load(ROOT/'models/concept_car.glb', force='scene')
assert len(model.geometry) >= 1
assert (model.bounds[1] > model.bounds[0]).all()
print('PASS: marker, 4+ objects, 2+ primitive types, text, 2 animation properties')
print('PASS: GLB local file, license credits, two different interaction components')
print('PASS: marker state events and click raycaster')
print(f'PASS: valid GLB with {len(model.geometry)} geometry parts, {(ROOT/"models/concept_car.glb").stat().st_size:,} bytes')
print('NOT AUTOMATABLE HERE: GitHub/HTTPS publication and real phone camera tests')
