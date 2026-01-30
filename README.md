
<details>
  <summary><strong>MY PROFILE</strong></summary>

  ```bash
int main()
{
  Profile my; // 🪪
  
  my.name = "Morgan";
  my.school = 42; /* Nice (France) */
  
  my.areasOfInterest = {
    "Software_Architecture" : "Designing scalable and efficient systems";
    "Web Development"       : "Javascript";
    "Game Development"      : "Unity, C#";
    "AI & Machine Learning" : "Natural language processing, cognitive science applications";
  };

  my.languages = { "English", "Русский", "Français", "汉语", "Esperanto" };
  my.assets = { "ambitious", "pragmatic", "adaptable" };
  my.currentTarget = "on 42 Common Core finish line";
  
  Background previousCarrier; // 📚
  
  previousCarrier.field = "Early education";
  previousCarrier.speciality = "Teaching French as a Foreign Language";
  previousCarrier.top[3] = { "Coordinator", "Trainer", "Director" };
  
  Company business; // 💼
  
  business._status = "IE"; /* Individual Entrepreneur */
  business._commercialName = "MARIDO";

  business._services = {
    "educational" : "private tutoring";
    "linguistic"  : "translation & localisation (en/ru/eo > fr); copyrighting"
    "informatics" : "undefined";
  };
  
  business._website = "https://www.marido.fr";

  Skills stack; // 🛠️

  stack.os[3] = { "Linux", "MacOS", "Windows" };
  stack.languages = { "C", "C++", "Javascript", "Python" };
  stack.frameworks = { "Typescript", "Tailwind CSS" };
  stack.ai_tools = { "GPT", "Claude", "Copilot", "Suno" };

   Misc facts[3] = { "hitchhiked around Europe for 3 years",
                     "lived 10 years in Russia",
                     "designed a bilingual preschool in the French Riviera" };

  if ( wantToKnowMore )
    sendMessage( "marido.entreprise[at]gmail.com" );
  else
    std::cout << "Thanks for reading, have a nice day!" << '\n';

  return ( $? );
}
```
</details>

<details>
  <summary><strong>MY LOGS</strong></summary>

<!-- WORKLOG:START -->

### 📅 2026-01-18

## Week of [18-01-2026 - 25-01-2026]

### [Workflow]
- It would be great to automate publishing this work log on Github. Draft: show the previous week's log, with a link to the full document.
- I am unsure whether creating a search system would be worth it, but I wll keep the idea just in case.
- As my schedule *should* be more stable for a couple of months, I can reorganise my workflow for more efficiency.
- Current goals before summer: 1- finish 42 Common Core (Transcendence Group + Exam); 2- finish Transcendence Solo; 3- define what's next!

### [Transcendence_Solo]
- Started implementing the chat. Websockets are working, time to store the conversations in DB. 
- Added a SQL schema for DB whose existence is assessed at startup. I might need to set a migration table later to handle version update.
- Refactored the project for modularity and clarity. 
- Finally set a 're' alias to recompile the project properly with one command:
    `
    npx tsc --build ./config/tsconfig.base.json --force
    npx tsc -p app/frontend/tsconfig.json
    npx tsc -p app/backend/tsconfig.json
    npx tsx app/backend/src/server.mjs'
    `

- [Reminder] To set an alias: 1. code ~/.zshrc 2. add alias re='{my commands}' 3. source ~/zshrc
- [Reminder] An EventListener supports Entry if applied on form element (instead of send button) and is good for accessibility. 
- [Reminder] Defining an interface can help with destructuration type errors with TypeScript.
- [Resources] [Guide: Setting up a Fastify WebSocket project](https://betterstack.com/community/guides/scaling-nodejs/fastify-websockets/)

### [Transcendence_Group]
- Suggested an idea for the project. As each of us is highly interested in implementing a RAG and a LLM, it should cover it without too much
    replication of my Transcendence Solo project. Another stack would be nice.
- Defined with my partners a meeting date.

### [42_Exam_Rank06]
- Reviewed the basics of a server.

### [Thoughts]
- 解 (xiè, hexagramme 40 du Yi King).

[View all worklogs →](./worklogs)

<!-- WORKLOG:END -->

</details>

<details>
  <summary><strong>MY PROJECTS</strong></summary>

# ~ COMMON CORE ~

## Circle 0

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| libft      | Build your own reusable C utility library. | libc re-implementation, pointers, memory, Makefile, linked lists | link |

---

## Circle 1

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| ft_printf | Recreate `printf` (subset) with formatted output. | variadic args, parsing, formatting, write(), modular C design | link |
| get_next_line | Read a file descriptor line-by-line. | file I/O, buffers, static state, memory management | link |
| Born2beroot | Set up and harden a Linux VM like a (mini) sysadmin. | virtualization, Linux, users/groups, sudo, SSH, firewall, cron | link |

---

## Circle 2

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| push_swap | Sort integers using two stacks and a limited instruction set. | sorting strategies, complexity, greedy/heuristics, data structures | link |
| minitalk | Send text between processes using UNIX signals. | signals, bitwise encoding, client/server | link |
| so_long  | Build a tiny 2D game using MiniLibX. | event loop, rendering, map parsing, collision, flood fill | link |
| Exam Rank 02 | Timed C algorithmic exercises (multiple levels). | C basics, strings, pointers, small algorithms, speed/accuracy | link |

---

## Circle 3

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| minishell | Implement a minimal Bash-like shell. | parsing, env, fork/exec, pipes, redirections, signals, termios | link |
| Philosophers | Solve the Dining Philosophers concurrency problem. | threads, mutexes, deadlocks, timing, synchronization | link |
| Exam Rank 03 | Timed C exam (often `ft_printf` or `get_next_line`-style tasks). | C fundamentals, limited specs, debugging under pressure | link |

---

## Circle 4

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| NetPractice | Solve networking exercises (IP/subnets/routing). | IPv4, subnetting, routing, masks, network reasoning | link |
| cub3D | Raycasting 3D maze (Wolf3D-style). | raycasting, textures, map parsing, rendering loop, math | link |
| CPP Module 00 | C++ basics & OOP intro. | classes, methods, namespaces, IO streams | link |
| CPP Module 01 | Memory & references in C++. | new/delete, references, pointers, RAII intro | link |
| CPP Module 02 | Ad-hoc polymorphism & orthodox canon form. | operator overload, canonical form, fixed-point-ish patterns | link |
| CPP Module 03 | Inheritance. | inheritance, protected/public, composition vs inheritance | link |
| CPP Module 04 | Subtype polymorphism & interfaces. | virtual, abstract classes, deep copy, polymorphism | link |
| Exam Rank 04 | Timed “micro-shell” style exam. | fork/exec, pipes, parsing argv, minimal shell behavior | link |

---

## Circle 5

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| Inception | Deploy a multi-service stack using Docker. | Docker, docker-compose, networks, volumes, Nginx, services | link |
| webserv  | Write an HTTP server (HTTP/1.1). | sockets, HTTP, non-blocking I/O, config parsing, CGI | link |
| CPP Module 05 | Exceptions. | try/throw/catch, exception safety | link |
| CPP Module 06 | Casts. | static/dynamic/reinterpret/const cast, RTTI ideas | link |
| CPP Module 07 | Templates. | templates, generic programming | link |v |
| CPP Module 09 | Containers in practice. | containers, parsing, algorithms, composition | link |
| Exam Rank 05 | Timed C++ exam (multiple modules). | C++ syntax, OOP, problem solving under time constraints, binary tree | link |

---

## Circle 6

| Project | Concise description | Main notions & concepts used | Link |
|---|---|---|---|
| ft_transcendence | Build a full-stack web app (multiplayer Pong). | web dev, auth, real-time (WebSockets), security, Docker, teamwork | link |
| Exam Rank 06 | Final timed "mini server" style exam. | advanced timed problem-solving, robustness, constraints | link |

# Post Common Core

(To be unlocked)
  
</details>
  



`
