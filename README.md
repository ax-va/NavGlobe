# AxVaGlobe

## Project

**AxVaGlobe** is a project for creating globes by hexagon-or-pentagon-like polygons and for navigating on them. The project targets many programming languages.

## Geometric Component

A *surface unit* is a hexagon-like polygon consisting of six triangles or a pentagon-like polygon consisting of five triangles (that share one vertex of the icosahedron). The surface units approximate the sphere or some part of the sphere. 

<img src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" data-canonical-src="https://user-images.githubusercontent.com/85578981/127783633-d5dc5e1b-57e8-426b-ae48-cb57790e715e.png" width="700"/>

When changing the radius of the sphere for the surface units you can create arbitrary 3D surfaces on the sphere. 

## Logical Component

The logical component is that each surface unit at the logical level knows its nearest neighbors that is implemented algorithmically, not by storage. Due to that, discrete movement on the surface is possible.
