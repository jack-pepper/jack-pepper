# get_next_line

## Overview
get_next_line is a 42 project focused on reading text from a file descriptor one line at a time.  
It recreates a common low-level input pattern found in standard library functions and builds a strong foundation for file handling and dynamic memory management in C.

- **Project name:** get_next_line
- **Type:** C / File I/O / Static State Management
- **Description:** A function that reads and returns one line at a time from a file descriptor, while preserving unread data between calls through a static storage mechanism.

## Project Context
- **Context:** Rank 01 project in the 42 Common Core, completed as an individual project under the school’s coding standard and function restrictions.
- Built under a strict C compilation profile (`-Wall -Wextra -Werror`).
- The goal is to implement a reusable line-reading function without relying on higher-level standard input helpers.

## Objectives
- Understand how low-level file reading works through file descriptors and `read`.
- Learn to manage buffers, partial reads, and persistent state across function calls.
- Practice dynamic memory allocation and safe string manipulation.
- Handle edge cases such as EOF, empty files, invalid descriptors, and lines of unknown length.

## Features
- Reads input **line by line** from a file descriptor.
- Returns one complete line per function call, including the newline when present.
- Preserves unread buffer content between calls using a static variable.
- Handles files with long lines, multiple short lines, or no trailing newline.
- Supports repeated calls until the full file has been consumed.
- **Feature notes:** I used a single static `stash` variable to keep the leftover content after each call. This allows the function to remember where the previous read stopped and continue correctly on the next call.
- **Bonus notes:** Depending on the version, the bonus can extend the logic to support multiple file descriptors at the same time.

## Usage
This project helps understand the internal logic of functions that read data from a file descriptor, similar to those found in the standard C library, such as `getline` and `fgets`.

It shows how to handle memory buffers, efficiently read data line by line, and manage dynamic memory allocation. It also gives a better view of how file I/O works under the hood, reinforcing key concepts such as edge-case handling, persistent state, and efficient input/output management in real C programs.

## Technical Approach
- The implementation relies on a **single static `stash` variable** that stores leftover data between function calls.
- Each call to `get_next_line` starts by checking the current content of the `stash` before reading more from the file descriptor.
- Data is read into a buffer until a newline is found or the end of file is reached.
- Once a full line is available, that line is extracted and returned.
- Any remaining data after the newline is kept for the next call.
- Public helpers are usually split across utility functions for string joining, newline detection, line extraction, and stash cleanup.
- **Approach notes:** In my implementation, I chose to first copy the buffer content into the `stash`, then extract the next line from it, and finally move the remaining unread data to the beginning of the `stash` for future calls.

## How It Works
When `get_next_line` reads from a file descriptor, it fills a buffer with data. If a newline character (`\n`) is found, the function returns everything up to that point as a complete line.

Any leftover data after the newline is saved in the `stash`. On the next call, the function starts by processing that saved content before reading more from the file again. This keeps continuity between calls and avoids losing unread data.

## Challenges
- Keeping the function behavior correct across repeated calls.
- Managing memory safely without leaks when concatenating or trimming buffer content.
- Handling partial reads and preserving only the useful leftover data.
- Correctly returning the last line when no trailing newline is present.
- Supporting edge cases such as empty files, invalid file descriptors, or very small `BUFFER_SIZE` values.
- **Challenges notes:** The trickiest part was maintaining a clean and reliable flow between reading, extracting the next line, and updating the static storage without losing data or introducing memory issues.

## What I Learned
- How file descriptors and the `read` system call work in practice.
- How to manage persistent function state with static variables.
- How to design buffer-based logic for incremental reading.
- How to handle dynamic allocation carefully in string-heavy code.
- Why edge cases matter so much in low-level C programming.
