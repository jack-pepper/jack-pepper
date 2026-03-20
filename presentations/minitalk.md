# minitalk

## Overview
minitalk is a 42 project focused on inter-process communication using UNIX signals.  
The goal is to send a text message from a client process to a server process without using higher-level communication tools such as sockets or pipes.

- **Project name:** minitalk
- **Type:** C / UNIX Signals / Inter-Process Communication
- **Description:** A small client-server communication system where messages are transmitted bit by bit through `SIGUSR1` and `SIGUSR2`.

## Project Context
- **Context:** Rank 02 project in the 42 Common Core, completed as an individual project under the school’s coding standard and function constraints.
- The project is based on communication between two separate processes:
  - a **server**, which waits for incoming signals
  - a **client**, which sends a message to the server
- The main challenge is to build a reliable communication protocol using only UNIX signals.

## Objectives
- Understand how UNIX signals work in practice.
- Learn how two independent processes can communicate at a low level.
- Practice bitwise logic and binary encoding.
- Build a simple but reliable client-server protocol.
- Handle synchronization issues between sender and receiver.

## Usage

### Server
Open the first terminal.

Run the server program:

```bash
./server
```

Its PID (`SERVER_PID`) will be displayed.

The server will display the received message in the terminal once it is fully transmitted.

### Client
Open the second terminal.

Run the client with the server PID and the message to send:

```bash
./client <SERVER_PID> <MESSAGE>
```

The message can be any string and is sent to the server as a sequence of signals representing binary data.

### Example

```bash
# Server Terminal
./server
Process ID (PID): 12345

# Client Terminal
./client 12345 "Hello 42 Nice"
```

## Features
The project achieves communication through a signal-based transmission protocol between the client and the server.

- The server listens for incoming signals using `sigaction`.
- Two user-defined signals are used:
  - `SIGUSR1` represents binary `0`
  - `SIGUSR2` represents binary `1`
- Characters are sent one at a time as binary data.
- Once 8 bits have been received, they are combined into one byte and converted into the corresponding character.
- The server reconstructs the full message progressively and prints it once transmission is complete.

To make the transmission more reliable:

- the client waits for an acknowledgment signal from the server before sending the next bit
- a small `usleep` delay is added between signal transmissions to avoid sending signals too quickly

This avoids overwhelming the server and reduces the risk of data loss or corrupted output.

## Technical Approach
The project is built around a simple client-server protocol using UNIX signals as the communication channel.

The server starts by displaying its process ID and then waits for signals using `sigaction`, which provides a cleaner and more robust way to manage signal handling than older APIs.

On the client side, each character of the message is converted into binary form. The bits are then sent one by one:

- `SIGUSR1` for bit `0`
- `SIGUSR2` for bit `1`

On the server side, each received signal updates the current byte being reconstructed. Once 8 bits have been received, the server converts that byte into a character and stores or prints it as part of the final message.

To keep the communication stable, the client does not send all bits at once. Instead, it waits for confirmation from the server after each transmitted bit before continuing. This acknowledgment-based approach helps prevent missed signals and keeps both processes synchronized.

## Challenges
- Understanding how asynchronous signal handling works.
- Building a reliable transmission system using only two signal types.
- Reconstructing characters correctly from individual bits.
- Avoiding lost signals when the client sends data too quickly.
- Synchronizing the client and server cleanly during the full message transmission.

The hardest part was making the communication reliable. Sending bits is simple in theory, but keeping the transmission synchronized and avoiding overflow or missed signals requires a proper protocol between both processes.

## What I Learned
- How UNIX signals can be used for low-level communication between processes.
- How binary data can be encoded and reconstructed bit by bit.
- How to use `sigaction` for cleaner signal handling.
- Why synchronization matters in client-server communication.
- How timing issues can affect even very small communication systems.

## Notes
- minitalk is a small project in size, but it introduces important system programming concepts.
- The project gives a practical view of how data transmission can be built from very basic mechanisms.
- It is also a good introduction to communication protocols, synchronization, and event-driven behavior in C.
