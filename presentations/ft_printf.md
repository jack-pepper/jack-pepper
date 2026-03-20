# ft_printf

## Overview
ft_printf is a custom implementation of the standard C `printf` function, developed as part of the 42 curriculum.  
The goal of the project is to reproduce formatted output behavior for a defined set of conversions while handling variadic arguments manually.

- **Project name:** ft_printf
- **Type:** C / Variadic Functions / Static Library
- **Description:** A simplified reimplementation of `printf` that parses format strings, handles multiple conversion specifiers, and prints formatted output through a custom low-level logic.

## Project Context
- **Context:** Rank 01 project in the 42 Common Core, completed as an individual project under the school’s coding standard and function restrictions.
- Built under a strict C compilation profile (`-Wall -Wextra -Werror`) and delivered as a reusable static library.

## Objectives
- Reproduce the core behavior of `printf` for the required conversion set.
- Learn how variadic functions work in C using `stdarg.h`.
- Practice parsing formatted strings and dispatching behavior depending on conversion specifiers.
- Improve understanding of low-level output, type handling, and modular code design.

## Features
- **Supported conversions**
   - `%c` — print a single character
   - `%s` — print a string
   - `%p` — print a pointer address in hexadecimal form
   - `%d` / `%i` — print signed decimal integers
   - `%u` — print unsigned decimal integers
   - `%x` — print hexadecimal in lowercase
   - `%X` — print hexadecimal in uppercase
   - `%%` — print a literal percent sign
- **Core behavior**
   - Parses the format string one character at a time
   - Detects `%` sequences and routes them to the correct conversion handler
   - Counts and returns the total number of printed characters
- **Feature notes:** The project focuses on the required conversion set only, with a modular implementation that separates parsing, printing, and type-specific formatting.
- **Bonus notes:** It handles the following flags as printf does: #, , +. It does NOT handle other flags.

## Technical Approach
- Public API exposed through `ft_printf.h`, with helper functions split by responsibility.
- The main `ft_printf` function parses the format string and uses variadic argument handling through `va_list`, `va_start`, `va_arg`, and `va_end`.
- Each conversion is delegated to a dedicated helper to keep the main parser short and readable.
- Printing is usually done with `write`, keeping the project close to low-level system calls.
- Integer and hexadecimal output rely on custom number-to-base conversion logic instead of standard formatting tools.
- **Approach notes:** The implementation is built around a small dispatcher model: detect a specifier, fetch the matching argument type, print it with the correct helper, and update the total printed length.

## Challenges
- Correctly handling variadic arguments without type mistakes.
- Matching the expected behavior of each conversion, especially edge cases like `NULL` strings or pointer formatting.
- Keeping the parsing logic simple while avoiding duplicated code.
- Returning the exact number of printed characters in every case.
- **Challenges notes:** The most delicate part was combining parsing accuracy with reusable helpers, especially for numeric conversions and output-length tracking.

## What I Learned
- How variadic functions work internally in C.
- How formatted output can be broken into parsing and conversion stages.
- How to design small helper functions around a central dispatcher.
- How to handle low-level output cleanly without relying on the standard `printf`.
- Why exact behavior and return values matter in system-level C projects.
