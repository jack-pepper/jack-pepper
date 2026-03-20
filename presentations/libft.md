# Libft

## Overview
Libft is a custom C static library developed as part of the 42 curriculum.  
It reimplements selected libc-like functions and adds utility helpers and linked-list tools that are reused in later projects.

- **Project name:** Libft
- **Type:** C / Static Library
- **Description:** A foundational library of reimplemented standard C functions, string and memory utilities, and bonus linked-list helpers designed to build stronger low-level programming habits and provide reusable tools for future 42 projects.

## Project Context
- **Context:** Rank 00 project in the 42 Common Core, completed as an individual project under the school’s coding standard and function constraints.
- Built under a strict C compilation profile (`-Wall -Wextra -Werror`) and archived as `libft.a`.

## Objectives
- Reimplement essential standard-library-style functions from scratch in C.
- Learn to design clear, reusable, and consistent low-level utility code.
- Build a reliable low-level utility base for future C projects.
- Strengthen understanding of memory handling, pointers, strings, and data structures.

## Features
- **Mandatory libc-style set**
   - Character checks/conversions: `ft_isalpha`, `ft_isdigit`, `ft_isalnum`, `ft_isascii`, `ft_isprint`, `ft_toupper`, `ft_tolower`
   - Numeric/string primitives: `ft_atoi`, `ft_strlen`, `ft_strdup`, `ft_strncmp`, `ft_strnstr`
   - Memory primitives: `ft_memset`, `ft_bzero`, `ft_memcpy`, `ft_memmove`, `ft_memchr`, `ft_memcmp`, `ft_calloc`
   - String buffer operations: `ft_strlcpy`, `ft_strlcat`, `ft_strchr`, `ft_strrchr`
- **Additional utilities**
   - `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_split`
   - `ft_itoa`, `ft_strmapi`, `ft_striteri`
   - File-descriptor output helpers: `ft_putchar_fd`, `ft_putstr_fd`, `ft_putendl_fd`, `ft_putnbr_fd`
- **Bonus (linked lists)**
   - `ft_lstnew`, `ft_lstadd_front`, `ft_lstsize`, `ft_lstlast`, `ft_lstadd_back`
   - `ft_lstdelone`, `ft_lstclear`, `ft_lstiter`, `ft_lstmap`
- **Feature notes:** The library covers the core set of utility functions commonly needed in later 42 projects, with special attention to correctness, consistency, and reuse.
- **Bonus notes:** The linked-list bonus extends the library beyond libc-style reimplementation and introduces dynamic data-structure handling through a small but practical API.

## Technical Approach
- Public API centralized in `libft.h` with a consistent `ft_` namespace.
- Source groups split by domain (libc-like, utility, and list handling), then archived through `Makefile` targets (`all`, `bonus`, `clean`, `fclean`, `re`).
- Emphasis on defensive memory behavior and edge-case handling in allocation-heavy functions.
- **Approach notes:** Each function was implemented with close attention to expected behavior, argument safety, return values, and separation of responsibilities, so the library remains easy to maintain and reliable as a base dependency.

## Challenges
- Keeping function behavior aligned with expected libc-like semantics.
- Managing allocation-failure paths cleanly (especially in composite routines).
- Preserving strict compilation cleanliness under `-Werror`.
- **Challenges notes:** The main difficulty was balancing low-level correctness with clean code structure, especially for functions involving dynamic allocation, pointer arithmetic, and chained operations such as splitting strings or mapping linked lists.
