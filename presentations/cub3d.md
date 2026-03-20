# cub3D

## Overview
cub3D is a 42 group project focused on building a raycasting-based 3D engine inspired by *Wolfenstein 3D*, written in C with MiniLibX.  
The core goal is to create a navigable 3D world from a 2D map while learning the fundamentals of raycasting, rendering, event handling, and map parsing.

- **Project name:** cub3D
- **Type:** C / Graphics / Raycasting / MiniLibX
- **Description:** A small first-person exploration game and rendering engine that turns a 2D map into a pseudo-3D environment using raycasting.
- **Team:** Group project completed by 2 people.

## Project Context
- **Context:** Rank 04 project in the 42 Common Core, completed as a team project under the school’s coding standard and graphical programming constraints.
- The project is built with **MiniLibX** and focuses on low-level rendering, user input, texture handling, and real-time scene updates.
- The mandatory part centers on raycasting and navigation, while this version also includes extra gameplay and presentation elements.

## Objectives
- Understand how raycasting creates a 3D illusion from a 2D map.
- Practice real-time rendering and event-driven programming in C.
- Learn how to parse and validate structured map/configuration files.
- Handle player movement, collisions, rotation, and scene updates.
- Build a complete graphical project combining low-level logic, math, and asset management.

## Demo
Game Demo

## Features
- 3D raycasting engine inspired by *Wolfenstein 3D*
- Multiple themed levels
  - ice
  - sand
  - pacman
  - mario
  - and others
- Collectibles, enemies, and exit doors
- Minimap and UI overlays
- Custom asset loading
- `.cub` file parsing and map validation
- Keyboard controls for movement and rotation
- Real-time rendering with texture-based walls and environment styling

## Controls
- `W` / `A` / `S` / `D` — Move
- Arrow keys — Rotate view
- `ESC` — Quit

## Build & Run
Compile the project with:

```bash
make
```

Run it with a valid map file:

```bash
./cub3D maps/VALID_SIMPLE.cub
```

## Customization
You can easily customize the game experience in several ways.

### Colors
Floor and ceiling colors can be edited directly in the `.cub` configuration file.

### Map Editing
Map layouts and elements can be changed by editing the map files in the `maps/` directory.

A valid map must:
- contain exactly one player starting position
- use one of `N`, `S`, `W`, or `E` for the initial direction
- be fully enclosed by walls

### Textures
Wall textures can be replaced or extended by editing the asset files and updating the paths in the configuration file.

- Texture files must use the `.xpm` format.
- Asset files are stored in the `ass/` folder.

## Technical Approach
The project is built around a classic raycasting pipeline.

A 2D map is parsed from a `.cub` file, validated, and used as the logical world representation. From the player’s position and viewing angle, rays are cast across the field of view to detect wall intersections. The distance returned by each ray is then used to compute the height of the corresponding vertical wall slice on screen, creating the illusion of depth.

Around this core rendering system, the project also includes:
- player movement and rotation handling
- collision checks against the map
- texture loading and projection
- minimap rendering
- overlay/UI elements
- themed assets and level variations

This version goes beyond a minimal raycasting demo by adding more game-oriented elements such as enemies, collectibles, and exit logic.

## Challenges
- Understanding the math behind raycasting and projection.
- Avoiding visual distortion and handling distance correction properly.
- Parsing `.cub` files safely and validating maps correctly.
- Managing real-time rendering while keeping the code organized.
- Handling textures, minimap drawing, and UI elements together in the same render loop.
- Coordinating the work cleanly in a two-person team project.

The hardest part was combining several systems that all depend on each other: parsing, rendering, movement, collisions, and assets. Once the raycasting core works, the rest of the project becomes a matter of integrating each layer cleanly without breaking performance or readability.

## What I Learned
- How a pseudo-3D engine can be built from a 2D map.
- How raycasting works at a practical level in C.
- How to manage rendering loops and input events with MiniLibX.
- How important map validation is in graphical projects.
- How to structure a larger C project with multiple modules and assets.
- How to collaborate on a graphics-heavy team project.

## Project Structure
```text
src/      - Main source files
libft/    - Custom C library
ass/      - Game assets (sprites, textures)
maps/     - Example map files
inc/      - Header files
```

## Team Work
This project was developed as a two-person collaboration.

- Work was shared across the main project areas such as rendering, parsing, gameplay logic, and integration.
- Team coordination was important because changes in one part of the engine could directly affect input handling, map logic, or rendering.
- The project required both technical collaboration and consistent code organization to keep the final result coherent.

## Credits
Developed by **yel-bouk** and **mmalie**

## Notes
- At its core, cub3D is a raycasting project meant to explore how early 3D engines work.
- This version extends that foundation with themed levels, UI elements, and additional gameplay mechanics.
- It is a strong introduction to graphics programming, game loops, geometric reasoning, and structured C project design.
