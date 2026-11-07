"""Rebuild the original low-poly concept-car GLB included in this assignment.

This model consists of original procedural geometry and uses no third-party mesh
or textures. Licensed CC0-1.0 (see models/LICENSE.txt).
"""
from pathlib import Path
import numpy as np
import trimesh
from trimesh.visual.material import PBRMaterial

OUTPUT = Path(__file__).resolve().parents[1] / 'models' / 'concept_car.glb'
scene = trimesh.Scene()

NAVY  = (22, 63, 118, 255)
AZURE = (35, 132, 229, 255)
LIGHT = (91, 182, 244, 255)
SILVER= (199, 214, 225, 255)
GLASS = (28, 49, 70, 255)
TIRE  = (23, 28, 35, 255)
METAL = (88, 101, 115, 255)
WHITE = (255, 244, 196, 255)
RED   = (228, 57, 68, 255)

materials = {}
def mat(rgb, metallic=0, roughness=.35):
    key = (rgb, metallic, roughness)
    if key not in materials:
        materials[key] = PBRMaterial(baseColorFactor=rgb,
                                     metallicFactor=metallic,
                                     roughnessFactor=roughness,
                                     doubleSided=True)
    return materials[key]

def add(mesh, name, color, metallic=0.0, roughness=.35):
    mesh.visual = trimesh.visual.TextureVisuals(material=mat(color, metallic, roughness))
    scene.add_geometry(mesh, node_name=name)

def box(name, size, pos, rgb, metallic=0, roughness=.4):
    mesh = trimesh.creation.box(extents=size)
    mesh.apply_translation(pos)
    add(mesh, name, rgb, metallic, roughness)

def tube(name, radius, length, pos, rgb, metallic=0, roughness=.6, sections=24):
    mesh=trimesh.creation.cylinder(radius=radius, height=length, sections=sections)
    # cylinder z-axis -> x-axis
    rot=trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])
    mesh.apply_transform(rot)
    mesh.apply_translation(pos)
    add(mesh,name,rgb,metallic,roughness)

def hull(name, pts, rgb, metallic=.3, roughness=.31):
    mesh=trimesh.convex.convex_hull(np.array(pts,dtype=float))
    add(mesh,name,rgb,metallic,roughness)

def panel(name, pts, rgb, metallic=0, roughness=.15, thickness=.009):
    """Small thickened polygon, triangulated as a prism using convex hull."""
    ps=np.asarray(pts,float)
    avg=ps.mean(axis=0)
    normal=np.cross(ps[1]-ps[0], ps[2]-ps[0]);normal/=np.linalg.norm(normal)
    volume=np.concatenate([ps+thickness*normal,ps-thickness*normal])
    hull(name, volume, rgb, metallic, roughness)

# Direction: front at z=-0.72, rear at z=+0.72. Wheels on x-sides.
# Stylized body shell, aerodynamic hood and tapered trunk.
base_pts=[]
for z,halfwidth,bottom,shoulder in [(-.79,.32,.21,.34),(-.50,.40,.16,.41),(.34,.40,.16,.43),(.77,.32,.21,.35)]:
    for x in [-halfwidth,halfwidth]:
        base_pts.extend([(x,bottom,z),(x,shoulder,z)])
hull('aero_body',base_pts,AZURE,.62,.28)
# Raised center spine / hood and highlight trim.
hull('hood_sculpture', [(-.25,.39,-.72),(.25,.39,-.72),(-.32,.45,-.28),(.32,.45,-.28),
                            (-.32,.40,-.14),(.32,.40,-.14)],AZURE,.62,.23)
# Cabin, raked windshield and back window.
cabin_pts=[]
for z,width,y in [(-.25,.32,.43),(-.10,.23,.67),(.29,.23,.67),(.53,.31,.42)]:
    for x in [-width,width]: cabin_pts.append((x,y,z))
hull('cabin_frame', cabin_pts,GLASS,.18,.19)
# Side windows above line y=.46, one window each side.
for side in [-1,1]:
    x=side
    panel(f'window_side_{side}',[(x*.321,.465,-.22),(x*.234,.632,-.075),(x*.234,.632,.26),(x*.308,.467,.46)],GLASS,.05,.07)
    # Center divider for window panel.
    box(f'window_pillar_{side}',(.021,.176,.028),(x*.277,.56,.10),NAVY,.25,.35)
# Front and rear windshields.
panel('front_windshield',[(-.296,.457,-.238),(.296,.457,-.238),(.214,.634,-.078),(-.214,.634,-.078)],GLASS,.02,.08)
panel('rear_windshield',[(-.214,.630,.27),(.214,.630,.27),(.290,.468,.484),(-.290,.468,.484)],GLASS,.02,.08)
# Roof accent, stripe and side skirts.
box('roof_insert',(.46,.023,.35),(0,.661,.106),AZURE,.5,.25)
for side in [-1,1]:
    box(f'side_skirt_{side}',(.050,.055,.97),(side*.395,.222,.06),METAL,.55,.42)
    # Slim bright trim strip running along shoulder.
    box(f'shoulder_accent_{side}',(.017,.018,.56),(side*.391,.404,.04),LIGHT,.64,.22)
# Wheel assemblies: rubber tires, hubs, fine center nuts.
for side in [-1,1]:
    for axle,z in [('front',-.49),('rear',.50)]:
        x=side*.409
        tube(f'{axle}_{side}_tire',.172,.098,(x,.175,z),TIRE,.04,.92,36)
        tube(f'{axle}_{side}_rim_outer',.118,.102,(x,.175,z),SILVER,.80,.26,36)
        tube(f'{axle}_{side}_rim_inset',.091,.107,(x,.175,z),METAL,.83,.30,36)
        tube(f'{axle}_{side}_rim_center',.035,.116,(x,.175,z),LIGHT,.80,.18,24)
# Front grill, slim lights, bumpers.
box('front_bumper',(.49,.080,.042),(0,.259,-.785),METAL,.55,.35)
box('front_grille',(.34,.071,.018),(0,.306,-.809),TIRE,.1,.74)
for side in [-1,1]:
    box(f'headlamp_{side}',(.155,.050,.027),(side*.250,.361,-.770),WHITE,.06,.16)
    box(f'tail_lamp_{side}',(.140,.063,.029),(side*.255,.352,.771),RED,.04,.2)
box('rear_diffuser',(.49,.064,.037),(0,.240,.788),TIRE,.1,.66)
# Hood signature stripe and rear insignia.
box('hood_center_ridge',(.029,.012,.390),(0,.441,-.487),SILVER,.8,.25)
box('tail_brand_bar',(.190,.023,.015),(0,.415,.779),SILVER,.7,.25)

OUTPUT.parent.mkdir(parents=True,exist_ok=True)
bytes_data=scene.export(file_type='glb')
OUTPUT.write_bytes(bytes_data)
print('Created',OUTPUT, 'bytes:',len(bytes_data),'scene parts:',len(scene.geometry))
