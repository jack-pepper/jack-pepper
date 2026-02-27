
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

### 📅 2026-02-08

## Week of [08-02-2026 - 15-02-2026]

### [Workflow]
- Getting faster.

### [Transcendence_Team]
- Solved conversion issues with my Python script (thanks to [Derek's article: why is it so hard to pdf text extraction?](https://dev.to/derek-compdf/why-is-it-so-hard-to-pdf-text-extraction-k6h?utm_source=chatgpt.com).
- Learned to set a Django project. Intimidating at first, but it does not bite.
- Added 42 OAuth (and learned about 42 API)

### [Transcendence_Solo]
- On pause.

### [42_Exam_Rank06]
- On pause.

### [Thoughts]
-  I read with great interest the article [Something Big is Happening (Matt Shumer)](https://shumer.dev/something-big-is-happening). Unsure on what to conclude though.

[View all worklogs →](./worklogs)

<!-- WORKLOG:END -->

</details>

<details>
  <summary><strong>MY PROJECTS</strong></summary>

# ~ COMMON CORE ~

## Circle 0

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| libft | Build your own reusable C utility library. | libc re-implementation, pointers, memory, Makefile, linked lists |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_LIBFT_1" width="260"/>
  <img src="PLACEHOLDER_LIBFT_2" width="260"/>
</p>

---

## Circle 1

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| ft_printf | Recreate `printf` (subset) with formatted output. | variadic args, parsing, formatting, write(), modular C design |
| get_next_line | Read a file descriptor line-by-line. | file I/O, buffers, static state, memory management |
| Born2beroot | Set up and harden a Linux VM like a (mini) sysadmin. | virtualization, Linux, users/groups, sudo, SSH, firewall, cron |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_PRINTF" width="260"/>
  <img src="PLACEHOLDER_GNL" width="260"/>
  <img src="PLACEHOLDER_B2BR" width="260"/>
</p>

---

## Circle 2

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| push_swap | Sort integers using two stacks and a limited instruction set. | sorting strategies, complexity, greedy/heuristics, data structures |
| minitalk | Send text between processes using UNIX signals. | signals, bitwise encoding, client/server |
| so_long | Build a tiny 2D game using MiniLibX. | event loop, rendering, map parsing, collision, flood fill |
| Exam Rank 02 | Timed C algorithmic exercises (multiple levels). | C basics, strings, pointers, small algorithms, speed/accuracy |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_PUSHSWAP" width="260"/>
  <img src="PLACEHOLDER_MINITALK" width="260"/>
  <img src="PLACEHOLDER_SOLONG" width="260"/>
</p>

---

## Circle 3

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| minishell | Implement a minimal Bash-like shell. | parsing, env, fork/exec, pipes, redirections, signals, termios |
| Philosophers | Solve the Dining Philosophers concurrency problem. | threads, mutexes, deadlocks, timing, synchronization |
| Exam Rank 03 | Timed C exam. | C fundamentals, debugging |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_MINISHELL" width="260"/>
  <img src="PLACEHOLDER_PHILO" width="260"/>
</p>

---

## Circle 4

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| NetPractice | Solve networking exercises (IP/subnets/routing). | IPv4, subnetting, routing, masks |
| cub3D | Raycasting 3D maze. | math, textures, rendering loop |
| CPP Modules | Object-oriented programming. | polymorphism, abstraction |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_NETPRACTICE" width="260"/>
  <img src="PLACEHOLDER_CUB3D" width="260"/>
  <img src="PLACEHOLDER_CPP" width="260"/>
</p>

---

## Circle 5

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| Inception | Multi-service Docker infrastructure. | containers, networking, services |
| webserv | HTTP server implementation. | sockets, HTTP, non-blocking I/O |
| CPP Advanced | Templates and exceptions. | generic programming |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_INCEPTION" width="260"/>
  <img src="PLACEHOLDER_WEBSERV" width="260"/>
</p>

---

## Circle 6

| Project | Concise description | Main notions & concepts used |
|---|---|---|
| ft_transcendence | Full-stack multiplayer web app. | real-time, authentication, Docker |
| Exam Rank 06 | Final timed exam. | robustness, constraints |

### Visual gallery
<p align="center">
  <img src="PLACEHOLDER_TRANSCENDENCE_1" width="260"/>
  <img src="PLACEHOLDER_TRANSCENDENCE_2" width="260"/>
</p>

---

# Post Common Core  
(To be unlocked)

</details>

  



`
