# Born2beroot

## Overview
Born2beroot is a system administration project from the 42 curriculum focused on setting up and securing a Linux server inside a virtual machine.  
Instead of building a classic C program, the project is about understanding how a real system is installed, configured, hardened, and maintained.

- **Project name:** Born2beroot
- **Type:** System Administration / Linux / Virtualization
- **Description:** A server setup project centered on Linux installation, user and permission management, security policies, networking, and service configuration inside a virtual machine.

## Project Context
- **Context:** Rank 01 project in the 42 Common Core, completed as an individual project in a virtualized environment.
- The project is based on a minimal Linux installation, with no graphical interface, and must follow strict security and administration rules.
- The work is usually presented during a defense where every configuration choice must be explained clearly.

## Objectives
- Learn the basics of virtualization and Linux server setup.
- Understand how to configure and secure a system step by step.
- Practice user, group, password, and permission management.
- Discover how core administration tools like SSH, sudo, cron, and firewall rules work together.
- Build a reliable and secure server environment that matches the project requirements.

## Features
- **Virtual machine setup**
   - Minimal Linux installation in a virtual machine
   - No graphical desktop environment
   - Clean and controlled system environment for administration practice

- **System administration**
   - Creation and management of users and groups
   - Secure hostname and user policy configuration
   - Use of `sudo` with logging and restricted behavior

- **Security configuration**
   - Password policy with expiration and complexity rules
   - Secure remote access through SSH
   - Active firewall configuration with only required ports opened
   - Hardening choices depending on the selected distribution and project rules

- **Monitoring**
   - Automatic monitoring script executed with `cron`
   - System information displayed regularly, such as:
     - architecture
     - CPU and memory usage
     - disk usage
     - logged-in users
     - network information
     - sudo command count

- **Storage and system layout**
   - Partitioning and logical volume management when required
   - Clear disk organization adapted to the project constraints

- **Feature notes:** The project focuses less on application development and more on building a secure, understandable, and properly maintained Linux environment.
- **Bonus notes:** Depending on the version completed, bonus work can include additional services or a more advanced server setup.

## Technical Approach
- The system was built from a minimal installation to keep the environment simple and controlled.
- Configuration was done step by step, with each service tested separately before moving to the next one.
- Core files and tools typically involved in the setup include:
   - SSH configuration
   - `sudoers` policy
   - password and PAM-related rules
   - firewall settings
   - cron scheduling
- The monitoring part is usually handled through a shell script that gathers system information from standard Linux commands and displays it periodically.
- **Approach notes:** The overall logic was to start from a minimal secure base, then add only the required services and rules while checking that every element remained coherent with the project requirements.

## Challenges
- Understanding how many system components interact with each other.
- Configuring SSH and firewall rules without breaking remote access.
- Applying password and sudo policies correctly without creating inconsistent behavior.
- Writing a monitoring script that gives useful and reliable system information.
- Becoming comfortable with Linux administration tools that are very different from standard C programming projects.
- **Challenges notes:** The hardest part was not writing code, but understanding the logic behind each configuration choice and making the full setup work as one consistent system.

## What I Learned
- How a Linux server is installed and configured in a virtual machine.
- How users, groups, permissions, and `sudo` policies are managed in practice.
- How SSH, firewall rules, and password policies contribute to system security.
- How to automate recurring system checks with shell scripts and `cron`.
- How to explain and justify technical configuration choices clearly.

## Notes
- Born2beroot is one of the first 42 projects that shifts the focus from programming to infrastructure and system administration.
- The most important part of the project is not only having a working VM, but understanding why each security and administration rule is in place.
- This project builds a strong foundation for later work involving servers, containers, deployment, and backend environments.
