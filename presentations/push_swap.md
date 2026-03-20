# push_swap

## Overview
push_swap is a 42 project focused on sorting integers using two stacks and a limited instruction set.  
The goal is not only to sort correctly, but to do it with as few operations as possible, which makes the project a mix of algorithm design, optimization, and data-structure handling.

- **Project name:** push_swap
- **Type:** C / Algorithms / Sorting
- **Description:** A stack-based sorting program that organizes integers using only predefined operations, with a strong focus on efficiency, heuristics, and operation count.

## Project Context
- **Context:** Rank 02 project in the 42 Common Core, completed as an individual project under the school’s coding standard and strict function constraints.
- The project uses two stacks, `a` and `b`, along with a restricted set of operations such as `sa`, `pb`, `ra`, `rra`, and related variants.
- The result is judged both on correctness and on the number of operations produced.

## Objectives
- Learn how to design a sorting algorithm under strict operational constraints.
- Practice building and manipulating custom stack-based data structures.
- Improve reasoning about complexity, heuristics, and optimization.
- Handle parsing, validation, duplicates, and edge cases safely.
- Produce a solution that remains efficient on both small and large input sets.

## Usage
Once the project is compiled, the executable can be used like this:

```bash
./push_swap <list_of_integers>
```

`<list_of_integers>` can be passed either as separate arguments:

```bash
./push_swap 1 -3 5 4 -2
```

or as a single quoted string:

```bash
./push_swap "-1 3 5 -4 2"
```

The program outputs the sequence of operations needed to sort the list.

These operations can also be visualized with a push_swap visualizer to better understand the behavior of the algorithm and evaluate its efficiency.

## Features

### Parsing
I dramatically improved my first parsing solution after a colleague identified critical flaws within seconds. The arguments are now properly sanitized by removing leading `+` signs and trimming leading zeros. Each argument is then validated to ensure it can be safely converted into an integer. Invalid inputs such as non-integer or duplicate values are handled correctly.

### Indexing for Sorting
While converting the arguments, I assign each element the index of its position in the sorted order. This strategy significantly improved debugging and made the process much easier to follow, since working with normalized indices is more manageable than dealing directly with raw values.

### Sorting Algorithm
The sorting begins with stack `a`.

A pivot value is calculated as the square root of the number of elements in the stack. The lowest element is identified, and the working range is defined by setting the maximum to `lowest + pivot`.

The sorting process continues as long as the stack is unsorted and contains more than 3 elements:

- the shortest distance to any number within the defined range `[min, max]` is calculated
- the optimal move is determined
- the required rotations are applied to bring the target element to the top of stack `a`
- if there is another element that belongs in this range, it is pushed to stack `b` as well

Once the process narrows down to 3 elements, these are sorted directly with the minimum possible moves.

The focus then shifts to stack `b`.

While stack `b` contains more than 3 elements:

- the highest element in stack `b` is identified
- the optimal rotation move is calculated to bring this element to the top of stack `b`
- if another element is in the way, it is pushed to stack `a`
- if a new element is pushed to stack `a` and it is smaller than the previously placed element, a swap is performed in stack `a` to maintain order

Finally, once only 3 elements remain in stack `b`, they are sorted directly and pushed back to stack `a`.

## Technical Approach
The project is built around three main ideas: solid parsing, indexed values, and a range-based sorting strategy.

The parsing phase was treated as a real part of the project, not just a preliminary step. Cleaning the input before conversion made the rest of the program much more reliable.

Indexing each value based on its final sorted position helped make the algorithm easier to debug and reason about. Instead of tracking arbitrary integers, the program works with values that directly represent order.

The sorting strategy itself combines pivot-based grouping, shortest-path rotation decisions, and direct handling of very small stack states. The goal was to keep the algorithm understandable while still producing strong results on larger random test sets.

## Challenges
- Designing a sorting strategy that stays efficient under a very limited instruction set.
- Reworking the parsing logic to properly sanitize and validate all arguments.
- Keeping stack operations reliable while performing many rotations and pushes.
- Finding a strategy that was both practical to implement and pleasant to debug.
- Balancing algorithmic simplicity with a good operation count.

The hardest part was finding an approach that felt both efficient and readable. Indexing the values made a big difference here, because it gave a much clearer view of what the algorithm was actually doing at every step.

## Performance
Average results obtained with this implementation:

- **5 random integers:** 7 operations
- **100 random integers:** 684 operations
- **500 random integers:** 7871 operations

These results gave me a solid balance between algorithmic simplicity and practical efficiency.

## What I Learned
- How constrained rules can completely reshape the design of a sorting algorithm.
- How much clean parsing matters in a project that starts from raw user input.
- How normalized indices can simplify both debugging and algorithm design.
- How to reason about move cost, rotation direction, and stack state.
- How useful feedback and iteration can be when improving an algorithmic solution.

## Notes
- push_swap is not just about sorting correctly, but about adapting sorting logic to a restricted operational model.
- The project became much more enjoyable once the parsing was cleaned up and the indexed representation made debugging easier.
- Visualizers were especially useful for checking both correctness and the overall behavior of the algorithm.
